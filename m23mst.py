#!/usr/local/bin/python3
import sys
sys.path.append('/home/staff/kurban/python')

import csc220

csc220.showForm("This is the comment on the form area.")  

textarea = csc220.getInput('textarea')
textbox = csc220.getInput('textbox')

from graph import Graph
from mst import MST_PrimJarnik, MST_Kruskal
split = textarea.splitlines()

graph_map = {}
g = Graph()
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
    v = g.insert_vertex(vname)
    graph_map[vname] = v
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
        g.insert_edge(graph_map[v1name], graph_map[v2name], weight)
    else:
        print("Error: Invalid vertex name in edge")
        error = True
        break
    i += 1

def print_tree(tree, name):
    total_weight = 0
    print(f"<p>{name} edges:<br>")
    for edge in tree:
        u, v = edge.endpoints()
        w = edge.element()
        print(f"{u.element()} -- {v.element()} (weight: {w})<br>")
        total_weight += w
    print(f"Total weight of {name}: {total_weight}</p>")

if not error:
    tree1 = MST_PrimJarnik(g)
    tree2 = MST_Kruskal(g)
    print("<br>")
    print_tree(tree1, "Prim-Jarnik")
    print_tree(tree2, "Kruskal")


print ("<h2>My username is syunalfian1 on linux </h2><br>")
print ("textbox contains <b>{}</b> <br>".format( textbox ))
print ("textarea contains <b>{}</b> <br>".format( textarea ))


# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Syafino Yunalfian
# there is nothing below here!
