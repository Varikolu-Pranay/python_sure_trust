class University:
    def __init__(self,name,Location,Fees,No_of_departments,Area :float):
        self.name=name
        self.Location=Location
        self.Fees=Fees
        self.No_of_departments=No_of_departments
        self.Area=Area
    def __str__(self):
        return f"University : {self.name} Loation : {self.Location} No of departments : {self.No_of_departments}"
    def __float__(self):
        return f"Area of university : {self.Area}"
class Engineering(University):
    def __init__(self,name,student_count,Faculty_count,Location,Area : float,Fees):
        super().__init__(name,Location,Fees,1,Area)
        self.student_count=student_count
        self.Faculty_count=Faculty_count
        
    def __str__(self):
        return (f"Engineering College: {self.name} Fees: {self.Fees}, Area: {self.Area}")

class Mba(University):
    def __init__(self, name, student_count, faculty_count, placement_rate, location, area: float, fees):
        super().__init__(name, location, fees, 2, area)
        self.student_count = student_count
        self.faculty_count = faculty_count
        self.placement_rate = placement_rate

    def __str__(self):
        return (f"MBA College: {self.name} Placement Rate: {self.placement_rate}, Fees: {self.Fees}, Area: {self.Area}")


obj1 = University("Geethanjali_university", "A", 50000, 10, 150.5)
obj2 = Engineering("Geethanjali college of engineering and technology", 1200, 80, "B", 75.0, 60000)
obj3 = Mba("Business School", 300, 30, 85, "C", 50.0, 70000)


print(obj1)
print(obj2)
print(obj3)