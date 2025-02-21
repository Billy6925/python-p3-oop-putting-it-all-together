#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self._brand = brand
        self._size = size
        self._condition = None
        
    @property
    def brand(self):
        return self._brand
    @brand.setter
    def brand(self, brand):
        self._brand = brand
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self,size):
        if isinstance(size,int):
            print(f"Setting size to {size}")
        else:
            print("size must be an integer" )
        self._size = size

    @property
    def condition(self):
        return self._condition 
    
    @condition.setter
    def condition(self,condition):
        self._condition = condition
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    
        

adidas = Shoe(brand="Adidas",size=9)
adidas.brand
adidas.size

