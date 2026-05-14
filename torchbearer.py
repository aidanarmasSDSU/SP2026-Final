"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Aidan Armas
Student ID:  827612871
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

def explain_problem():
    return """
    Why a single shortest-path run from S is not enough:
    Single Dijkstra gives shortest distance to every other node from spawn, but not the costs between nodes/relics. Torchbearer will visit relics one after another, so it needs those costs as well

    What decision remains after all inter-location costs are known:
    The order in which relics are visited must be decided. We must find which route has the smallest total cost for Torchbearer.

    Why this requires a search over orders (one sentence):
    An optimal answer is entirely dependent on the order in which the nodes are visited for lowest cost, so we must search over orders.
"""


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    #Spawn As Source
    sources = [spawn]

    for relic in relics:
        if relic not in sources: # Don't add Spawn Twice
            sources.append(relic)

    return sources


def run_dijkstra(graph, source):
    # Start Empty & Fill As Go
    shortest = {source: 0}

    # MinHeap (distance, node)
    heap = [(0, source)]

    while heap:
        popped = heapq.heappop(heap)
        currentdistance = popped[0]
        currentnode = popped[1]

        #Skip Stale Entry
        if currentdistance > shortest[currentnode]:
            continue

        for edge in graph[currentnode]:
            neighbor = edge[0]
            edgecost = edge[1]
            newdistance = currentdistance + edgecost

            if newdistance < shortest.get(neighbor, float('inf')):
                shortest[neighbor] = newdistance
                heapq.heappush(heap, (newdistance, neighbor))

    #Fill Unreachable Nodes With Infinity
    for node in graph:
        if node not in shortest:
            shortest[node] = float('inf')

    return shortest


def precompute_distances(graph, spawn, relics, exit_node):
    #List of Nodes To Run Dijkstra
    sources = select_sources(spawn, relics, exit_node)

    if not sources:
        return {}

    #Store Results of each source (Spawn, Relic)
    distances = {}
    for source in sources:
        distances[source] = run_dijkstra(graph, source)

    return distances


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    return """
    Part 3a: What the Invariant Means
        For nodes already finalized (in S):
            This means the shortest distance to this node from source is already found and will not be altered.
        For nodes not yet finalized (not in S):
            These nodes have not yet been fully checked and all that is stored so far is the shortest path we have so far with the given finalized nodes in S.

    Part 3b: Why Each Phase Holds
        Initialization : why the invariant holds before iteration 1:
            Before the first iteration S is empty and only the source is within the dictionary with its given distance value of 0. The invariant hold because it should be a distance of 0 from source to source with an empty S, which is true.
        Maintenance : why finalizing the min-dist node is always correct:
            When looking at the current node with the min-dist, every other options forces the current node to pass through an unfinalized neighbor node. Since we know the edge weights are all nonnegative, that action would add cost, showing the min-dist node is always the correct choice.
        Termination : what the invariant guarantees when the algorithm ends:
            At the end of the loop, every reachable node has been finalized and every unreachable node is set to infinity. Every finalized node has its shortest distance from the source/spawn, showing the algorithm correctly finds the shortest path.
    Part 3c: Why This Matters for the Route Planner
        The entire route plan relies on correct distances to between the spawn node, relic nodes, and the exit, because the planner adds them up to score each route and make a decision._
    """


# =============================================================================
# PART 4
# =============================================================================

