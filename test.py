
import os

os.mkdir("test", 0o333)

fd = os.open("test", os.O_DIRECTORY | 0x8000)
# fd = os.open("test", os.O_DIRECTORY | os.O_PATH)

fd2 = os.open("file", os.O_CREAT|os.O_WRONLY, dir_fd=fd)
os.write(fd2, b"sup")
os.close(fd2)

os.rename("test", "test2")

fd2 = os.open("file", os.O_RDONLY, dir_fd=fd)
print(os.read(fd2, 100))
os.close(fd2)
