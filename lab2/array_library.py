"""модуль для 2гої лабараторної включає в себе функції для роботи з масивами (ну взагалі з list-ами але всетаки)"""

def quicksort(array):
    """швидке сортування , повертає відсортваний масив але вхідне значенння незмінне"""
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)

        return quicksort(less)+equal+quicksort(greater)
    else:
        return array


def quicksort_(array):
    """швидке сортування з зміною вхідного масиву"""
    array[:] = quicksort(array)
    return


def find_first_element(arr, num):  
    """пошук першого елемента в масиві , функція повертає id улементу якщо він є"""
    for i in range(len(arr)):
        if arr[i] == num:
            return i
    return min


def first_5_min_elements(arr):
    """перших 5 мінімальних елементів , повертається масив з 5 елементів"""
    array = quicksort(arr)
    if len(array) >= 5:
        return array[0:5]
    else:
        return array[0]


def first_5_max_elements(arr):
    """перших 5 максимальних елементів , повертається масив з 5 елементів"""
    array = quicksort(arr)
    if len(array) >= 5:
        return array[len(array)-5:len(array)]
    else:
        return array[len(array)-1]


def arithmetic_mean(arr):
    """середнє арифметичне всього масиву , повертається дійсне число"""
    sum = 0
    for i in arr:
        sum += i
    return sum/len(arr)


def delete_duplicates_(arr):
    """видалення дублікатів в масиві , вхідний масив змінюється"""
    array = quicksort(arr)
    tmp = []
    i = 0
    while i <= (len(array)-1):
        if array[i] != array[i+1]:
            tmp.append(array[i])
        i += 1
    tmp.append(array[i])    
    arr[:] = tmp
    return

def delete_duplicates(arr):
    """видалення дублікатів в масиві , вхідний масив не змінюється"""
    array = quicksort(arr)
    tmp = []
    i = 0
    while i <= (len(array)-2):
        if array[i] != array[i+1]:
            tmp.append(array[i])
        i += 1
    tmp.append(array[i])
    return tmp
def find_list_on_list(arr1,arr2):
    '''пошук послідовності елементів в масиві ,функція повертає масив індексів під якими елементи другого масиву знаходяться в першому масиві'''
    index_arr=[]
    for i in range(len(arr1)):
        if(arr1[i]==arr2[0]):
            for j in range(len(arr2)):
                if(arr1[i+j]!=arr2[j]):
                    index_arr.clear()
                    break
                else:
                    index_arr.append(i+j)
    return index_arr    
