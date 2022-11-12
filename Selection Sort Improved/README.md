# *Improved Selection Sort*

Selection sort is the simplest sorting algorithm that sorts an array by repeatedly finding the minimum element (considering ascending order) among the unsorted part of elements in the array and putting it at the appropriate position into the array. We can consider array into two subarrays. One is the subarray which already sorted. The other one being the remaining subarray which is not unsorted. In every iteration of the algorithm, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray. 
*	in-place Sorting Algorithm
*	comparison-based algorithm
*	average and worst-case complexities are of Ο(n2), where n - number of items.
*	O(1) Space Complexity
*	Non-Stable Algorithm

## Algorithm:
Slightly improved version of Selection sort, sorting the array in both sides by finding min, max in every iteration hence making no of outer iterations reduce by half.
