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
