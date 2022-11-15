# *Improved Selection Sort*

Selection sort is the simplest sorting algorithm that sorts an array by repeatedly finding the minimum element (considering ascending order) among the unsorted part of elements in the array and putting it at the appropriate position into the array. We can consider array into two subarrays. One is the subarray which already sorted. The other one being the remaining subarray which is not unsorted. In every iteration of the algorithm, the minimum element (considering ascending order) from the unsorted subarray is picked and moved to the sorted subarray. 
*	in-place Sorting Algorithm
*	comparison-based algorithm
*	average and worst-case complexities are of Ο(n2), where n - number of items.
*	O(1) Space Complexity
*	Non-Stable Algorithm

## Algorithm:
Slightly improved version of Selection sort, sorting the array in both sides by finding min, max in every iteration hence making no of outer iterations reduce by half.

    selection(arr[], n)
        i <- 0
        j <- n - 1
        while(i < j):
            min <- arr[i]
            max <- arr[i]
            min_i, max_i <- i
            for k <- i to j + 1 :
                if (arr[k] > max):
                    max <- arr[k]
                    max_i <- k
                elif (arr[k] < min):
                    min <- arr[k]
                    min_i <- k
        
        # shifting the min.
        swap (arr[i], arr[min_i])

        # Shifting the max. The equal condition happens if we shifted the max to arr[min_i] in the previous swap.
        if (arr[min_i] == max):
            swap(arr[j], arr[min_i])
        else:
            swap(arr[j], arr[max_i])

        i += 1
        j -= 1
        
 ## Correctness
 Loop Invariant:
  A[0..i] and A[j..n-1] are in sorted order respectively and A[0..i-1] U A[j+1..n-1] together is sorted
  * Initialisation : - At begining, i = 0 and j = n-1, each array has only 1 element and hence, each subarray is sorted and A[0..i-1] U A[j+1..n-1] is empty
  * Maintainance : - It remains true at the beginning of the loop as well end of the loop(i, j will varry)
  * Termination : - At the end, i = j or i = j+1, ie i = ceil(n/2) and j = floor(n/2), So, A[0...i] and A[j...n-1] is sorted and A[0..i-1] U A[j+1..n-1] = A[] full array is sorted
