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

        self.session.modified = True

    def __len__(self):
        '''
        Adding and updating the users cart session data
        '''
        return sum(item['qty'] for item in self.cart.values())
