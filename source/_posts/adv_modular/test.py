import os, shutil
import glob

# 获取文件个数 2060
path_file_number = glob.glob(pathname='./asuka/*.jpg')
img = path_file_number
# print(img)
# print(len(path_file_number))

# 计算生成文件夹个数
pages = len(path_file_number) / 20
# print(pages)

# 新建文件夹
for folder in range(0, int(pages)):
    # print(i)
    # 新建
    try:
        os.makedirs('./img/' + str(folder))
    except Exception as e:
        # print(e)
        pass
    # 删除
    # try:
    #     os.rmdir('./asuka/' + str(folder))
    # except Exception as e:
    #     print(e)
    # print(len(os.listdir('./asuka/')))

# 获取文件夹
folders = []
rootdrir = './img/'
f_list = os.listdir(rootdrir)
# print(len(f_list))
# print(f_list)

for i in range(0, len(f_list)):
    path = os.path.join(rootdrir, f_list[i])
    # print(path)
    if os.path.isdir(path):
        # print(path)
        folders.append(path)
# print(folders)

# 移动文件
for f in range(len(folders)):
    image = img[(f*20):((f+1)*20)]
    for item in range(len(image)):
        shutil.move(image[item], folders[f])

