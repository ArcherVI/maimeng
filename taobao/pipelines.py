# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from taobao.settings import DB_SETTING


class TaobaoPipeline(object):
    # def __init__(self):
    #     self.filename = open("mm.json", "w")
    #
    # def process_item(self, item, spider):
    #     text = json.dumps(dict(item), ensure_ascii=False) + ",\n"
    #     self.filename.write(text.encode("utf-8"))
    #     return item
    #
    # def close_spider(self, spider):
    #     self.filename.close()
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host=DB_SETTING['host'],
            db=DB_SETTING['db'],
            user=DB_SETTING['user'],
            passwd=DB_SETTING['password'],
            charset='utf8',
            use_unicode=True)

        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();

    def process_item(self, item, spider):
        try:
            # 插入数据
            self.cursor.execute(
                """insert into maimeng(title, pic, describtion)
                value (%s, %s, %s)""",
                (item['title'],
                 item['pic'],
                 item['describtion']))

            # 提交sql语句
            self.connect.commit()

        except Exception as error:
            # 出现错误时打印错误日志
            raise
        return item
