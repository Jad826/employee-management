class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display_info(self):
        print(f"name: {self.name} salary: {self.salary}") 