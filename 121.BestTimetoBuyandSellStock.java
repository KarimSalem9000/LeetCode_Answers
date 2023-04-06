class Solution {
    public int maxProfit(int[] prices) {
        int cam = 0;
        int pre = 0;
        for(int i = 1; i < prices.length; i++){
            if(prices[i]-prices[pre] < 0){
                pre = i;
                continue;
            }
            int temp = Math.max(prices[i] - prices[pre], cam);
            cam = temp;
        }
        return cam;

    }
}
