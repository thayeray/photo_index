#!/usr/local/bin/python3

# This script will list all the files in the folder from which it is run, it will show a thumbnail of image files.
#   and create an HTML file named 'photolist.html' in that folder. You can then edit that file in Word, to add the
#   marker details like the name and image order.
# To run this script copy the file into the folder with the photos. Then from a terminal:
#         python3 'path/to/copy/of/this/file/main.py'
# Note that the file path can be obtained by dragging and dropping the file into the terminal window.

import os

# file definitions
write_name = 'photo_list.html'
root = os.path.dirname(__file__)

# photo parameters
width = 500 #  adjust this to change photo width
height = 800 # adjust this to change photo height

# html tag definitions
start = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8" /><title>File list</title><style>table, th, td { border: 1px solid black;}</style></head><body>'
tab_st='<table>'
head='<tr><th>File Name</th><th>Photo</th><th>Marker</th><th>Photo Order</th><th>Caption</th></tr>'
pth = '<td>%s</td>'
photo = '<td><img src="%s" alt="%s" width="%s" height="%s"></td>'
marker = '<td>blank</td>'
order = '<td>blank</td>'
caption = '<td>blank</td>'
tab_end = '</table>'
end = '</body> </html>'

f = open(os.path.join(root, write_name),'w')
f.write(start + '\n' + tab_st + '\n' + head)
for path, subdirs, files in os.walk(root):
    for name in files:
        fp = os.path.join(path, name)
        f.write('<tr>' + pth % (name) + photo % (fp,name,width,height) + marker + order + caption + '</tr>')
f.write(tab_end+end)
f.close()
