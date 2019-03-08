import re

from model.Yaml import MyYaml


class GetConfigMessage(object):
    """用例读取common.yaml文件中的内容"""
    def __init__(self, module="login", class_name="TestLogin", case_name="test_accountError"):
        """
        初始化，读取common中的数据，self.data_messages为对应数据
        :param module: 模块：如 staff_manage
        :param class_name: 类：如：'className': 'TestLogin'
        :param case_name: 用例名称：如：test_accountError
        """
        self.url = MyYaml('SCRM').base_url
        data_messages = {}
        self.all_parm = MyYaml().parameter_ui
        for a in self.all_parm[module]:
            if a["className"] == class_name:
                data_messages["url"] = a["url"]
                for b in a["funName"]:
                    value = b[case_name]
                    if value["url"] is None:
                        value["url"] = self.url + data_messages["url"]
                    data_messages["url"] = value["url"]
                    data_messages["author"] = value["author"]
                    data_messages["level"] = value["level"]
                    data_messages["asserts"] = value["asserts"]
                    data_messages["scene"] = value["scene"]
        if data_messages:
            self.data_messages = data_messages
        else:
            raise TypeError("data_messages无数据，请检查对应参数是否正确")

    def re(self):
        """返回数据"""
        value_data = self.data_messages.get("scene")
        if value_data:
            re_value = re.findall("{.*?}", value_data)
            print(re_value)
        return self.data_messages



if __name__ == '__main__':
    print(GetConfigMessage().re())
