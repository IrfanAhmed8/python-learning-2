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
        writer.writerow([record.date,record.kmWalked, record.waterDrinked, record.sleephour])


def comment_on_input(record):
    print("\n📝 Daily Feedback:")
    
    if record.kmWalked < 8:
        short_by = 8 - record.kmWalked
        print(f"🚶 You are short by {short_by} km. Try to walk more.")

    if record.waterDrinked < 3:
        short_by = 3 - record.waterDrinked
        print(f"💧 Drink {short_by} litre(s) more water to meet your goal.")

    if record.sleephour < 7:
        short_by = 7 - record.sleephour
        print(f"😴 You need {short_by} more hour(s) of sleep.")

    if (
        record.kmWalked >= 8 and
        record.waterDrinked >= 3 and
        record.sleephour >= 7
    ):
        print("✅ Great job! You met all your health goals today.")



def userInput():
    
    kmWalked=int(input("enter walked distance in km"))
    waterDrinked=int(input("enter water amount in litre"))
    sleepHours=int(input("enter the sleep time in hours"))
   
    record=track(kmWalked,waterDrinked,sleepHours)
    comment_on_input(record)
    Write_to_csv(record)