from sqlalchemy import Column, String, create_engine  #导入包
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import time
# 创建对象的基类:
Base = declarative_base()
#定义一个类
class User(Base):# 表的名字:
    __tablename__ = 'users'# 表的结构:
    id = Column(String(10), primary_key=True)
    name = Column(String(20))
    email = Column(String(255))
    password = Column(String(60))
    created_at = Column(String(11))
    updated_at = Column(String(11))

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:root@localhost:3306/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()
query = session.query(User)
print(query.filter(User.id != 12).first().name)
# now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# # 创建新User对象:
# new_user = User(id='null',name='bob',email='123@qq.com',password='123456',created_at=now,updated_at=now)
# # 添加到session:
# session.add(new_user)
# # 提交即保存到数据库:
# session.commit()
# # 关闭session:
# session.close()