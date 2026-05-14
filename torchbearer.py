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
    """
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
        The entire route plan relies on correct distances to between the spawn node, relic nodes, and the exit, because the planner adds them up to score each route and make a decision.
    """


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return "TODO"


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


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
