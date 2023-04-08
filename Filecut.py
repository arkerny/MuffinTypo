import zipfile
import os
import shutil
from glob import glob
from urllib.request import urlopen
from bs4 import BeautifulSoup
from nt import chdir
# from nt import chdir

##删除文件
def Delfile(file_path):
    ls=os.listdir(file_path)
    for i in ls:
        f_path=os.path.join(file_path, i)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)

##移动文件
def Movefile(srcfile,destination):
    filepath,filename=os.path.split(srcfile)             # 分离文件名和路径
    shutil.move(srcfile,os.path.join(destination,filename))       # 移动文件

# 读取压缩文件
def Decompression(zip_path,save_path):
    file=zipfile.ZipFile(zip_path)
    file.extractall(save_path)
    file.close()

##遍历文件夹，找出网页文件
def search(filepath,destination):
    if os.path.isfile(filepath):
        if '.html'in filepath or '.xhtml' in filepath or '.htm' in filepath:
            Movefile(filepath,destination)
    else:
        filename=os.path.basename(filepath)
        filelist=os.listdir(filepath)
        if filename=='Images':
            shutil.move(filepath,destination)
        else:
            for files in filelist:
                path=os.path.join(filepath,files)
                search(path,destination)

##将.epub修改成.rar
def epub_rar(Start):
    save_path=os.path.join(Start,'save')
    Files=os.listdir(Start)  #获取当前目录下的文件
    for filename in Files:
        portion=os.path.splitext(filename)  #将文件名拆成名字和后缀
        folder=os.path.exists(save_path)
        if not folder:
            os.makedirs(save_path)
        if portion[1]==".epub":
            newname=portion[0]+".zip"
            save_path=os.path.join(Start,'save')
            destination=os.path.join(Start,portion[0])
            print('destionation',destination)

            folder=os.path.exists(destination)
            if not folder:
                os.makedirs(destination)

            os.rename(os.path.join(Start,filename),os.path.join(Start,newname))  #修改
            Decompression(os.path.join(Start,newname),save_path)
            search(save_path,destination)
            os.remove(os.path.join(Start,portion[0])+'.zip')
            #Delfile(save_path)
        else:
            print(portion[0],portion[1],'files not found')

Name='C:\\Users\\Lenovo\\Desktop\\python'  #文件所在目录
Files=os.listdir(Name)  #获取当前目录下的文件
'''
Starts=[]  #如果有多个文件夹
for Filename in Files:
    Starts.append(Name)
'''
epub_rar(Name)
