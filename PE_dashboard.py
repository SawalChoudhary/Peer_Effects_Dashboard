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
# #loading the data with single selection MCQ variables to create the data set of first set 
# # df = pd.read_stata(r"C:\Dropbox\Peer_Effects_and_Roll_Models\Analysis_Experiment\1_Raw\Output\enrollment_survey\label_data_raw_onechoice.dta")
# # print(labels)

# # Loading up the data for multi-choice it imports the variable lables and saving the variable lables in a new list  
# multi_df = pd.read_stata(r"C:\Dropbox\Peer_Effects_and_Roll_Models\Analysis_Experiment\1_Raw\Output\enrollment_survey\label_data_raw_multichoice.dta", iterator=True)
# multi_tags  = multi_df.variable_labels()
# multi_var, multi_labels = zip(*multi_tags.items())
# #loading the data with single selection MCQ variables to create the data set of first set 
# # multi_df = pd.read_stata(r"C:\Dropbox\Peer_Effects_and_Roll_Models\Analysis_Experiment\1_Raw\Output\enrollment_survey\label_data_raw_multichoice.dta")

# ####################################################################################
# ## some additions
tags = {'relationship': 'relationship with wm', 'politician_edu': 'Highest education of resp', 'politican_rel': 'Religion of resp', 'mar_status': 'Marital status of respondent', 'resp_caste_cat': 'Caste category', 'resp_jati': 'Jati name', 'caste_sc': 'SC from survey', 'wm_bef': 'Ever WM before', 'wm_years': 'How many times, if WM before', 'wm_familybefore': 'Ever WM before, from family', 'wm_familyyears': 'How many times, if WM from famliy before', 'pol_infamily': 'Anyone politician in family', 'self_emp': 'Any other job self', 'inc_sor': 'Primary HH source of income', 'govt_empinfam': 'Any govt employee in family', 'wm_train': 'received training', 'wm_app': 'E-gramswaraj app', 'wm_app_use': 'last app usage', 'wm_watersupply': 'type of watersupply connection village', 'wm_moneycol': 'collected money Nal Jal scheme', 'whatsapp': 'using whatsapp', 'whatsapp_number': 'same calling and whatsapp number', 'whatsapp_self': 'whatsapp in phone', 'message': 'frequency of reading whatsapp messages?', 'wm_wagroup': 'if other wm WA group', 'join_interestyesno': 'wanted to do discuss with other wm', 'join_interest': 'work related discussion partner', 'sc_group': 'group of preference for SC member', 'scheme_noproblem': 'scheme with least or no problem', 'scheme_problem': 'scheme with most problem', 'citiprbrt': 'Row total of problem to citizen', 'phone_mukhiya': 'Mukhiya Phone number', 'phone_scret': 'Panchayat scretary number', 'phone_bpro': 'BPRO phone number', 'phone_lasttimebpro': 'Last talk BPRO', 'phone_bdo': 'BDO phone number', 'phone_lasttimebdo': 'Last talk to BDO', 'interaction_gp': 'work related discussion with WM in GP', 'candidate_gp_count': 'Network in GP', 'interaction_block': 'work related discussion with WM outside GP and in block', 'candidate_block_count': 'Network in block', 'interaction_samedist': 'discussion with WM same block', 'candidate_samedist_count': 'Network in Dist', 'interaction_outside': 'work related discussion with WM outside the district', 'candidate_outside_count': 'Network in outside dist', 'acctrt': 'Row total of WM account steps', 'awasrt': 'Row total of awas steps', 'schknwrt': 'Row total of WMs responsibilities', 'schconfirt': 'Row total of confidence in schemes', 'polpref_self': 'support any pol party self', 'pol_party_part': 'Involment in the politicial party', 'polpref_supportelec': 'Any politicial support', 't_dummy': 'Treatment condition'}
var, labels = zip(*tags.items())
df = pd.read_csv("https://raw.githubusercontent.com/SawalChoudhary/Peer_Effects_Data/main/label_data_raw_onechoice.csv")


