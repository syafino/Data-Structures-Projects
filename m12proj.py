#!/usr/local/bin/python3
import sys
import heapq
sys.path.append('/home/staff/kurban/python')

import csc220

csc220.showForm("This is the comment on the form area.")  

textarea = csc220.getInput('textarea')
textbox = csc220.getInput('textbox')

def countchar(text):
    mapofchar = {}
    for char in text:
        mapofchar[char] = mapofchar.get(char, 0) + 1
    return mapofchar

def huffman_compress(text):
    freq_map = countchar(text)
    priority_queue = []
    for char, freq in freq_map.items():
        heapq.heappush(priority_queue, (freq, char))
    code_map = {}

    while len(priority_queue) > 1:
        freq1, str1 = heapq.heappop(priority_queue)
        freq2, str2 = heapq.heappop(priority_queue)

        for char in str1:
            code_map[char] = '0' + code_map.get(char, '')
        for char in str2:
            code_map[char] = '1' + code_map.get(char, '')

        heapq.heappush(priority_queue, (freq1 + freq2, str1 + str2))
    return code_map

char_frequency = countchar(textarea)
binary_codes = huffman_compress(textarea)


print ("<h2>My username is syunalfian1 on linux </h2><br>")

print('<table style="width:25%; border: 1px solid black;">')
print("<p><b>Character Frequency Map:</b></p>")
for char, freq in char_frequency.items():
    print(f"<tr><p><b><td>'{char}'</td><td>{freq}</td></b></p></tr>")
print("</table>")

print('<table style="width:25%; border: 1px solid black;">')
print("<p><b>Possible Huffman Character Code Map:</b></p>")
for char, freq in binary_codes.items():
    print(f"<tr><p><b><td>'{char}'</td><td>{freq}</td></b></p></tr>")
print("</table>")


#print ("textbox contains <b>{}</b> <br>".format( textbox ))
#print ("textarea contains <b>{}</b> <br>".format( textarea ))


# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

# Syafino Yunalfian
# there is nothing below here!


