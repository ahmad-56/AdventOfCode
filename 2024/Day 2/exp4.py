checking_list = [1, 2, 3]
print(checking_list)
for i in checking_list:
    place = checking_list.index(i)
    checking_list.remove(i)
    print(checking_list)
    checking_list.insert(place, i)
    print(checking_list)