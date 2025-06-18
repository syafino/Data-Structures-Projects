#!/usr/local/bin/python3
import sys
sys.path.append('/home/staff/kurban/python')

import csc220

csc220.showForm("This is the comment on the form area.")  

textarea = csc220.getInput('textarea')
textbox = csc220.getInput('textbox')


#if textbox == "sum":
 #       print(a+b+c)
#if textbox == "product":
 #       print(a*b*c)

print ("<h2>My username is syunalfian1 on linux, use textarea </h2><br>")

from avl_tree import AVLTreeMap

filename = "/home/staff/kurban/public/lists/web2.txt"
wordMap = AVLTreeMap()

with open(filename, "r") as dictionaryFile:
    for line in dictionaryFile:
        for word in line.strip().split():
            wordMap[word] = True

split_txt = textarea.split()
misspelled = []
for word in split_txt:
    if word not in wordMap:
        misspelled.append(word)

print('<table style="width:25%; border: 1px solid black;">')
print("<p><b>Possible Misspelled Words:</b></p>")
for word in misspelled:
    print(f"<tr><b><td>'{word}'</td></b></tr>")
print("</table>")


# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Syafino Yunalfian
# there is nothing below here!
