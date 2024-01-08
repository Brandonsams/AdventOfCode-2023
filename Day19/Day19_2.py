from tqdm import tqdm
import copy

fname = "./Day19/example.txt"
# fname = "./Day19/input.txt"
answer = 0


class Rule:
    def __init__(self, source):
        self.source = source
        if "<" in source or ">" in source:
            self.category = source[0]
            self.comparator = source[1]
            self.threshold = int(source.split(":")[0][2:])
            self.consequent = source.split(":")[1]
        else:
            self.category = None
            self.comparator = None
            self.threshold = None
            self.consequent = source

    def follow_rule(self, part):
        rule_succeeds = False
        if self.comparator is None:
            return self.consequent
        elif self.comparator == "<":
            match self.category:
                case "x":
                    rule_succeeds = part.x < self.threshold
                case "m":
                    rule_succeeds = part.m < self.threshold
                case "a":
                    rule_succeeds = part.a < self.threshold
                case "s":
                    rule_succeeds = part.s < self.threshold
        else:
            match self.category:
                case "x":
                    rule_succeeds = part.x > self.threshold
                case "m":
                    rule_succeeds = part.m > self.threshold
                case "a":
                    rule_succeeds = part.a > self.threshold
                case "s":
                    rule_succeeds = part.s > self.threshold

        if rule_succeeds:
            return self.consequent
        else:
            return None


class Workflow:
    def __init__(self, source):
        self.source = source
        self.name = source.split("{")[0]
        self.rules = list(map(Rule, source.split(
            "{")[1].replace("}", "").split(",")))
        # self.last_resort = source.split("{")[1].replace("}", "").split(",")[-1]

    def follow_workflow(self, part):
        work = None
        rule_index = 0
        while work is None:
            work = self.rules[rule_index].follow_rule(part=part)
            rule_index += 1
        return work


class Part:
    def __init__(self, source):
        self.source = source
        temp = list(map(int, source.replace("{", "").replace("}", "").replace(
            "x=", "").replace("m=", "").replace("a=", "").replace("s=", "").split(",")))
        self.x = temp[0]
        self.m = temp[1]
        self.a = temp[2]
        self.s = temp[3]
        self.all = sum(temp)


with open(fname) as f:
    content = f.read()

workflows = content.split("\n\n")[0].split("\n")
workflows = list(map(Workflow, workflows))

parts = content.split("\n\n")[1].split("\n")
parts = list(map(Part, parts))

for part in tqdm(parts):
    step = "in"
    while step not in ["A", "R"]:
        relevant_workflow = next(w for w in workflows if w.name == step)
        step = relevant_workflow.follow_workflow(part=part)
    if step == "A":
        answer += 1


print(f"Answer: {answer}")
