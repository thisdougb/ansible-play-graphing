# ansible-play-graphing
A little area for research into creating a 'complexity' value for Ansible plays, in the McCabe sense.

```
$ python parse_play_file.py 
['sample.yml']

Parsed tasks.....
first play TASK: task one 282381829 None
first play TASK: task two 282394921 False
first play TASK: task three 282391001 group is web
second play TASK: task one 282395025 None
second play TASK: task two 282395021 None

Built graph.....
{
    "282395025": [
        282395021
    ], 
    "282381829": [
        282394921, 
        282391001
    ], 
    "282394921": [
        282391001, 
        282395025
    ], 
    "282391001": [
        282395025
    ]
}

Found paths.....
path:  [282381829, 282394921, 282391001, 282395025, 282395021]
path:  [282381829, 282394921, 282395025, 282395021]
path:  [282381829, 282391001, 282395025, 282395021]
```
