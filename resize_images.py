from PIL  import Image
import os

fit_size = int(input("entar size :"))
output_folder = input("entar output folder name : ")

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

for filename in os.listdir('.'):
    if not filename.endswith((".jpg" , ".png",".JPG",".gif")):
        continue
    image = Image.open(filename)
    width , height = image.size 

    if width > fit_size and height> fit_size: ## image should be greated than the fit  value
        if width > height :
            height = int ((fit_size/width)*height) 
            width = fit_size
        else:
            width = int((fit_size/ height)*width) 
            height = fit_size      
        image = image.resize((width ,height))
        print('resizing : %s' % (filename))
    image = image.save(os.path.join(output_folder , filename ))
    print(" ------------------------")
print("done resizing all Images")
