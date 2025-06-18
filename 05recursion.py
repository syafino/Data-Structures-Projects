#!/usr/local/bin/python3
import sys
sys.path.append('/home/staff/kurban/python')

import csc220

csc220.showForm("This is the comment on the form area.")  

textarea = csc220.getInput('textarea')
textbox = csc220.getInput('textbox')

print ("<h2>Use the text area not the text box, separate each interger with a space</h2><br>")

#print ("textbox contains <b>{}</b> <br>".format( textbox ))
#print ("textarea contains <b>{}</b> <br>".format( textarea ))

def recurgame(arr,i = 0, path = None, visited = None):
  if path == None:
    path = []
  if visited == None:
    visited = []

  
  path.append(i)
  visited.append(i)

  if i == (len(arr) - 1):
    return path

  if arr[i] == 0:
    return None

  moves = [] #all possible path

  right = i + arr[i]
  if right < len(arr) and right not in visited:
    rpath = recurgame(arr,right,path[:], visited.copy())
    if rpath:
      moves.append(rpath)
  
  left = i - arr[i]
  if left >= 0 and left not in visited:
    lpath = recurgame(arr,left,path[:], visited.copy())
    if lpath:
      moves.append(lpath)
  
  shortest_move = None
  for move in moves:
    if move:
      if shortest_move is None or len(move) < len(shortest_move):
        shortest_move = move

  return shortest_move

arr = list(map(int, textarea.split()))
result = recurgame(arr)

if result:
    print("Shortest path:", result)
else:
    print("No path to the end found.")


#for _ in range(100):
#    print split[_]
#    for s in range(100):
#       print

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Syafino Yunalfian
# there is nothing below here!


