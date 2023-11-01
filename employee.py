class employee():
    def __init__(self,name,id,dept,sal):
        self.name = name
        self.id = id
        self.dept = dept
        self.sal = sal

    def upsal(self,sal,hrs):
        overtime= 0
        if hrs>50 :
            overtime = hrs - 50
        self.sal = self.sal +(overtime*(self.sal/50))
    def assign_dept(self,dept):
        self.dept = dept

    def print(self):
        print("Name: ",self.name)
        print("ID: ", self.id)
        print("Department: ", self.dept)
        print("Salary: ", self.sal)

obj = employee("Rajat", 1, "AIML", 5000)
obj.print()
obj.upsal(5000,70)
obj.print()
obj.assign_dept("CS")
obj.print()
