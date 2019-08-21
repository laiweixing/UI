import unittest
import requests
import time
import os
import traceback

from config_path.path_file import PATH
from model.MyUnitTest import UnitTests
from model.CaseSupport import test_re_runner
from model.SkipModule import Skip, current_module
from door_ui.interface.currency import get_my_conf

_SKIP = Skip(current_module(PATH(__file__))).is_skip
_SKIP_REASON = Skip(current_module(PATH(__file__))).is_reason


@unittest.skipIf(_SKIP, _SKIP_REASON)
class InterfaceSet(UnitTests):
    """
    :param: RE_LOGIN:  需要切换账号登录，当RE_LOGIN = True时，需要将LOGIN_INFO的value值全填写完成，
                      如果请求的账号中只有一家公司,那么company中的value就可以忽略不填写，否则会报错...
    :param: MODULE: 为当前运行的模块，根据当前运行的模块调用common中的对应的用例方法，需保留此变量方法
    :param: toke_module: 读取token的node
    :param: BROWSER: True执行浏览器，默认为开启
    """
    RE_LOGIN = False
    BROWSER = False
    LOGIN_INFO = {"account": None, "password": None, "company": None}
    MODULE = os.path.abspath(__file__)
    toke_module = str(MODULE).split('\\')[-1].split('.')[0]
    
    set_up = UnitTests.setUp

    @test_re_runner(set_up)
    def test_visit_statistics(self):
        """
        验证openapi访问统计是否正常
        """
        try:
            self.url = self.url % (get_my_conf('backstage_token', 'tenantId'))
            r = requests.get(url=self.url, stream=True, timeout=10)
            self.first = r.json().get('msg')
            self.assertEqual(self.first, self.second, msg=r.content.decode())
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_WeChat(self):
        """
        使用接口验证openapi微信
        """
        try:
            self.url = self.url % (get_my_conf('backstage_token', 'tenantId'))
            r = requests.get(url=self.url, stream=True, timeout=10)
            self.first = r.json().get('msg')
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise

    @test_re_runner(set_up)
    def test_Redis(self):
        """
        使用接口验证openapi+redis->>清理Redis缓存
        """
        try:
            self.url = self.url % (get_my_conf('backstage_token', 'tenantId'))
            r = requests.get(url=self.url, stream=True, timeout=10)
            self.first = r.json().get('code')
            self.assertEqual(self.first, self.second)
        except Exception:
            self.error = str(traceback.format_exc())
            raise
