# -*- coding: utf-8 -*-
import pymysql
from scrapy.utils.project import get_project_settings
# engine = create_engine("mysql+mysqldb://weiyz:123456@192.168.1.101:3306/flask_DB")
#
# Session = sessionmaker(bind=engine)

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class DyttMoviePipeline(object):

    def __init__(self):
        # 连接数据库
        settings = get_project_settings()
        self.connect = pymysql.connect(host = 'localhost',user = 'root',passwd = '123456',db = 'test',charset = 'utf8')

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor()

    vat_factor = 1.15

    def process_item(self, item, spider):
        try:
            # 插入数据
            self.cursor.execute(
                """insert into lol_dytt(cat, title, actor, magnetic_link ,thunder_link, plot,hot_point,bt_link)
                value (%s, %s, %s, %s, %s, %s, %s,%s)""",(
                 item['cat'],
                 item['title'],
                 item['actor'],
                 item['magnetic_link'],
                 item['thunder_link'],
                 item['plot'],
                 item['hot_point'],
                 item['bt_link']
                 )
            )

            # 提交sql语句
            self.connect.commit()
            print(u"成功插入一条数据!")

        except Exception as error:
            # 出现错误时打印错误日志
            print(error)
        return item
