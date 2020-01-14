#!/usr/bin/env python
"""func_timer v0.01 @ Oliver Sandli 2020"""

import argparse
import os
import tempfile
import timeit
import types
import importlib
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        add_help=True,
        formatter_class=argparse.RawTextHelpFormatter,
        description="A Python function benchmarking tool."
        )
    parser.add_argument(
        "file",
        action="store",
        help="Python file to benchmark.")
    pargs = parser.parse_args()
    pargs.file = pargs.file[:-3]
    mod = importlib.import_module(pargs.file)
    functions = {}
    for i in dir(mod):
        item = getattr(mod, i)
        if not i.startswith("_") and type(item) == types.FunctionType:
            functions[i] = item
    loops = 100000
    its = 15
    times = {}
    for i in functions:
        times[i] = timeit.repeat("functions[i]()", number=loops, repeat=its, globals=globals())
    x_axis = np.arange(1, its + 1)
    for i in times:
        plt.plot(x_axis, times[i], label=i)
    plt.title("Function Times")
    plt.legend(loc="upper right")
    with tempfile.NamedTemporaryFile(delete=False) as t1:
        plt.savefig(f"{t1.name}.svg")
    with open(f"{t1.name}.svg", "r") as f:
        svg = f.read()
    os.unlink(t1.name)
    svg = svg[:215] + '<svg width="100%" version="1.1" viewBox="0 0 460.8 345.6">\n' + svg[373:]

    htm = f"""<!DOCTYPE html>
<html>
<head>
<style>
p {{
    font-family: Arial, Helvetica, sans-serif;
    font-size: 110%;
}}
th {{
    font-family: Arial, Helvetica, sans-serif;
    font-size: 110%;
    font-weight: bold;
}}
td {{
    font-family: Arial, Helvetica, sans-serif;
    font-size: 110%;
}}
</style>
<title>Report</title>
</head>
<body>
<h1>Function Times Report</h1>
<h2>on module {pargs.file}</h2>
{svg}
<h2>Measurements</h2>
<table border='1'>
    <tr>
        <th></th>
        <th>Min</th>
        <th>Max</th>
        <th>Avg</th>
        <th>Total</th>
    </tr>
"""

    for i in functions:
        ti = times[i]
        ts = sum(ti)
        htm += f"""\t<tr>
        <th>{i}</th>
        <td>{min(ti)}</td>
        <td>{max(ti)}</td>
        <td>{ts / len(ti)}</td>
        <td>{ts}</td>
    </tr>
"""
    htm += "</body>\n</html>"
    with open(f"{pargs.file}_report.htm", "w") as f:
        f.write(htm)
