from track import track,userInput,set_limit
from visual import water_consumption_graph

path_file="data/healthdata.csv"
print("1.)set limit for task \n2.)add todays workout\n3.)view graph\n4.)Exit")
taskKey=int(input("Enter the key for task"))

while(taskKey):
    if(taskKey==1):
        print("Enter the task limit")
        set_limit()
        taskKey=int(input("Enter the key for task"))


    elif(taskKey==2):
        userInput()
        taskKey=int(input("Enter the key for task"))

    elif(taskKey==3):
        water_consumption_graph(path_file)
        taskKey=int(input("Enter the key for task"))


    else:
        exit()