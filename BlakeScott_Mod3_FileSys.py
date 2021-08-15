#Blake Scott 08/09/2021
import os
import pickle

#-Creates a triple nested directory tree on the path of your choice.
#Before you run this script, change the path variables to the desired location on your system. p0, p1, p2, plist, and
#all save_object calls. Should've added an input for this but ran out of time.
p0 = "C:/Users/blake/PyCharmProjects/"
dir_id0 = input("Enter your parent dir id:")
path0 = os.path.join(p0, dir_id0)
os.makedirs(path0, exist_ok=True)

p1 = "C:/Users/blake/PyCharmProjects/"+dir_id0
dir_id1 = input("Enter your first sub_dir id:")
path1 = os.path.join(p1, dir_id1)
os.makedirs(path1, exist_ok=True)

p2 = "C:/Users/blake/PyCharmProjects/"+dir_id0+"/"+dir_id1
dir_id2 = input("Enter your second sub_dir id:")
path2 = os.path.join(p2, dir_id2)
os.makedirs(path2, exist_ok=True)

plist = "C:/Users/blake/PyCharmProjects/"
dir_list = os.listdir(plist)
print("Files and directories in '", plist, "' :")
print(dir_list)


#saves objects to your file of choice. file path declared within call
def save_object(obj,filename):

    with open(filename,'wb') as outp:
        pickle.dump(obj,outp,pickle.HIGHEST_PROTOCOL)


class FileItem:
    file_name = ""
    file_id = ""
    location = ""
    size = ""
    perms = ""
    date_created = ""
    owner = ""

    def __init__(self, fn, fi, loc, s, p, dc, o):
        self.file_name = fn
        self.file_id = fi
        self.location = loc
        self.size = s
        self.perms = p
        self.date_created = dc
        self.owner = o

    def display(self):
        print("File name: " + self.file_name)
        print("File id: " + self.file_id)
        print("Location: " + self.location)
        print("Size: " + self.size)
        print("Permissions: " + self.perms)
        print("Date Created: " + self.date_created)
        print("Owner: " + self.owner)


class CsvFile(FileItem):
    rows = ""
    cols = ""
    val = list()

    def __init__(self, fi, r, c, val):
        FileItem.__init__(self, fi, r, c, [])
        self.rows = r
        self.cols = c
        self.val = []

    def display(self):
        print("File id: " + self.file_id)
        print("Rows: " + self.rows)
        print("Cols: " + self.cols)


class JpgFile(FileItem):
    pic_desc = ""

    def __init__(self, fi, pic):
        FileItem.__init__(self, fi, pic)
        self.pic_desc = pic

    def display(self):
        print("File id: " + self.file_id)
        print("Pic Desc:" + self.pic_desc)


class Mp3File(FileItem):
    song_desc = ""

    def __init__(self, fi, song):
        FileItem.__init__(self, fi, song)
        self.song_desc = song

    def display(self):
        print("File id: " + self.file_id)
        print("Song Desc:" + self.song)


#ran out of time to make 20 objects...same idea applies tho
f0 = FileItem("f0", 0, "Home/test", "100 KB", 744, "08/09/2021", "blake")
f1 = f0.JpgFile(0, "a fam portrait")
f2 = f0.Mp3File(0, "my fav song")
f3 = f0.CsvFile(0, 10, 10, ['this', 'is', 'a', 'list'])

#example to demonstrate implementation on "directories"
#you have to mod permissions of your selected path for this to work
save_object(f0, "C:/Users/blake/PyCharmProjects/"+dir_id0+"/"+"f0.txt")
save_object(f1, "C:/Users/blake/PyCharmProjects/"+dir_id1+"/"+"f1.txt")
save_object(f2, "C:/Users/blake/PyCharmProjects/"+dir_id2+"/"+"f2.txt")
save_object(f3, "C:/Users/blake/PyCharmProjects/"+dir_id2+"/"+"f3.txt")

