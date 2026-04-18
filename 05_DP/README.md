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