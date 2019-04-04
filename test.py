
import os

os.mkdir("test", 0o333)

info = os.stat("test")
path = "/.vol/" + str(info.st_dev) + "/" + str(info.st_ino) + "/"

# fd = os.open("test", os.O_DIRECTORY | os.O_PATH)

#fd2 = os.open("file", os.O_CREAT|os.O_WRONLY, dir_fd=fd)
fd2 = os.open(path + "file", os.O_CREAT|os.O_WRONLY)
os.write(fd2, b"sup")
os.close(fd2)

os.rename("test", "test2")

#fd2 = os.open("file", os.O_RDONLY, dir_fd=fd)
fd2 = os.open(path + "file", os.O_RDONLY)
print(os.read(fd2, 100))
os.close(fd2)
