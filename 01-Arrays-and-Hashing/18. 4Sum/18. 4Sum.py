    /**
     * Runtime O(n^2) and Space O(n^2)
     */
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Set<List<Integer>> res = new HashSet<>();
        int len = nums.length;
        
        Map<Integer, Set<List<Integer>>> sum2Nums = new HashMap<>();
        for (int i = 0; i < len - 1; i++) {
            for (int j = i + 1; j < len; j++) {
                sum2Nums.computeIfAbsent(nums[i] + nums[j], k -> new HashSet<>()).add(Arrays.asList(i, j));
            }
        }
        for (int i = 0; i < len - 1; i++) {
            for (int j = i + 1; j < len; j++) {
                int s = target - (nums[i] + nums[j]);
                if (sum2Nums.containsKey(s)) {
                    for (List<Integer> kl : sum2Nums.get(s)) {
                        if (kl.get(0) > j && kl.get(1) > j) {
                            // even with this index arranging, the quardruplet of [i,j,k,l] is never dup, but 
                            // [nums[i], nums[j], nums[k], nums[l]] may still be dup when those 4 nums are
                            // not all different from each other, so use Set<List<Integer>> for result.
                            // Further more, the quardruplet need to follow certain order for the set to
                            // differentiate them, hence need sorting. This sort on 4 elements may not be a big deal
                            List<Integer> quard = Arrays.asList(nums[i], nums[j], nums[kl.get(0)], nums[kl.get(1)]);
                            Collections.sort(quard);
                            res.add(quard);
                        }
                    }
                }
            }
        }
        return new ArrayList<>(res);
    }