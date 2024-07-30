from employee import Employee
class Manager (Employee):
    def __init__(self,name,salary,departement):
        super().__init__(name,salary)
        self.departement = departement
    def display_info(self):
        print(f"name: {self.name} salary: {self.salary} departement: {self.departement}")