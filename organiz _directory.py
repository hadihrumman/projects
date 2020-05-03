import os
import shutil

current_dir = os.path.dirname(os.path.realpath(__file__))

print("welcome in  organaize.py script_ happy clean folder")

for filename in os.listdir(current_dir):
    ## organiz images   into images folder
    if filename.endswith((".jpg" , ".png",".tif",".gif","PNG")):
        if not os.path.exists("images"):
            os.mkdir("images")
        shutil.copy(filename ,"images")
        os.remove(filename)
        print("done in images")

    ## organiz code  files into codes folder
    if filename.endswith((".py" , "css","html","bash")):
        if not os.path.exists("codes"):
            os.mkdir("codes")
        shutil.copy(filename ,"codes")
        os.remove(filename)
        print("done in codes")    
   
   
    ## organiz video  files into videos folder
    if filename.endswith(("mp4" , "wam","wmv")):
        if not os.path.exists("videos"):
            os.mkdir("videos")
        shutil.copy(filename ,"videos")
        os.remove(filename)
        print("done in videos")     
   
    ## organiz docs  files into documentes folder
    if filename.endswith((".pdf" , ".word","doc","docx")):
        if not os.path.exists("docs"):
            os.mkdir("docs")
        shutil.copy(filename ,"docs")
        os.remove(filename)
        print("done in docs")    

    ## organiz apps  files into apps folder
    if filename.endswith((".dmg" , "exe")):
        if not os.path.exists("apps"):
            os.mkdir("apps")
        shutil.copy(filename ,"apps")
        os.remove(filename)
        print("done in apps")    

    ## organiz archive  files into archives folder
    if filename.endswith((".zip" , ".rar")):
        if not os.path.exists("archives"):
            os.mkdir("archives")
        shutil.copy(filename ,"archives")
        os.remove(filename)
        print("done in archives") 

print ("done organizing this folder")
