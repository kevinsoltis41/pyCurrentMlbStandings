# import urllib2
# import json

# class Team:
# 	def __init__(self, abb, fn, ln, conf, div, city, state, fullnm):
# 		self.abbreviation = abb
# 		self.firstName = fn
# 		self.lastName = ln
# 		self.conference = conf
# 		self.division = div
# 		self.city = city
# 		self.state = state
# 		self.fullName = fullnm

# 	def toString(self):
# 		return self.fullName


# site = 'https://erikberg.com/mlb/teams.json'
# req = urllib2.Request(site, headers={'User-Agent' : "Magic Browser"})
# con = urllib2.urlopen( req )
# page = con.read()
# jsonTeams = json.loads(page)
# teams = []

# for t in jsonTeams:
# 	teams.append(Team(t['abbreviation'], t['first_name'], t['last_name'], t['conference'],
# 		          t['division'], t['city'], t['state'], t['full_name']))



import urllib2
import json

class Division:
	def __init__(self, league, div):
		self.league = league
		self.division = div
		self.teamList = []

	def addTeam(self, team):
		self.teamList.append(team)

	def printDivision(self):
		returnString = '##############################\n'
		returnString += '#\t' + self.league.upper() + ' ' + self.division.upper() + '\n'
		for t in self.teamList:
			returnString += '#\t  (' + str(t.gamesBack) + ') ' + t.toString() + ' -- (' + str(t.won) + ')/(' + str(t.lost) + ')\n'
		returnString += '##############################'

		return returnString

class Team:
	def __init__(self, rank, won, lost, streak, fn, ln, tid, gb, pf, pa, hw, hl, aw, al, cw, cl, lv, lt, conf, div, gp):		
		self.rank = rank
		self.won = won
		self.lost = lost
		self.streak = streak
		self.firstName = fn
		self.lastName = ln
		self.team_id = tid
		self.gamesBack = gb
		self.pointsFor = pf
		self.pointsAgainst = pa
		self.homeWon = hw
		self.homeLost = hl
		self.awayWon = aw
		self.awayLost = al
		self.conferenceWon = cw
		self.conferenceLost = cl
		self.lastFive = lv
		self.lastTen = lt
		self.conference = conf
		self.division = div
		self.gamesPlayed = gp
		self.pointsScoredPerGame = self.pointsFor / self.gamesPlayed
		self.pointsAllowedPerGame = self.pointsAgainst / self.gamesPlayed
		self.winPercentage = self.won / self.gamesPlayed
		self.pointDifferential = self.pointsFor - self.pointsAgainst
		self.pointDifferentialPerGame = self.pointDifferential / self.gamesPlayed

	def toString(self):
		return self.firstName + ' ' + self.lastName

def Main():	
	site = 'https://erikberg.com/mlb/standings.json'
	req = urllib2.Request(site, headers={'User-Agent' : "Magic Browser"})
	con = urllib2.urlopen( req )
	page = con.read()

	jsonTeams = json.loads(page)

	teams = []
	divisions = []

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

Main()
