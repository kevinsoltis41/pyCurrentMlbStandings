import urllib2
import json
from Division import *
from Team import *


def Display_Division_Standings():	
	teams = []
	divisions = []
	
	site = 'https://erikberg.com/mlb/standings.json'
	req = urllib2.Request(site, headers={'User-Agent' : "Magic Browser"})
	con = urllib2.urlopen( req )
	page = con.read()
	
	jsonTeams = json.loads(page)
	
	
	AmericanCentral = Division('American', 'Central')
	AmericanEast = Division('American', 'East')
	AmericanWest = Division('American', 'West')
	NationalCentral = Division('National', 'Central')
	NationalEast = Division('National', 'East')
	NationalWest = Division('National', 'West')

	for team in jsonTeams['standing']:
		teams.append(Team(team['rank'], team['won'], team['lost'], team['streak'], team['first_name'], team['last_name'], 
						  team['team_id'], team['games_back'], team['points_for'], team['points_against'], 
						  team['home_won'], team['home_lost'], team['away_won'], team['away_lost'], team['conference_won'], 
						  team['conference_lost'], team['last_five'], team['last_ten'], team['conference'], 
						  team['division'], team['games_played']))

	for t in teams:
		if (t.conference == 'AL' and t.division == 'C'):
			AmericanCentral.addTeam(t)
		elif (t.conference == 'AL' and t.division == 'E'):
			AmericanEast.addTeam(t)
		elif (t.conference == 'AL' and t.division == 'W'):
			AmericanWest.addTeam(t)
		elif (t.conference == 'NL' and t.division == 'C'):
			NationalCentral.addTeam(t)
		elif (t.conference == 'NL' and t.division == 'E'):
			NationalEast.addTeam(t)
		elif (t.conference == 'NL' and t.division == 'W'):
			NationalWest.addTeam(t)

	divisions.append(AmericanCentral)
	divisions.append(AmericanEast)
	divisions.append(AmericanWest)
	divisions.append(NationalCentral)
	divisions.append(NationalEast)
	divisions.append(NationalWest)

	for d in divisions:
		print(d.printDivision())

Display_Division_Standings()
