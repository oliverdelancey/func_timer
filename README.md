# func_timer

*func_timer* is a profiler which reads functions from a source file, times them precisely, and generates a report on those times.

## Setup

Create a Python file with the functions that need to be timed. *func_timer* will time all functions not starting with "\_" (underscore), so names of functions which do not need to be timed should begin with a single underscore to differentiate them from both dunders and the user functions that should be timed. To set up applicable use cases for the timed functions, the arguments should be assigned defaults, as *func_timer* will run the functions with their defaults.

Example file:
```python
#!usr/bin/env python
"""sample functions"""

# this function will be ignored by func_timer
def _utility(a, b):
    return a * b

# this function will be timed
def alpha(x=3, y=_utility(5, 6)):
    return 2 * x - y
```

Also, keep in mind that *func_timer* imports the input source file, so any runtime code in the source file should be placed in:
```python
if __name__ == "__main__":
  # do runtime things
```
or very disastrous errors may occur.

## Usage

Once the source file has been prepared, simply run:
```bash
python func_timer.py source_file_to_input.py
#or
./func_timer.py source_file_to_input.py
```
