from app import db, app
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    products = relationship('Product', backref='category', lazy=True)

class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=0)
    image = Column(String(100), default='https://phuclongmobile.com/wp-content/uploads/2023/09/15pmxanh.png')
    active = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Tablet')
        # c3 = Category(name='PC')
        # db.session.add(c1)
        # db.session.add(c2)
        # db.session.add(c3)

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