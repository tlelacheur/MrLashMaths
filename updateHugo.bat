@echo on
cd "C:\Users\tlelacheur\OneDrive - ivanhoegirls.vic.edu.au\2022\Hugo\MrLashMaths"
@REM xcopy "C:\Users\tlelacheur\OneDrive - ivanhoegirls.vic.edu.au\2022\Hugo\MrLashMaths\content\.obsidian\plugins\obsidian-math-plus\drawings" "C:\Users\tlelacheur\OneDrive - ivanhoegirls.vic.edu.au\2022\Hugo\MrLashMaths\static\images\math" /y
hugo
@REM python "C:\Users\tlelacheur\OneDrive - ivanhoegirls.vic.edu.au\Desktop\getFiles.py"
python "C:\Users\tlelacheur\OneDrive - ivanhoegirls.vic.edu.au\Desktop\insertSVG.py"
xcopy "C:\Users\tlelacheur\OneDrive - ivanhoegirls.vic.edu.au\2022\Hugo\MrLashMaths\public"  "C:\Users\tlelacheur\OneDrive - ivanhoegirls.vic.edu.au\2022\Hugo\Website\tlelacheur.github.io" /y /s /e
@REM git add -A 
@REM git commit -a -m "automatic update"
@REM git push
cd "C:\Users\tlelacheur\OneDrive - ivanhoegirls.vic.edu.au\2022\Hugo\Website\tlelacheur.github.io"
git add -A 
git commit -a -m "automatic update"
git push

