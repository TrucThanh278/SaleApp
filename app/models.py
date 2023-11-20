from app import db, app
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from flask_login import UserMixin
import enum

class UserRoleEnum(enum.Enum):
    USER = 1
    ADMIN = 2

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    avatar = Column(String(100), default='https://phuclongmobile.com/wp-content/uploads/2023/09/15pmxanh.png')
    user_role = Column(Enum(UserRoleEnum), default=UserRoleEnum.USER)

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

    def __str__(self):
        return self.name

class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100), default='https://phuclongmobile.com/wp-content/uploads/2023/09/15pmxanh.png')
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        import hashlib
        u = User(name='Admin', username='Admin', password=str(hashlib.md5('123456'.encode('utf-8')).hexdigest()), user_role=UserRoleEnum.ADMIN)
        db.session.add(u)
        db.session.commit()

        c1 = Category(name='Mobile')
        c2 = Category(name='Tablet')
        c3 = Category(name='PC')
        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)

        c1 = Product(name='Iphone 15', price=15000000, category_id=1)
        c2 = Product(name='Macbook pro 2023', price=20000000, category_id=3, image='https://masta.vn/wp-content/uploads/2023/03/teaser.jpg')
        c3 = Product(name='Thinkpad X1 Nano', price=19000000, category_id=3, image='https://cdn.sforum.vn/sforum/wp-content/uploads/2021/02/olympus-digital-camera-997-625x417-c-1.jpg')
        c4 = Product(name='Ipad 2023', price=15000000, category_id=2, image='https://cdn.tgdd.vn/Files/2022/11/01/1482679/3_1280x720-800-resize.jpg')
        c5 = Product(name='Samsung S23 Ultra', price=17000000, category_id=1, image='https://cdn11.dienmaycholon.vn/filewebdmclnew/DMCL21/Picture/News/News_expe_6369/6369.png')

        db.session.add(c1)
        db.session.add(c2)
        db.session.add(c3)
        db.session.add(c4)
        db.session.add(c5)
        db.session.commit()