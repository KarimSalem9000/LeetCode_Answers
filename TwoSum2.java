///167. Two Sum II - Input Array Is Sorted

class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int start = 0;
        int end = numbers.length-1;
        int[] ans = new int[2];
        while(numbers[start]+ numbers[end] != target){
            if(numbers[start]+ numbers[end] > target)
                end--;
            else if(numbers[start]+ numbers[end] < target)
                start++;
        }
        ans[0] = start + 1;
        ans[1] = end + 1;
        return ans;
        
    }
}
