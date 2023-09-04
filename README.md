# is_lp_tight
A simple tool to find out whether an answer set program is tight, or not.

The tightness check is based on whether the positive dependency graph contains
at least one [simple cycle](https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.cycles.simple_cycles.html), or not. Due to the involved gringo preprocessing,
the positive dependency graph may not be entirely accurate, causing false positive
results.

## Usage
```sh 
$ pip -r install requirements.txt 
                                                             # ... installing dependencies
$ python3 main.py examples/a.lp
NO  examples/a.lp
total 1
0.0 YES
1.0 NO
$ python3 main.py -v examples/a.lp                           # display cyclic atoms
{'a', 'b'} # cyclic atoms
NO  examples/a.lp
total 1
0.0 YES
1.0 NO
$ python3 main.py examples/*.lp                              # several files
NO  examples/a.lp
<block>:1:6-7: info: atom does not occur in any rule head:
  g

<block>:2:6-7: info: atom does not occur in any rule head:
  g

YES examples/b.lp
<block>:2:6-7: info: atom does not occur in any rule head:
  b

YES examples/c.lp
total 3
0.67 YES
0.33 NO
```
