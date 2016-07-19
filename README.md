# ansible-play-graphing
A little area for research into creating a 'complexity' value for Ansible plays, in the McCabe sense.

```
$ python parse_play_file.py 
['sample.yml']

Parsed tasks.....
TASK: task one 275863813 None
TASK: task two 275876905 False
TASK: task three 275872985 group is web
TASK: task one 275877009 None
TASK: task two 275877005 None

Built graph.....
{
    "275877009": [
        275877005
    ], 
    "275863813": [
        275876905, 
        275872985
    ], 
    "275876905": [
        275872985, 
        275877009
    ], 
    "275872985": [
        275877009
    ]
}

Found paths.....
path:  [275863813, 275876905, 275872985, 275877009, 275877005]
path:  [275863813, 275876905, 275877009, 275877005]
path:  [275863813, 275872985, 275877009, 275877005]
```
