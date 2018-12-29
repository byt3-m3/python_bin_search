# Binary Search with Python 


This Code was written to demonstrate the use of binary search methods 
with Python. 

## Binary Search Execution
* Determine lower index of the list, always 0
    * L = 0
* Determine upper index of the list, len(list)
    * U = len(list) - 1
* while L < U, calculate the mid-point index of the list
    * mid = (L + U) // 2 
    * floor division must be used as the mid-point index number must be a whole number for indexing purposes as results with remainders will throw errors. 
* If the mid-point value is less than the  target value, the lower bound index must change shifting the list to the right
    * L = mid-point + 1 
* If the mid-point value is greater than the target value, the upper bound index must change shifting the list to the left
    * U  = mid-point - 1
* Repeat from step C until mid-point value is matched to the target made


## Example

In the example below I have a list with 6 elements. In this case we would like to determine if the number 100 is present in the list. We use the Binary search method 
to find the index position of the number 100. 

![image](https://github.com/byt3-m3/python_bin_search/blob/master/img/Binary%20Searches-Page-1.jpg)
