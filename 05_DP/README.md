# Dynamic Programming (6 Core Patterns)
* Dynamic Programming is a mathematical optimization strategy.
*  The core idea is breaking a massive problem into smaller overlapping subproblems, solve them once, cache the result.
* Identify the pattern, the state variables and transitions come naturally.

## Pattern 1: Linear DP (1D)
**Key Idea:** 
The answer for step i depends strictly on **fixed number** of previous steps (e.g. i - 1 and i - 2)

**Intuition:**
Imagine walking down a conveyor belt. At every step, you can only look at last 1 or 2 steps to make next decision.

Meaning to say, to calculate answer for any step i, don't need to know history, just need to know numbers written for 2 steps immediately before.

**Implementation Blueprint:**
```
dp = [0] * (n + 1)

# Base Cases (for 2 step cases)
dp[0] = base_case_1
dp[1] = base_case_2

for i in range(2, n+1):
    dp[i] = max_or_min(dp[i-1], d[[i-2]]) + cost[i]
```

**Leetcode Qns:**
* Climbing Stairs
* Fibonacci Number
* Min Cost Climbing Stairs
* House Robber
* House Robber II
* Decode Ways
* Word Break

## Pattern 2: Grid DP (2D Pathfinding)
**Key Idea:**
State is defined by 2 coordinates: (r, c) -> row, col.
Movement is usually restricted to {right, down}

**Intuition:**
* Imagine walking through Manhattan-style grid of streets. The goal is to move from top-left corner to bottom-right corner. 
* Movement is limited strictly to right or down.
* Only 2 possibilities on grid[i] -> came from left or from above.
* To find total ways to reach grid, ask the 2 neighbors
    * grid[i][j-1] : Left Neighbor
    * grid[i-1][j] : Top Neighbor

**Implementation Blueprint:**
```
dp = [[0] * COLS for _ in range(ROWS)]

for r in range(1, ROWS):
    for c in range(1, COLS):
        dp[r][c] = dp[r-1][c] + dp[r][c-1]
```

**Leetcode Qns:**
* Unique Paths
* Unique Paths II
* Minimum Path Sum
* Triangle
* Maximal Square
* Minimum Falling Path Sum


## Pattern 3: State Machine DP (Multi-State Linear)

**Key Idea:**
At any step i, can be in 1 of K mutually exclusive states.
Moving to step i+1 might change state

**Intuition:**
* Imagine driving manual car. At any second, either in gear 1, 2 or Neutral.
* Speed at i depends on which gear

**Implementation Blueprint:**
```
hold = [-infinity] * n
empty = [0] * n

for i in range(1, n):
    hold[i] = max(hold[i-1], empty[i-1] - price[i]) # keep holding or buy today
    empty[i] = max(empty[i-1], hold[i-1] + price[i]) # keep empty or sell today
```

**Leetcode Qns:**
* Best Time to Buy and Sell Stock
* Best Time to Buy and Sell Stock II
* Best Time to Buy and Sell Stock Cooldown
* Best Time to Buy and Sell Stock with Transaction Fee
* Paint House
* Paint Fence
* Wiggle Subsequence

## Pattern 4: Knapsack DP (Combinatorics & Subsets)
**Key Idea:**
Given limited capacity and must choose from pool of items to min-max

**Intuition:**
* Thief with backpack that holds exactly W pounds
* For every items, ask -> keep or take?
* If take, capacity shrink but value increases

**Implementation Blueprint:**
```
dp = [0] * (CAPACITY + 1)

for weight, value in items:
    for w in range(CAPACITY, weight - 1, -1):
        dp[w] = max(dp[w], dp[w - weight] + value)
```

**Leetcode Qns:**
* Partition Equal Subset Sum (0/1 Knapsack) -> 0/1 binary choice
* Target Sum (01 Knapsack)
* Coin Change (Unbounded Knapsack)
* Coin Change II (Unbounded)
* Perfect Squares

## Pattern 5: String / Subsequence DP (LCS & LIS)
**Key Idea:**
Used when comparing 2 arrays / strings or finding Longest continuous / discontinuous sequence within an array

**Intuition:**
* Imagine given 2 strings Word A & B
* Setup Matrix where word A is columns and B is rows
* check char by char, if match, move idx i / j as required
    * i -> rows -> word B
    * j -> cols -> word A

**Implementation Blueprint:**
```
dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

for i iin range(1, len(text1) + 1):
    for j in range(1, len(text2) + 1):
        if text1[i-1] == text2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

**Leetcode Qns:
* Longest Increasing Subsequence (1D)
* Edit Distance (2D)
* Interleaving String (2D)
* Delete Operation for Two Strings
* Maximum Length of Repeated Subarray
* Longest Common Subsequence 