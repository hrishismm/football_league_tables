#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import requests
import pandas as pd
from bs4 import BeautifulSoup



print("\n1)Premier League\n2)Champoions League\n3)La-liga\n4)Serie A\n5)Bundesliga")
#To get input from  the user
choice=int(input("Enter your choice:"))
if(choice==1):
    a="premier-league-table"
elif(choice==2):
    a="champions-league-table"
elif(choice==3):
    a="la-liga-table"
elif(choice==4):
    a="serie-a-table"
elif(choice==5):
    a="bundesliga-table"

#Input for the particular season
print("Pleaase Note:Data Available from 2008-09 season onwards")
year=str(input("Enter the league season(Eg:2011-12):"))
year=year[:4]

#Adding the user inputs to the url
url="https://www.skysports.com/"+a+"/"+year

#Getting the url
res=requests.get(url)

#To check if the url is working you get 200
#print(res.status_code) 

#Using Beautiful Soup to get only the required text
bs4=BeautifulSoup(res.text,"lxml")

#To get data under tbody tag
head=bs4.find_all("tbody")

#Creating empty list which would have a dictionary inside it
league=[]

for heading in head:
    #finding all the elements with tr tag within tbody
    rows=heading.find_all("tr")
    for row in rows:
        """To find the desired td tag inside the tr tags which are inside tbody
        Indexing based on the position of class name  
        """
        Team=row.find("td",{"class":"standing-table__cell standing-table__cell--name"}).text.strip()
        Pl=row.find_all("td",{"class":"standing-table__cell"})[2].text.strip()
        W=row.find_all("td",{"class":"standing-table__cell"})[3].text.strip()
        D=row.find_all("td",{"class":"standing-table__cell"})[4].text.strip()
        L=row.find_all("td",{"class":"standing-table__cell"})[5].text.strip()
        F=row.find_all("td",{"class":"standing-table__cell"})[6].text.strip()
        A=row.find_all("td",{"class":"standing-table__cell"})[7].text.strip()
        GD=row.find_all("td",{"class":"standing-table__cell"})[8].text.strip()
        team_points=row.find_all("td",{"class":"standing-table__cell"})[9].text.strip()
        #Creating a dictionary
        league_dict={"Name":Team,"Pl":Pl,"W":W,"D":D,"L":L,"F":F,"A":A,"GD":GD,"P":team_points}
        #Appending the dictionary to the list
        league.append(league_dict)
 
#Creating the dataframe to display the final o/p to the user        
df=pd.DataFrame(data=league)
print(df)
