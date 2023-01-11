#loading the packages 
import pandas as pd 
import dash 
from dash import dcc
from dash import html
from dash import dash_table
import plotly.express as px
import plotly.graph_objs as go

# # loading the data for single choice questions such that it imports the variable lables and saving the variable lables in a new list  
# df = pd.read_stata(r"C:\Dropbox\Peer_Effects_and_Roll_Models\Analysis_Experiment\1_Raw\Output\enrollment_survey\label_data_raw_onechoice.dta", iterator=True)
# tags  = df.variable_labels()
# var, labels = zip(*tags.items())
# # loading the data with single selection MCQ variables to create the data set of first set 
# df = pd.read_stata(r"C:\Dropbox\Peer_Effects_and_Roll_Models\Analysis_Experiment\1_Raw\Output\enrollment_survey\label_data_raw_onechoice.dta")
# # print(labels)

# # Loading up the data for multi-choice it imports the variable lables and saving the variable lables in a new list  
# multi_df = pd.read_stata(r"C:\Dropbox\Peer_Effects_and_Roll_Models\Analysis_Experiment\1_Raw\Output\enrollment_survey\label_data_raw_multichoice.dta", iterator=True)
# multi_tags  = multi_df.variable_labels()
# multi_var, multi_labels = zip(*multi_tags.items())
# # loading the data with single selection MCQ variables to create the data set of first set 
# multi_df = pd.read_stata(r"C:\Dropbox\Peer_Effects_and_Roll_Models\Analysis_Experiment\1_Raw\Output\enrollment_survey\label_data_raw_multichoice.dta")

#####################################################################################
#some additions
df = pd.read_csv("https://raw.githubusercontent.com/SawalChoudhary/Peer_Effects_Dashboard/main/assets/label_data_raw_onechoice.csv")
labels = ('relationship with wm', 'Highest education of resp', 'Religion of resp', 'Marital status of respondent', 'Caste category', 'Jati name', 'SC from survey', 'Ever WM before', 'How many times, if WM before', 'Ever WM before, from family', 'How many times, if WM from famliy before', 'Anyone politician in family', 'Any other job self', 'Primary HH source of income', 'Any govt employee in family', 'received training', 'E-gramswaraj app', 'last app usage', 'type of watersupply connection village', 'collected money Nal Jal scheme', 'using whatsapp', 'same calling and whatsapp number', 'whatsapp in phone', 'frequency of reading whatsapp messages?', 'if other wm WA group', 'wanted to do discuss with other wm', 'work related discussion partner', 'group of preference for SC member', 'scheme with least or no problem', 'scheme with most problem', 'Row total of problem to citizen', 'Mukhiya Phone number', 'Panchayat scretary number', 'BPRO phone number', 'Last talk BPRO', 'BDO phone number', 'Last talk to BDO', 'work related discussion with WM in GP', 'Network in GP', 'work related discussion with WM outside GP and in block', 'Network in block', 'discussion with WM same block', 'Network in Dist', 'work related discussion with WM outside the district', 'Network in outside dist', 'Row total of WM account steps', 'Row total of awas steps', 'Row total of WMs responsibilities', 'Row total of confidence in schemes', 'support any pol party self', 'Involment in the politicial party', 'Any politicial support', 'Treatment condition')


