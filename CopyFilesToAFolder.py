import os
import shutil

print('输入格式：E:\myprojectnew\jupyter\整理文件夹\示例')
path = input('请键入需要整理的文件夹地址：')
# path="C:\Users\QIN SIJIA\Desktop\folder1"

new_path = input('请键入要复制到的文件夹地址：')
# new_path="C:\Users\QIN SIJIA\Desktop\folder"

for root, dirs, files in os.walk(path):
    for i in range(len(files)):
        file_path = root + '/' + files[i]
        new_file_path = new_path + '/' + files[i]
        if os.path.exists(new_file_path):
            print(file_path + " is same to " + new_file_path)
            print("please rename the file of "+ file_path)
        else:
            shutil.copy(file_path, new_file_path)