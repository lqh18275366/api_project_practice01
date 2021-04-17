#主要功能：实现所有接口的请求
import requests
from loguru import logger
class Base():
    #请求方法:get
    def get(self,url):
        """
        作用；get方法
        :param url: 接受的接口地址
        :return: 返回的响应body值为json格式
        """
        result = None
        response = requests.get(url)
        try:
            result = response.json()
            logger.info("请求get方法的json值：".format(result))
            return result
        except Exception as e:
            logger.error("请求get方法异常，json值；".format(result))