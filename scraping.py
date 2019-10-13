import requests
import re
from pymongo import MongoClient
from bs4 import BeautifulSoup

import csv

def deleteSpace(string):
    start = 0
    end = len(string)-1
    module = " \n\r"
    while start <= end and string[start] in module:
        start += 1
    while start <= end and string[end] in module:
        end -= 1
    if start == end:
        return "null"
    return string[start:end+1]

def processAlgorithm(string):
    items = string.split(',')
    res = ""
    for item in items:
        res = res  + deleteSpace(item) + ";"
    return res[0:len(res)-1]


def getBsObj(url, writer, Id_tag):
    session = requests.Session()
    headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36", 
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"}
    req = session.get(url, headers=headers)
    bsObj = BeautifulSoup(req.text,'html.parser')
    y = 1
    for sibling in bsObj.find("div",{"class":"datatable"}).tr.next_siblings:
        #print(sibling)
        if y%2 == 0:
            Id = sibling.find("td",{"class":"id"}).get_text()
            name = sibling.find("div",{"style":"float: left;"}).get_text()
            algorithms = sibling.find("div",{"style":"float: right; font-size: 1.1rem; padding-top: 1px; text-align: right;"}).get_text()
            if sibling.find("span",{"title":"Difficulty"}) == None:
                difficulty = 2200
            else:
                difficulty = sibling.find("span",{"title":"Difficulty"}).get_text()
            

            Id = deleteSpace(Id)
            name = deleteSpace(name)
            algorithms = processAlgorithm(algorithms)
            if algorithms == "":
                algorithms="null"
            # print(Id, name, algorithms, difficulty)
            writer.writerow([Id_tag, Id, name, algorithms, difficulty])
            Id_tag = Id_tag+1
        y = y + 1
    return bsObj


#def getMongoDB_ProblemSet():
#    connection = MongoClient("127.0.0.1", 27017)
#    db = connection.cloud
#    problem_set = db.problem_set
#    return problem_set

with open("problemset.csv","w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Id_tag", "Id", "Name","Algorithms","Difficulty"])
    url = "http://codeforces.com/problemset/page/"
    Id_tag = 0
    for page in range(1, 56):
        getBsObj(url + str(page), writer, Id_tag)
        Id_tag = Id_tag + 100
    


