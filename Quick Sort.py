import os
os.system('cls')
import random

notArray = list(range(1, 100))

RandNumbs = random.sample(notArray, k=10)
print("Nomor acak : ",RandNumbs)

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0] 

        print(f"Pivot : {pivot}")
        
        lowerValue = [x for x in arr[1:] if x <= pivot]

        higherValue = [x for x in arr[1:] if x > pivot]
    
        return quickSort(lowerValue) + [pivot] + quickSort(higherValue)

SortedResult = quickSort(RandNumbs)

print("Data yang telah di urut : ",SortedResult)
