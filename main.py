import networkx as nx
from lib import clingoext
from lib import utils

def is_tight(encoding: str) -> bool:
    ctl = clingoext.Control()
    ctl.add("base", [], encoding)
    ctl.ground([("base", [])])
    lp = utils.Program(ctl)
    lp._computeComponents()
    dependency_graph = lp.dep
    simple_cycles = list(
        map(
            lambda x: {lp._nameMap[y] for y in x},
            map(frozenset, nx.simple_cycles(dependency_graph)),
        )
    )
    return len(simple_cycles) == 0

if __name__ == "__main__":
    import sys

    path = sys.argv[1]
    instances = sys.argv[1:]
    total = len(instances)
    n,y = 0,0
    for instance in instances:
        with open(instance, "r") as f:
            lp = f.read()
            if not is_tight(lp):
                print("no ", instance, file=sys.stderr)
                n += 1
            else:
                print("yes", instance, file=sys.stderr)
                y += 1
    print(f"read {total}")
    print(f"{y/total:.2} yes")
    print(f"{n/total:.2} no")
