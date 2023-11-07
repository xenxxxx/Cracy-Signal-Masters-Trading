from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

""""მთავარი გვერდი"""
b1 = KeyboardButton('Add/change Coins')



kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1)
############################################################

"""""კრიპტოვალუტები"""
g1 = KeyboardButton('BTC/USDT')
g2 = KeyboardButton('ETH/USDT')
g3 = KeyboardButton('BCH/USDT')



kb_coins = ReplyKeyboardMarkup(resize_keyboard=True)

kb_coins.add(g1).add(g2).add(g3)

#################################################################################

"""ბიტკოინის. ქვედა და ზედა ზვღარი"""

c1 = KeyboardButton('BTC/USDT Upper Limit')
c2 = KeyboardButton('BTC/USDT Lower Limit')
c3 = KeyboardButton('Back')

kb_updown = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_updown.add(c1).add(c2).add(c3)
############################################################################

#####
"""ეთერიუმის ქვედა და ზედა ზღვარი"""
eth1 = KeyboardButton('ETH/USDT Upper Limit')
eth2 = KeyboardButton('ETH/USDT Lower Limit')
eth3 = KeyboardButton('Back')

kb_ethereum = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_ethereum.add(eth1).add(eth2).add(eth3)

###########################################################


######
"""BCH-ს ქვედა და ზედა ზღვარი"""
bch1 = KeyboardButton('BCH/USDT Upper Limit')
bch2 = KeyboardButton('BCH/USDT Lower Limit')
bch3 = KeyboardButton('Back')

kb_bitcoincash = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_bitcoincash.add(bch1).add(bch2).add(bch3)






"""""უკან დაბრუნების ღილაკი"""
home1 = KeyboardButton('Back')



kb_home = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_home.add(home1)