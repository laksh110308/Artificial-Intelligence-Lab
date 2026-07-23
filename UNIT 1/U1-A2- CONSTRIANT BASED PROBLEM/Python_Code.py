# ============================================================
# ARTIFICIAL INTELLIGENCE ASSESSMENT
# Question 1 - Hospital Doctor Scheduling using Backtracking
# Question 2 - Robot Navigation using Breadth First Search
# Question 3 - Rescue Robot using Uniform Cost Search
# ============================================================

from collections import deque
import heapq

# ============================================================
# QUESTION 1
# Hospital Doctor Scheduling using Backtracking Search
# ============================================================

print("\n========== QUESTION 1 ==========")
print("Hospital Doctor Scheduling using Backtracking Search\n")

doctors = ["D1", "D2", "D3"]
shifts = ["Morning", "Afternoon", "Night"]

assignment = {}

def is_safe(doctor, shift):

    if doctor == "D1" and shift == "Night":
        return False

    if doctor == "D3" and shift == "Morning":
        return False

    if shift in assignment.values():
        return False

    if doctor == "D3" and "D2" in assignment:
        order = {
            "Morning": 1,
            "Afternoon": 2,
            "Night": 3
        }

        if order[assignment["D2"]] >= order[shift]:
            return False

    return True


def backtrack(index):

    if index == len(doctors):
        return True

    doctor = doctors[index]

    for shift in shifts:

        if is_safe(doctor, shift):

            assignment[doctor] = shift

            if backtrack(index + 1):
                return True

            del assignment[doctor]

    return False


if backtrack(0):

    print("Doctor Shift Schedule")
    print("---------------------")

    for doctor in assignment:
        print(doctor, "->", assignment[doctor])

else:
    print("No Valid Schedule Found")


# ============================================================
# QUESTION 2
# Robot Navigation using Breadth First Search
# ============================================================

print("\n========== QUESTION 2 ==========")
print("Robot Navigation using Breadth First Search\n")

graph = {
    'S': ['A', 'B'],
    'A': ['C'],
    'B': ['D'],
    'C': ['G'],
    'D': ['G'],
    'G': []
}

visited = []
queue = deque()

queue.append(('S', ['S']))

while queue:

    node, path = queue.popleft()

    if node not in visited:

        visited.append(node)

        if node == 'G':

            print("Shortest Path")
            print(" -> ".join(path))
            print("Total Cost =", len(path) - 1)
            break

        for neighbour in graph[node]:

            if neighbour not in visited:

                queue.append((neighbour, path + [neighbour]))


# ============================================================
# QUESTION 3
# Rescue Robot using Uniform Cost Search
# ============================================================

print("\n========== QUESTION 3 ==========")
print("Rescue Robot using Uniform Cost Search\n")

graph = {

    'S': [('A', 1), ('B', 4)],

    'A': [('C', 2), ('D', 5)],

    'B': [('D', 1)],

    'C': [('G', 3)],

    'D': [('G', 2)],

    'G': []

}

priority_queue = []

heapq.heappush(priority_queue, (0, 'S', ['S']))

visited = []

while priority_queue:

    cost, node, path = heapq.heappop(priority_queue)

    if node not in visited:

        visited.append(node)

        if node == 'G':

            print("Least Cost Path")
            print(" -> ".join(path))
            print("Total Cost =", cost)
            break

        for neighbour, weight in graph[node]:

            if neighbour not in visited:

                heapq.heappush(
                    priority_queue,
                    (
                        cost + weight,
                        neighbour,
                        path + [neighbour]
                    )
                )

print("\n========== PROGRAM COMPLETED ==========")
