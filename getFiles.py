import os
import sys
import fileinput
path =r'C:\Users\tlelacheur\OneDrive - ivanhoegirls.vic.edu.au\2022\Hugo\MrLashMaths\public'
list_of_files = []

for root, directories, file in os.walk(path):
	for file in file:
		if(file.endswith(".html")):
			list_of_files.append(os.path.join(root,file))



text1='<code class="language-math" data-lang="math">||{&#34;id&#34;:'
testReplace1='<img class="math" src="/images/math/data-'
text2='}||\n</code>'
testReplace2 = '.svg" alt="math" />'


for name in list_of_files:
    replace=False
    f=open(name, "r")
    lines=f.read()
    if text1 in lines:
        replace=True
        lines = lines.replace(text1, testReplace1)
        lines = lines.replace(text2, testReplace2)
    f.close()

    if replace:
        f=open(name,"w")
        f.write(lines)
        print(name)

