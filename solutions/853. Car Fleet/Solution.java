import java.util.*;

class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        Map<Integer, Double> carMap = new TreeMap<>(Collections.reverseOrder());
        for (int i = 0; i < position.length; i++) {
            carMap.put(position[i], (double) (target - position[i]) / speed[i]);
        }
        int result = 0;
        double current = 0;
        for (double time : carMap.values()) {
            if (time > current) {
                current = time;
                result++;
            }
        }
        return result;
    }
}
