from datetime import datetime
import csv
import os
from report import generate_pdf_report

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
    feedback_lines = []

    try:
        with open("data/set_limit.csv", 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)

            if not rows:
                print("⚠️ No limits set.")
                return

            # Skip empty rows from the end
            for row in reversed(rows):
                if row:
                    last_row = row
                    break
            else:
                print("⚠️ No valid data in limit file.")
                return

            print("Last row:", last_row)

            try:
                date = last_row[0]
                limit_km = float(last_row[1])
                limit_water = float(last_row[2])
                limit_sleep = float(last_row[3])
            except (IndexError, ValueError):
                print("⚠️ Error reading limit values.")
                return

            if record.kmWalked < limit_km:
                short_by = limit_km - record.kmWalked
                feedback = f"🚶 You are short by {short_by:.1f} km. Try to walk more."
                print(feedback)
                feedback_lines.append(feedback)
            else:
                feedback_lines.append("🚶 Great! You met your walking goal.")

            if record.waterDrinked < limit_water:
                short_by = limit_water - record.waterDrinked
                feedback = f"💧 Drink {short_by:.1f} litre(s) more water to meet your goal."
                print(feedback)
                feedback_lines.append(feedback)
            else:
                feedback_lines.append("💧 Well done on drinking enough water.")

            if record.sleephour < limit_sleep:
                short_by = limit_sleep - record.sleephour
                feedback = f"😴 You need {short_by:.1f} more hour(s) of sleep."
                print(feedback)
                feedback_lines.append(feedback)
            else:
                feedback_lines.append("😴 You've had enough sleep. Good job!")

            if (
                record.kmWalked >= limit_km and
                record.waterDrinked >= limit_water and
                record.sleephour >= limit_sleep
            ):
                final_msg = "✅ Great job! You met all your health goals today."
                print(final_msg)
                feedback_lines.append(final_msg)

            # Call PDF report function
            generate_pdf_report(date, record.kmWalked, record.waterDrinked, record.sleephour, feedback_lines)

    except FileNotFoundError:
        print("⚠️ Limit file not found.")


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
    date = datetime.now().strftime('%Y-%m-%d')
    with open ("data/set_limit.csv",'a',newline='') as file:
        

        writer=csv.writer(file)
        writer.writerow([date,walked_limit,water_limit,sleep_limit])