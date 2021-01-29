import os

print('输入格式：E:\myprojectnew\jupyter\整理文件夹\示例')
path = input('请键入需要整理的文件夹地址：')

fw = open('res.csv', 'w')    #将要输出保存的文件地址

res = ""


for root, dirs, files in os.walk(path, topdown=False):
    for di in dirs:
        res = res + di + ","
        for root1, dirs1, files1 in os.walk(os.path.join(root, di)):
            for file in files1:
                if file == files1[-1]:
                    res = res + file + "\n"
                else:
                    res = res + file + ","

print(res)
fw.write(res)
fw.close()

# for root, dirs, files in os.walk(path, topdown=False):
#   for name in dirs:
#      for root1, dirs1, files1 in os.walk(os.path.join(root, name)):
#          print(root1)
#          print(dirs1)
#          print(files1)