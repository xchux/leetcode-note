import java.util.*;

class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int min = 1, max = Arrays.stream(piles).max().getAsInt();
        int ans = max;

        while(min <= max){
            int mid = min + (max - min) / 2;
            long hours = 0;
            for(int pile : piles){
                hours += (pile + mid - 1) / mid;
            }
            if(hours <= h){
                max = mid - 1;
                ans = mid;
            }
            else{
                min = mid + 1;
            }
        }
        return ans;
    }
}
