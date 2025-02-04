#Default Path
basepath = "/home/kali/Scripts/Python/ELA_Ted_Talk_Project/Ascii_Images/"
filename = "W_John_Talk.txt"

def Print_File(filename):
    #Combines the base path and the file name used for this
    filepath = basepath + filename
    #Opens the file as read only
    with open(filepath, "r") as ascii_art:
        #Read the file contents
        content = ascii_art.read()
        print(content)