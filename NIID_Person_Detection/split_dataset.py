import os
import random

#balance
# sets = ['train', 'test']
# list_file_test =  open('%s/%s.txt' % ("/home/ykn/dataset/NonIID_Person_Detect_Dataset/list_file", "test"), 'w')
# #image_id_test =  open('%s/%s.txt' % ("/home/ykn/dataset/NonIID_Person_Detect_Dataset/list_file", "test_id"), 'w')
# for i in range(1, 6):
#     camera_id = "camera_"+str(i)
#     path = os.path.join("/home/ykn/dataset/NonIID_Person_Detect_Dataset/images", camera_id)
#     filelist = os.listdir(path)
#     filelist.sort(key=lambda x: int(x[:4])) 
#     list_file_train =  open('%s/%s/%s.txt' % ("/home/ykn/dataset/NonIID_Person_Detect_Dataset/list_file", camera_id, "train"), 'w')
#     #image_id_train =  open('%s/%s/%s.txt' % ("/home/ykn/dataset/NonIID_Person_Detect_Dataset/list_file", camera_id, "train_id"), 'w')
#     for filename in filelist:
#         src = os.path.join(os.path.abspath(path),filename)
#         x = random.random()
#         if x >= 0.2:
#             list_file_train.write(src+"\n")
#             #image_id_train.write(filename[:4]+"\n")
#         else:
#             list_file_test.write(src+"\n")
#             #image_id_test.write(filename[:4]+"\n")
#     list_file_train.close()
#     #image_id_train.close()
# list_file_test.close()
# #image_id_test.close()


#imbalance
sets = ['train']
imbalance_base_rate = 0.1

imbalance_rate = [1, 1 - imbalance_base_rate,1 - imbalance_base_rate * 2,1 - imbalance_base_rate * 3,1 - imbalance_base_rate * 4]

for i in range(1, 6):
    camera_id = "camera_"+str(i)
    list_file_train =  open('%s/%s/%s.txt' % ("/home/ykn/dataset/NonIID_Person_Detect_Dataset/list_file", camera_id, "train"), 'r')
    new_list_file_train = open('%s/%s/%s.txt' % ("/home/ykn/dataset/NonIID_Person_Detect_Dataset/list_file", camera_id, "train_imbalance"), 'w')
    print(imbalance_rate[i-1])
    for file_path in list_file_train.readlines():
        #print(file_path)
        x = random.random()
        if x <= imbalance_rate[i-1]:
            new_list_file_train.write(file_path)

    list_file_train.close()
    new_list_file_train.close()
