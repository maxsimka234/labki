class book:
    def __init__(self,name='колобок',author='народна творчість',year='none',genre='казка'):
        self.name=name
        self.author=author
        self.year=year
        self.genre=genre
        
    def display_info(self):
        print(self.name+' '+self.author+' '+self.year+' '+self.genre+'\n')

def create_new_book(Name='колобок',Author='народна творчість',Year='none',Genre='казка'):
    return(book(name=Name,author=Author,year=Year,genre=Genre))

class library:
    books=[]
    def add_book(self,book):
        self.books.append(book)


    def delete_book(self,index):
        i=0
        for book_ in self.books:
            if(i==index):
                self.books.remove(book_)
            i+=1

    def book_(self,index):
        i=0
        for book_ in self.books:
            if(i==index):
                book_.display_info()
            i+=1            

    def all_books_info(self):
        i=0
        for book_ in self.books:
            print(i,". ")
            book_.display_info()
            i+=1        