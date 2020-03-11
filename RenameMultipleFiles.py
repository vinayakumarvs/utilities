# Function to rename multiple files 
def main(): 
    i = 0
      
    for filename in os.listdir("."):
        f_name, e_name = os.path.splitext(filename)
        dst ="Image" + str(i) + e_name
        os.rename(filename,dst)
        i += 1
