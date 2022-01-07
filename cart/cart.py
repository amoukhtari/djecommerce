from decimal import Decimal

from catalogue.models import Product


class Cart():
    """
    A base Cart class, providing some default behaviors that can be inherited or overided, as necessary
    """

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('skey')  # user confirms that session exists
        if 'skey' not in request.session:
            cart = self.session['skey'] = {}  # create new session
        self.cart = cart

    def add(self, product, qty):
        """
        Adding and updating the users cart session data
        """
        product_id = product.id

        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price), 'qty': int(qty)}

        self.save()

    def __len__(self):
        '''
        Adding and updating the users cart session data
        '''
        return sum(item['qty'] for item in self.cart.values())

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database and return products
        """
        product_ids = self.cart.keys()
        products = Product.products.filter(id__in=product_ids)  # model manager only returns product that are active
        cart = self.cart.copy()  # copy instance from session data

        for product in products:
            cart[str(product.id)]['product'] = product  # add product data to each indivdual item

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.cart.values())

    def delete(self, product):
        """
        Find item within cart and remove it and save
        """
        product_id = str(product)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        # used 2 times so following dry principle we put it into a function
        self.session.modified = True
