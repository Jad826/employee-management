import employee
from Manager import Manager
name = input("Enter the name of the employee : ")
salary = int(input("Enter the salary of the employee : "))
departement = input ("Enter the departement of the employee : ")
m = Manager(name,salary,departement)
m.display_info()
