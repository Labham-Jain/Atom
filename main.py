# Importing datetime module to use time functionality...
from datetime import datetime

# Importing sqlite3 Module To Connect With Database
import sqlite3

# Importing Atom Module Which Is Part Of This Project. Atom Module Provides Speech Recognition And Speech Synthesis.
from modules.atom import Atom

# Importing os Module
import os

# Importing Webbrowser Module
import webbrowser as wb

# Importing wikisearch Module
from modules.wikisearch import wikipediaSummary

# Importing sys Module
import sys

# Importing Flappy Bird Game Dev. By CodeWithHarry (YT Channel)
from modules.Games.flappy_bird import FlappyBird

# Creating Instance Of Atom
atom = Atom()


# Connecting With Database
connection = sqlite3.connect('sqlite_database.db')
cursor = connection.cursor()


def insert_Database(Command, Task):
    query = (f"INSERT INTO 'Commands' VALUES('{Command}','{Task}')")
    cursor.execute(query)
    connection.commit()
    print("Done!!!")


def time():
    time = f"""Time Is : {datetime.now().strftime("%H hours %M minutes")}"""
    atom.Speak(time)
    print(time)


while True:
    recogText = atom.voiceRecognition()
    recogText = recogText.lower()
    query = f"""SELECT * FROM 'Commands'"""
    cursor.execute(query)
    for row in cursor.fetchall():
        if row[0] in recogText:
            exec(row[1])
            atom.Speak(row[2])
            break
