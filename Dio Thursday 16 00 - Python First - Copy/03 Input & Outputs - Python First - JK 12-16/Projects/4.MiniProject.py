import random
from shutil import make_archive

filename_zip = random.randrange(100,200)

folder_to_zip = input("What is folder name to be zipped: ")

make_archive(f"{filename_zip}", "zip", folder_to_zip)