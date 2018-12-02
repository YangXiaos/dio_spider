# @Time         : 18-2-13 下午9:06
# @Author       : DioMryang
# @File         : setup.py
# @Description  :
from setuptools import setup, find_packages
from DioSpider import __version__

setup(
    name="DioSpider",
    version=__version__,
    description="dio 爬虫包",
    author="dio_mryang",
    url="https://github.com/YangXiaos/",
    packages=find_packages(), install_requires=[]
)
