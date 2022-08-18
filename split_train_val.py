import random
import os
import argparse


# annotations_path and save_txt_path
def get_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--xml_path', default='C:/Users/12587/Desktop/通知&工作/机器学习与python/yolov5-master/people_data'
                                              '/Annotations/',
                        type=str, help='input xml file ')
    parser.add_argument('--txt_path', default="C:/Users/12587/Desktop/通知&工作/机器学习与python/yolov5-master/people_data"
                                              "/ImageSets/Main/",
                        type=str, help='output txt file')
    opt = parser.parse_args()
    return opt


opt = get_opt()
# xml_path
xml_file = opt.xml_path
# save_txt_path
save_txt_file = opt.txt_path
# 若save_txt_path不存在，则手动创建
if not os.path.exists(save_txt_file):
    os.makedirs(save_txt_file)
# 迭代xml_path路径下所有的文件返回包含该目录下所有文件的list(无序)
total_xml = os.listdir(xml_file)
# 获取包含所有数据list的长度
num = len(total_xml)
# list的范围，后续用于迭代向txt文件中写入数据(image)
list_index = range(num)
# 采集的数据集中训练数据和验证数据的总占比
train_val_percent = 1
# 训练数据的占比
train_percent = 0.99
# 采集的数据集中训练数据和验证数据的数量
tv = int(num * train_val_percent)
# 训练数据的数量,int()向下取整
tr = int(tv * train_percent)
# 从总数据中随机抽取训练集和验证集数据
train_val = random.sample(list_index, tv)
# 从训练集和验证集中随机抽取训练集数据
train = random.sample(train_val, tr)

# 创建train_val.txt,train.txt,test.txt,val.txt
file_train_vale = open(save_txt_file + 'train_val.txt', 'w')
file_train = open(save_txt_file + "train.txt", 'w')
file_test = open(save_txt_file + "test.txt", 'w')
file_val = open(save_txt_file + "val.txt", 'w')

# train_val.txt将训练集和验证集数据写入
# train.txt将训练集数据写入
# test.txt将测试集数据写入
# val.txt将验证集数据写入
for i in list_index:
    # [:-4]将图片格式去掉，比如.jpg
    data_name = total_xml[i][:-4] + '\n'
    # 若该index存在于train_val中，则写入
    if i in train_val:
        file_train_vale.write(data_name)
        if i in train:
            file_train.write(data_name)
        else:
            file_val.write(data_name)
    else:
        file_test.write(data_name)

# 文件流关闭
file_train_vale.close()
file_train.close()
file_test.close()
file_val.close()

