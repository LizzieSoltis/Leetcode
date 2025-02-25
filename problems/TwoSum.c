/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
//Solution 1: Brute Force
//Time Complexity: O(n^2)
//Space Complexity: O(1)
#include <stdlib.h>
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int i, j;
    int* result = (int*)malloc(2 * sizeof(int));
    *returnSize = 2; // Set the returnSize to 2 since we are returning 2 indices

    for (i = 0; i < numsSize; i++) {
        for (j = i + 1; j < numsSize; j++) { // Start j from i+1 to avoid using the same element twice
            if (nums[i] + nums[j] == target) {
                result[0] = i;
                result[1] = j;
                return result; // Return the result as soon as the pair is found
            }
        }
    }

    // Return NULL if no solution is found (though the prompt assumes one solution always exists)
    return NULL;
}
//Solution 2: Hash Map -> TwoSum.py
//Time Complexity: O(n)
//Space Complexity: O(n)

