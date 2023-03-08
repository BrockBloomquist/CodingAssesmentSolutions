class twoSum {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> tempMap = new HashMap();
        
        for(int i = 0; i < nums.length; i++) {
            if(tempMap.containsKey(target - nums[i]) && i != tempMap.get(target - nums[i])) {
                return new int[] {i, tempMap.get(target - nums[i])};
            }
            tempMap.put(nums[i], i);
        }
        return new int[2];
    }
}
