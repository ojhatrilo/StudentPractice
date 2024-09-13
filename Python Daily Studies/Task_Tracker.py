# import json
# data = open("data.json","r")
# data1 = json.load(data)
# print(data1['HELLO'])



import json
from enum import Enum

class Status(Enum):
    COMPLETED = 1
    PENDING = 2
  

# Creating Task
# def Create_Task():
    # id = int(input("Enter your id:"))
    # Task = input("Enter your Task:")
    # print('''To insert task update
    #       1. COMPLETED
    #       2. PENDING''')
    # Task_Status = int(input("Enter task update:"))
    # if Task_Status == 1:
    #     Task_Status = Status(1).name
    # elif Task_Status == 2:
    #     Task_Status = Status(2).name

    # exact_data = open("data.json",'+a')
    # file = json.load(exact_data)
    # data = {
    #     "id": id,
    #     "Task": Task,
    #     "Task_Status": Task_Status
    #     }
    # file["Task_Schedule"].append(data)
    # json.dump(file,indent=4)
    # exact_data.close()
def write_json(new_data, filename='data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["emp_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

y = {"emp_name":"Nikhil",
     "email": "nikhil@geeksforgeeks.org",
     "job_profile": "Full Time"
    }
    
write_json(y) 






# Read Task
# def Read_Task():
#     id = int(input("Enter the number:"))-1
#     data = open("data.json", "r")
#     data1 = json.load(data)
#     print(data1[id])


# Read_Task()





    


    
    # with open('data.json', 'r+') as file:
    #     data = json.load(file)
    #     data['Tasks'].append(Task)


















