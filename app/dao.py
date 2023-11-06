def get_categories():
    return [
        {
            'id': 1,
            'name': 'Mobile'
        },
        {
            'id': 2,
            'name': 'PC'
        }
    ]

def get_products(kw):
    prods = [
        {
            'id': 1,
            'name': 'Iphone 13',
            'price': 2000000,
            'img': 'https://phuclongmobile.com/wp-content/uploads/2023/09/15pmxanh.png',
            'category_id': 1
        },
        {
            'id': 2,
            'name': 'Samsung Galaxy S23',
            'price': 2200000,
            'img': 'https://phuclongmobile.com/wp-content/uploads/2023/09/15pmxanh.png',
            'category_id': 1
        },
        {
            'id': 3,
            'name': 'Google Pixel',
            'price': 2500000,
            'img': 'https://phuclongmobile.com/wp-content/uploads/2023/09/15pmxanh.png',
            'category_id': 1
        }
    ]

    if kw:
        prods = [p for p in prods if p['name'].find(kw) >= 0]

    return prods