<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-wenan

_✨ 一款可以自由增删文案指令和api的插件 ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/Q1351998764/nonebot-plugin-wenan.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-wenan">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-wenan.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>



## 📖 介绍

在我调用各种文案api的时候，觉得每个api取一个指令并写一个小插件太麻烦了，因此写了本插件，只需配置yml即可增添文案api以及触发指令，如下图所示：

![image](https://github.com/Q1351998764/nonebot-plugin-wenan/assets/57926506/bd1f63c7-9c6c-420a-95b0-ec470fb30764)


## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-wenan

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-wenan
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot-plugin-wenan"]

</details>

## ⚙️ 配置

本插件的配置在bot根目录下的config文件夹下，名为wenan_api_config.yml，该文件会在插件第一次运行时自动生成。其内容如同介绍中的截图所示。
可参考 https://github.com/Q1351998764/nonebot-plugin-picture-api

写法如下所示：


    情话|qh:
      - url: https://api.f4team.cn/API/qing/api.php
        is_proxy: false
        type: text


其中，情话|qh 代表api的触发指令，用"情话"或者是"qh"均可触发。url后跟api；is_proxy代表是否使用代理，可不写，默认false；type代表该api是否直接返回文案，可不写，默认为text

也可在一个关键词下设置多个url，如下所示：


    一言:
      - url: https://api.f4team.cn/API/dmyiyan/api.php
      - url: https://api.f4team.cn/API/wryl/api.php
      
其中，is_proxy与image均没写，采用默认值false和text

如果api返回是json，如下所示：

    一言:
      - url: https://v1.hitokoto.cn/
        path: hitokoto
        type: json

其中 https://v1.hitokoto.cn/ 接口返回的json格式如下：

{"id":6210,"uuid":"bc908f7e-9985-44d3-8234-4e0273e19672","hitokoto":"我不是畏惧风，我只是怕风把沙子吹到我的眼睛里！","type":"e","from":"日常随笔","from_who":"白凝羽","creator":"白凝羽","creator_uid":6045,"reviewer":1044,"commit_from":"app","created_at":"1590722736","length":23}

path后就需要跟路径hitokoto，指向最终图片的url，注意：返回格式为json的api，必须要写path，并最终指向图片url

一个关键词下可以设置多个url，并且返回不同类型的url也可以混合设置，如下所示：

    一言:
      - url: https://v1.hitokoto.cn/
        path: hitokoto
        type: json
      -url: https://api.f4team.cn/API/dmyiyan/api.php

在上面的配置中，指令"一言"对应了两个url，第一个url返回json格式，第二个url直接返回文本。

大概配置就这样。

## 🎉 使用
配置完后直接对机器人发送配置的指令即可，机器人将随机调用该指令下的一个接口。
