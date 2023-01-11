#loading the packages 
import pandas as pd 
import dash 
from dash import dcc
from dash import html
from dash import dash_table
import plotly.express as px
import plotly.graph_objs as go

# loading the data for single choice questions such that it imports the variable lables and saving the variable lables in a new list  
df = pd.read_stata(r"C:\Dropbox\Peer_Effects_and_Roll_Models\Analysis_Experiment\1_Raw\Output\enrollment_survey\label_data_raw_onechoice.dta", iterator=True)
tags  = df.variable_labels()
var, labels = zip(*tags.items())
# loading the data with single selection MCQ variables to create the data set of first set 
df = pd.read_stata(r"C:\Dropbox\Peer_Effects_and_Roll_Models\Analysis_Experiment\1_Raw\Output\enrollment_survey\label_data_raw_onechoice.dta")
# print(labels)

# Loading up the data for multi-choice it imports the variable lables and saving the variable lables in a new list  
multi_df = pd.read_stata(r"C:\Dropbox\Peer_Effects_and_Roll_Models\Analysis_Experiment\1_Raw\Output\enrollment_survey\label_data_raw_multichoice.dta", iterator=True)
multi_tags  = multi_df.variable_labels()
multi_var, multi_labels = zip(*multi_tags.items())
# loading the data with single selection MCQ variables to create the data set of first set 
multi_df = pd.read_stata(r"C:\Dropbox\Peer_Effects_and_Roll_Models\Analysis_Experiment\1_Raw\Output\enrollment_survey\label_data_raw_multichoice.dta")
# Get the unique values in the last row of the dataframe
unique_values = multi_df.iloc[-1,:].unique()
#Get the total number of participants in the survey data 
total_participants = multi_df.shape[0] - 1


# # Loading up the data for multi-choice it imports the variable lables and saving the variable lables in a new list  
# multi_df = pd.read_stata(r"C:\Dropbox\Peer_Effects_and_Roll_Models\Analysis_Experiment\1_Raw\Output\enrollment_survey\label_data_raw_multichoice1.dta", iterator=True)
# multi_tags  = multi_df.variable_labels()
# multi_var, multi_labels = zip(*multi_tags.items())
# # loading the data with single selection MCQ variables to create the data set of first set 
# multi_df = pd.read_stata(r"C:\Dropbox\Peer_Effects_and_Roll_Models\Analysis_Experiment\1_Raw\Output\enrollment_survey\label_data_raw_multichoice1.dta")
# # Get the unique values in the last row of the dataframe
# unique_values = multi_df.iloc[-1,:].unique()
# #Get the total number of participants in the survey data 
# total_participants = multi_df.shape[0] - 1


# Create a Dash app
app = dash.Dash()


# Define the layout and interactivity of the dashboard
app.layout = html.Div([
     # Tab component for multiple pages
     dcc.Tabs(id='tabs', value='page-1', children=[
         dcc.Tab(label='Single-Choice Summary', value='page-1'),
         dcc.Tab(label='Singe-Choice CrossTab', value='page-2'),
         dcc.Tab(label ='Multi-Choice Summary', value='page-3')
     ]),
     # Page 1
     html.Div(id='page-1', children=[
         # Dropdown menu with each column of the DataFrame as an option
         dcc.Dropdown(
             id='page-1-column-dropdown',
             options=[{'label': label, 'value': col} for label, col in zip(labels, df.columns)],
             value=df.columns[0]
         ),
         # Table displaying the value counts
         dash_table.DataTable(id='counts-table'),
         # Pie chart
         dcc.Graph(id='pie-chart',figure={'height': 600},style={'margin-top': '50px'})
     ]),
     # Page 2
     html.Div(id='page-2', children=[
         # Dropdown menu with each column of the DataFrame as an option and the ability to select multiple columns
         dcc.Dropdown(
             id='page-2-column-dropdown',
             options=[{'label': label, 'value': col} for label, col in zip(labels, df.columns)],
             value=df.columns[0],
             multi=True
         ),
         # Button to compute the cross tabulation of the selected columns
         html.Button('Compute Cross Tabulation', id='compute-button'),
         # Table displaying the cross tabulation results
         dash_table.DataTable(id='cross-tab-table'),
        # bar graph
        dcc.Graph(id='bar-chart',figure={'height': 50,'layout': {
        'title': 'share of variable 1 for each option of variable 2',
        'xaxis': {'title': 'Variable2'},
        'yaxis': {'title': 'Percentage Share'}}}, style= {'margin-top': '50px'})         
     ]),
    # Page 3 
    html.Div(id='page-3', children=[
        # A multi-select dropdown menu with Labes of multi-choice variable
    dcc.Dropdown(
        id='page-3-label-dropdown',
        options=[{'label': value, 'value': value} for value in unique_values],
        multi=True
    ),
    # Checklist of column names
    dcc.Checklist(id='checklist'),
    # Output value 
    html.Div(id='output',style={'display': 'flex', 'justify-content': 'center', 'transform': 'scale(2)','margin-top': '70px'})
])        
    
 ])


# Add a callback function to update the value counts table and pie chart based on the selected column
@app.callback(
     [dash.dependencies.Output('counts-table', 'data'),
      dash.dependencies.Output('pie-chart', 'figure')],
     [dash.dependencies.Input('page-1-column-dropdown', 'value')])
