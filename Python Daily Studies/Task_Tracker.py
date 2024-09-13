# import json
# data = open("data.json","r")
# data1 = json.load(data)
# print(data1['HELLO'])



import json
# from enum import Enum

# class Status(Enum):
#     COMPLETED = 1
#     PENDING = 2
  

# # Creating Task
# def Create_Task():
#     id = int(input("Enter your id:"))
#     Task = input("Enter your Task:")
#     print('''To insert task update
#           1. COMPLETED
#           2. PENDING''')
#     Task_Status = int(input("Enter task update:"))
#     if Task_Status == 1:
#         Task_Status = Status(1).name
#     elif Task_Status == 2:
#         Task_Status = Status(2).name

#     exact_data = open("data.json",'+a')
#     data = {
#         "id": id,
#         "Task": Task,
#         "Task_Status": Task_Status
#         }
#     info = json.dumps(data)
#     exact_data.write(info,",")


# Create_Task()



# Read Task
def Read_Task():
    id = int(input("Enter the number:"))-1
    data = open("data.json", "r")
    data1 = json.load(data)
    print(data1[id])


Read_Task()





    


    
    # with open('data.json', 'r+') as file:
    #     data = json.load(file)
    #     data['Tasks'].append(Task)


















