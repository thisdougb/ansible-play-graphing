#!/usr/bin/python
#
# Simple graphing of an Ansible play
#
# (one)   task: install httpd
# (two)   task: install httpd.conf
# (three) task: deploy application code
#           when: deploy_var is defined
# (four)  task: restart httpd
#

graph = { 'one': ['two'],
          'two': ['three', 'four'],
          'three': ['four']}

def discover_paths(graph, start, end, path=[]):

    path = path + [start]

    if start == end:
        return [path]

    if not graph.has_key(start):
        return []

    paths = []

    for node in graph[start]:
        if node not in path:
            newpaths = discover_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths


print discover_paths(graph, 'one', 'four')
