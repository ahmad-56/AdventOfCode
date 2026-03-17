def input_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.strip() == "":
            break

    crate_order = "".join(lines[:i]).rstrip()
    user_input = [line.strip() for line in lines[i+1:]]
    return crate_order, user_input