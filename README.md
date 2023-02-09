# chevereto_Recovery

将Chevereto的图片按照相册整理

## 起因

因为chevereto在前一段时间移除了对中文的支持，所以我打算将图片从chevereto中转移出来。
可是我发现这个图床对文件的排布是按照时间顺序的，这就让我很难直接整理了。近80G的图片，手动整理也不太可能。于是就有了这个小脚本。

## 用法

1、首先配置好Python环境，需求的库如下：
```pymysql
  pandas
  shutil
  os```

2、把chevereto里所有的图片放进一个文件夹里，修改好run.py文件中的数据库连接地址、用户名和密码，再运行：
  ```python runb.py```
就能按照chevereto里图片归属的相册名创建文件夹，并且将对应的图片存放过去（以复制的形式）。


