from nba_api.stats.endpoints import leaguestandingsv3
from django.shortcuts import render
import pandas as pd
from django.http import HttpRequest
import json

# def getData(endpoint):
#     request = endpoint
#     request.get_request()
#     return request.data_sets[0].get_dict()

# def headersAsIndex(dic):
#     return [dict(zip(dic["headers"], d)) for d in dic["data"]]

# def sortBy(lst, column):
#     return sorted(lst, key=lambda x: int(x.get(column, 0)), reverse=True)

# def getColumn(dic, column):
#     return [x[column] for x in dic]

# # Team standings 
# def teamsStandings(request, devopmode=False):
#     endpoint = leaguestandingsv3.LeagueStandingsV3()
#     data = getData(endpoint)
#     columns = data["headers"]
#     rows = data["data"]
#     keys_analisis = [
#         "TeamName",
#         "ConferenceRecord Wins",
#         "ConferenceRecord Loses",
#         "PlayoffRank",
#         "DivisionRecord Wins",
#         "DivisionRecord Loses",
#         "DivisionRank",
#         "WINS",
#         "LOSSES",
#         "WinPCT",
#         "LeagueRank",
#         "Record Wins",
#         "Record Loses",
#         "HOME Wins",
#         "HOME Loses",
#         "ROAD Wins",
#         "ROAD Loses",
#         "L10 Wins",
#         "L10 Loses",
#         "Last10Home Wins",
#         "Last10Home Loses",
#         "Last10Road Wins",
#         "Last10Road Loses",
#         "OT Wins",
#         "OT Loses",
#         "ThreePTSOrLess Wins",
#         "ThreePTSOrLess Loses",
#         "TenPTSOrMore Wins",
#         "TenPTSOrMore Loses",
#         "LongHomeStreak",
#         "strLongHomeStreak",
#         "LongRoadStreak",
#         "strLongRoadStreak",
#         "LongWinStreak",
#         "LongLossStreak",
#         "CurrentHomeStreak",
#         "strCurrentHomeStreak",
#         "CurrentRoadStreak",
#         "strCurrentRoadStreak",
#         "CurrentStreak",
#         "strCurrentStreak",
#         "ConferenceGamesBack",
#         "DivisionGamesBack",
#         "ClinchedConferenceTitle",
#         "ClinchedDivisionTitle",
#         "ClinchedPlayoffBirth",
#         "ClinchedPlayIn",
#         "EliminatedConference",
#         "EliminatedDivision",
#         "AheadAtHalf Wins",
#         "AheadAtHalf Loses",
#         "BehindAtHalf Wins",
#         "BehindAtHalf Loses",
#         "TiedAtHalf Wins",
#         "TiedAtHalf Loses",
#         "AheadAtThird Wins",
#         "AheadAtThird Loses",
#         "BehindAtThird Wins",
#         "BehindAtThird Loses",
#         "TiedAtThird Wins",
#         "TiedAtThird Loses",
#         "Score100PTS Wins",
#         "Score100PTS Loses",
#         "OppScore100PTS Wins",
#         "OppScore100PTS Loses",
#         "OppOver500 Wins",
#         "OppOver500 Loses",
#         "LeadInFGPCT Wins",
#         "LeadInFGPCT Loses",
#         "LeadInReb Wins",
#         "LeadInReb Loses",
#         "FewerTurnovers Wins",
#         "FewerTurnovers Loses",
#         "PointsPG",
#         "OppPointsPG",
#         "DiffPointsPG",
#         "vsEast Wins",
#         "vsEast Loses",
#         "vsAtlantic Wins",
#         "vsAtlantic Loses",
#         "vsCentral Wins",
#         "vsCentral Loses",
#         "vsSoutheast Wins",
#         "vsSoutheast Loses",
#         "vsWest Wins",
#         "vsWest Loses",
#         "vsNorthwest Wins",
#         "vsNorthwest Loses",
#         "vsPacific Wins",
#         "vsPacific Loses",
#         "vsSouthwest Wins",
#         "vsSouthwest Loses",
#         "Jan Wins",
#         "Jan Loses",
#         "Feb Wins",
#         "Feb Loses",
#         "Mar Wins",
#         "Mar Loses",
#         "Apr Wins",
#         "Apr Loses",
#         "Oct Wins",
#         "Oct Loses",
#         "Nov Wins",
#         "Nov Loses",
#         "Dec Wins",
#         "Dec Loses",
#         "Score_80_Plus Wins",
#         "Score_80_Plus Loses",
#         "Opp_Score_80_Plus Wins",
#         "Opp_Score_80_Plus Loses",
#         "Score_Below_80 Wins",
#         "Score_Below_80 Loses",
#         "Opp_Score_Below_80 Wins",
#         "Opp_Score_Below_80 Loses",
#         "TotalPoints",
#         "OppTotalPoints",
#         "DiffTotalPoints",
#         "LeagueGamesBack",
#         "PlayoffSeeding",
#         "ClinchedPostSeason",
#     ]
#     context = {
#         "columns": columns,
#         "rows": rows,
#         "keys_analisis": keys_analisis,
#     }
#     if devopmode:
#         return JsonResponse(json.dumps(headersAsIndex(data), indent=4), safe=False)
#     else:
#         return render(request, "teamStandings.html", context)

