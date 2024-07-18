class Car :
    def __init__(self, used, miles, model) :
        if type(used) is not bool :
            raise TypeError("Used must be boolean type")
        if type(miles) is not int and type(miles) is not float :
            raise TypeError("Miles must be integer or float type")
        if type(model) is not str and type(model) is not int :
            raise TypeError("Model must be string or integer type")
        if miles < 0 :
            raise ValueError("Miles must be a positive value")
        
        self.__used = used
        self.__miles = miles
        self.__model = model
    
    def set_model(self, model) :
        if type(model) is not str and type(model) is not int :
            raise TypeError("Model must be string or integer type")
        
        self.__model = model

    def get_model(self) :
        return self.__model
    
    def set_miles(self, miles) :
        if type(miles) is not int and type(miles) is not float :
            raise TypeError("Miles must be integer or float type")
        if miles < 0 :
            raise ValueError("Miles must be a positive value")
        
        self.__miles = miles
    
    def add_miles(self, new_miles) :
        if type(new_miles) is not int and type(new_miles) is not float :
            raise TypeError("New miles must be integer or float type")
        if new_miles < 0 :
            raise ValueError("New miles must be a positive value")
        
        self.__miles += new_miles

    def get_miles(self) :
        return self.__miles
    
    def is_used(self) :
        return self.__used