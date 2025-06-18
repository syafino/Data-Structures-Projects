#!/usr/local/bin/python3
import sys
sys.path.append('/home/staff/kurban/python')

import csc220

csc220.showForm("This is the comment on the form area.")  

textarea = csc220.getInput('textarea')
textbox = csc220.getInput('textbox')


from kmpalgo import KMPmatch #java algorithm from the pdf translated into py

#since the algorithm from the pdf only returns the first index where the pattern matches i only need to print once
#textbox = pattern, textarea = text

found = (KMPmatch(textbox, textarea))
print ("<h2>My username is syunalfian1 on linux, textarea for the text, textbox for the pattern </h2><br>")
print (f"<p>Found at textarea starting at index {found}</p>" )


# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Syafino Yunalfian
# there is nothing below here!

