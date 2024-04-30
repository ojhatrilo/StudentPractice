
data1 ={
    "name": "Aravind",
   "salary": 30000,
   "designation":"Analyst"
}

data2 ={
    "name":"Dharani",
    "salary": 35000,
    "designation":"Analyst"
}

details = {
    "data1":data1,
    "data2":data2
}

# print("salary of id 1=",details[1].get("salary"))
# print(details["data2"].get("designation"))


if details["data1"]["salary"] > details["data2"]["salary"]:
    print(details["data2"])

else:
    print(details["data1"])










