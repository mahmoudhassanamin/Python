class Book:
    __title=None
    __author=None
    def __init__(self,author,title):
        self.__author=author        
        self.__title=title
    def display(self):
        print(f'The book\' title is {self.__title} \nthe book author is {self.__author}')
        
        
book1=Book("mahmoud","IT journey")

book1.display()