def input_file(filename):
    array = []
    with open(filename, "r") as f:
        for line in f:
            array.append([int(c) for c in line.rstrip("\n")])
    return array