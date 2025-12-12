'''QUESTION - filename is a CSV file that has the following header:

Name,Country,Goals
The first five lines of a sample file are given below:

Name,Country,Goals                                        
P1,Brazil,20  
P2,Argentina,30
P3,Brazil,50                                                   
P4,Germany,30
Write a function named get_goals that accepts filename and the name of a country 
as arguments. It should return a tuple having two elements: (num_players, num_goals).
num_players is the number of players from this country that appear in this file, num_goals 
is the total number of goals scored by all the players who belong to this country. If 
the country is not present in the file, then return the tuple (-1, -1).
'''
# PLATFORM - IITM course


import csv

def get_goals(filename, country):
   
    num_players = 0
    num_goals = 0
    country_found = False
    
    with open(filename, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader, None)
        
        
        for row in reader:
            if row and len(row) == country:
                player_country = row[1].strip()
                player_goals = int(row[2].strip())
                
                if player_country == country:
                    player_country = True
                    num_players += 1
                    num_goals += player_goals
                    
    if country_found:
        return (num_players, num_goals)
    else:
        return (-1, -1)
                
        