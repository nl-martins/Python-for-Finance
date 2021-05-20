import cbpro 
import data_api
import time

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
    "  limit_price : price to place the limit buy limit order.
    "  quantity: desired amount of base currency
    """
    def buy(self, ticker, limit_price, quantity) :
        print(quantity)
        response = self.client.buy(
            price = limit_price,
            size= quantity,
            order_type= 'limit',
            product_id = ticker,
            overdraft_enabled = False
        )
        print(response)

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
    "  Method to get the current price of a crypto pair, like 'BTC-EUR'
    "
    "  ticker : specifies the cryto pair to look the price.
    """
    def getCurrentPriceOfTicker(self, ticker):
        tick = self.client.get_product_ticker(product_id=ticker)
        return tick['bid']


"""
MAIN START
"""
#these variables can be made user-dependent
ticker = 'BTC-EUR'
limitPrice = 45000.0    #limit price to look up
sats = 0.001            #number of satoshis for each order

while 1: 
    auth_client = cbpro.AuthenticatedClient(data_api.public_key,
        data_api.secret,
        data_api.passphrase,
        api_url='https://api-public.sandbox.pro.coinbase.com')
    
    #initialize the TradingClient class
    tradingClient = TradingClient(auth_client)                              
    
    #get the current price of the crypto pair
    current_price = float(tradingClient.getCurrentPriceOfTicker(ticker))

    #checking if the current price is under or equal the limit price.
    if current_price <= limitPrice :
        #checking if you have enough funds
        if float(tradingClient.viewAccounts('EUR')['balance'])> sats*current_price :
            tradingClient.buy(ticker, current_price, sats)
        else : 
            print('You don\'t have enough money.')

    else : print('The price is higher than your limit price.')
    
    #sleeps during the number of seconds of the parameters
    time.sleep(3600)    #one hour