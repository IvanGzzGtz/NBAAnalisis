# views.py
from django.shortcuts import render
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguestandingsv3

# def teamStandings(request):
# #     if request.method == "POST":
# #         team = request.POST.get('team')  # Retrieve the selected team from the POST request
# #         print(team)
# #         print(type(team))
# #         # Instantiate the LeagueStandingsV3 class
# #         standings = leaguestandingsv3.LeagueStandingsV3()
# #         # Call the get_request method to fetch data from the NBA API
# #         standings.get_request()
# #         # Access the data retrieved from the API
# #         standings_cleaned = standings.data_sets[0].get_data_frame()  # Assuming the data is stored in the first dataset
# #         print('try')
# #         try:
# #             teamID = standings_cleaned.loc[standings_cleaned['TeamName'] == team, 'TeamID'].iloc[0]
# #             teamX = standings_cleaned[standings_cleaned['TeamID'] == teamID]
# #             return render(request, 'index.html', {'teamX': teamX ,'rows': standings_cleaned.values.tolist(), 'columns': standings_cleaned.columns}) 

# #         except IndexError:
# #             print("here")
# #             error_message = f"No standings found for team: {team}"

# #             return render(request, 'index.html', {'error_message': error_message})
# #     print("here1")
# #     teams_list = teams.get_teams()
# #     teams_list_cleaned = [team['nickname'] for team in teams_list]
# #     return render(request, 'index.html', {'teams_list': teams_list_cleaned})
#     # Instantiate the LeagueStandingsV3 class
#     standings = leaguestandingsv3.LeagueStandingsV3()
#     # Call the get_request method to fetch data from the NBA API
#     standings.get_request()
#     # Access the data retrieved from the API
#     standings_cleaned = standings.data_sets[0].get_data_frame()  # Assuming the data is stored in the first dataset
#     return render(request, 'teamStandings.html', { 'rows': standings_cleaned.values.tolist(), 'columns': standings_cleaned.columns, 'teams_list' : standings_cleaned['TeamName'].tolist() ,'standings_cleaned' : standings_cleaned} ) 

# from django.shortcuts import render
# from django.http import HttpResponse

# def pickTeam(request, team, standings_cleaned):
#     # Your view logic here
#     df = standings[standings_cleaned['TeamName'] == team]

#     return HttpResponse(f"You picked {team}.")

from nba_api.stats.endpoints import leaguestandingsv3
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from nba_api.stats.endpoints import leaguestandingsv3
from django.http import JsonResponse



def fetch_standings_data():
    standings = leaguestandingsv3.LeagueStandingsV3()
    standings.get_request()
    return standings.data_sets[0].get_data_frame()
 


# def teamsStandings(request):
#     standings_cleaned = fetch_standings_data()
#     standings_cleaned = standings_cleaned.sort_values('TeamName')
#     return render(request, 'teamStandings.html', { 
#         'rows': standings_cleaned.values.tolist(), 
#         'columns': standings_cleaned.columns, 
#         'teams_list': standings_cleaned['TeamName'].tolist(),
#         'standings_cleaned': standings_cleaned,
#     })

def teamsStandings(request):
    standings_cleaned = fetch_standings_data()
    standings_cleaned = standings_cleaned.sort_values('TeamName')
    teams_list = standings_cleaned.to_json()

    return JsonResponse(teams_list, safe=False)





def playerstats(request, var):
    standings_cleaned = fetch_standings_data()
    standings_cleaned = standings_cleaned.sort_values('TeamName')
    team_standings = standings_cleaned[standings_cleaned['TeamName'] == var]
    return render(request, 'teamStandings.html', { 
        'rows': team_standings.values.tolist(), 
        'columns': team_standings.columns, 
        'teams_list': team_standings['TeamName'].tolist(),
        'standings_cleaned': standings_cleaned,

    })


def wins(request):
    standings_cleaned = fetch_standings_data()
    standings_cleaned = standings_cleaned.sort_values('WINS', ascending=False)
    yaxis = 'Wins'
    return render(request, 'teamStandings.html', { 
        'rows': standings_cleaned.values.tolist(), 
        'columns': standings_cleaned.columns, 
        'teams_list': standings_cleaned['TeamName'].tolist(),
        'teams_wins': standings_cleaned['WINS'].tolist(),
        'standings_cleaned': standings_cleaned,
        'yaxis': yaxis,
    })