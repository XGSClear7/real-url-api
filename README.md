## 各直播平台直播流接口

### 说明

看到了wbt5的github仓库[real-url][1]，觉得不给写成一个接口着实太麻烦了，花了几小时时间把各个脚本整合成了服务。

再次感谢wbt5的开源！

本人热衷于python，水平属于低端层次，所以经常看崔大大的项目，本项目中[live_api_routing.py][3]调用类对象的方法就是copy的崔大大的。

项目详情稍后会在我的博客中说明，欢迎大家留言吼。我的博客：[PYDUCK][2]

#### 支持的平台

本项目支持的平台与wbt5的[real-url][1]项目支持的平台一致，因为用的是人家的脚本。

#### 关于维护

由于本身有工作，再加上下班就躺，所以有问题请发issue，我会用上班摸鱼的时间去看。

### 运行环境
docker
docker pull miven/real-url-api
docker run -d --restart=always -p 7000:7000 miven/real-url-api

首先要有python3.6及以上

然后在项目路径下运行：

```shell
pip install -r requirements.txt
```

具体兄弟们自行测试吧，按理说没啥问题。

### 部署

linux可以使用gunicorn部署。

```shell
gunicorn -w 4 -b 127.0.0.1:8080 flask_server:app
```

```
-c CONFIG, --config=CONFIG 设定配置文件。
-b BIND, --bind=BIND 设定服务需要绑定的端口。建议使用HOST:PORT。 
-w WORKERS, --workers=WORKERS 设置工作进程数。建议服务器每一个核心可以设置2-4个。 
-k MODULE 选定异步工作方式使用的模块。
```

windows用tornado之类的也可，还是建议直接跑吧。

```shell
python flask_server.py
```

mac的话原谅我穷。

### 接口地址

http://api.pyduck.com/live-api/get-url

接口免费，服务器性能有限，请爱惜。

### 接口文档请访问

http://api.pyduck.com/live-api/api-docs

[1]: https://github.com/wbt5/real-url

[2]: https://www.pyduck.com/

[3]: routings/live_api_routing.py
