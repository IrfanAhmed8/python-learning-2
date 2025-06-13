import matplotlib.pyplot as plt
import numpy as np
import csv

def water_consumption_graph(path_file):
    dates = []
    waterconsumption = []
    sleephours=[]
    kmwalked=[]
    

    with open(path_file, 'r') as file:
        reader = csv.reader(file)
        

        for row in reader:
            
            if len(row) >= 3:
                try:
                    date = row[0].strip()
                    water = float(row[2].strip())
                    sleephour=float(row[3])
                    walked=float(row[1])
                    dates.append(date)
                    waterconsumption.append(water)
                    sleephours.append(sleephour)
                    kmwalked.append(walked)
                except ValueError as e:
                    print(f"Skipping row due to error: {row} ({e})")


    if not dates:
        print("⚠️ No valid data to plot.")
        return

    fig,axs=plt.subplots(3,1,figsize=(10,8))



    axs[0].bar(dates, waterconsumption, color='skyblue')
    axs[0].set_title("Daily Water Consumption")
    axs[0].set_ylabel("Litres")
    axs[0].grid(True, linestyle='--', alpha=0.6)

    
    axs[1].plot(dates, sleephours, marker='o', linestyle='--', color='purple')
    axs[1].set_title("Daily Sleep Duration")
    axs[1].set_ylabel("Hours Slept")
    axs[1].grid(True, linestyle='--', alpha=0.6)

   
    axs[2].plot(dates, kmwalked, marker='s', linestyle='-', color='green')
    axs[2].set_title("Daily Distance Walked")
    axs[2].set_ylabel("Kilometers")
    axs[2].set_xlabel("Date")
    axs[2].grid(True, linestyle='--', alpha=0.6)
    axs[2].tick_params(axis='x', rotation=45)

    plt.tight_layout()
    plt.show()