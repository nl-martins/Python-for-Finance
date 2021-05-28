import cbpro 
import data_api

"""
"  Class that contains the trading functions that we want to use
"""
class TradingClient :

    def __init__(self, cbpro_client):
        self.client = cbpro_client

    """
    "  Method to buy the crypto specified at the ticker.
    "
    "  ticker : specifies the cryto pair that we are going to buy. (Ex. BTC-EUR)
    "  limit_price : price to place the buy limit order.
    "  quantity: desired amount of base currency
    """
    def buy(self, ticker, limit_price, quantity) :
        response = self.client.buy(
            price = limit_price,
            size= quantity,
            order_type= 'limit',
            product_id = ticker,
            overdraft_enabled = False
        )
    
    """
    "  Method to sell the crypto specified at the ticker.
    "
    "  ticker : specifies the cryto pair that we are going to sell. (Ex. BTC-EUR)
    "  limit_price : price to place the sell limit order.
    "  quantity: desired amount of base currency
    """
    def sell(self, ticker, limit_price, quantity) :
        response = self.client.sell(
            price = limit_price,
            size= quantity,
            order_type= 'limit',
            product_id = ticker,
            overdraft_enabled = False
        )

    """
    "  Method to check the remaining funds of the currency.
    "
    "  currency : specific currency to look up for remaining funds.
    """
    def viewAccounts(self, currency):
        accounts = self.client.get_accounts()
        account = list(filter(lambda x: x['currency'] == currency, accounts))[0]
        return account
    
    """
    "  Method to get the list of offered products by Coinbase Pro.
    """
    def listProducts(self):
        cbpro_products = self.client.get_products()
        return cbpro_products

    """
    "  Method to get the current price of a crypto pair, like 'BTC-EUR'
    "
    "  ticker : specifies the cryto pair to look the price.
    """
    def getCurrentPriceOfTicker(self, ticker):
        tick = self.client.get_product_ticker(product_id=ticker)
        return tick['bid']

"""
"  Function to comprobate if the ticker is a valid product
"""
def validate_ticker(products, ticker_splited):
    for product in products : #alo mejor cambiar esto por get product
        if product['base_currency'] == ticker_splited[0] and product['quote_currency'] == ticker_splited[1] :
            return True
    return False


"""
"  Function to comprobate if the quantity of base currency is above not below minimum
"""
def validate_amount(products, quantity):
    for product in products :
        if product['base_currency'] == ticker_splited[0] and product['quote_currency'] == ticker_splited[1] :
            if quantity >= float(product['base_min_size']) :
                return True
            else :
                print("Quantity is below minimun for this product. Minimum for "+product['base_currency']+"  is "+product['base_min_size'])
                return False
    return False

"""
"   Function to ask for the ticker and validate it as a product
"""
def ask_for_ticker(products):
    correct_len = False
    valid_ticker = False
    while not correct_len or not valid_ticker :
        tck = str(input("Introduce the ticker you want to trade (Ex: BTC-EUR) :"))
        ticker_splited = tck.split("-")
        valid_ticker = validate_ticker(products, ticker_splited)
        
        if(len(ticker_splited) != 2) : print("Invalid.")
        
        elif not valid_ticker  : print("This product is not supported by Coinbase Pro.")

        else : correct_len = True
    return tck

"""
"  Function to ask for quantity to trade
"
"  products : contains the crypto pairs offered by Coinbase Pro to trade.
"""
def ask_for_quantity(products):
    float_type = False
    while not float_type :
        try:
            quantity = float(input("Introduce the quantity of "+ticker_splited[0]+ " to trade:"))
            float_type = True
        except ValueError:
            print("Invalid number.")
    if validate_amount(products, quantity) :
        return quantity
    return 0.0

"""
MAIN START
"""
auth_client = cbpro.AuthenticatedClient(data_api.public_key,
    data_api.secret,
    data_api.passphrase,
    api_url='https://api-public.sandbox.pro.coinbase.com')
   
#initialize the TradingClient class
tradingClient = TradingClient(auth_client)                              

#get the list of products an their minimuns? 
products = tradingClient.listProducts()

#ask for ticker 
ticker = ask_for_ticker(products)
ticker_splited = ticker.split("-")

#ask for quantity to buy
quantity = 0.0
while quantity == 0.0 :
    quantity = ask_for_quantity(products)

buy_limit_price = 0.0
sell_limit_price = 0.0

#exception controls
orderType = False
while not orderType :
    order = str("Invalid. Introduce type of order [buy or sell] :")
    try:
        order = str(input("Introduce type of order [buy or sell] :"))
        if order != "buy" and order != "sell" :
            print('Invalid.')
        else :
            orderType = True
    except ValueError:
        print("Invalid.")

if order == "buy" :
    #exception controls
    float_type = False
    while not float_type :
        try:
            buy_limit_price = float(input("Introduce buy limit price: "))
            float_type = True
        except ValueError:
            print("Invalid number.")
    
    #checking if you have enough funds
    if float(tradingClient.viewAccounts(ticker_splited[1])['balance'])> buy_limit_price * quantity :
        tradingClient.buy(ticker, buy_limit_price, quantity)
        print('Your purchase order has been placed on Coinbase Pro.')
    else : 
        print('You don\'t have enough funds to buy.')

elif order == "sell" :
    #exception controls
    float_type = False
    while not float_type :
        try:
            sell_limit_price = float(input("Introduce sell limit price: "))
            float_type = True
        except ValueError:
            print("Invalid number.")
    
    #checking if you have enough funds
    if float(tradingClient.viewAccounts(ticker_splited[0])['balance']) >=  quantity :
        tradingClient.sell(ticker, sell_limit_price, quantity)
        print('Your sell order has been placed on Coinbase Pro.')
    else : 
        print('You don\'t have enough funds to sell.')