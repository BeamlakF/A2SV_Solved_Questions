def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    
    for a, b in prerequisites:
        graph[b].append(a)

    state = [0] * numCourses

    def dfs(course):
        if state[course] == 1:
            return False  # cycle
        if state[course] == 2:
            return True   # already checked

        state[course] = 1

        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False

        state[course] = 2
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False

    return True