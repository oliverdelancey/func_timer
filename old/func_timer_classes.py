#%%
#!/usr/bin/env python
"""func_timer v0.01 Copyright Oliver Sandli 2020"""

import argparse
import importlib
import matplotlib.pyplot as plt
import numpy as np
import timeit
import types



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        add_help=True,
        formatter_class=argparse.RawTextHelpFormatter,
        description="A Python function benchmarking tool."
        )
    parser.add_argument(
        "--file",
        action="store",
        help="Python file to benchmark.")
    pargs = parser.parse_args()
    pargs.file = "source_funcs.py"
    mod = importlib.import_module(pargs.file[:-3])

    classes = {}
    functions = {}
    variables= {}
    for i in dir(mod):
        item = getattr(mod, i)
        if not i.startswith("__"):
            classes[i] = item
            variables[i] = []
            for j in dir(classes[i]):
                item = getattr(classes[i], j)
                if type(item) == types.FunctionType:
                    functions[i] = item
                elif type(item) == int:
                    variables[i].append(item)
#%% run the parsed data
    loops = 100000
    its = 15
    times = {}
    for i in classes:
        times[i] = timeit.repeat("functions[i](0, *variables[i])", number=loops, repeat=its, globals=globals())
#%% plot times
    x_axis = np.arange(1, its + 1)
    for i in times:
        plt.plot(x_axis, times[i], label=i)
    plt.title("Function Times")
    plt.legend(loc="upper right")
    plt.show()