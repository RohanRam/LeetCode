1/**
2 * Note: The returned array must be malloced, assume caller calls free().
3 */
4int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
5
6int* result = (int*)malloc(2 * sizeof(int));
7
8    for (int i = 0; i < numsSize ; i++) {
9        for(int j=i+1; j< numsSize; j++){
10            if (nums[i] + nums [j] == target){
11                    result[0]=i;
12                    result[1]=j;
13                     *returnSize = 2;
14                    return result;
15            }
16
17        }
18    }
19
20    *returnSize = 0;
21    return NULL;
22}