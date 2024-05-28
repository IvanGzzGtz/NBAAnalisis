

import pandas as pd
from nba_api.stats.endpoints import leaguestandingsv3
import json 

# Replace empty values with NaN
pd.set_option('display.max_columns', None)
import pdb; pdb.set_trace()
endpoint = leaguestandingsv3.LeagueStandingsV3() ## Replace this module class
print(endpoint.keys())
endpoint.get_request()
#Request info as a dataframe
request_dataframe = endpoint.data_sets[0].get_data_frame()
#Clean dataframe for data anlisis
columns_to_delete = [
                        'LeagueID',  'TeamCity', 'TeamSlug','PlayoffRank', 
                        'ClinchIndicator', 'DivisionRank', 'WinPCT','LeagueRank', 'Record',
                        'Record', 'strLongHomeStreak', 'strLongRoadStreak', 'strCurrentHomeStreak',
                        'strCurrentRoadStreak','strCurrentStreak', 'ClinchedConferenceTitle', 'ClinchedDivisionTitle',
                        'ClinchedPlayoffBirth', 'ClinchedPlayIn', 'EliminatedConference',
                        'EliminatedDivision','OppOver500', 'LeadInFGPCT', 'LeadInReb',
                        'FewerTurnovers', 'DiffPointsPG','LeagueGamesBack',
                        'PlayoffSeeding', 'ClinchedPostSeason','May', 'Jun',
                        'Jul', 'Aug', 'Sep',   'Opp_Score_80_Plus', 'Score_Below_80', 'Opp_Score_Below_80',
                    ]
request_dataframe = request_dataframe.drop(columns_to_delete, axis=1)
columns_as_list = {}
for column in request_dataframe:
    ###Column_list represents each column data
    column_list = request_dataframe[column].to_list() 
    ### All columns with each column as a key in a dictonary and its data as a value 
    columns_as_list[column] =  column_list
    # Convert integer values to strings and check for hyphen
# Check if any value in the column contains '-'
    if any('-' in str(value) for value in request_dataframe[column]):
        # print(f"Processing - in column: '{column}'")
        # Convert values to strings and split them by '-'
        split_values = request_dataframe[column].astype(str).str.split('-', expand=True)
        # Assign the split values to new columns
        request_dataframe[f'{column}_wins'] = split_values[0]
        request_dataframe[f'{column}_loses'] = split_values[1]
        # Drop the original column
        request_dataframe.drop(column, axis=1, inplace=True)
    else:
        # print(f"No any - found in column: '{column}'")
        pass
# Assuming request_dataframe is your DataFrame
columns_to_convert = []
# Iterate through columns to identify which ones can be converted to float
for column in request_dataframe:
    try:
        # Attempt to convert the column to float
        request_dataframe[column] = pd.to_numeric(request_dataframe[column])
    except ValueError:
        # If conversion fails, print a message indicating the column
        print(f"Column '{column}' could not be converted to float.")
# Now, convert the identified columns to float
request_dataframe[columns_to_convert] = request_dataframe[columns_to_convert].astype(float)

columns_as_list = {column: request_dataframe[column].tolist() for column in request_dataframe.columns}

# Convert NaN values to None
for key, value in columns_as_list.items():
    columns_as_list[key] = [None if pd.isna(v) else v for v in value]

# Convert dictionary to JSON
json_data = json.dumps(columns_as_list)
context = {
    'columns': request_dataframe.columns.tolist(),
    'rows': request_dataframe.values.tolist(),
    'keys_analisis':columns_as_list.keys(),
    'columns_as_list': columns_as_list,
    'json_data':json_data
}