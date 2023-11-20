from app.models import Category, Product, User
import hashlib

def get_categories():
    # return [
    #     {
    #         'id': 1,
    #         'name': 'Mobile'
    #     },
    #     {
    #         'id': 2,
    #         'name': 'PC'
    #     }
    # ]
    return Category.query.all()

def get_products(kw):
    # prods = [
    #     {
    #         'id': 1,
    #         'name': 'Iphone 13',
    #         'price': 2000000,
    #         'img': 'https://phuclongmobile.com/wp-content/uploads/2023/09/15pmxanh.png',
    #         'category_id': 1
    #     },
    #     {
    #         'id': 2,
    #         'name': 'Samsung Galaxy S23',
    #         'price': 2200000,
    #         'img': 'https://phuclongmobile.com/wp-content/uploads/2023/09/15pmxanh.png',
    #         'category_id': 1
    #     },
    #     {
    #         'id': 3,
    #         'name': 'Google Pixel',
    #         'price': 2500000,
    #         'img': 'https://phuclongmobile.com/wp-content/uploads/2023/09/15pmxanh.png',
    #         'category_id': 1
    #     }
    # ]
    #
    # if kw:
    #     prods = [p for p in prods if p['name'].find(kw) >= 0]
    #
    # return prods
    products = Product.query
    if kw:
        products = products.filter(Product.name.contains(kw))
    return products.all()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def auth_user(username, password):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())

    print(User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(password)).first())

    return User.query.filter(User.username.__eq__(username),
                             User.password.__eq__(password)).first()