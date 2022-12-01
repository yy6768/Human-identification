import os

lines = []
# 方法2，使用文件后自动关闭文件
with open('people_data2/train.txt', "r") as f:
    for line in f:
        if os.path.exists("C:/Users/12587/Desktop/通知&工作/机器学习与python/yolov5-master/people_data2/JPEGImages/" + line[0:11] + ".jpg"):
            s = "/home/chenshuting/yolov5-master/people_data2/images/" + line[0:11] + ".jpg"
            lines.append(s)

with open("people_data2/new_train.txt", "w") as f2:
    for line in lines:
        f2.writelines(line)
        f2.writelines('\n')

# name_list = []
#
# for root, dirs, files in os.walk('C:/Users/12587/Desktop/通知&工作/机器学习与python/yolov5-master/people_data2/labels/'):
#     for file in files:
#         src_file = os.path.join(root, file)
#         if os.path.getsize(src_file) == 0:
#             os.remove(src_file)
#             os.remove("C:/Users/12587/Desktop/通知&工作/机器学习与python/yolov5-master/people_data2/JPEGImages/" + file[0:11] + ".jpg")
