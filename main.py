import requests
print("Welcome to the Valorant Stink Tracker! \n" )
    
name = input("What is your username? Make sure to be case sensitive! \n")
tag = input("What is your tagline? Make sure to be case sensitive!\n ")
print(" ")

extension = ((name)+"/:"+(tag))

url = "/valorant/v3/matches/:region/:"

url = url+extension 