# var = ('relationship', 'politician_edu', 'politican_rel', 'mar_status', 'resp_caste_cat', 'resp_jati', 'caste_sc', 'wm_bef', 'wm_years', 'wm_familybefore', 'wm_familyyears', 'pol_infamily', 'self_emp', 'inc_sor', 'govt_empinfam', 'wm_train', 'wm_app', 'wm_app_use', 'wm_watersupply', 'wm_moneycol', 'whatsapp', 'whatsapp_number', 'whatsapp_self', 'message', 'wm_wagroup', 'join_interestyesno', 'join_interest', 'sc_group', 'scheme_noproblem', 'scheme_problem', 'citiprbrt', 'phone_mukhiya', 'phone_scret', 'phone_bpro', 'phone_lasttimebpro', 'phone_bdo', 'phone_lasttimebdo', 'interaction_gp', 'candidate_gp_count', 'interaction_block', 'candidate_block_count', 'interaction_samedist', 'candidate_samedist_count', 'interaction_outside', 'candidate_outside_count', 'acctrt', 'awasrt', 'schknwrt', 'schconfirt', 'polpref_self', 'pol_party_part', 'polpref_supportelec', 't_dummy')
# labels = ('relationship with wm', 'Highest education of resp', 'Religion of resp', 'Marital status of respondent', 'Caste category', 'Jati name', 'SC from survey', 'Ever WM before', 'How many times, if WM before', 'Ever WM before, from family', 'How many times, if WM from famliy before', 'Anyone politician in family', 'Any other job self', 'Primary HH source of income', 'Any govt employee in family', 'received training', 'E-gramswaraj app', 'last app usage', 'type of watersupply connection village', 'collected money Nal Jal scheme', 'using whatsapp', 'same calling and whatsapp number', 'whatsapp in phone', 'frequency of reading whatsapp messages?', 'if other wm WA group', 'wanted to do discuss with other wm', 'work related discussion partner', 'group of preference for SC member', 'scheme with least or no problem', 'scheme with most problem', 'Row total of problem to citizen', 'Mukhiya Phone number', 'Panchayat scretary number', 'BPRO phone number', 'Last talk BPRO', 'BDO phone number', 'Last talk to BDO', 'work related discussion with WM in GP', 'Network in GP', 'work related discussion with WM outside GP and in block', 'Network in block', 'discussion with WM same block', 'Network in Dist', 'work related discussion with WM outside the district', 'Network in outside dist', 'Row total of WM account steps', 'Row total of awas steps', 'Row total of WMs responsibilities', 'Row total of confidence in schemes', 'support any pol party self', 'Involment in the politicial party', 'Any politicial support', 'Treatment condition')


