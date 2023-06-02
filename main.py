import requests
import json

a1 = "https://api.henrikdev.xyz/valorant/v1/account"
a2 = "https://api.henrikdev.xyz/valorant/v1/mmr"
a3 = "https://api.henrikdev.xyz/valorant/v3/matches"
a4 = "https://api.henrikdev.xyz/valorant/v1/content"

print("______________________________________________________________________________________\n")
print("Welcome to the Valorant Information Center!")
print("______________________________________________________________________________________\n")
user = input ("What is your Valorant username? \n")
tag = input("What is your Valorant tag? \n")
region = input("What is your region? (eu,na,kr,ap) \n")

a1 = a1 + "/" + user
a1 = a1 + "/" + tag

a2 = a2 + "/" + region
a2 = a2 + "/" + user
a2 = a2 + "/" + tag

a3 = a3 + "/" + region
a3 = a3 + "/" + user
a3 = a3 + "/" + tag

r = requests.get(a1)
s1 = json.loads(r.text)

t = requests.get(a2)
s2 = json.loads(t.text)

xd = requests.get(a3)
s3 = json.loads(xd.text)

pm = requests.get(a4)
s4 = json.loads(pm.text)

while True:

    print("______________________________________________________________________________________")
    check = input ("What would you like to check? Press 'n' if you want to quit!\n")
    
    if check == "n":
        print("Thanks for using the Valorant Tracker!")
        print("______________________________________________________________________________________")

        break

    if check == ("level"):
        print(s1['data']['account_level'])
    
    if check == ("elo"):
        print(s2['data']['elo'])

    if check == ("banner"):
        print(s1['data']['card']['large'])
    
    if check == ("rank"):
        print(s2['data']['currenttierpatched'])
        print(s2['data']['images']['small'])
    
    if check == ("mchange"):
        print(s2['data']['mmr_change_to_last_game'])
        if ((s2['data']['mmr_change_to_last_game']) < 1):
            print ("L")

    if check == ("rit"):
        print(s2['data']['ranking_in_tier'])

    if check == ("prevmatch"):
        match_data = s3['data'][0]  

        map = match_data['metadata']['map'] 
        mode = match_data['metadata']['mode']
        rounds = match_data['metadata']['rounds_played']
        game_length = match_data['metadata']['game_length']
        date = match_data['metadata']['game_start_patched']
        minutes = int(game_length) // 60

        print('Mode:', mode)
        print('Date:', date)
        print("Map:", map)
        print("Rounds played:", rounds)
        print("Length of Match:", minutes, "minutes")

        
           
