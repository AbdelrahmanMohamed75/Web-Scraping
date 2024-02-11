# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from bs4 import BeautifulSoup
import csv
from itertools import zip_longest

jop_title = []
company_name = []
location_name = []
jop_skill = []
links=[]
result = requests.get("https://wuzzuf.net/a/IT-Software-Development-Jobs-in-Egypt?ref=browse-jobs")

src = result.content
soup = BeautifulSoup(src, "lxml")

jop_titles = soup.find_all("h2", {"class": "css-m604qf"})
company_names = soup.find_all("a", class_="css-17s97q8")
location_names = soup.find_all("span", class_="css-5wys0k")
jop_skills = soup.find_all("div", {"class": "css-y4udm8"})

for i in range(len(jop_titles)):
    jop_title.append(jop_titles[i].text)
    links.append(jop_titles[i].find("a").attrs["href"])
    company_name.append(company_names[i].text)
    location_name.append(location_names[i].text)
    jop_skill.append(jop_skills[i].text)

file_list=[jop_title,company_name,location_name,jop_skill,links]
exported=zip_longest(*file_list)
with open(r"D:\work\New Microsoft Excel Worksheet.xlsx", "w") as bedoEmam:
    wr = csv.writer(bedoEmam)
    wr.writerow(["jop title", "company name", "location", "skills","links"])
    wr.writerows(exported)

