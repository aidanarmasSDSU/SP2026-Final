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

> State the total complexity and show the arithmetic. Two to three lines max.

- **Number of Dijkstra runs:** _k + 1_
- **Cost per run:** _O(m log n)_
- **Total complexity:** _O((k + 1) * O(m log n) = O(k * m log n)_
- **Justification (one line):** _This makes sense because Dijkstra must run one time from spawn and one from each k relics giving k + 1. O(m log n) is given and by combining these we get O(k* m log n) as the 1 is dropped in big O._

---

## Part 3: Algorithm Correctness

> Document your understanding of why Dijkstra produces correct distances.
> Bullet points and short sentences throughout. No paragraphs.

### Part 3a: What the Invariant Means

> Two bullets: one for finalized nodes, one for non-finalized nodes.
> Do not copy the invariant text from the spec.

- **For nodes already finalized (in S):**
  _Your answer here._

- **For nodes not yet finalized (not in S):**
  _Your answer here._

### Part 3b: Why Each Phase Holds

> One to two bullets per phase. Maintenance must mention nonnegative edge weights.

- **Initialization : why the invariant holds before iteration 1:**
  _Your answer here._

- **Maintenance : why finalizing the min-dist node is always correct:**
  _Your answer here._

- **Termination : what the invariant guarantees when the algorithm ends:**
  _Your answer here._

### Part 3c: Why This Matters for the Route Planner

> One sentence connecting correct distances to correct routing decisions.

_Your answer here._

---

## Part 4: Search Design

### Why Greedy Fails

> State the failure mode. Then give a concrete counter-example using specific node names
> or costs (you may use the illustration example from the spec). Three to five bullets.

- **The failure mode:** _Your answer here._
- **Counter-example setup:** _Your answer here._
- **What greedy picks:** _Your answer here._
- **What optimal picks:** _Your answer here._
- **Why greedy loses:** _Your answer here._

### What the Algorithm Must Explore

> One bullet. Must use the word "order."

- _Your answer here._

---

## Part 5: State and Search Space

### Part 5a: State Representation

> Document the three components of your search state as a table.
> Variable names here must match exactly what you use in torchbearer.py.

| Component | Variable name in code | Data type | Description |
|---|---|---|---|
| Current location | | | |
| Relics already collected | | | |
| Fuel cost so far | | | |

### Part 5b: Data Structure for Visited Relics

> Fill in the table.

| Property | Your answer |
|---|---|
| Data structure chosen | |
| Operation: check if relic already collected | Time complexity: |
| Operation: mark a relic as collected | Time complexity: |
| Operation: unmark a relic (backtrack) | Time complexity: |
| Why this structure fits | |

### Part 5c: Worst-Case Search Space

> Two bullets.

- **Worst-case number of orders considered:** _Your answer (in terms of k)._
- **Why:** _One-line justification._

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
