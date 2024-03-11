import os, shutil 

path = "/Users/chris/Desktop/Projects/project3//"

# Creating the folders for filing:
folder_names = ["Csv","Text","Images","Tsv"]

for folder in folder_names:
    if not os.path.exists(path + folder):
        os.makedirs(path + folder)
        
        
# Checking to see if the folders exists:
file_names = os.listdir(path)

for file in file_names:
    if ".csv" in file and not os.path.exists(path + "Csv//"+ file):
        shutil.move(path + file,path + "Csv//"+ file)
    elif ".png" in file and not os.path.exists(path + "Images//"+ file):
        shutil.move(path + file,path + "Images//"+ file)
    elif ".txt" in file and not os.path.exists(path + "Text//"+ file):
        shutil.move(path + file,path + "Text//"+ file)
    elif ".tsv" in file and not os.path.exists(path + "tsv//"+ file):
        shutil.move(path + file,path + "tsv//"+ file)
        
    
        
    
    
        


        

