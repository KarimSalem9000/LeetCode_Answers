class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {

        int row = matrix.length;
        int col = matrix[0].length;
        int low = 0;
        int high = col * row;
        while(low < high){
            int mid = (low + high)/2;

            if(matrix[mid/col][mid%col] == target){
                return true;
            }
            else if (matrix[mid/col][mid%col] > target){
                high = mid;
            }
            else{
                low = mid+1;
            }

        }
        return false;
        
    }
}