# def teamsStandingsColumn(request, column, devopmode=False):
#     dic = getData(leaguestandingsv3.LeagueStandingsV3())
#     data_not_clean = headersAsIndex(dic)
#     analysis_data = cleanTeamsStandings(data_not_clean)
#     sorted_data = sortBy(analysis_data, column)
#     teams = getColumn(sorted_data, "TeamName")
#     column_as_list = getColumn(sorted_data, column)
#     context = {
#         "XaxisLabels": teams,
#         "YaxisLabel": column,
#         "sorted_data": column_as_list,
#     }
#     if devopmode:
#         return JsonResponse(json.dumps(context, indent=4), safe=False)
#     else:

#         return render(request, "teamStandings.html", context)



# def cleanTeamsStandings(data_not_clean):
#     data_clean = []
#     keys_to_delete = [
#         "LeagueID",
#         "SeasonID",
#         "TeamID",
#         "TeamSlug",
#         "ClinchIndicator",
#         "TeamCity",
#         "Conference",
#         "Division",
#     ]
#     for data in data_not_clean:
#         new_data = {}
#         for key, value in data.items():
#             # if value is not None:  Check if value is not None
#             if isinstance(value, (int, float, str)):
#                 # Check if value is numeric (int or float), or if it's a string containing only digits (potential float)
#                 if key not in keys_to_delete:
#                     if isinstance(value, str):
#                         if "W" in value or "L" in value:
#                             # Extract the numeric part from the value if it's in the format 'W 2' or 'L 3'
#                             parts = value.split()
#                             if len(parts) == 2:
#                                 streak_number = int(parts[1])
#                                 # Assign positive or negative sign based on 'W' or 'L'
#                                 if "W" in value:
#                                     streak_number = abs(streak_number)
#                                 elif "L" in value:
#                                     streak_number = -abs(streak_number)
#                                 # Assign the modified streak number to the key
#                                 new_data[key] = streak_number
#                             else:
#                                 # If the value doesn't have the expected format, keep the original value
#                                 new_data[key] = value
#                         elif "-" in value:
#                             # Split the value by the hyphen if it's in the format '50-12'
#                             parts = value.split("-")
#                             if len(parts) == 2:
#                                 new_data[key + " Wins"] = parts[0]
#                                 new_data[key + " Loses"] = parts[1]
#                             else:
#                                 # If the value doesn't have the expected format, keep the original value
#                                 new_data[key] = value
#                         else:
#                             # If no 'W', 'L', or '-', keep the original value
#                             new_data[key] = (
#                                 int(value.strip()) if value.strip().isdigit() else value
#                             )
#                     else:
#                         # If the value is not a string, keep the original column
#                         new_data[key] = value
#             else:
#                 # If the value is not a string, keep the original column
#                 new_data[key] = 0
#         data_clean.append(new_data)

#     # Now data_clean contains the modified data with specified keys removed and new columns created if necessary
#     return data_clean




def teamsStandings(request):
    # Replace empty values with NaN
    pd.set_option('display.max_columns', None)
    endpoint = leaguestandingsv3.LeagueStandingsV3() ## Replace this module class
    endpoint.get_request()
    #Request info as a dataframe
    request_dataframe = endpoint.data_sets[0].get_data_frame()
    #Clean dataframe for data anlisis
    columns_to_delete = [
                            'LeagueID', 'SeasonID', 'TeamID', 'TeamCity', 'TeamSlug','PlayoffRank', 
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
    return render(request, "teamStandings.html", context)