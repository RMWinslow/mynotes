# HARDCODED CATEGORY. REMEMBER TO CHANGE WHEN MOVING TO A DIFFERENT FOLDER
category = "textbook"


# Generate the file name
import datetime
today = datetime.date.today()
todayinfo = [str(today.year),str(today.month),str(today.day)]
datestring = "-".join(todayinfo)

title = input("Post name: ")

name = input("Post url shortname: ")
if "" == name:
    name = title[:100]
name = name.lower()
name = name.replace(" ","-")
allowed_chars = "qwertyuiopasdfghjklzxcvbnm-"
for c in name:
    if c not in allowed_chars:
        name = name.replace(c,"")

filename = datestring + "-" + name + ".md"
print(filename)



#generate the file content
content = "---\ntitle: "+title[:100]+"\ncategories: "+category+"\ntags:\n  - \n---\n\n\n\n\n"
print(content)




#Actually write the file

f = open(filename,"w+")
f.write(content)
f.close() 
