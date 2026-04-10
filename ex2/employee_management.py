import json
file="employees.json"
def load():
   try:
      with open (file,"r")as f:
         return json.load(f)
      except:
         return{}
def save (data):
   with open (file,"w")as f:
      json.dump(data,f,indent=4)
def add_employee(data):
   eid=input("enter employee id:")
   name=input("enter name:")
   basic=float(input("enter basic salary:"))
   data[eid]={"name":name,"basic":basic}
   save(data)
   print("employee added successfully")
def view_employee(data):
   eid=input("enter employee id:")
   if eid in data:
      print(data[eid])
   else:
      print("employee not found")
def calculate_salary(data):
   eid=input("enter employee id")
   if eid in data:
      basic=data[eid]["basic"]
      hra=basic*0.2
      da=basic*0.1
      pf=basic*0.12
      net=basic+hra+da-pf
      print("net salary=",net)
   else:
      print("employee not found")
def delete_employee(data):
   eid=input("enter employee id:")
   if eid in data:
      del data[eid]
      save (data)
      print("employee deleted")
   else:
      print("not found")
def main():
   data=load()
   while True:
      print("\n1.add\n2.view\n3.calculate
