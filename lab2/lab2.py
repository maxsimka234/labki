import array_library as arrLib 
import random 


arr=[]
arr2=[4,1,4,8,6]
arr3=[4,8,6]

for i in range(15):
    arr.append(random.randint(0,10))
    
print("інформація по модулю :\n  "+arrLib.__doc__)
print(arr, " первинний масив") 
print(arrLib.find_first_element(arr,7)," id елементу з значенням 7") 
print(arrLib.quicksort(arr)," відсортований масив")
print(arrLib.arithmetic_mean(arr)," середнє арифметичне масиву")
print(arrLib.first_5_max_elements(arr)," перших 5 максимальних елементів")
print(arrLib.first_5_min_elements(arr)," перших 5 мінімальних елементів")
print(arrLib.delete_duplicates(arr)," видалення дублікатів з масиву\n\n")
print(arr2)
print(arr3)
print(arrLib.find_list_on_list(arr2,arr3)," ",arrLib.find_list_on_list.__doc__)