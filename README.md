# The Torchbearer

**Student Name:** Aidan Armas
**Student ID:** 827612871
**Course:** CS 460 – Algorithms | Spring 2026

---

## Part 1: Problem Analysis

- **Why a single shortest-path run from S is not enough:**
  - Single Dijkstra gives shortest distance to every other node from spawn, but not the costs between nodes/relics. Torchbearer will visit relics one after another, so it needs those costs as well

- **What decision remains after all inter-location costs are known:**
  - The order in which relics are visited must be decided. We must find which route has the smallest total cost for Torchbearer.

- **Why this requires a search over orders (one sentence):**
  - An optimal answer is entirely dependent on the order in which the nodes are visited for lowest cost, so we must search over orders.

---

## Part 2: Precomputation Design

### Part 2a: Source Selection

| Source Node Type | Why it is a source                                                                                                         |
|------------------|----------------------------------------------------------------------------------------------------------------------------|
| _Spawn Node_     | _This will always be the beginning of the route, so we must see all initial distances from this node._                     |
| _Relics_         | _The Torchbearer will go from relic to relic if that is the most optimal solution, so we need the distances between each._ |

### Part 2b: Distance Storage

| Property | Your answer                                                                                |
|---|--------------------------------------------------------------------------------------------|
| Data structure name | Nested Dictionary                                                                          |
| What the keys represent | The outer key represents source node and the inner key is destination node                 |
| What the values represent | Shortest path from the source node to destination node                                     |
| Lookup time complexity | O(1)                                                                                       |
| Why O(1) lookup is possible | O(1) is possible because pythons dictionaries are just hash tables which have O(1) lookup. |

### Part 2c: Precomputation Complexity

- **Number of Dijkstra runs:** _k + 1_
- **Cost per run:** _O(m log n)_
- **Total complexity:** _O((k + 1) * O(m log n) = O(k * m log n)_
- **Justification (one line):** _This makes sense because Dijkstra must run one time from spawn and one from each k relics giving k + 1. O(m log n) is given and by combining these we get O(k* m log n) as the 1 is dropped in big O._

---

## Part 3: Algorithm Correctness


### Part 3a: What the Invariant Means

- **For nodes already finalized (in S):**
  _This means the shortest distance to this node from source is already found and will not be altered._

- **For nodes not yet finalized (not in S):**
  _These nodes have not yet been fully checked and all that is stored so far is the shortest path we have so far with the given finalized nodes in S._

### Part 3b: Why Each Phase Holds

- **Initialization : why the invariant holds before iteration 1:**
  _Before the first iteration S is empty and only the source is within the dictionary with its given distance value of 0. The invariant hold because it should be a distance of 0 from source to source with an empty S, which is true._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _When looking at the current node with the min-dist, every other options forces the current node to pass through an unfinalized neighbor node. Since we know the edge weights are all nonnegative, that action would add cost, showing the min-dist node is always the correct choice._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _At the end of the loop, every reachable node has been finalized and every unreachable node is set to infinity. Every finalized node has its shortest distance from the source/spawn, showing the algorithm correctly finds the shortest path._

### Part 3c: Why This Matters for the Route Planner

_The entire route plan relies on correct distances to between the spawn node, relic nodes, and the exit, because the planner adds them up to score each route and make a decision._

---

## Part 4: Search Design

### Why Greedy Fails
- **The failure mode:** _Greedy strategy picks the next immediate lowest cost relic to travel to each time. This can cause problems as a local min might not always lead to a global min._
- **Counter-example setup:** _If from S to the first relic, a crown is cost 1, and S to the second relic, a sword is cost 2, greedy would choose to travel to the crown since it's the local min cost. However, what greedy failed to notice because of its locality decision-making is the cost from the crown to the sword is 1000 while the cost from the sword to the crown is only 3. From this setup, we see that the greedy strategy is not optimal for this solution._
- **What greedy picks:** _In the example above, greedy would choose to go to the crown first for a cost of 1 and then go to the sword for a cost of 1000, giving a total cost of 1001._
- **What optimal picks:** _In the optimal solution, the algorithm would travel to the sword first for a cost of 2, and then travel to the crown for a total of 3, much lower than that of the greedy solution._
- **Why greedy loses:** _Greedy loses because it doesn't look ahead. It only looks for the most optimal solution at the local level which causes a larger global total down the line. In this example it didn't look for the consequences of picking the local minimum._

### What the Algorithm Must Explore

- _The algorithm must explore every possible order of visiting the relics, because we must find every combination of pathing since there is no greedy solution that can decide the order._

---

## Part 5: State and Search Space

### Part 5a: State Representation

| Component | Variable name in code | Data type  | Description                                                                   |
|---|-----------------------|------------|-------------------------------------------------------------------------------|
| Current location | current_loc           | node       | The location(spawn/relic) the torchbearer is current at in the route.         |
| Relics already collected | relics_visited_order  | list[node] | The relics already collected, so we know to not go down that path once again. |
| Fuel cost so far | cost_so_far           | float      | This notes the running total fuel cost and is key in allowing us to prune.    |

### Part 5b: Data Structure for Visited Relics

| Property | Your answer                                                                                                                      |
|---|----------------------------------------------------------------------------------------------------------------------------------|
| Data structure chosen | collection set                                                                                                                   |
| Operation: check if relic already collected | Time complexity: O(1)                                                                                                            |
| Operation: mark a relic as collected | Time complexity:  O(1)                                                                                                           |
| Operation: unmark a relic (backtrack) | Time complexity:  O(1)                                                                                                           |
| Why this structure fits | This structure fits because sets are hash tables that give O(1) for checking, adding, and removing, a key in quick backtracking. |

### Part 5c: Worst-Case Search Space

- **Worst-case number of orders considered:** _O(k!)_
- **Why:** _As described before, the worst case of orders is O(k!) because we would have to search every viable path for k relics which is k!._

---

## Part 6: Pruning

### Part 6a: Best-So-Far Tracking

> Three bullets.

- **What is tracked:** _Your answer here._
- **When it is used:** _Your answer here._
- **What it allows the algorithm to skip:** _Your answer here._

### Part 6b: Lower Bound Estimation

> Three bullets.

- **What information is available at the current state:** _Your answer here._
- **What the lower bound accounts for:** _Your answer here._
- **Why it never overestimates:** _Your answer here._

### Part 6c: Pruning Correctness

> One to two bullets. Explain why pruning is safe.

- _Your answer here._

---

## References

> Bullet list. If none beyond lecture notes, write that.

- _Your references here._
