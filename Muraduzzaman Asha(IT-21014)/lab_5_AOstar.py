import sys

# Node class to represent AND-OR graph node
class Node:
    def __init__(self, name, h):
        self.name = name
        self.cost = h          # heuristic / estimated cost
        self.solved = False
        # Each element is a list of child nodes (AND condition)
        # Multiple such lists represent OR choices
        self.childrenOptions = []
        self.edgeCosts = []    # cost for each OR option

# Recursive cost calculation
def calculate_cost(u):
    # If solved or leaf node
    if u.solved or not u.childrenOptions:
        return u.cost

    best_cost = sys.maxsize

    # Check each OR option
    for i in range(len(u.childrenOptions)):
        current_cost = u.edgeCosts[i]
        option = u.childrenOptions[i]

        # AND: sum of all child costs
        for child in option:
            current_cost += calculate_cost(child)

        if current_cost < best_cost:
            best_cost = current_cost

    # Update node cost
    u.cost = best_cost
    return best_cost

def ao_star(root):
    print(f"Expanding Node: {root.name} | Initial Heuristic: {root.cost}")

    min_cost = calculate_cost(root)

    print(f"Updated Cost for {root.name}: {min_cost}")
    root.solved = True

if __name__ == "__main__":
    # 1. Create nodes with heuristic values
    A = Node("A", 100)   # Start node
    B = Node("B", 6)
    C = Node("C", 12)
    D = Node("D", 10)
    E = Node("E", 4)
    F = Node("F", 4)

    # 2. Build AND-OR graph

    # A -> B (OR option 1)
    A.childrenOptions.append([B])
    A.edgeCosts.append(1)

    # A -> C AND D (OR option 2)
    A.childrenOptions.append([C, D])
    A.edgeCosts.append(1)

    # B -> E AND F
    B.childrenOptions.append([E, F])
    B.edgeCosts.append(1)

    # C, D, E, F are leaf nodes

    print("Starting AO* Search...\n")
    ao_star(A)

    print(f"\nFinal Cost of Optimal Solution: {A.cost}")
