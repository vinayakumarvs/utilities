from ..imports import *


# Function to rename multiple files 
def main(): 
    i = 0
      
    for filename in os.listdir("."): #List all the files from the working directory
        f_name, e_name = os.path.splitext(filename) #Split filename and the extension
        dst ="Image" + str(i) + e_name #Destination filename
        os.rename(filename,dst) #Rename the file
        i += 1  #Increment the file numbers
