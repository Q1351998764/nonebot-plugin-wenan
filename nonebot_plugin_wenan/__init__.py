from nonebot import get_driver
from nonebot import on_fullmatch
from .config import Config
from nonebot.params import Fullmatch
import httpx
from random import choice
from nonebot.plugin import PluginMetadata

__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-wenan",
    description="一款可以自由增删文案指令和api的插件",
    usage="配置好后发送相应的指令即可，配置文件在config/wenan_api_config.yml",
    type="application",
    # 发布必填，当前有效类型有：`library`（为其他插件编写提供功能），`application`（向机器人用户提供功能）。

    homepage="https://github.com/Q1351998764/nonebot-plugin-wenan",
    # 发布必填。
    config=Config,
    # 插件配置项类，如无需配置可不填写。
    supported_adapters={"~onebot.v11"},
    # 支持的适配器集合，其中 `~` 在此处代表前缀 `nonebot.adapters.`，其余适配器亦按此格式填写。
    # 若插件可以保证兼容所有适配器（即仅使用基本适配器功能）可不填写，否则应该列出插件支持的适配器。
)
plugin_config = Config.parse_obj(get_driver().config)
cmds_config = plugin_config.data

cmds = []
for i in cmds_config:
    if '|' in i:
        cmds = cmds + (i.split('|'))
    else:
        cmds.append(i)

yiyan = on_fullmatch(cmds, priority=10, block=True)
jktj = on_fullmatch(["文案接口统计","文案接口","文案api统计","文案api"], priority=10, block=True)

@yiyan.handle()
async def handle_function(arg: str = Fullmatch()):
    for i in cmds_config:
        if arg in i:
            urls = cmds_config[i]
            url_dict = choice(urls)
            url = url_dict.get('url')
            api_type = 'text'
            is_proxy = False
            path = None
            if url_dict.get('type'):
                api_type = url_dict['type']
            if url_dict.get('is_proxy'):
                is_proxy = url_dict['is_proxy']
            if url_dict.get('path'):
                path = url_dict['path']
            await get_yiyan(url, api_type, is_proxy, path)
            break
    return

async def get_yiyan(url, api_type, is_proxy=False, path=None):
    proxies = None
    if is_proxy:
        try:
            proxy = plugin_config.global_config.proxies_http
        except:
            await yiyan.finish("请先在.env中配置代理")
        proxies = {
            "all://": proxy,
        }
    async with httpx.AsyncClient(proxy=proxies) as client:
        res = await client.get(url,follow_redirects=True, timeout = 10.0)
        if api_type == 'text':
            wenan = res.text
            await yiyan.send(wenan)
        elif api_type == 'json':
            wenan = await from_json_get_content(res.json(), path)
            if isinstance(wenan,list):
                msg = ''
                for i in wenan:
                    if not i.endswith('\n'):
                        i += '\n'
                    msg += i
                if msg.endswith('\n'):
                    msg = msg[:-1]
                wenan = msg
            await yiyan.send(wenan)

async def from_json_get_content(json_dict,str_path):
    res = str_path.split('.')
    res_list = []
    content = json_dict
    for i in res:
        i = i.split('[')
        for j in i:
            j = j.strip(']')
            res_list.append(j)
    for i in res_list:
        if i.isdigit():
            i = int(i)
        content = content[i]
    return content


@jktj.handle()
async def wenan_jktj():
    msg = ''
    for i in cmds_config:
        msg = msg + i + "\n"
    msg = msg[:-1]
    await jktj.finish(msg)