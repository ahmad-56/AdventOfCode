user_input = """111221""" #312211

new = ""
visited = []
visited_j = []
index = 0
for i in range(len(user_input)-1):
    if i not in visited:
        count = 1
        for j in range(1, len(user_input)):    
            if j not in visited_j:
                if user_input[i] == user_input[j]:
                    count += 1
                    index += 1
                else:
                    break
        new += str(count)
        new += user_input[i]
        for c in range(index):
            if c not in visited:
                visited.append(c)
            if c not in visited_j:
                visited_j.append(c)    
        visited_j.append(c+1)
print(new)  #312211