multi_df = pd.read_csv("https://raw.githubusercontent.com/SawalChoudhary/Peer_Effects_Dashboard/main/assets/label_data_raw_multichoice.csv") 
multi_var = ('issues_campign_1', 'issues_campign_2', 'issues_campign_3', 'issues_campign_4', 'issues_campign_5', 'issues_campign_6', 'issues_campign_7', 'issues_campign_8', 'issues_campign_9', 'issues_campign_10', 'issues_campign_11', 'issues_campign_12', 'issues_campign_100', 'wm_year_2016', 'wm_year_2011', 'wm_year_2006', 'wm_year_2001', 'wm_year_100', 'wm_familyyear_2016', 'wm_familyyear_2011', 'wm_familyyear_2006', 'wm_familyyear_2001', 'wm_familyyear_100', 'pol_level_1', 'pol_level_2', 'pol_level_3', 'pol_level_4', 'pol_level_5', 'pol_level_100', 'wm_train_learn_0', 'wm_train_learn_99', 'wm_train_learn_100', 'wm_app_usewhy_1', 'wm_app_usewhy_2', 'wm_app_usewhy_3', 'wm_app_usewhy_100', 'wm_nomoneycol_1', 'wm_nomoneycol_2', 'wm_nomoneycol_3', 'wm_nomoneycol_100', 'wm_moneycolyes_1', 'wm_moneycolyes_2', 'wm_moneycolyes_3', 'wm_moneycolyes_100', 'whatsapp_whosephone_1', 'whatsapp_whosephone_2', 'whatsapp_whosephone_100', 'scheme_noproblemwhy_1', 'scheme_noproblemwhy_2', 'scheme_noproblemwhy_100', 'scheme_implement_1', 'scheme_implement_2', 'scheme_implement_3', 'scheme_implement_4', 'scheme_implement_5', 'scheme_implement_100', 'scheme_whatproblem_1', 'scheme_whatproblem_2', 'scheme_whatproblem_3', 'scheme_whatproblem_4', 'scheme_whatproblem_100', 'scheme_soltoproblem_1', 'scheme_soltoproblem_2', 'scheme_soltoproblem_3', 'scheme_soltoproblem_4', 'scheme_soltoproblem_5', 'scheme_soltoproblem_6', 'scheme_soltoproblem_7', 'scheme_soltoproblem_8', 'scheme_soltoproblem_100', 'scheme_probtocitizen_1', 'scheme_probtocitizen_2', 'scheme_probtocitizen_3', 'scheme_probtocitizen_4', 'scheme_probtocitizen_5', 'scheme_probtocitizen_6', 'scheme_probtocitizen_7', 'scheme_probtocitizen_8', 'scheme_probtocitizen_9', 'scheme_probtocitizen_10', 'scheme_probtocitizen_11', 'scheme_probtocitizen_0', 'scheme_probtocitizen_100', 'interaction_gpno_1', 'interaction_gpno_2', 'interaction_gpno_3', 'interaction_gpno_100', 'interaction_gpyes_1', 'interaction_gpyes_2', 'interaction_gpyes_3', 'interaction_gpyes_4', 'interaction_gpyes_5', 'interaction_gpyes_6', 'interaction_gpyes_7', 'interaction_gpyes_8', 'interaction_gpyes_9', 'interaction_gpyes_10', 'interaction_gpyes_11', 'interaction_gpyes_12', 'interaction_gpyes_13', 'interaction_gpyes_100', 'interaction_blockno_1', 'interaction_blockno_2', 'interaction_blockno_3', 'interaction_blockno_100', 'interaction_blockyes_1', 'interaction_blockyes_2', 'interaction_blockyes_3', 'interaction_blockyes_4', 'interaction_blockyes_5', 'interaction_blockyes_6', 'interaction_blockyes_7', 'interaction_blockyes_8', 'interaction_blockyes_9', 'interaction_blockyes_10', 'interaction_blockyes_11', 'interaction_blockyes_12', 'interaction_blockyes_13', 'interaction_blockyes_100', 'interaction_samedistno_1', 'interaction_samedistno_2', 'interaction_samedistno_3', 'interaction_samedistno_100', 'interaction_samedistyes_1', 'interaction_samedistyes_2', 'interaction_samedistyes_3', 'interaction_samedistyes_4', 'interaction_samedistyes_5', 'interaction_samedistyes_6', 'interaction_samedistyes_7', 'interaction_samedistyes_8', 'interaction_samedistyes_9', 'interaction_samedistyes_10', 'interaction_samedistyes_11', 'interaction_samedistyes_12', 'interaction_samedistyes_13', 'interaction_samedistyes_100', 'interaction_outsideno_1', 'interaction_outsideno_2', 'interaction_outsideno_3', 'interaction_outsideno_100', 'interaction_outsideyes_1', 'interaction_outsideyes_2', 'interaction_outsideyes_3', 'interaction_outsideyes_4', 'interaction_outsideyes_5', 'interaction_outsideyes_6', 'interaction_outsideyes_7', 'interaction_outsideyes_8', 'interaction_outsideyes_9', 'interaction_outsideyes_10', 'interaction_outsideyes_11', 'interaction_outsideyes_12', 'interaction_outsideyes_13', 'interaction_outsideyes_100', 'ward_account_0', 'ward_account_1', 'ward_account_2', 'ward_account_3', 'ward_account_4', 'ward_account_5', 'ward_account_6', 'ward_account_100', 'awas_knowledge_1', 'awas_knowledge_2', 'awas_knowledge_3', 'awas_knowledge_4', 'awas_knowledge_5', 'awas_knowledge_100', 'scheme_knowledge', 'scheme_knowledge_1', 'scheme_knowledge_2', 'scheme_knowledge_3', 'scheme_knowledge_4', 'scheme_knowledge_5', 'scheme_knowledge_6', 'scheme_knowledge_7', 'scheme_knowledge_8', 'scheme_knowledge_9', 'scheme_knowledge_10', 'scheme_knowledge_0', 'scheme_knowledge_100', 'scheme_knowconfi', 'scheme_knowconfi_1', 'scheme_knowconfi_2', 'scheme_knowconfi_3', 'scheme_knowconfi_4', 'scheme_knowconfi_5', 'scheme_knowconfi_6', 'scheme_knowconfi_7', 'scheme_knowconfi_8', 'scheme_knowconfi_9', 'scheme_knowconfi_10', 'scheme_knowconfi_0', 'scheme_knowconfi_100', 'polpref_party_1', 'polpref_party_2', 'polpref_party_3', 'polpref_party_4', 'polpref_party_5', 'polpref_party_6', 'polpref_party_7', 'polpref_party_8', 'polpref_party_9', 'polpref_party_10', 'polpref_party_100', 'pol_partysupport_1', 'pol_partysupport_2', 'pol_partysupport_3', 'pol_partysupport_4', 'pol_partysupport_5', 'pol_partysupport_6', 'pol_partysupport_7', 'pol_partysupport_8', 'pol_partysupport_9', 'pol_partysupport_10', 'pol_partysupport_100', 'pol_support_1', 'pol_support_2', 'pol_support_3', 'pol_support_4')
#####################################################################################





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
server = app.server



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





