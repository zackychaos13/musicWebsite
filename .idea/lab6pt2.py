# Lab 6
# Author: Zack Lutz
# Date: May 14, 2020
# Purpose: Creates web page to display favorite artists

from flask import Flask
import datetime

app = Flask(__name__)

def musicH1(myString): # Use of heading 1 style
    newString = '<H1>' + myString + '</H1>'
    return newString

def musicH2(myString): # Use of heading 2 style
    newString = '<H2>' + myString + '</H2>'
    return newString

def favoriteArtist(): # creates ordered list of artists
    list1 = "<ol type='1'>"
    list1 += "<!-- List not in order -->"
    list1 += "</li>Every Time I Die, </li>"
    list1 += "</li>Frank Ocean, </li>"
    list1 += "</li>Norma Jean, </li>"
    list1 +="</li>The Chariot, </li>"
    list1 += "</li>Tyler, the Creator</li>"
    list1 += "</ol>"
    return list1

def favoriteAlbum(): # creates unordered list of artists
    list2 = "<ul style='list-style-type:disc'>"
    list2 += "<li>Low Teens by Every Time I Die</li>"
    list2 += "<li>Blond by Frank Ocean</li>"
    list2 += "<li>One Wing by The Chariot</li>"
    list2 += "<li>It Hates You by He Is Legend</li>"
    list2 += "<li>M3LL155X by FKA Twigs</li>"
    list2 += "</ul>"
    return list2

def bandLinks(): # displays artists wiki page
    list3 = "<!-- Use Wikipedia for artist info -->"
    list3 += "<a href='https://en.wikipedia.org/wiki/Every_Time_I_Die'>Every Time I Die, </a>"
    list3 += "<a href='https://en.wikipedia.org/wiki/Frank_Ocean'>Frank Ocean, </a>"
    list3 += "<a href='https://en.wikipedia.org/wiki/Norma_Jean_(band)'>Norma Jean, </a>"
    list3 += "<a href='https://en.wikipedia.org/wiki/The_Chariot_(band)'>The Chariot, </a>"
    list3 += "<a href='https://en.wikipedia.org/wiki/Tyler,_the_Creator'>Tyler, the Creator </a>"
    list3 += "</ul>"
    return list3

def musicHead(): # starts webpage # gives title
    date = datetime.date.today().strftime('%d:%m:%y') # displays time

    headData = "<!DOCTYPE html> "
    headData +="<head> "
    headData += date
    headData +="<title>Zacks Favorite Music</title>"
    headData +="</head>"
    headData +="<body>"
    return headData

def musicEnd(): # ends page
    endData = "</body>"
    endData += "</html>"
    return endData

@app.route('/') # creates URL
def greeting(): # builds website
    myGreeting = musicHead();
    myGreeting += musicH1('Zacks Favorite Music')
    myGreeting += "<!-- Brief paragraph to introduce fave music -->"
    myGreeting += "<p>My music taste is eclectic, which is represented</p> " \
                  "</p>by the artists I have listed. Even though I grew up a metal</p>" \
                  "</p>head, I am open to all types. Below are some of my favorite artists,</p>" \
                  "</p>favorite albums, and links to learn more.</p>"
    myGreeting += musicH2("My Favorite Artists")
    myGreeting += favoriteArtist()
    myGreeting += musicH2('My Favorite Albums')
    myGreeting += favoriteAlbum()
    myGreeting += musicH2("Artist Links")
    myGreeting += bandLinks()
    return myGreeting

app.run() # runs website