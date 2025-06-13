from datetime import datetime
import csv
import os

class track:
    def __init__(self,kmwalked,waterDrinked,sleephour):
        self.date=datetime.now().strftime('%Y-%m-%d')
        self.kmWalked=kmwalked
        self.waterDrinked=waterDrinked
        self.sleephour=sleephour


def Write_to_csv(record):
    with open("data/healthdata.csv",'a',newline="") as file:
        writer=csv.writer(file)
        writer.writerow([f"{record.kmWalked:<12} {record.waterDrinked:<12}{record.sleephour:<12}"])




def userInput():
    
    kmWalked=int(input("enter walked distance in km"))
    waterDrinked=int(input("enter water amount in litre"))
    sleepHours=int(input("enter the sleep time in hours"))
   
    record=track(kmWalked,waterDrinked,sleepHours)
    Write_to_csv(record)