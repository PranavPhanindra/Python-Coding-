import shutil
disk_usage = shutil.disk_usage("/")
print(disk_usage)
print((disk_usage.free/disk_usage.total)*100)
