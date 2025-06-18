#!/usr/local/bin/python3
import random
import csv

def insertionSort():
    listvisits = 0
    sizearr = random.randint(1000, 10000)
    array = [random.randint(1, 200) for _ in range(sizearr)]  


    for step in range(1, len(array)):
        key = array[step]
        listvisits += 1
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            listvisits += 1
            j = j - 1
            listvisits += 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key
        listvisits += 1
    return sizearr, listvisits

with open("03insort.csv", mode="w", newline="") as file:
    writer = csv.writer(file)

    for _ in range(350):
        size, visits =  insertionSort()
        writer.writerow([size, visits])
print("finished")

