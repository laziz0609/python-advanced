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


def is_admin(func):
    
    def wrapper(user: dict, *args, **kwargs):
        
        if user['role'] == 'admin':
            data = func(user=user, *args, **kwargs)

            return data
        else:
            raise Exception('siz admin emassiz.')

    return wrapper


@is_admin
def create_product(user: dict, product: dict):
    products.append(product)

create_product(user=user01, product=product)
create_product(user=user02, product=product)
print(products)
