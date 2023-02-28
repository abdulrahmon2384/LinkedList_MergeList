from time import time
import random as rn
from merge import mergeSort
from linked_list import Linked
from linkedList_mergesort import linkedList_MergeSort


limit = 1000000
lst = [str(rn.randint(0,limit)) for count in range(limit)]
def list_timerange():
	#using the merge with python list
	#Checking how long it takes to Merge sort python list
	old = time()
	print("Sorting 1M Data with Mergesort")
	mergeSort(lst)
	print(f"Merge Sorted for {round((time()-old),2)} seconds")

print("\t\t\t[NOTE]\n\t**Sorry this may longer depend On Your IDE**\n")

# Calling python 1M data function
print("loading Python builtin Data....")	
list_timerange()




l = Linked()
print("\nloading Linked_List Random Data of 1M")
# the Linked accept four parameter (name,age,tel,adrs)
[l.add(i,"0",000,"fake") for i in lst]
print("Sorting 1M Data with LinkedList_Mersort...")

old = time()
sorted_linked = linkedList_MergeSort(l)
print(f"LinkedList Sorted 1M Data for {round((time()-old),3)} seconds\n")
sorted_linked.find(rn.choice(lst))