multi_tags = {'issues_campign_1': 'Nali -Gali', 'issues_campign_2': 'Nal Jal', 'issues_campign_3': 'Sath Nishchay', 'issues_campign_4': 'Ration Card', 'issues_campign_5': 'Pension; Old age, CM pension', 'issues_campign_6': 'Shauchalay', 'issues_campign_7': 'Indira Awas', 'issues_campign_8': 'E- Sharam Card', 'issues_campign_9': 'Corruption', 'issues_campign_10': 'Mnrega', 'issues_campign_11': 'Ujjwala', 'issues_campign_12': 'Solar Light', 'issues_campign_100': 'Other Issues', 'wm_year_2016': '2016', 'wm_year_2011': '2011', 'wm_year_2006': '2006', 'wm_year_2001': '2001', 'wm_year_100': 'other years self', 'wm_familyyear_2016': '2016', 'wm_familyyear_2011': '2011', 'wm_familyyear_2006': '2006', 'wm_familyyear_2001': '2001', 'wm_familyyear_100': 'Other years family', 'pol_level_1': 'MP/MLA/Minister', 'pol_level_2': 'Mukhiya', 'pol_level_3': 'At District level', 'pol_level_4': 'At Block level', 'pol_level_5': 'At Gram panchayat level', 'pol_level_100': 'Other level pol', 'wm_train_learn_0': 'Were not told about anything', 'wm_train_learn_99': 'Prefer not to say', 'wm_train_learn_100': 'Other training', 'wm_app_usewhy_1': 'Information about new schemes for own GP', 'wm_app_usewhy_2': 'Information about the funds released for own GP', 'wm_app_usewhy_3': 'To monitor Mukhiya for the use of funds', 'wm_app_usewhy_100': 'Other app usage', 'wm_nomoneycol_1': 'Scheme not working properly', 'wm_nomoneycol_2': 'Scheme is working fine but people donot want to pay', 'wm_nomoneycol_3': 'WM donot want to collect', 'wm_nomoneycol_100': 'Other no nal jal money ', 'wm_moneycolyes_1': 'For electricity bill', 'wm_moneycolyes_2': 'For repairing', 'wm_moneycolyes_3': 'Have not used yet', 'wm_moneycolyes_100': 'Other use of nal jal money', 'whatsapp_whosephone_1': 'Spouse', 'whatsapp_whosephone_2': 'Child', 'whatsapp_whosephone_100': 'Others phone', 'scheme_noproblemwhy_1': 'Does not recieve any scheme', 'scheme_noproblemwhy_2': 'Account is not updated or opened', 'scheme_noproblemwhy_100': 'Other no problem scheme', 'scheme_implement_1': 'From relatives/family/friends', 'scheme_implement_2': 'From WMs of same GP', 'scheme_implement_3': 'From WMs of other GP', 'scheme_implement_4': 'From training', 'scheme_implement_5': 'From youtube,newspaper,online', 'scheme_implement_100': 'Other implement scheme', 'scheme_whatproblem_1': 'Mukhiya informed Lack of funds ', 'scheme_whatproblem_2': 'Account not opened yet', 'scheme_whatproblem_3': 'Commission to Anyon', 'scheme_whatproblem_4': 'Work under the control of mukhiya', 'scheme_whatproblem_100': 'Other problem in scheme implemmet', 'scheme_soltoproblem_1': 'Interact with other ward members', 'scheme_soltoproblem_2': 'Interact with Mukhiya/others in Panchayat', 'scheme_soltoproblem_3': 'Interact with BDO/others in Block', 'scheme_soltoproblem_4': 'Interact with SDO/others in Sub division', 'scheme_soltoproblem_5': 'Interact with DM/others in District', 'scheme_soltoproblem_6': 'Interact with MP/MLA/Minister/Departemt', 'scheme_soltoproblem_7': 'Nothing', 'scheme_soltoproblem_8': "We don't face any problem", 'scheme_soltoproblem_100': 'Other solution to problem', 'scheme_probtocitizen_1': 'NalJal', 'scheme_probtocitizen_2': 'Nali-gali', 'scheme_probtocitizen_3': 'shauchalaya', 'scheme_probtocitizen_4': 'indira awas', 'scheme_probtocitizen_5': 'pds', 'scheme_probtocitizen_6': 'electricity to all', 'scheme_probtocitizen_7': 'ujwala gas', 'scheme_probtocitizen_8': 'mnrega', 'scheme_probtocitizen_9': 'pension', 'scheme_probtocitizen_10': 'Solar Light', 'scheme_probtocitizen_11': 'No problem', 'scheme_probtocitizen_0': 'No work done', 'scheme_probtocitizen_100': 'Other scheme citizen prob', 'interaction_gpno_1': 'No contact details', 'interaction_gpno_2': 'Never felt the need', 'interaction_gpno_3': 'No issue to talk about', 'interaction_gpno_100': 'Other no interaction in gp', 'interaction_gpyes_1': 'Nal Jal', 'interaction_gpyes_2': 'Nali Gali', 'interaction_gpyes_3': 'MNREGA', 'interaction_gpyes_4': 'Pension', 'interaction_gpyes_5': 'Shauchalay', 'interaction_gpyes_6': 'PDS', 'interaction_gpyes_7': 'Saat Nishchay', 'interaction_gpyes_8': 'E-shram', 'interaction_gpyes_9': 'Indira Awas', 'interaction_gpyes_10': 'How to get funds', 'interaction_gpyes_11': 'How to open account', 'interaction_gpyes_12': 'Updates and info on schemes', 'interaction_gpyes_13': 'Solar light', 'interaction_gpyes_100': 'Other scheme discussion in gp', 'interaction_blockno_1': 'No contact details', 'interaction_blockno_2': 'Never felt the need', 'interaction_blockno_3': 'No issue to talk about', 'interaction_blockno_100': 'Others no discussion in block', 'interaction_blockyes_1': 'Nal Jal', 'interaction_blockyes_2': 'Nali Gali', 'interaction_blockyes_3': 'MNREGA', 'interaction_blockyes_4': 'Pension', 'interaction_blockyes_5': 'Shauchalay', 'interaction_blockyes_6': 'PDS', 'interaction_blockyes_7': 'Saat Nishchay', 'interaction_blockyes_8': 'E-shram', 'interaction_blockyes_9': 'Indira Awas', 'interaction_blockyes_10': 'How to get funds', 'interaction_blockyes_11': 'How to open account', 'interaction_blockyes_12': 'Updates and info on schemes', 'interaction_blockyes_13': 'Solar light', 'interaction_blockyes_100': 'Others scheme discussion in block', 'interaction_samedistno_1': 'No contact details', 'interaction_samedistno_2': 'Never felt the need', 'interaction_samedistno_3': 'No issue to talk about', 'interaction_samedistno_100': 'Others no discussion in dist', 'interaction_samedistyes_1': 'Nal Jal', 'interaction_samedistyes_2': 'Nali Gali', 'interaction_samedistyes_3': 'MNREGA', 'interaction_samedistyes_4': 'Pension', 'interaction_samedistyes_5': 'Shauchalay', 'interaction_samedistyes_6': 'PDS', 'interaction_samedistyes_7': 'Saat Nishchay', 'interaction_samedistyes_8': 'E-shram', 'interaction_samedistyes_9': 'Indira Awas', 'interaction_samedistyes_10': 'How to get funds', 'interaction_samedistyes_11': 'How to open account', 'interaction_samedistyes_12': 'Updates and info on schemes', 'interaction_samedistyes_13': 'Solar light', 'interaction_samedistyes_100': 'Others scheme discussion in dist', 'interaction_outsideno_1': 'No contact details', 'interaction_outsideno_2': 'Does not feel the need', 'interaction_outsideno_3': 'No issue to talk about', 'interaction_outsideno_100': 'Others no discussion in outside dist', 'interaction_outsideyes_1': 'Nal Jal', 'interaction_outsideyes_2': 'Nali Gali', 'interaction_outsideyes_3': 'MNREGA', 'interaction_outsideyes_4': 'Pension', 'interaction_outsideyes_5': 'Shauchalay', 'interaction_outsideyes_6': 'PDS', 'interaction_outsideyes_7': 'Saat Nishchay', 'interaction_outsideyes_8': 'E-shram', 'interaction_outsideyes_9': 'Indira Awas', 'interaction_outsideyes_10': 'How to get funds', 'interaction_outsideyes_11': 'How to open account', 'interaction_outsideyes_12': 'Updates and info on schemes', 'interaction_outsideyes_13': 'Solar light', 'interaction_outsideyes_100': 'Others scheme discussion in outside dist', 'ward_account_0': "Don't know", 'ward_account_1': 'Ward sabha will happen', 'ward_account_2': 'election of ward sec', 'ward_account_3': 'Fill form', 'ward_account_4': 'sign from GP sec', 'ward_account_5': 'acceptance from BDO', 'ward_account_6': 'BDO copy to bank', 'ward_account_100': 'Others WM account step', 'awas_knowledge_1': "Don't know'", 'awas_knowledge_2': 'WM will prepare a list of elligible HH', 'awas_knowledge_3': 'Priortise SC', 'awas_knowledge_4': 'According to funds Mukhiya will decide the final benificaries', 'awas_knowledge_5': 'Mukhiya will submit the list to Indira Awas Sahayak', 'awas_knowledge_100': 'Others awas steps', 'scheme_knowledge': 'name schemes where WMs are primary responsible', 'scheme_knowledge_1': 'Nal jal', 'scheme_knowledge_2': 'Nali Gali', 'scheme_knowledge_3': 'Shauchalay', 'scheme_knowledge_4': 'Pension', 'scheme_knowledge_5': 'Sat Nischay', 'scheme_knowledge_6': 'PDS', 'scheme_knowledge_7': 'Monitoring dev work', 'scheme_knowledge_8': 'Support to resolve conflict in a ward', 'scheme_knowledge_9': 'MNREGA', 'scheme_knowledge_10': 'Indira Awas', 'scheme_knowledge_0': "Don't know", 'scheme_knowledge_100': 'Others scheme knowledge', 'scheme_knowconfi': 'In which schems knowledge you are confident', 'scheme_knowconfi_1': 'Nal jal', 'scheme_knowconfi_2': 'Nali-gali', 'scheme_knowconfi_3': 'Shauchalay', 'scheme_knowconfi_4': 'Indira awas', 'scheme_knowconfi_5': 'PDS', 'scheme_knowconfi_6': 'Electricity to all', 'scheme_knowconfi_7': 'Ujjwala', 'scheme_knowconfi_8': 'MNREGA', 'scheme_knowconfi_9': 'Pension', 'scheme_knowconfi_10': 'Solar light', 'scheme_knowconfi_0': 'None', 'scheme_knowconfi_100': 'Others scheme confidence', 'polpref_party_1': 'Tir chap (JDU)', 'polpref_party_2': 'Kamal (BJP)', 'polpref_party_3': 'Haat (Congress)', 'polpref_party_4': 'Laltern (RJD)', 'polpref_party_5': 'Haat (Congress)', 'polpref_party_6': 'Bungalow (LJP)', 'polpref_party_7': 'Telephone (HAM)', 'polpref_party_8': 'Naav (VIP)', 'polpref_party_9': 'Kite (AIMIM)', 'polpref_party_10': 'Not prefer to say', 'polpref_party_100': 'Others support party', 'pol_partysupport_1': 'Tir chap (JDU)', 'pol_partysupport_2': 'Kamal (BJP)', 'pol_partysupport_3': 'Haat (Congress)', 'pol_partysupport_4': 'Laltern (RJD)', 'pol_partysupport_5': 'Haat (Congress)', 'pol_partysupport_6': 'Bungalow (LJP)', 'pol_partysupport_7': 'Telephone (HAM)', 'pol_partysupport_8': 'Naav (VIP)', 'pol_partysupport_9': 'Kite (AIMIM)', 'pol_partysupport_10': 'Not prefer to say', 'pol_partysupport_100': 'Others part of party', 'pol_support_1': 'All logistics', 'pol_support_2': 'Party workers campigned for me', 'pol_support_3': 'Helped finance my campaign', 'pol_support_4': 'some leader campigned for me in village'}
multi_var, multi_labels = zip(*multi_tags.items())
multi_df = pd.read_csv("https://raw.githubusercontent.com/SawalChoudhary/Peer_Effects_Data/main/label_data_raw_multichoice.csv") 


