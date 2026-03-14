products = []

user01 = {
    'username': 'ali',
    'role': 'admin'
}
user02 = {
    'username': 'vali',
    'role': 'user'
}
product = {
    'name': 'samsung s22',
    'price': 250
}


def is_admin():
    pass


@is_admin
def create_product(user: dict, product: dict):
    products.append(product)


@is_admin
def delete_product(user: dict, product: dict):
    pass


create_product(user01, {})
