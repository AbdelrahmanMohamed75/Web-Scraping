# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup
import csv


url="https://www.yallakora.com/match-center/%D9%85%D8%B1%D9%83%D8%B2-%D8%A7%D9%84%D9%85%D8%A8%D8%A7%D8%B1%D9%8A%D8%A7%D8%AA?date=1/31/2024#"

respond=requests.get(url)

html_content=respond.content

soup=BeautifulSoup(html_content,"html.parser")

championchip=soup.find_all('div',class_='matchCard')

# print(championchip[0].contents)

championchip_title=championchip[0].contents[1].find('h2').text.strip()




for i in range(len(championchip)):
    print(championchip[i].contents[1].find('h2').text.strip())

    matchs=championchip[i].contents[3].find_all('div',class_='teamsData')
    for j in range(len(matchs)):
        teamA=matchs[j].find('div',class_='teams teamA').text.strip()
        teamB=matchs[j].find('div',{'class':'teams teamB'}).text.strip()
        result=matchs[j].find('div',class_='MResult').find_all('span',class_='score')
        score=f"{result[0].text.strip()} - {result[1].text.strip()}"
        time=matchs[j].find('div',class_='MResult').find('span',class_='time').text.strip()
        print(f" {teamA} {score} {teamB}\n\t{time}")
        print(20*"_")

