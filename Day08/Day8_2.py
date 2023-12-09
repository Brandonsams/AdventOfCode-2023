from tqdm import tqdm


class Node:
    def __init__(self, node_string):
        self.name = node_string.split(" = (")[0]
        self.left = node_string.split(" = (")[1].split(", ")[0]
        self.right = node_string.split(
            " = (")[1].split(", ")[1].replace(")", "")


nodes = []
instruction_sequence = None
fname = "./Day08/input.txt"
# fname = "./Day08/example.txt"
# fname = "./Day08/example_2.txt"
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


steps = 0
current_node_collection = list(filter(lambda node: node.name.endswith("A"), nodes))
current_node_name_collection = [node.name for node in current_node_collection]
concurrent_node_count = len(current_node_collection)
found_all_end_z = False
while not found_all_end_z:

    print(steps)
    for instruction in instruction_sequence:


        if len(list(filter(lambda node: node.name.endswith("Z"), current_node_collection))) == len(current_node_collection):
            found_all_end_z = True
            break

        steps += 1
        if instruction == "L":
            # Go left
            # current_node_name = current_node.left
            # current_node = list(filter(lambda node: node.name == current_node_name, nodes))[0]
            current_node_name_collection = [node.left for node in current_node_collection]
            current_node_collection = [list(filter(lambda node: node.name == current_node,nodes))[0] for current_node in current_node_name_collection]
        else:
            # Go right
            # current_node_name = current_node.right
            # current_node = list(filter(lambda node: node.name == current_node_name, nodes))[0]
            current_node_name_collection = [node.right for node in current_node_collection]
            current_node_collection = [list(filter(lambda node: node.name == current_node,nodes))[0] for current_node in current_node_name_collection]

print(f"Answer: {steps}")


