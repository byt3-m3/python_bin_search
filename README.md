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



![image](https://drive.google.com/file/d/11ErfclvTEMwuHrGY7xNvTX0Uve2I4xLO/view?usp=sharing )