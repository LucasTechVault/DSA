# Greedy Algorithms Intuition
Imagine scenario of climbing mountain.

**Dynamic Programming:**
```
- Planner with topographic map
- Look at every possible path - calculate effort for each
- pick best
- slow due to calculating every possible path
```

**Greedy Algorithms:**
```
- Hiker looking 5 feet in front
- Look at the best step 5 feet ahead
- don't care if dead-end later, assume best step now

```


**Gist of Greedy Algorithms:**
```
- Make locally optimal choice at every step
- hope it leads to global optimum
- never look back, no backtracking, no recalculation
```

**Can we use Greedy?:**
```
If i make a local choice now, will i regret it later?
Regret: Take $10 now, miss $100 next -> use DP
No Regret: Take $10 now, still can take $100 next
```

## 3 Greedy Patterns:

### Pattern A - Running (Balance & Survival)
**Intuition:** Have a "Tank" (fuel, balance, score). Iterate, add or subtract score. If negative, die / reset.

**Mechanism:**
    - iterate once
    - keep `current_balance`
        - if `current_balance` < 0 -> reset / start from next / fail attempt


### A1. Lemonade Change
**Problem:**
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you and order one at a time (in the order specified by bills). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you do not have any change in hand at first.

You are given an integer array bills where bills[i] is the bill the ith customer pays, return true if you can provide every customer with the correct change, or false otherwise.
**Example:**
```
Input: bills = [5,10,5,5,20]
Output: true
```
**Strategy:**
```
1. Only {5, 10, 20} bills, 20 will never be used as change
    - keep track of `fives` and `tens`
2. if receive 5 -> fives += 1 (no change needed)
3. if receive 10:
    -> if fives > 0 -> fives -= 1
    - > else return False (no change)
4. if receive 20:
    -> fives-=1 and tens-=1
    -> else fives -= 3
    -> else return False
```
**Code:**
```
def lemonadeChange(self, bills: List[int]) -> bool:
    fives, tens = 0, 0 # we don't give 20 change

    for bill in bills:
        if bill == 5:
            fives += 1
        elif bill == 10:
            if fives > 0:
                fives -= 1
                tens += 1
            else:
                return False
        elif bill == 20:
            if fives > 0 and tens > 0:
                tens -= 1
                fives -= 1
            elif fives >= 3:
                fives -= 3
            else:
                return False
    return True
```

### A2. Maximum Subarray
**Problem:**
Given an array of integers nums, find the subarray with the largest sum and return the sum.
A subarray is a contiguous non-empty sequence of elements within an array.
**Example:**
```
Input: nums = [2,-3,4,-2,2,1,-1,4]
Output: 8
```
**Strategy:**
```
1. cur_sum -> track running sum
2. max_sum -> track global max -> max_sum = nums[0]
3. iterate each number
    - cur_sum += num
    - max_sum = max(max_sum, cur_sum)
4. if cur_sum < 0 -> discard & set to 0, start over
```
**Code:**
```
def maxSubArray(self, nums: List[int]) -> int:
    cur_sum = 0
    max_sum = nums[0]

    for num in nums:
        cur_sum += num
        max_sum = max(max_sum, cur_sum)
        if cur_sum < 0:
            cur_sum = 0
```
### A3. Maximum Sum Circular Subarray
**Problem:**
You are given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

**Example:**
```
Input: nums = [-2,4,-5,4,-5,9,4]
Output: 15
```
**Strategy:**
```
2 Possible Scenario
    1. Standard Kadane [LOW HIGH LOW] - middle seq is high
    2. Head Tal [HIGH LOW HIGH] - mid seq low, chop off

1. init cur_max, global_max
2. init cur_min, global_min
3. init total = 0
4. iterate each num in nums
    - total += num
    - cur_max = max(n, cur_max+n)
    - cur_min = min(n, cur_min+n)
    - update global_max and global_min
5. if global_max < 0 -> all val are -ve -> return global_max
6. else, return max(global_max , total-global_min)
    - max(standard_kadane, chopped middle)
```

### Pattern B - Reach (Intervals & Jumps)
**Intuition:** Have elastic band, want to see how far it can stretch before needing to let go and move to next anchor point

**Mechanism:**
    - maintain `max_reach` variable
    - `max_reach = max(max_reach, i + nums[i])`

### Pattern C Sorting (Priority)
**Intuition:** Want to fit most box in truck, put small ones in first. If want to pair people, sort by height
**Mechanism:** SORT input first, then iterate linearly, picking first item that fits

