import os
sets = ['train', 'val']
for image_set in sets:
    if not os.path.exists('C:/Users/12587/Desktop/通知&工作/机器学习与python/yolov5-master/people_data2/labels/'):
        os.makedirs('C:/Users/12587/Desktop/通知&工作/机器学习与python/yolov5-master/people_data2/labels/')
    f = open('C:/Users/12587/Desktop/通知&工作/机器学习与python/yolov5-master/people_data2/ImageSets/Person/%s.txt' % image_set, "r")
    lines = []
    for i in f:
        lines.append(i[0:11])
    f.close()
    wf = open('C:/Users/12587/Desktop/通知&工作/机器学习与python/yolov5-master/people_data2/ImageSets/Person/%s.txt' % image_set, "w")
    for i in lines:
        wf.writelines(i)
        wf.writelines('\n')
    wf.close()
