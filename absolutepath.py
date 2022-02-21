import os
import datetime as dt

file_name = "Test_file.txt"
print(os.path.abspath(file_name))
print(os.getcwd())
date_time = os.path.getmtime(file_name)
print(dt.datetime.fromtimestamp(date_time))

"""
Creating and moving from one directory to other directory

os.mkdir("directory_name")

os.chdir("directory_path")

os.rmdir("dir_path")

"""
