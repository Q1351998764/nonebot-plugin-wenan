from pydantic import BaseModel, Extra
import yaml
import nonebot
from nonebot.config import Config as NBConfig
from pathlib import Path

config_path = Path('config/wenan_api_config.yml')

CONFIG_TEMPLATE = {
    #key值设置为要触发的词
    '每日一文':[
        {'url': 'https://api.f4team.cn/API/mryw/?type=text', #在url字段后面写接口链接
        'type': 'text',
        'is_proxy': False,} #是否使用代理,默认为False
        #根据接口指定类型类型包括 text json 如不写则默认为text
        # text指接口返回文本文案
        # json指接口返回json字符串 ,返回json需指定path请参考以下json示例
    ],

    #也可以以"|"分隔设置多个触发词
    '毒鸡汤|鸡汤':[
        {'url': 'https://api.f4team.cn/API/du/api.php'},
        #可以采用这种格式进行一个关键词设置多个链接
    ],
    #返回json示例
    '一言':[
        {'url': 'https://v1.hitokoto.cn/',
        'type': 'json',
        'path': 'hitokoto'} #指向文案链接
    ],
    #返回text示例
    '情话':[
    {'url': 'https://api.f4team.cn/API/qing/api.php',
    'type': 'text'}
    ]
}
# 检查config文件夹是否存在 不存在则创建
if not Path("config").exists():
    Path("config").mkdir()
if not config_path.exists():
    with open(config_path, 'w', encoding='utf-8') as f:
        yaml.dump(CONFIG_TEMPLATE, f, allow_unicode=True)  

global_config = nonebot.get_driver().config

with open(config_path,'r') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)#读取yaml文件

try:
    class Config(BaseModel, extra=Extra.ignore, from_attributes=True):
        """Plugin Config Here"""
        
        api_data: dict = data
        global_config: NBConfig = global_config
except:
    class Config(BaseModel, extra=Extra.ignore):
        """Plugin Config Here"""
        
        api_data: dict = data   
        global_config: NBConfig = global_config