def explain_search():

    return """
    Why Greedy Fails
        The failure mode: Greedy strategy picks the next immediate lowest cost relic to travel to each time. This can cause problems as a local min might not always lead to a global min.
        Counter-example setup: If from S to the first relic, a crown is cost 1, and S to the second relic, a sword is cost 2, greedy would choose to travel to the crown since it's the local min cost. However, what greedy failed to notice because of its locality decision-making is the cost from the crown to the sword is 1000 while the cost from the sword to the crown is only 3. From this setup, we see that the greedy strategy is not optimal for this solution.
        What greedy picks: In the example above, greedy would choose to go to the crown first for a cost of 1 and then go to the sword for a cost of 1000, giving a total cost of 1001.
        What optimal picks: In the optimal solution, the algorithm would travel to the sword first for a cost of 2, and then travel to the crown for a total of 3, much lower than that of the greedy solution.
        Why greedy loses: Greedy loses because it doesn't look ahead. It only looks for the most optimal solution at the local level which causes a larger global total down the line. In this example it didn't look for the consequences of picking the local minimum.
    
    What the Algorithm Must Explore
        The algorithm must explore every possible order of visiting the relics, because we must find every combination of pathing since there is no greedy solution that can decide the order.
    """


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    # Edge Case with no Relics Just go to Exit
    if not relics:
        reliccost = dist_table[spawn][exit_node]
        if reliccost == float('inf'):
            return (float('inf'), [])
        return (reliccost, [])

    #STORE BEST SOLUTION SO FAR, b[0] lowest total cost, b[1] order found
    best = [float('inf'), []]

    # Begin Search from Spawn, No relics found yet
    relics_remaining = set(relics)
    relics_visited_order = []
    _explore(dist_table, spawn, relics_remaining, relics_visited_order, 0, exit_node, best)

    return (best[0], best[1])



def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    # Base Case: ALL RELICS VISITED GO TO EXIT
    if not relics_remaining:
        finalcost = cost_so_far + dist_table[current_loc][exit_node]
        if finalcost < best[0]:
            best[0] = finalcost
            best[1] = list(relics_visited_order)
        return

    # PRUNING: This is a safe option because of the running cost is more expensive than the lowest total cost found in the paths explored, there is no possible way
    # the branch can help improve total cost because edges are nonnegative. The fact they are nonnegative allows us to skip checks that are already above our running lowest total
    if cost_so_far >= best[0]:
        return

    #Recursive Case: Go through each unvisited relic
    for next_node in relics_remaining:
        step_cost = dist_table[current_loc][next_node]

        #Skip Dead Branches that can't be reached
        if step_cost == float('inf'):
            continue

        #Mark As Visited
        relics_remaining.remove(next_node)
        relics_visited_order.append(next_node)

        #Continue with updated State
        _explore(dist_table, next_node, relics_remaining, relics_visited_order, cost_so_far + step_cost, exit_node, best)

        #BACKTRACK KEY
        relics_remaining.add(next_node)
        relics_visited_order.pop()


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    distancetable = precompute_distances(graph, spawn, relics, exit_node)
    return find_optimal_route(distancetable, spawn, relics, exit_node)

# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    print(f"  Test 1 passed  cost={cost}  order={order}")

    # Test 2: Single relic. Optimal cost = 5.
    graph_2 = {
        'S': [('R', 3)],
        'R': [('T', 2)],
        'T': []
    }
    cost, order = solve(graph_2, 'S', ['R'], 'T')
    assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    print(f"  Test 2 passed  cost={cost}  order={order}")

    # Test 3: No valid path to exit. Must return (inf, []).
    graph_3 = {
        'S': [('R', 1)],
        'R': [],
        'T': []
    }
    cost, order = solve(graph_3, 'S', ['R'], 'T')
    assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    print(f"  Test 3 passed  cost={cost}")

    # Test 4: Relics reachable only through intermediate rooms.
    # Optimal cost = 6.
    graph_4 = {
        'S': [('X', 1)],
        'X': [('R1', 2), ('R2', 5)],
        'R1': [('Y', 1)],
        'Y': [('R2', 1)],
        'R2': [('T', 1)],
        'T': []
    }
    cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    print(f"  Test 4 passed  cost={cost}  order={order}")

    # Test 5: Explanation functions must return non-placeholder strings.
    for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
        result = fn()
        assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
            f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    print("  Test 5 passed  explanation functions are non-empty")

    print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
