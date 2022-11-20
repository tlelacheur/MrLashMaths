import os
import sys
import fileinput
path =r'C:\Users\toby\OneDrive - ivanhoegirls.vic.edu.au\2022\Hugo\MrLashMaths\public'
pathsvg =r'C:\Users\toby\OneDrive - ivanhoegirls.vic.edu.au\2022\Hugo\MrLashMaths\content\.obsidian\plugins\obsidian-math-plus\drawings'
list_of_files = []
list_of_svg = []
text1='<code class="language-math" data-lang="math">||{&#34;id&#34;:'
text2='}||\n</code>'

for root, directories, file in os.walk(path):
	for file in file:
		if(file.endswith(".html")):
			list_of_files.append(os.path.join(root,file))

for root, directories, file in os.walk(pathsvg):
	for file in file:
		if(file.endswith(".svg")):
			list_of_svg.append(os.path.join(root,file))

sub1="data-"
sub2=".svg"
for svgfile in list_of_svg:
    idx1 = svgfile.index(sub1)
    idx2 = svgfile.index(sub2)
    res = text1 + svgfile[idx1 + len(sub1): idx2] + text2
    found=False
    htmlInt=0
    while (not found and htmlInt<len(list_of_files)):
        f=open(list_of_files[htmlInt], "r")
        lines=f.read()
        if res in lines:
            found=True
            svgf = open(svgfile)
            svglines=svgf.read()
            svglines=svglines.replace('svg version="1.1"','svg version="1.1" class="math"')
            lines = lines.replace(res, svglines)
            svgf.close()
        f.close()
        if found:
            f=open(list_of_files[htmlInt], "w")
            f.write(lines)
            f.close()
        htmlInt+=1



# text1='<code class="language-math" data-lang="math">||{&#34;id&#34;:'
# testReplace1='<img class="math" src="/images/math/data-'
# text2='}||\n</code>'
# testReplace2 = '.svg" alt="math" />'


# for name in list_of_files:
#     replace=False
#     f=open(name, "r")
#     lines=f.read()
#     if text1 in lines:
#         replace=True
#         lines = lines.replace(text1, testReplace1)
#         lines = lines.replace(text2, testReplace2)
#     f.close()

#     if replace:
#         f=open(name,"w")
#         f.write(lines)
#         print(name)

