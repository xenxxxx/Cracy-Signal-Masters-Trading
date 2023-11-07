import sqlite3 as sq

def sql_start():
    global base, cur
    base = sq.connect('users_new.db')
    cur = base.cursor()


async def sql_add_command(state):
    async with state.proxy() as data:
        ID = data['user_id']
        btcusdtup_message = data['btcusdt_up']

        cur.execute(f"SELECT user_id from coins_users where user_id = '{ID}'")
        select = cur.fetchone()

        if select is None:
            sql = "INSERT INTO coins_users  (btc_up, user_id) VALUES (?, ?)"
            val = (btcusdtup_message, ID)
            cur.execute(sql, val)

            base.commit()

        else:

            sql = "UPDATE coins_users SET btc_up = ? \
                                                WHERE user_id = ?"

            val = (btcusdtup_message, ID)
            cur.execute(sql, val)

            base.commit()



async def sql_add_command_delete_bitcoin(state):
    async with state.proxy() as data:
        ID = data['user_id']
        delete = data['btcusdt_up']
        cur.execute(f"SELECT user_id from coins_users where user_id = '{ID}'")
        select = cur.fetchone()

        if select is None:
            pass


        else:

            sql = "UPDATE coins_users SET btc_up = ? \
                                                WHERE user_id = ?"

            val = (delete, ID)
            cur.execute(sql, val)

            base.commit()



"""""ბიტკოინის ქვედა ზღვარი"""


async def sql_add_command_btc_lower(state):
    async with state.proxy() as data:
        ID = data['user_id']
        btcusdtdown_message = data['btcusdt_down']
        cur.execute(f"SELECT user_id from coins_users where user_id = '{ID}'")
        select = cur.fetchone()

        if select is None:
            sql = "INSERT INTO coins_users  (btc_down, user_id) VALUES (?, ?)"
            val = (btcusdtdown_message, ID)
            cur.execute(sql, val)

            base.commit()

        else:

            sql = "UPDATE coins_users SET btc_down = ? \
                                                WHERE user_id = ?"

            val = (btcusdtdown_message, ID)
            cur.execute(sql, val)

            base.commit()



async def sql_add_command_delete_bitcoin_lower(state):
    async with state.proxy() as data:
        ID = data['user_id']
        delete_btc_down = data['btcusdt_down']
        cur.execute(f"SELECT user_id from coins_users where user_id = '{ID}'")
        select = cur.fetchone()

        if select is None:
            pass


        else:

            sql = "UPDATE coins_users SET btc_down = ? \
                                                WHERE user_id = ?"

            val = (delete_btc_down, ID)
            cur.execute(sql, val)

            base.commit()


####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
####################################
"""""eth/usdt"""

async def sql_add_eth_usdt(state):
    async with state.proxy() as data:
        ID = data['user_id']
        ethusdtup_message = data['ethusdt_up']
        cur.execute(f"SELECT user_id from coins_users where user_id = '{ID}'")
        select = cur.fetchone()

        if select is None:
            sql = "INSERT INTO coins_users (eth_up, user_id) VALUES (?, ?)"
            val = (ethusdtup_message, ID)
            cur.execute(sql, val)

            base.commit()

        else:

            sql = "UPDATE coins_users SET eth_up = ? \
                                                WHERE user_id = ?"

            val = (ethusdtup_message, ID)
            cur.execute(sql, val)

            base.commit()



async def sql_add_command_delete_eth_usdt(state):
    async with state.proxy() as data:
        ID = data['user_id']
        delete = data['ethusdt_up']
        cur.execute(f"SELECT user_id from coins_users where user_id = '{ID}'")
        select = cur.fetchone()

        if select is None:
            pass


        else:

            sql = "UPDATE coins_users SET eth_up = ? \
                                                WHERE user_id = ?"

            val = (delete, ID)
            cur.execute(sql, val)

            base.commit()



"""""ეთერიუმის ქვედა ზღვარი"""


async def sql_add_command_eth_usdt_lower(state):
    async with state.proxy() as data:
        ID = data['user_id']
        ethusdtdown_message = data['ethusdt_down']
        cur.execute(f"SELECT user_id from coins_users where user_id = '{ID}'")
        select = cur.fetchone()

        if select is None:
            sql = "INSERT INTO coins_users  (eth_down, user_id) VALUES (?, ?)"
            val = (ethusdtdown_message, ID)
            cur.execute(sql, val)

            base.commit()

        else:

            sql = "UPDATE coins_users SET eth_down = ? \
                                                WHERE user_id = ?"

            val = (ethusdtdown_message, ID)
            cur.execute(sql, val)

            base.commit()



async def sql_add_command_delete_eth_usdt_lower(state):
    async with state.proxy() as data:
        ID = data['user_id']
        delete_eth_down = data['ethusdt_down']
        cur.execute(f"SELECT user_id from coins_users where user_id = '{ID}'")
        select = cur.fetchone()

        if select is None:
            pass


        else:

            sql = "UPDATE coins_users SET eth_down = ? \
                                                WHERE user_id = ?"

            val = (delete_eth_down, ID)
            cur.execute(sql, val)

            base.commit()

###############################################################################
                     #bchusdt
###############################################################################

async def sql_add_bch_usdt(state):
    async with state.proxy() as data:
        ID = data['user_id']
        bchusdtup_message = data['bchusdt_up']
        cur.execute(f"SELECT user_id from coins_users where user_id = '{ID}'")
        select = cur.fetchone()

        if select is None:
            sql = "INSERT INTO coins_users (bch_up, user_id) VALUES (?, ?)"
            val = (bchusdtup_message, ID)
            cur.execute(sql, val)

            base.commit()

        else:

            sql = "UPDATE coins_users SET bch_up = ? \
                                                WHERE user_id = ?"

            val = (bchusdtup_message, ID)
            cur.execute(sql, val)

            base.commit()



async def sql_add_command_delete_bch_usdt(state):
    async with state.proxy() as data:
        ID = data['user_id']
        delete = data['bchusdt_up']
        cur.execute(f"SELECT user_id from coins_users where user_id = '{ID}'")
        select = cur.fetchone()

        if select is None:
            pass


        else:

            sql = "UPDATE coins_users SET bch_up = ? \
                                                WHERE user_id = ?"

            val = (delete, ID)
            cur.execute(sql, val)

            base.commit()















#############


