class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> a = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int z = target - nums[i];
            if (a.containsKey(z)) {
            return new int[] {a.get(z), i}; 
            } else {
                a.put(nums[i], i);
            }
        }
        return new int[] {};
        }
    }
