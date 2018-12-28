"""
Selection Sort Algorithm:
Selection Sort works by repeatedly finding the minimum element(ascending order) from the unsorted sub array and placing
it at the beginning of the unsorted sub array.

Selection sort improves on the bubble sort by making only one swap for every iteration through the list

Inplace sorting algorithm
Time Complexity: O(n*n)
"""

def SelectionSort(sort_list):
    n = len(sort_list)
    for i in range(n):
        pos=i
        for j in range(i+1,n):
            if sort_list[j] < sort_list[pos]:  # Iteratively update the minimum element for every iteration in sub array
                pos = j
        sort_list[i],sort_list[pos]=sort_list[pos],sort_list[i] # Place the min element at start of unsorted sub array

# Driver code
my_list = [3,9,1,20,2,7,4,8,5,16,6]
SelectionSort(my_list)
print(my_list)
