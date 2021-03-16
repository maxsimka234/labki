import classes 

lib=classes.library()
for i in range(5):
    lib.add_book(classes.create_new_book(Year=str(i)))
lib.all_books_info()
print("\n\n")
lib.book_(2)
lib.delete_book(2)
print("\n\n")
lib.all_books_info()
print("\n\n")
lib.book_(2)

