def grid():
    rows = []
    for i in range(1000):
        row = []
        for j in range(1000):
            row.append(0)
        rows.append(row)
    return rows

lists = [[1,2],
  [3,4]]

print(lists[0][1])