import os
import sys 

name = sys.argv[1]

image_files = []
os.chdir(os.path.join("data", name))
for folder in os.listdir(os.getcwd()):
    os.chdir(folder)
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".JPG"):
            image_files.append(f"data/{name}/{folder}/" + filename)
    os.chdir("..")

os.chdir("..")
with open(name+".txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")