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
    with open("data/set_limit.csv",'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

        if rows:
            last_row = rows[-1]
            print("Last row:", last_row)
            try:
                limit_km = float(last_row[1])
                limit_water = float(last_row[2])
                limit_sleep = float(last_row[3])
            except (IndexError, ValueError):
                print("⚠️ Error reading limit values.")
                return
        

    
            if record.kmWalked < limit_km:
                short_by = 8 - record.kmWalked
                print(f"🚶 You are short by {short_by} km. Try to walk more.")

            if record.waterDrinked < limit_water:
                short_by = 3 - record.waterDrinked
                print(f"💧 Drink {short_by} litre(s) more water to meet your goal.")

            if record.sleephour < limit_sleep:
                short_by = 7 - record.sleephour
                print(f"😴 You need {short_by} more hour(s) of sleep.")

            if (
                record.kmWalked >= limit_km and
                record.waterDrinked >= limit_water and
                record.sleephour >= limit_sleep
            ):
                print("✅ Great job! You met all your health goals today.")



def userInput():
    
    kmWalked=int(input("enter walked distance in km"))
    waterDrinked=int(input("enter water amount in litre"))
    sleepHours=int(input("enter the sleep time in hours"))
   
    record=track(kmWalked,waterDrinked,sleepHours)
    comment_on_input(record)
    Write_to_csv(record)


def set_limit():
    water_limit=int(input("set water limit"))
    sleep_limit=int(input("set sleep limit"))
    walked_limit=int(input("set walked distance limit"))
    with open ("data/set_limit.csv",'a') as file:
        

        writer=csv.writer(file)
        writer.writerow([walked_limit,water_limit,sleep_limit])