from tqdm import tqdm

class Node:
    def __init__(self, node_string):
        self.name = node_string.split(" = (")[0]
        self.left = node_string.split(" = (")[1].split(", ")[0]
        self.right = node_string.split(" = (")[1].split(", ")[1].replace(")","")

nodes = []
instruction_sequence = None
# fname = "./Day08/example.txt"
fname = "./Day08/input.txt"
with open(fname) as f:
    f_index = 0
    for line in tqdm(f.readlines()):
        line = line.rstrip()
        # print(line)
        if f_index == 0:
            instruction_sequence = line
        elif f_index == 1:
            pass
        else:
            nodes.append(Node(node_string=line))
        f_index += 1

step_collection = []

current_node_collection = list(filter(lambda node: node.name.endswith("A"), nodes))
current_node_name_collection = [node.name for node in current_node_collection]
ends_with_a = current_node_name_collection

for node_name in ends_with_a:

    print(node_name)

    steps = 0
    current_node_name = node_name
    current_node = list(filter(lambda node: node.name == current_node_name, nodes))[0]
    visited_nodes = []
    found_zzz = False
    while not found_zzz:
        for instruction in instruction_sequence:
        
            # print(steps)

            if (current_node_name, instruction) in visited_nodes:
                # print("uh oh")
                pass
            visited_nodes.append((current_node_name,instruction))

            if current_node_name.endswith("Z"):
                found_zzz = True
                break

            steps += 1
            if instruction == "L":
                # Go left
                current_node_name = current_node.left
                current_node = list(filter(lambda node: node.name == current_node_name, nodes))[0]
            else:
                # Go right
                current_node_name = current_node.right
                current_node = list(filter(lambda node: node.name == current_node_name, nodes))[0]

    step_collection.append(steps)
    print(step_collection)


from math import gcd
a = step_collection   #will work for an int array of any length
lcm = 1
for i in a:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)

print(f"Answer: {lcm}")
