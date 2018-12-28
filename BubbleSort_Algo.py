"""
Bubble Sort Algorithm:
Bubble Sort works by repeatedly swapping the adjacent elements if they are not in increasing or decreasing order

Inplace sorting algorithm
Time Complexity: O(n*n)
"""

def BubbleSort(lst):
    n = len(lst)
    for i in range(len(lst)):
        for j in range(len(lst) - 1 - i): # After Every iteration largest element is pushed to the end
            if lst[j] >= lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j] # Swap two adjacent elements if they are not in sorted order

# Driver code:

lst1 = [6,4,3,1,2,20,8,7,9,15,0,5]
BubbleSort(lst1)
print("Sorted List:",lst1)

"""
Optmized BubbleSort:
"""

def Optmized_Bubblesort(lst):
    n = len(lst)    
    for i in range(len(lst)):
        flag = 0  # Initialize it to False
        for j in range(len(lst) - 1 - i):  # After Every iteration largest element is pushed to the end
            if lst[j] >= lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Swap two adjacent elements if they are not in order
                flag = 1  # If swap occurs, make it True
        if flag == 0:  # If no change after inner loop ,then break as elements are already in sorted order
            break
