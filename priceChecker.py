from mws import mws
from yelpapi import yelpapi




access_key = "AKIAJJE4GABFJU7OGNIQ"
seller_id = "ATJR1LYAM2AQI"
secret_key = "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"
marketplace_usa = "ATVPDKIKX0DER"

def checkPrice(asin):
    """Takes an asin and prints whether or not our price is the competitive price.
    Use 'ourPrice' to set the price we are selling the product at."""


    products_api = mws.Products(access_key, secret_key, seller_id, region='US')
    captAmTripPrice = products_api.get_lowest_priced_offers_for_asin(marketplace_usa, asin)
    ourPrice = products_api.get_my_price_for_asin(marketplace_usa, asin)
    """print(captAmTripPrice.parsed['Offers']['Offer'][0]['ListingPrice']['Amount']['value'])"""


    competPrice = float(captAmTripPrice.parsed['Offers']['Offer'][0]['ListingPrice']['Amount']['value'])
    print(ourPrice.parsed['Product']['Offers'])

    if competPrice < ourPrice:
        print("Someone is selling for less! Competitive price = " + str(competPrice))
    else:
       print("Our price, " + str(ourPrice) + ", is the competitive price.")

