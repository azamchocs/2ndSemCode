import os
os.system('cls')
import random

notArray = list(range(1, 100))

RandNumbs = random.sample(notArray, k=10)
print("Nomor acak : ",RandNumbs)

def shellShort(data):
    gap = (len(data)//2)
    a=0

    while gap > 0 :
        for i in range(gap,len(data)):
            value = data[i]
            j = i

            while j >= gap and data[j-gap] > value:
                data[j] = data[j-gap]
                j-=gap

            data[j] = value
            print(data)
        print("Iterasi ke",a,": ",data,"dengan gap ",gap )
        a+=1

        gap //= 2

    return data

print("Sebelum di-sort : ",RandNumbs)
print("Setelah di-sort : ",shellShort(RandNumbs))