# multi_var = ('issues_campign_1', 'issues_campign_2', 'issues_campign_3', 'issues_campign_4', 'issues_campign_5', 'issues_campign_6', 'issues_campign_7', 'issues_campign_8', 'issues_campign_9', 'issues_campign_10', 'issues_campign_11', 'issues_campign_12', 'issues_campign_100', 'wm_year_2016', 'wm_year_2011', 'wm_year_2006', 'wm_year_2001', 'wm_year_100', 'wm_familyyear_2016', 'wm_familyyear_2011', 'wm_familyyear_2006', 'wm_familyyear_2001', 'wm_familyyear_100', 'pol_level_1', 'pol_level_2', 'pol_level_3', 'pol_level_4', 'pol_level_5', 'pol_level_100', 'wm_train_learn_0', 'wm_train_learn_99', 'wm_train_learn_100', 'wm_app_usewhy_1', 'wm_app_usewhy_2', 'wm_app_usewhy_3', 'wm_app_usewhy_100', 'wm_nomoneycol_1', 'wm_nomoneycol_2', 'wm_nomoneycol_3', 'wm_nomoneycol_100', 'wm_moneycolyes_1', 'wm_moneycolyes_2', 'wm_moneycolyes_3', 'wm_moneycolyes_100', 'whatsapp_whosephone_1', 'whatsapp_whosephone_2', 'whatsapp_whosephone_100', 'scheme_noproblemwhy_1', 'scheme_noproblemwhy_2', 'scheme_noproblemwhy_100', 'scheme_implement_1', 'scheme_implement_2', 'scheme_implement_3', 'scheme_implement_4', 'scheme_implement_5', 'scheme_implement_100', 'scheme_whatproblem_1', 'scheme_whatproblem_2', 'scheme_whatproblem_3', 'scheme_whatproblem_4', 'scheme_whatproblem_100', 'scheme_soltoproblem_1', 'scheme_soltoproblem_2', 'scheme_soltoproblem_3', 'scheme_soltoproblem_4', 'scheme_soltoproblem_5', 'scheme_soltoproblem_6', 'scheme_soltoproblem_7', 'scheme_soltoproblem_8', 'scheme_soltoproblem_100', 'scheme_probtocitizen_1', 'scheme_probtocitizen_2', 'scheme_probtocitizen_3', 'scheme_probtocitizen_4', 'scheme_probtocitizen_5', 'scheme_probtocitizen_6', 'scheme_probtocitizen_7', 'scheme_probtocitizen_8', 'scheme_probtocitizen_9', 'scheme_probtocitizen_10', 'scheme_probtocitizen_11', 'scheme_probtocitizen_0', 'scheme_probtocitizen_100', 'interaction_gpno_1', 'interaction_gpno_2', 'interaction_gpno_3', 'interaction_gpno_100', 'interaction_gpyes_1', 'interaction_gpyes_2', 'interaction_gpyes_3', 'interaction_gpyes_4', 'interaction_gpyes_5', 'interaction_gpyes_6', 'interaction_gpyes_7', 'interaction_gpyes_8', 'interaction_gpyes_9', 'interaction_gpyes_10', 'interaction_gpyes_11', 'interaction_gpyes_12', 'interaction_gpyes_13', 'interaction_gpyes_100', 'interaction_blockno_1', 'interaction_blockno_2', 'interaction_blockno_3', 'interaction_blockno_100', 'interaction_blockyes_1', 'interaction_blockyes_2', 'interaction_blockyes_3', 'interaction_blockyes_4', 'interaction_blockyes_5', 'interaction_blockyes_6', 'interaction_blockyes_7', 'interaction_blockyes_8', 'interaction_blockyes_9', 'interaction_blockyes_10', 'interaction_blockyes_11', 'interaction_blockyes_12', 'interaction_blockyes_13', 'interaction_blockyes_100', 'interaction_samedistno_1', 'interaction_samedistno_2', 'interaction_samedistno_3', 'interaction_samedistno_100', 'interaction_samedistyes_1', 'interaction_samedistyes_2', 'interaction_samedistyes_3', 'interaction_samedistyes_4', 'interaction_samedistyes_5', 'interaction_samedistyes_6', 'interaction_samedistyes_7', 'interaction_samedistyes_8', 'interaction_samedistyes_9', 'interaction_samedistyes_10', 'interaction_samedistyes_11', 'interaction_samedistyes_12', 'interaction_samedistyes_13', 'interaction_samedistyes_100', 'interaction_outsideno_1', 'interaction_outsideno_2', 'interaction_outsideno_3', 'interaction_outsideno_100', 'interaction_outsideyes_1', 'interaction_outsideyes_2', 'interaction_outsideyes_3', 'interaction_outsideyes_4', 'interaction_outsideyes_5', 'interaction_outsideyes_6', 'interaction_outsideyes_7', 'interaction_outsideyes_8', 'interaction_outsideyes_9', 'interaction_outsideyes_10', 'interaction_outsideyes_11', 'interaction_outsideyes_12', 'interaction_outsideyes_13', 'interaction_outsideyes_100', 'ward_account_0', 'ward_account_1', 'ward_account_2', 'ward_account_3', 'ward_account_4', 'ward_account_5', 'ward_account_6', 'ward_account_100', 'awas_knowledge_1', 'awas_knowledge_2', 'awas_knowledge_3', 'awas_knowledge_4', 'awas_knowledge_5', 'awas_knowledge_100', 'scheme_knowledge', 'scheme_knowledge_1', 'scheme_knowledge_2', 'scheme_knowledge_3', 'scheme_knowledge_4', 'scheme_knowledge_5', 'scheme_knowledge_6', 'scheme_knowledge_7', 'scheme_knowledge_8', 'scheme_knowledge_9', 'scheme_knowledge_10', 'scheme_knowledge_0', 'scheme_knowledge_100', 'scheme_knowconfi', 'scheme_knowconfi_1', 'scheme_knowconfi_2', 'scheme_knowconfi_3', 'scheme_knowconfi_4', 'scheme_knowconfi_5', 'scheme_knowconfi_6', 'scheme_knowconfi_7', 'scheme_knowconfi_8', 'scheme_knowconfi_9', 'scheme_knowconfi_10', 'scheme_knowconfi_0', 'scheme_knowconfi_100', 'polpref_party_1', 'polpref_party_2', 'polpref_party_3', 'polpref_party_4', 'polpref_party_5', 'polpref_party_6', 'polpref_party_7', 'polpref_party_8', 'polpref_party_9', 'polpref_party_10', 'polpref_party_100', 'pol_partysupport_1', 'pol_partysupport_2', 'pol_partysupport_3', 'pol_partysupport_4', 'pol_partysupport_5', 'pol_partysupport_6', 'pol_partysupport_7', 'pol_partysupport_8', 'pol_partysupport_9', 'pol_partysupport_10', 'pol_partysupport_100', 'pol_support_1', 'pol_support_2', 'pol_support_3', 'pol_support_4')
# multi_labels = ('Nali -Gali', 'Nal Jal', 'Sath Nishchay', 'Ration Card', 'Pension; Old age, CM pension', 'Shauchalay', 'Indira Awas', 'E- Sharam Card', 'Corruption', 'Mnrega', 'Ujjwala', 'Solar Light', 'Other Issues', '2016', '2011', '2006', '2001', 'other years self', '2016', '2011', '2006', '2001', 'Other years family', 'MP/MLA/Minister', 'Mukhiya', 'At District level', 'At Block level', 'At Gram panchayat level', 'Other level pol', 'Were not told about anything', 'Prefer not to say', 'Other training', 'Information about new schemes for own GP', 'Information about the funds released for own GP', 'To monitor Mukhiya for the use of funds', 'Other app usage', 'Scheme not working properly', 'Scheme is working fine but people donot want to pay', 'WM donot want to collect', 'Other no nal jal money ', 'For electricity bill', 'For repairing', 'Have not used yet', 'Other use of nal jal money', 'Spouse', 'Child', 'Others phone', 'Does not recieve any scheme', 'Account is not updated or opened', 'Other no problem scheme', 'From relatives/family/friends', 'From WMs of same GP', 'From WMs of other GP', 'From training', 'From youtube,newspaper,online', 'Other implement scheme', 'Mukhiya informed Lack of funds ', 'Account not opened yet', 'Commission to Anyon', 'Work under the control of mukhiya', 'Other problem in scheme implemmet', 'Interact with other ward members', 'Interact with Mukhiya/others in Panchayat', 'Interact with BDO/others in Block', 'Interact with SDO/others in Sub division', 'Interact with DM/others in District', 'Interact with MP/MLA/Minister/Departemt', 'Nothing', "We don't face any problem", 'Other solution to problem', 'NalJal', 'Nali-gali', 'shauchalaya', 'indira awas', 'pds', 'electricity to all', 'ujwala gas', 'mnrega', 'pension', 'Solar Light', 'No problem', 'No work done', 'Other scheme citizen prob', 'No contact details', 'Never felt the need', 'No issue to talk about', 'Other no interaction in gp', 'Nal Jal', 'Nali Gali', 'MNREGA', 'Pension', 'Shauchalay', 'PDS', 'Saat Nishchay', 'E-shram', 'Indira Awas', 'How to get funds', 'How to open account', 'Updates and info on schemes', 'Solar light', 'Other scheme discussion in gp', 'No contact details', 'Never felt the need', 'No issue to talk about', 'Others no discussion in block', 'Nal Jal', 'Nali Gali', 'MNREGA', 'Pension', 'Shauchalay', 'PDS', 'Saat Nishchay', 'E-shram', 'Indira Awas', 'How to get funds', 'How to open account', 'Updates and info on schemes', 'Solar light', 'Others scheme discussion in block', 'No contact details', 'Never felt the need', 'No issue to talk about', 'Others no discussion in dist', 'Nal Jal', 'Nali Gali', 'MNREGA', 'Pension', 'Shauchalay', 'PDS', 'Saat Nishchay', 'E-shram', 'Indira Awas', 'How to get funds', 'How to open account', 'Updates and info on schemes', 'Solar light', 'Others scheme discussion in dist', 'No contact details', 'Does not feel the need', 'No issue to talk about', 'Others no discussion in outside dist', 'Nal Jal', 'Nali Gali', 'MNREGA', 'Pension', 'Shauchalay', 'PDS', 'Saat Nishchay', 'E-shram', 'Indira Awas', 'How to get funds', 'How to open account', 'Updates and info on schemes', 'Solar light', 'Others scheme discussion in outside dist', "Don't know", 'Ward sabha will happen', 'election of ward sec', 'Fill form', 'sign from GP sec', 'acceptance from BDO', 'BDO copy to bank', 'Others WM account step', "Don't know'", 'WM will prepare a list of elligible HH', 'Priortise SC', 'According to funds Mukhiya will decide the final benificaries', 'Mukhiya will submit the list to Indira Awas Sahayak', 'Others awas steps', 'name schemes where WMs are primary responsible', 'Nal jal', 'Nali Gali', 'Shauchalay', 'Pension', 'Sat Nischay', 'PDS', 'Monitoring dev work', 'Support to resolve conflict in a ward', 'MNREGA', 'Indira Awas', "Don't know", 'Others scheme knowledge', 'In which schems knowledge you are confident', 'Nal jal', 'Nali-gali', 'Shauchalay', 'Indira awas', 'PDS', 'Electricity to all', 'Ujjwala', 'MNREGA', 'Pension', 'Solar light', 'None', 'Others scheme confidence', 'Tir chap (JDU)', 'Kamal (BJP)', 'Haat (Congress)', 'Laltern (RJD)', 'Haat (Congress)', 'Bungalow (LJP)', 'Telephone (HAM)', 'Naav (VIP)', 'Kite (AIMIM)', 'Not prefer to say', 'Others support party', 'Tir chap (JDU)', 'Kamal (BJP)', 'Haat (Congress)', 'Laltern (RJD)', 'Haat (Congress)', 'Bungalow (LJP)', 'Telephone (HAM)', 'Naav (VIP)', 'Kite (AIMIM)', 'Not prefer to say', 'Others part of party', 'All logistics', 'Party workers campigned for me', 'Helped finance my campaign', 'some leader campigned for me in village')
# #####################################################################################





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