import pymysql
import pandas as pd
import shutil
import os


def mkalbumdir(album_name): #创建文件夹函数
    oripath=os.getcwd() #获取本python文件所在路径
    os.makedirs(oripath+"//"+album_name)  # makedirs 创建文件时如果路径不存在会创建这个路径。
    print ("创建新文件夹：",album_name,"---")



# 创建数据库连接(需要修改)
con = pymysql.connect(host='127.0.0.1',
                      port=3306,
                      user='root',
                      password='123456',
                      db='chevereto_test',
                      charset="utf8")

# 创建游标(默认数据返回tuple,修改为dict)
cur = con.cursor(cursor=pymysql.cursors.DictCursor)

# 读取相册表
get_album_sql = "SELECT album_id,album_name FROM chv01_albums"  # sql语句
cur.execute(get_album_sql)  # 执行sql语句
albums = pd.DataFrame(cur.fetchall())  # 获取结果转为dataframe
#print(albums)

#建立相册文件夹
for index,row in albums.iterrows():#循环整个相册dataframe，取相册名来建立文件夹
    current_album_name=row["album_name"]
    mkalbumdir(current_album_name)



# 读取图片表
get_image_sql = "SELECT image_album_id,image_original_filename FROM chv01_images"  # sql语句
cur.execute(get_image_sql)  # 执行sql语句
images = pd.DataFrame(cur.fetchall())  # 获取结果转为dataframe
#print(images)


#移动图片
for index,row in images.iterrows():
    current_album_id = row["image_album_id"]  #获取当前图片所属的相册ID
    current_image_filename=row["image_original_filename"] #获取当前图片的文件名
    current_ablum_name=albums.loc[current_album_id-1, 'album_name']
    #查询相册dataframe，找到当前图片所属的相册名
    shutil.copy(current_image_filename,".//"+current_ablum_name)
    #copy(src, dst)： 将文件src复制至dst。dst可以是个目录，会在该目录下创建与src同名的文件，若该目录下存在同名文件，将会报错提示已经存在同名文件。权限会被一并复制。本质是先后调用了copyfile与copymode
    print("移动图片",current_image_filename,"到目录",current_ablum_name,"下成功")

