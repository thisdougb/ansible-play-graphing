# ansible-play-graphing
A little area for research into creating a 'complexity' value for Ansible plays, in the McCabe sense.

```
$ python parse_play_file.py 
['sample.yml']

Parsed tasks.....
first play TASK: task one 278644229  condition:  None
first play TASK: task two 278657065  condition:  False
first play TASK: task three 278653401  condition:  group is web
second play TASK: task one 278657169  condition:  None
second play TASK: task two 278657165  condition:  None

Built graph.....
{
    "278657169": [
        278657165
    ], 
    "278644229": [
        278657065, 
        278653401
    ], 
    "278657065": [
        278653401, 
        278657169
    ], 
    "278653401": [
        278657169
    ]
}

Found paths.....
path:  [278644229, 278657065, 278653401, 278657169, 278657165]
path:  [278644229, 278657065, 278657169, 278657165]
path:  [278644229, 278653401, 278657169, 278657165]
```