def update_counts_and_pie_chart(column):
    # Compute the value counts for the selected column
    counts = df[column].value_counts(normalize=True) * 100
    # round off table values 
    counts = counts.apply(lambda x : round(x,0))
    # Add a row to the value counts to display the total non-empty values
    counts['Total'] = df[column].count()
    # Convert the value counts to a list of dictionaries
    counts_table = [{'name': val, 'value': count} for val, count in counts.items()]
    pie_chart_data = [{'name': val, 'value': count} for val, count in counts.items() if val != 'Total']
    # Create a pie chart of the value counts for the selected column
    pie_chart = px.pie(pie_chart_data, values='value', names='name')
    return counts_table, pie_chart



# Add a callback function to compute the cross tabulation of the selected columns
@app.callback(
    [dash.dependencies.Output('cross-tab-table', 'data'),
     dash.dependencies.Output('bar-chart', 'figure')],
    [dash.dependencies.Input('compute-button', 'n_clicks')],
    [dash.dependencies.State('page-2-column-dropdown', 'value')]
)
def compute_cross_tab(n_clicks, columns):
    # Compute the cross tabulation of the selected columns- can't normalise here as need totals
    cross_tab = pd.crosstab(df[columns[0]], df[columns[1]],margins=True)
    # Convert the cross tabulation to a list of dictionaries
    cross_tab = cross_tab.reset_index().to_dict('records')
    # converting the dictionary back to dataframe 
    new = pd.DataFrame.from_dict(cross_tab)
    # now editing the information to create graphs that provide extra information
    # get the last row of the data 
    last_row = new.iloc[-1]
    # Divide each row by the last row, except for the first column
    new.iloc[:, 1:] = new.iloc[:, 1:].div(last_row[1:], axis=1)
    # Multiply all values by 100, except for the first column
    new.iloc[:, 1:] = new.iloc[:, 1:]*100
    # Remove the last row
    new = new.iloc[:-1]
    # Remove the last column
    new = new.iloc[:, :-1]
    # Get the column names for the x-axis
    x = new.columns[1:]
    # Get the string labels for each stack
    labels = new.iloc[:, 0]
    # Create a list of lists with the values for each stack
    values = [list(row[1:]) for _, row in new.iterrows()]
    # Create a bar chart
    fig = go.Figure()
    # Add a bar for each stack
    for label, y in zip(labels, values):
        fig.add_trace(go.Bar(name=label, x=x, y=y))
    # Add the labels as ticktext
    bar_chart = fig.update_layout(barmode='stack', xaxis={'ticktext': x, 'tickvals': x})
    return cross_tab, bar_chart    

# @app.callback(
#     dash.dependencies.Output('checklist', 'options'),
#     [dash.dependencies.Input('page-3-label-dropdown', 'value')])
# def update_checklist(labels):
#     # Get the list of column names for which the last value is equal to the selected string
#     columns = [col for col in multi_df.columns if multi_df[col].iloc[-1] in labels]
#     # Set the options property of the checklist component to the list of column names
#     return [{'label': label, 'value': col} for label,col in zip(multi_labels,columns)]
###################
@app.callback(
    dash.dependencies.Output('checklist', 'options'),
    [dash.dependencies.Input('page-3-label-dropdown', 'value')])
def update_checklist(selected_labels):
    # Get the list of columns for which the last value is equal to one of the selected labels
    columns = multi_df.columns[multi_df.iloc[-1,:].isin(selected_labels)]
    # Set the options property of the checklist component to the list of column names and labels
    return [{'label': multi_tags[col], 'value': col} for col in columns]



##################
# Add a callback function to count the percentage of reponses common across the selected columns 
@app.callback(
    dash.dependencies.Output('output', 'children'),
    [dash.dependencies.Input('checklist', 'value')])
def update_output(selected_columns):
    
    if len(selected_columns) == 1:
        count = (multi_df[selected_columns[0]] == "1").sum()
        count = (count/total_participants)*100
        count = round(count, 0)
        return f'Percentage of participants who chose the selected options as their answer : {count}'
    else:
        count = ((multi_df[selected_columns] == "1").all(axis=1)).sum()
        count = (count/total_participants)*100
        count = round(count, 0)
        return f'Number of participants who chose all selected options as thier answer: {count}' 




# Add a callback function to update the page content based on the selected tab
@app.callback(dash.dependencies.Output('page-1', 'style'), [dash.dependencies.Input('tabs', 'value')])
def update_page_content(tab):
    if tab == 'page-1':
        # Display page 1
        return {'display': 'block'}
    elif tab == 'page-2':
        # Hide page 1
        return {'display': 'none'}
    elif tab == 'page-3':
        # Hide page 2 
        return {'display': 'none'}

# Add a callback function to update the page content based on the selected tab
@app.callback(dash.dependencies.Output('page-2', 'style'), [dash.dependencies.Input('tabs', 'value')])
def update_page_content(tab):
    if tab == 'page-1':
        # Hide page 1
        return {'display': 'none'}
    elif tab == 'page-2':
        # Display page 2
        return {'display': 'block'}
    elif tab == 'page-3':
        # Hide page 2 
        return {'display': 'none'}
# Add a callback function to update the page content based on the selected tab
@app.callback(dash.dependencies.Output('page-3', 'style'), [dash.dependencies.Input('tabs', 'value')])
def update_page_content(tab):
    if tab == 'page-1':
        # Hide page 1
        return {'display': 'none'}
    elif tab == 'page-2':
        # Hide page 2
        return {'display': 'none'}
    elif tab == 'page-3':
        # Display page 3 
        return {'display': 'block'}
 
 # Run the app
if __name__ == '__main__':
    app.run_server()





