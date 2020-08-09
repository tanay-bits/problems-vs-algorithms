I am taking a divide and conquer approach in this problem to find the floored square root of an input integer. I first create a
list of potential candidates with all integers from 0 to the input integer. Then I check if the middle number from this list is
the square root of our input. Based on the value of the square of this mid number, I eliminate half of the candidates from the list
and look for the answer in the other half recursively. Since at every step I'm cutting the input size in half, the worst case time
complexity of this algorithm is `O(log n)` where n is the input integer (since the size of the candidates list I create is n + 1).
