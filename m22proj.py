#!/usr/local/bin/python3
import sys
sys.path.append('/home/staff/kurban/python')

import csc220

csc220.showForm("This is the comment on the form area.")  

textarea = csc220.getInput('textarea')
textbox = csc220.getInput('textbox')

from owngraph import Digraph

split = textarea.splitlines()

graph_map = {}
g = Digraph()
error = False

i = 0
while i < len(split) and split[i] != "#end" and not error:
    words = split[i].split()
    if len(words) != 1:
        print("Error: invalid input of vertices")
        error = True
        break
    vname = split[i]
    if vname in graph_map:
        print("Error: Duplicate Vertex Name")
        error = True
        break
    v = g.add_vertex(vname)
    graph_map[vname] = vname
    i += 1

#skip #end
i += 1

# input edges
while i < len(split) and not error:
    splitwords = split[i].split(", ")
    if len(splitwords) != 3:
        print("Error: Invalid input of edges")
        error = True
        break
    v1name, v2name, weight = splitwords[0].strip(), splitwords[1].strip(), float(splitwords[2].strip())
    if weight == None:
        weight = 0
    if v1name in graph_map and v2name in graph_map:
        g.add_edge(graph_map[v1name], graph_map[v2name], weight)
    else:
        print("Error: Invalid vertex name in edge")
        error = True
        break
    i += 1

if not error:
    print("<br>")
    if "START" in g.vertices() and "END" in g.vertices():
        path, cost = g.dijkstra_shortest_path('START', 'END')
        print("Path:<br>")
        print(", ".join(path))
        print(f"<br>Cost: {cost}")
    print("<br>")
    print("<br>")
    for v in g.vertices():
        print("Edges to {}<br>".format(v))
        for e in g.incident_edges(v):
            print("-- {}<br>".format(e))


print ("<h2>My username is syunalfian1 on linux </h2><br>")
print ("textbox contains <b>{}</b> <br>".format( textbox ))
print ("textarea contains <b>{}</b> <br>".format( textarea ))


# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Syafino Yunalfian
# there is nothing below here!

