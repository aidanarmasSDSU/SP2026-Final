# Development Log – The Torchbearer

**Student Name:** Aidan Armas
**Student ID:** 827612871
---

## Entry 1 – 5/14 8:28AM- : Initial Plan

_My plan is to implement the functions in order and tackle the precomputation first. I will then use Dijkstra to 
 evaluate and store the mapping of paths to each relic from spawn. I then will use backtracking to resolve. The first
implementation will be run_dijkstra because it is the core module and everything is built upon it. I expect pruning 
and state and search space to be difficult because those are areas in which I lack the prior knowledge. 
I will test using the ones given to us while also coming up with my own test cases._

---

## Entry 2 – 5/14 1:05PM: Design Change

_At part 5, my initial instinct was to backtrack by passing a new copy of relics_remaining and relics_visited_order into each recursive call. However, after tracing my own program, I notice that my algorithm doesn't backtrack as explicitly as told in the directions. To fix this, I opted for a mutate and undo pattern that uses more explicit backtracking._

---

## Entry 3 – 5/14 2:11PM: Pruning Explanations

_After reading part 6, I realized pruning explanation and the science behind it wasn't really that clear in my mind. After reading up on it, I learned that pruning is crucial in allowing us to skip whole branches that are unable to beat the current solution. This was incredibly helpful because it allows my program to avoid exploring orderings that have no chance of being optimal, meaning we wouldn't hit that k!._

---

## Entry 4 – 5/14 2:38: Post-Implementation Reflection

_Given more time, I would have liked to add more unit test cases and checked bounds more strictly. I also think my code organization was a little poor and structure could be simplified heavily. I also would set all nodes to infinty at the begin instead of loop over at the end to set unreachable nodes to infinity._

---

## Final Entry – 5/14 2:50: Time Estimate

| Part | Estimated Hours |
|---|-----------------|
| Part 1: Problem Analysis | 30 Minutes      |
| Part 2: Precomputation Design | 90 Minutes      |
| Part 3: Algorithm Correctness | 30 Minutes      |
| Part 4: Search Design | 40 Minutes      |
| Part 5: State and Search Space | 90 Minutes      |
| Part 6: Pruning | 60 Minutes      |
| Part 7: Implementation | 10 Minutes      |
| README and DEVLOG writing | 60 Minutes      |
| **Total** | 410 Minutes     |
