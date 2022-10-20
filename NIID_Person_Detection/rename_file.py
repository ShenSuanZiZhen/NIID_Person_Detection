import os
import xml.etree.ElementTree as ET

class BatchName():

    def rename(self,name):
        path = name
        filelist = os.listdir(path)
        filelist.sort(key=lambda x: int(x[:4])) 
        print(filelist)
        i = 1
        j = 1
        m = 1
        for filename in filelist:
            print(filename)
            if filename.endswith('.xml'):#修改xml文件名
                src = os.path.join(os.path.abspath(path),filename)
                dst = os.path.join(os.path.abspath(path),''+str(i).zfill(4)+'.xml')
                try:
                    os.rename(src,dst)
                    doc = ET.parse(dst)#修改xml文件中的filename
                    root = doc.getroot()
                    sub1 = root.find('filename')
                    sub1.text = str(i)+'.jpg'
                    doc.write(dst)
                    i += 1
                except:
                    print(src+"改名错误")
        #     if filename.endswith('.jpg'):#修改jpg文件名
        #         print(filename)
        #         src = os.path.join(os.path.abspath(path),filename)
        #         dst = os.path.join(os.path.abspath(path),''+str(j).zfill(4)+'.jpg')
        #         try:
        #             os.rename(src,dst)
        #             j += 1
        #         except:
        #             print(src+"改名错误")
        #     if filename.endswith('.txt'):#修改jpg文件名
        #         print(filename)
        #         src = os.path.join(os.path.abspath(path),filename)
        #         dst = os.path.join(os.path.abspath(path),''+str(m).zfill(4)+'.txt')
        #         try:
        #             os.rename(src,dst)
        #             m += 1
        #         except:
        #             print(src+"改名错误")
        print("总共改名照片"+str(j-1)+"张，修改xml文件共"+str(i-1)+"个！！！")


if __name__ =='__main__':
    demo = BatchName()
    demo.rename("/home/ykn/dataset/NonIID_Person_Detect_Dataset/voc_label/camera_3")#修改文件夹绝对地址