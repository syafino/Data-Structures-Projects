#!/usr/local/bin/python3
import sys
sys.path.append('/home/staff/kurban/python')

import csc220

csc220.showForm("This is the comment on the form area.")  

textarea = csc220.getInput('textarea')
textbox = csc220.getInput('textbox')

print ("<h2>Use the text area not the text box</h2><br>")

#print ("textbox contains <b>{}</b> <br>".format( textbox ))
#print ("textarea contains <b>{}</b> <br>".format( textarea ))

split = textarea.split()
print("<p>There are <b>" + str(len(split)) + "</b> words</p>")

def avglen(stringslist):
    total = 0
    for string in stringslist:
        total += len(string)
    return total/len(stringslist)

avglength = avglen(split)
print("<p>There average word length is <b>" + str(avglength) + "</b> characters</p>")

sorted_split = sorted(split, key=len)
n = 0

print("<br><b> Here are the first 100 sorted words. </b><br><br>")

for _ in range(10):
    if _ > len(sorted_split):
        break
    else:
        print ("<p>")
        for o in range(10):
            print (sorted_split[o+n])
        print ("</p><br>")
        n += 10


#for _ in range(100):
#    print split[_]
#    for s in range(100):
#       print

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Syafino Yunalfian
# there is nothing below here!
