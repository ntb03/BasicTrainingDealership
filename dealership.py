class Dealership:

    def __init__(self, name):
        self.name = name                            # Name of Dealership
        self.staff = []                             # List of employees
        self.inventory = []                         # Inventory (List of Car objects)
        self.revenue = 0                            # Revenue from selling cars
    


    def get_revenue(self):                         # Returns total revenue
        return self.revenue
    

    def sell_car(self, model, used, employee_who_sold):         # Sells a car including information: model, used, and seller
        isThere = False

        for car in self.inventory:
            if car.model() == model:
                isThere = True

                if used:
                    soldFor = car.price / 2
                else:
                    soldFor = car.price
                
                self.inventory.remove(car)
                self.revenue += soldFor

                employee_who_sold.cars_sold += 1
                employee_who_sold.revenue_generated += soldFor

                break

        if not isThere:
            print("Car not found")
        

    def add_car(self, model, used):                 # Adds a car to inventory
        car = (model, used)
        self.inventory.append(car)


    def get_cars(self):                             # Returns car inventory
        return self.inventory


    def in_stock(self, model, used):                # Checks if certain car model and usage status is in stock
        car = (model, used)
        for car in self.inventory:
            if car.model() == model:
                return True
        return False
                

    def add_employee(self, name, position):         # Adds an employee
        employee = (name, position)
        self.staff.append(employee)
        print(f"Employee added: {employee}")


    def fire(self, name):                           # Removes an employee
        for employee in self.staff:
            if employee.name == name:
                self.staff.remove(employee)
                print(f"Employee fired: {name}")
                return True
        print(f"Employee not found: {name}")
        return False