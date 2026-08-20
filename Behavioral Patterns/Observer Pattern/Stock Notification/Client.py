from stocks import AAPL, GOOG, TSLA
from subscribers import MobileApp, EmailAlert


appl_stock = AAPL()
goog_stock = GOOG() 
tsla_stock = TSLA()

appl_stock.add_subscriber(mobile_app_subscriber := MobileApp(user_id="user123"))
goog_stock.add_subscriber(email_alert_subscriber := EmailAlert(email="user123@example.com"))
tsla_stock.add_subscriber(mobile_app_subscriber := MobileApp(user_id="user123"))

appl_stock.set_price(210)
goog_stock.set_price(2800)
tsla_stock.set_price(700)