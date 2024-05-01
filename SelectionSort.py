def selectionSort(array, size):
    for ind in range(size):
        min_index = ind
        for i in range(ind + 1, size):
            if array[i] < array[min_index]:
                min_index = i
        
        (array[ind], array[min_index]) = (array[min_index], array[ind])
        
size = int(input("Enter the size of the array: "))
arr=[]
print(" Enter the elements of the array")
for i in range(size):
    arr.append(int(input()))

selectionSort(arr, size)

print("The array after sorting is: ")
print(arr)
