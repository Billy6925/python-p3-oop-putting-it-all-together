#!/usr/bin/env python3

class Book:
    def __init__(self,title, page_count):
        self._title = title
        self._page_count = page_count
        
    @property
    def title(self):
        return self._title 
    @title.setter
    def title(self,title):
        self._title = title
    @property
    def page_count(self):
        return self._page_count
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count,int):
            print(f'Setting page_count to {page_count}')
        else:
            print('page_count must be an integer')
        self._page_count = page_count
   
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")



and_then_there_were_none = Book(title ="And Then There Were None", page_count=272)
and_then_there_were_none.title
and_then_there_were_none.page_count

    
        