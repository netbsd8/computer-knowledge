import collections

# handle item when popping out of the queue 
# using set to check loop
# (course schedule)
visited = set()
q = collections.deque()
for i in range(numCourses):
    if i not in ins:
        q.append(i)

if len(q) == 0:
    return False

while q:
    cur = q.popleft()
    if cur not in visited:
        visited.add(cur)
    else:
        return False

    for nei in m[cur]:
        ins[nei] -= 1
        if ins[nei] == 0:
            q.append(nei)