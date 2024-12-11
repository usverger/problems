# given a list nodes and their dependencies
# example of input is
# a: b,c
# b: d
# d:
# c: f
# e: f
# f:
# given a name of a node, build a list of execution order for this node

from typing import List
from typing import Dict

def parse(input: str) -> Dict[str, List[str]]:
    lines = input.splitlines()
    tasks = {}

    for line in lines:
        name, deps = [x.strip() for x in line.split(':')]
        if deps:
            tasks[name] = [x.strip() for x in deps.split(',')] # assuming no double entries in the input
        else:
            tasks[name] = []
    return tasks


def build_order(graph: Dict[str, List[str]], starting_node: str) -> List[str]:
    result = []
    stack = [starting_node]

    while stack:
        node = stack.pop()

        # this can be removed to the parse stage
        # if not node in graph:
        #     raise Exception(f'Unknown task referenced "{node}"')
        
        # if all dependecies are already in the result, or there are no dependencies, then it is a leaf node
        if (all(dep in result for dep in graph[node])):
            if node not in result: # never want to execute the same twice
                result.append(node)
            continue
        
        # otherwise add the node back and also all of its unexplored dependencies to the stack
        stack.append(node)
        for dep in reversed(graph[node]):
            if dep in stack:
                return 'Circular dependency detected'

            if node not in result: # never want to execute the same twice
                stack.append(dep)

    return result
