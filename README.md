## About
This python 3 application consolidates log traces based on open tracing. A full explanation of the task is under `spec/task.md`

## Instructions
There are no external dependencies, run with `python run.py`, output is displayed in stdout

## Runtime
total runtime is O(3n + nlogn) broken down as follows: 
- O(nlogn) for pythons native sort
- O(n) for iteration of all logs to build a heirachical dictionary grouped by trace ids
- O(2n) to iterate through all logs, recursing on parents to print their children.

We can optimize the print step by keeping a reference only to parent spans, which would change it from 2n to n.

Memory usage is 2n, one for the sorted dict and another for trace dictionary.
