import wikipedia as wk
import numpy

#only 10 random pages at a time are supported.
#it's fine since sometimes disambiguation cannot work
#run this many times.
pageList = wk.random(10);

print(pageList[:3])

FILE_OBJ = open(r"summaries.txt", "a", encoding = "utf-8")

for titles in pageList:
    webpage = wk.page(title=titles)
    temp = webpage.content
    FILE_OBJ.write(temp)
    FILE_OBJ.write("\n\n\n\n\n\n")


FILE_OBJ.close()
