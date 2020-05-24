from coinbase.wallet.client import Client
from tkinter import *
from tkinter.ttk import *
from threading import Thread
import queue
import json
import requests
import time
from tkinter import messagebox

api_key = "qllinMZsWKJxMbm1"
secret_key = "O8166FUvpXgZk5XowalRE8cP0tVXRWkT"
coinbase_id = "98d51393-b7bf-5381-b727-21200c515708"
client = Client(api_key, secret_key)


file_1 = open('axemo_bal.json', 'r')
bt_bal = json.load(file_1)
file_1.close()
btc_bal = f"{bt_bal:.5f}"
naira = 100

root = Tk()
root.resizable(False, False)
root.geometry("750x550")

style = Style()
style.configure('W.TButton', font=('Calibri', 30))

logo = PhotoImage(file='photos/logo.png')
logo2 = PhotoImage(file='photos/logo2.png')
ex = PhotoImage(file='photos/exc.png')
sc = PhotoImage(file='photos/success.png')
sn = PhotoImage(file='photos/send.png')
rc = PhotoImage(file='photos/recive.png')
ln = PhotoImage(file='photos/line.png')

in_use_l = False
in_use_c = False
sent = False


def home():
    print('checking balance....\n')
    file = open('axemo_bal.json', 'r')
    b_bal = json.load(file)
    file_1.close()
    b_bal = f"{b_bal:.5f}"

    lst = root.place_slaves()
    for l in lst:
        l.place_forget()
    Label(root, image=logo).place(x=-10, y=-40)

    style = Style()
    style.configure('W.TButton', font=('Bell MT', 25))

    print('rendering homepage...')

    name = Label(root, text='DEMO APP')
    name.config(background='white', foreground='red', font=('Calibri Light', 12, 'bold'))
    name.place(x=665, y=0)

    name = Label(root, text=f'{b_bal}btc')
    name.config(background='white', foreground='black', font=('Calibri Light', 50))
    name.place(x=20, y=240)

    name = Label(root, text='Balance:')
    name.config(background='white', foreground='black', font=('Bell MT', 30))
    name.place(x=20, y=210)
    Button(root, text='Transaction history', style='W.TButton', command=lambda: link_transaction()).place(x=380, y=260,
                                                                                                  height=50,
                                                                                                  width=300)
    Button(root, text='Send bitcoin', style='W.TButton', command=lambda: send_btc()).place(x=80, y=360, height=68,
                                                                                           width=600)
    Button(root, text='Create an address', style='W.TButton', command=lambda: address_()).place(x=80, y=450,
                                                                                                height=68,
                                                                                                width=600)


def link_transaction():
    print('rendering transaction page...\n')
    file = open('final_receive_data_save.json', 'r')
    r_lst = json.load(file)
    file_1.close()
    file = open('final_send_data_save.json', 'r')
    send_lst = json.load(file)
    confirmed = r_lst + send_lst
    print(confirmed)
    file_1.close()
    n = 0
    k = 0
    p = 1
    transaction_page(confirmed, n, k, p)


def transaction_page(confirmed, n, k, p):
    lst = root.place_slaves()
    for l in lst:
        l.place_forget()
    Label(root, image=logo).place(x=-10, y=-40)
    name = Label(root, text=f'Transaction history')
    name.config(background='white', foreground='purple', font=('Calibri Light', 30, 'bold'))
    name.place(x=210, y=220)
    name = Label(root, text=f'page{p}')
    name.config(background='white', foreground='purple', font=('Calibri Light', 15, 'bold'))
    name.place(x=650, y=240)
    Button(root, text='Home', command=lambda: home()).place(x=0, y=0)

    p_y = 280
    p2_y = 310
    pc_y = 285
    pl_y = 350

    x = 0
    z = len(confirmed) - k

    if z >= 3:
        for t in range(3):
            t = confirmed[n]
            btc = float(t[2])
            bt_d = f"{btc:.8f}"

            add = t[3]
            if btc > 0:
                Label(root, image=rc, background='white').place(x=5, y=pc_y)
                name = Label(root, text=f'source: {add}')
                name.config(background='white', foreground='purple', font=('Calibri', 15))
                name.place(x=50, y=p2_y)

                name = Label(root, text=f'{bt_d}btc recieved ')
                name.config(background='white', foreground='purple', font=('Calibri', 15))
                name.place(x=50, y=p_y)
            elif btc < 0:
                Label(root, image=sn, background='white').place(x=5, y=pc_y)
                name = Label(root, text=f'To {add}')
                name.config(background='white', foreground='purple', font=('Calibri', 15))
                name.place(x=50, y=p2_y)

                name = Label(root, text=f'{bt_d}btc')
                name.config(background='white', foreground='purple', font=('Calibri', 15))
                name.place(x=50, y=p_y)
            Label(root, image=ln, background='white').place(x=5, y=pl_y)

            p_y += 100
            p2_y += 100
            pc_y += 100
            pl_y += 100
            n += 1
            x += 1
            k += 1

        Button(root, text='next', command=lambda: transaction_page(confirmed, n, k, p + 1)). \
            place(x=630, y=510, height=25, width=100)
        if p > 1:
            _n = n - 6
            _k = k - 6
            Button(root, text='back', command=lambda: transaction_page(confirmed, _n, _k, p - 1)). \
                place(x=500, y=510, height=25, width=100)

    elif z < 3:
        for t in range(z):
            t = confirmed[n]
            btc = float(t[2])
            bt_d = f"{btc:.8f}"

            add = t[3]
            if btc > 0:
                Label(root, image=rc, background='white').place(x=5, y=pc_y)
                name = Label(root, text=f'source: {add}')
                name.config(background='white', foreground='purple', font=('Calibri', 15))
                name.place(x=50, y=p2_y)

                name = Label(root, text=f'{bt_d}btc recieved ')
                name.config(background='white', foreground='purple', font=('Calibri', 15))
                name.place(x=50, y=p_y)
            elif btc < 0:
                Label(root, image=sn, background='white').place(x=5, y=pc_y)
                name = Label(root, text=f'To {add}')
                name.config(background='white', foreground='purple', font=('Calibri', 15))
                name.place(x=50, y=p2_y)

                name = Label(root, text=f'{bt_d}btc ')
                name.config(background='white', foreground='purple', font=('Calibri', 15))
                name.place(x=50, y=p_y)
            Label(root, image=ln, background='white').place(x=5, y=pl_y)

            Label(root, image=ln, background='white').place(x=5, y=pl_y)

            p_y += 100
            p2_y += 100
            pc_y += 100
            pl_y += 100
            n += 1
            x += 1
            k += 1

        if z == 1:
            x = 4
        elif z == 2:
            x = 5
        elif z == 2:
            x = 6
        _n = n - x
        _k = k - x
        Button(root, text='back', command=lambda: transaction_page(confirmed, _n, _k, p - 1)). \
            place(x=500, y=510, height=25, width=100)


def create_address_page():
    print('rendering address page...\n')
    lst = root.place_slaves()
    for l in lst:
        l.place_forget()
    Label(root, image=logo2).place(x=-10, y=-40)

    name = Label(root, text='DEMO APP')
    name.config(background='white', foreground='red', font=('Calibri Light', 12, 'bold'))
    name.place(x=665, y=0)

    name = Label(root, text='Your bitcoin accont address')
    name.config(background='white', foreground='black', font=('Calibri Light', 30))
    name.place(x=142, y=240)
    print('passed here')


def send_btc():
    print('rendering send page....\n')
    lst = root.place_slaves()
    for l in lst:
        l.place_forget()
    Label(root, image=logo2).place(x=-10, y=-40)

    Button(root, text='<-Back', command=lambda: send_btc()).place(x=0, y=0)

    name = Label(root, text='DEMO APP')
    name.config(background='white', foreground='red', font=('Calibri Light', 12, 'bold'))
    name.place(x=665, y=0)

    Button(root, text='<-Back', command=lambda: home()).place(x=0, y=0)
    Button(root, text='Send to bitcoin address with a fee', style='W.TButton',
           command=lambda: take_details_btc_address()). \
        place(x=80, y=220, height=68, width=600)
    Button(root, text='Send to a luno account for free', style='W.TButton', command=lambda: take_details_luno()). \
        place(x=80, y=300, height=68, width=600)
    Button(root, text='Send to a coinbase acount  for free ', style='W.TButton',
           command=lambda: take_details_coinbase()). \
        place(x=80, y=380, height=68, width=600)
    Button(root, text='Send to an axemo acount for free', style='W.TButton', command=lambda: take_details_axemo()). \
        place(x=80, y=460, height=68, width=600)


def take_details_coinbase():
    print('rendering details page for coinbase...\n')
    lst = root.place_slaves()
    for l in lst:
        l.place_forget()
    Label(root, image=logo2).place(x=-10, y=-40)
    amount_btc = IntVar()
    amount_local = IntVar()
    destination = StringVar()
    description = StringVar()
    fee = 0
    route = 'coinbase'

    name = Label(root, text='DEMO APP')
    name.config(background='white', foreground='red', font=('Calibri Light', 12, 'bold'))
    name.place(x=665, y=0)

    exc = Label(root, image=ex)
    exc.config(background='white')
    exc.place(x=266, y=330)

    Button(root, text='<-Back', command=lambda: send_btc()).place(x=0, y=0)

    Entry(root, width=20, textvariable=amount_btc).place(x=320, y=340)
    Entry(root, width=20, textvariable=amount_local).place(x=140, y=340)
    Entry(root, width=60, textvariable=destination).place(x=278, y=280)
    Entry(root, width=60, textvariable=description).place(x=210, y=392)

    name = Label(root, text='Send bitcoin to a coinbase account')
    name.config(background='white', foreground='black', font=('Calibri Light', 30, 'bold'))
    name.place(x=115, y=200)

    name = Label(root, text='Please cross-check your entries before proceeding')
    name.config(background='white', foreground='purple', font=('Calibri Light', 12, 'bold'))
    name.place(x=217, y=240)

    name = Label(root, text='NGN')
    name.config(background='white', foreground='green', font=('Calibri Light', 20))
    name.place(x=80, y=330)
    name = Label(root, text='BTC')
    name.config(background='white', foreground='purple', font=('Calibri Light', 20))
    name.place(x=450, y=330)
    name = Label(root, text='Coinbase address')
    name.config(background='white', foreground='black', font=('Calibri Light', 20))
    name.place(x=80, y=270)
    name = Label(root, text='Description')
    name.config(background='white', foreground='black', font=('Calibri Light', 20))
    name.place(x=80, y=380)

    cont = Button(root, text='Continue', style='W.TButton', command=lambda: check_det(amount_btc.get(),
                                                                                        amount_local.get(),
                                                                                        destination.get(),
                                                                                        description.get(), fee,
                                                                                        route))

    cont.place(x=80, y=460, height=68, width=600)


def take_details_luno():
    print('rendering details page for luno...\n')
    lst = root.place_slaves()
    for l in lst:
        l.place_forget()
    Label(root, image=logo2).place(x=-10, y=-40)
    amount_btc = IntVar()
    amount_local = IntVar()
    destination = StringVar()
    description = StringVar()
    fee = 0
    route = 'luno'

    name = Label(root, text='DEMO APP')
    name.config(background='white', foreground='red', font=('Calibri Light', 12, 'bold'))
    name.place(x=665, y=0)

    exc = Label(root, image=ex)
    exc.config(background='white')
    exc.place(x=266, y=330)

    Button(root, text='<-Back', command=lambda: send_btc()).place(x=0, y=0)

    Entry(root, width=20, textvariable=amount_btc).place(x=320, y=340)
    Entry(root, width=20, textvariable=amount_local).place(x=140, y=340)
    Entry(root, width=60, textvariable=destination).place(x=232, y=280)
    Entry(root, width=60, textvariable=description).place(x=210, y=392)

    name = Label(root, text='Send bitcoin to a luno account')
    name.config(background='white', foreground='black', font=('Calibri Light', 30, 'bold'))
    name.place(x=125, y=200)
    name = Label(root, text='Please cross-check your entries before proceeding')
    name.config(background='white', foreground='purple', font=('Calibri Light', 12, 'bold'))
    name.place(x=217, y=240)

    name = Label(root, text='NGN')
    name.config(background='white', foreground='green', font=('Calibri Light', 20))
    name.place(x=80, y=330)
    name = Label(root, text='BTC')
    name.config(background='white', foreground='purple', font=('Calibri Light', 20))
    name.place(x=450, y=330)
    name = Label(root, text='Luno address')
    name.config(background='white', foreground='black', font=('Calibri Light', 20))
    name.place(x=80, y=270)
    name = Label(root, text='Description')
    name.config(background='white', foreground='black', font=('Calibri Light', 20))
    name.place(x=80, y=380)

    cont = Button(root, text='Continue', style='W.TButton', command=lambda: check_det(amount_btc.get(),
                                                                                        amount_local.get(),
                                                                                        destination.get(),
                                                                                        description.get(), fee,
                                                                                        route))
    cont.place(x=80, y=460, height=68, width=600)


def take_details_axemo():
    print('rendering details page for axemo...\n')
    lst = root.place_slaves()
    for l in lst:
        l.place_forget()
    Label(root, image=logo2).place(x=-10, y=-40)
    amount_btc = IntVar()
    amount_local = IntVar()
    destination = StringVar()
    description = StringVar()
    fee = 0
    route = 'axemo'

    name = Label(root, text='DEMO APP')
    name.config(background='white', foreground='red', font=('Calibri Light', 12, 'bold'))
    name.place(x=665, y=0)

    exc = Label(root, image=ex)
    exc.config(background='white')
    exc.place(x=266, y=330)

    Button(root, text='<-Back', command=lambda: send_btc()).place(x=0, y=0)

    Entry(root, width=20, textvariable=amount_btc).place(x=320, y=340)
    Entry(root, width=20, textvariable=amount_local).place(x=140, y=340)
    Entry(root, width=60, textvariable=destination).place(x=250, y=280)
    Entry(root, width=60, textvariable=description).place(x=210, y=392)

    name = Label(root, text='Send bitcoin to an axemo account')
    name.config(background='white', foreground='black', font=('Calibri Light', 30, 'bold'))
    name.place(x=125, y=200)
    name = Label(root, text='Please cross-check your entries before proceeding')
    name.config(background='white', foreground='purple', font=('Calibri Light', 12, 'bold'))
    name.place(x=217, y=240)

    name = Label(root, text='NGN')
    name.config(background='white', foreground='green', font=('Calibri Light', 20))
    name.place(x=80, y=330)
    name = Label(root, text='BTC')
    name.config(background='white', foreground='purple', font=('Calibri Light', 20))
    name.place(x=450, y=330)
    name = Label(root, text='Axemo address')
    name.config(background='white', foreground='black', font=('Calibri Light', 20))
    name.place(x=80, y=270)
    name = Label(root, text='Description')
    name.config(background='white', foreground='black', font=('Calibri Light', 20))
    name.place(x=80, y=380)

    cont = Button(root, text='Continue', style='W.TButton', command=lambda: check_det(amount_btc.get(),
                                                                                        amount_local.get(),
                                                                                        destination.get(),
                                                                                        description.get(), fee,
                                                                                        route))
    cont.place(x=80, y=460, height=68, width=600)


def take_details_btc_address():
    print('rendering details page for btc wallet address...\n')
    lst = root.place_slaves()
    for l in lst:
        l.place_forget()
    Label(root, image=logo2).place(x=-10, y=-40)
    amount_btc = IntVar()
    amount_local = IntVar()
    destination = StringVar()
    description = StringVar()
    fee = 'testing..'
    route = 'bitcoin'

    name = Label(root, text='DEMO APP')
    name.config(background='white', foreground='red', font=('Calibri Light', 12, 'bold'))
    name.place(x=665, y=0)

    exc = Label(root, image=ex)
    exc.config(background='white')
    exc.place(x=266, y=330)

    Button(root, text='<-Back', command=lambda: send_btc()).place(x=0, y=0)

    Entry(root, width=20, textvariable=amount_btc).place(x=320, y=340)
    Entry(root, width=20, textvariable=amount_local).place(x=140, y=340)
    Entry(root, width=60, textvariable=destination).place(x=251, y=280)
    Entry(root, width=60, textvariable=description).place(x=210, y=392)

    name = Label(root, text='Send bitcoin to a bitcoin account')
    name.config(background='white', foreground='black', font=('Calibri Light', 30, 'bold'))
    name.place(x=125, y=200)
    name = Label(root, text='Please cross-check your entries before proceeding')
    name.config(background='white', foreground='purple', font=('Calibri Light', 12, 'bold'))
    name.place(x=217, y=240)

    name = Label(root, text='NGN')
    name.config(background='white', foreground='green', font=('Calibri Light', 20))
    name.place(x=80, y=330)
    name = Label(root, text='BTC')
    name.config(background='white', foreground='purple', font=('Calibri Light', 20))
    name.place(x=450, y=330)
    name = Label(root, text='Bitcoin address')
    name.config(background='white', foreground='black', font=('Calibri Light', 20))
    name.place(x=80, y=270)
    name = Label(root, text='Description')
    name.config(background='white', foreground='black', font=('Calibri Light', 20))
    name.place(x=80, y=380)

    cont = Button(root, text='Continue', style='W.TButton', command=lambda: check_det(amount_btc.get(),
                                                                                      amount_local.get(),
                                                                                      destination.get(),
                                                                                      description.get(), fee,
                                                                                      route))
    cont.place(x=80, y=460, height=68, width=600)


def check_det(a, b, c, d, f, e):
    print(f'validating send details ({a}btc, NGN{b}, {c}, description: {d}, fee: {f}, route: {e})...')
    if a or b:
        if not a:
            a = 0
        if not b:
            b = 0
        if c:
            if a <= bt_bal:
                if b <= naira:
                    print('details confirmed..\n')
                    confirm_det(a, b, c, d, f, e)

                else:
                    print(f'insufficient funds. bal = {bt_bal}\n')
                    messagebox.showinfo(message='insufficient funds')
            else:
                print(f'insufficient funds. bal = {naira}\n')
                messagebox.showinfo(message='insufficient funds')
        else:
            print('invalid email entered')
            messagebox.showinfo(message='please enter a valid email')
    else:
        print('invalid amount entered')
        messagebox.showinfo(message='please enter a valid amount')


def confirm_det(am_btc, am_ngn, dest, desc, fee, route):
    def open_page():
        print('rendering confirmation page...\n')
        lst = root.place_slaves()
        for l in lst:
            l.place_forget()
        Label(root, image=logo2).place(x=-10, y=-40)

        if route == 'coinbase':
            Button(root, text='<-Back', command=lambda: take_details_coinbase()).place(x=0, y=0)
        elif route == 'luno':
            Button(root, text='<-Back', command=lambda: take_details_luno()).place(x=0, y=0)
        elif route == 'axemo':
            Button(root, text='<-Back', command=lambda: take_details_axemo()).place(x=0, y=0)
        elif route == 'bitcoin':
            Button(root, text='<-Back', command=lambda: take_details_btc_address()).place(x=0, y=0)

        name = Label(root, text='Please confirm your details before sending')
        name.config(background='white', foreground='black', font=('Bell MT', 25))
        name.place(x=100, y=200)

        name = Label(root, text='Address:')
        name.config(background='white', foreground='black', font=('Bell MT', 18))
        name.place(x=50, y=250)
        name = Label(root, text=dest)
        name.config(background='white', foreground='purple', font=('Calibri', 17))
        name.place(x=140, y=250)

        name = Label(root, text='Amount:')
        name.config(background='white', foreground='black', font=('Bell MT', 20))
        name.place(x=50, y=310)

        name = Label(root, text='Description:')
        name.config(background='white', foreground='black', font=('Bell MT', 20))
        name.place(x=50, y=370)
        if desc:
            name = Label(root, text=desc)
            name.config(background='white', foreground='purple', font=('Calibri', 17))
            name.place(x=191, y=370)
        else:
            name = Label(root, text='')
            name.config(background='white', foreground='black', font=('Calibri', 17))
            name.place(x=191, y=370)

        name = Label(root, text='Network fee: ')
        name.config(background='white', foreground='black', font=('Bell MT', 20))
        name.place(x=50, y=440)
        if fee:
            name = Label(root, text=f'{fee}btc')
            name.config(background='white', foreground='purple', font=('v', 17))
            name.place(x=200, y=441)
        else:
            name = Label(root, text='Free')
            name.config(background='white', foreground='purple', font=('Calibri', 17))
            name.place(x=200, y=441)

    def check_price():
        print('checking conversion rate...')
        price = client.get_buy_price(currency_pair='BTC-NGN')

        if am_btc:
            ng = float(am_btc) * float(price['amount'])
            ngn = f"{ng:.2f}"
            name = Label(root, text=f'NGN{ngn}    /    {am_btc}btc')
            name.config(background='white', foreground='purple', font=('Calibri', 15))
            name.place(x=150, y=314)

            print(f'conversion:  NGN{ngn}    /    {am_btc}btc\n')

            Button(root, text='Send', style='W.TButton', command=lambda: send_page(am_btc, dest, desc, fee, route)). \
                place(x=100, y=490, height=50, width=500)
        elif am_ngn:
            btc = float(am_ngn) / float(price['amount'])
            btc = f"{btc:.8f}"
            name = Label(root, text=f'NGN{am_ngn}    /    {btc}btc')
            name.config(background='white', foreground='purple', font=('Calibri', 15))
            name.place(x=150, y=314)

            print(f'conversion:   NGN{am_ngn}    /    {btc}btc\n')

            Button(root, text='Send', style='W.TButton', command=lambda: send_page(btc, dest, desc, fee, route)). \
                place(x=100, y=490, height=50, width=500)
        else:
            name = Label(root, text=f'NGN{0.00}    /    {0.00000000}btc')
            name.config(background='white', foreground='purple', font=('Calibri', 15))
            name.place(x=150, y=314)

            print(f'conversion:   NGN{0.00}    /    {0.00000000}btc\n')

            Button(root, text='Send', style='W.TButton', command=lambda: send_page(btc, dest, desc, fee, route)). \
                place(x=100, y=490, height=50, width=500)

        name = Label(root, text='Amount:')
        name.config(background='white', foreground='black', font=('Bell MT', 20))
        name.place(x=50, y=310)

        name = Label(root, text='DEMO APP')
        name.config(background='white', foreground='red', font=('Calibri Light', 12, 'bold'))
        name.place(x=665, y=0)

    thread1 = Thread(target=open_page)
    thread2 = Thread(target=check_price)

    thread1.start()
    thread2.start()


def initiate_transaction(btc, address, desc, fee, route):
    print('initiating transfer...\n')
    print(f'route: {route}\n')
    if route == 'coinbase':
        print(f'transfer details: {btc}, {address}, {desc}, {fee}')
        print(f'########## initiating transfer of {btc}btc to {address} through coinbase ########\n')
        send_coinbase(btc, address, desc, fee)
    elif route == 'bitcoin':
        print(f'transfer details: {btc}, {address}, {desc}, {fee}')
        print(f'########## initiating transfer of {btc}btc to {address} through coinbase ########\n')
        send_coinbase(btc, address, desc, fee)
    elif route == 'axemo':
        print(f'########## initiating transfer of {btc}btc to {address} through coinbase ########\n')
        send_coinbase(btc, address, desc, fee)
    elif route == 'luno':
        print(f'########## initiating transfer of {btc}btc to {address} through luno ########\n')
        print(f'transfer details: {btc}, {address}, {desc}, {fee}')
        send_to_luno(btc, address, desc)

    else:
        print('error: unable to identify route')


def send_page(btc, address, desc, fee, route):
    global sent
    sent = False
    lst = root.place_slaves()
    for l in lst:
        l.place_forget()
    Label(root, image=logo2).place(x=-10, y=-40)
    name = Label(root, text=f'Sending {btc}btc to {address}...')
    name.config(background='white', foreground='black', font=('Calibri', 20))
    name.place(x=98, y=208)

    thread2 = Thread(target=initiate_transaction, args=(btc, address, desc, fee, route))
    thread2.start()

    success_page()


def success_page():
    print('rendering success page...\n')
    lst = root.place_slaves()
    for l in lst:
        l.place_forget()
    Label(root, image=logo2).place(x=-10, y=-40)
    print(sent)
    Label(root, image=sc, background='white').place(x=20, y=150)
    name = Label(root, text='TRANSACTION SUCCESSFUL!')
    name.config(background='white', foreground='green', font=('Bell MT', 30))
    name.place(x=98, y=380)
    Button(root, text='Done', style='W.TButton', command=lambda: home()).place(x=80, y=450, height=68, width=600)


def create_address():
    name = Label(root, text='Loading..')
    name.config(background='white', foreground='black', font=('Calibri Light', 30))
    name.place(x=98, y=300)

    print('getting address....\n')

    get_id = open('coinbase_funded_keys.json', 'r')
    id = json.load(get_id)
    get_id.close()

    use_id = id[0][2]

    address = client.create_address(use_id)
    address = [address['address']]
    print(address)

    pending = open('addresses.json', 'r')
    public_ads = json.load(pending)
    pending.close()

    public_ads.append([address[0], 'demo_user'])

    pending = open('addresses.json', 'w')
    json.dump(public_ads, pending)
    pending.close()

    temp_address = open('copy_address.json', 'w')
    json.dump(address, temp_address)
    temp_address.close()

    name = Label(root, text=address)
    name.config(background='white', foreground='black', font=('Calibri Light', 25))
    name.place(x=98, y=300)
    Button(root, text='copy', command=lambda: copy()).place(x=350, y=350)
    Button(root, text='Done', style='W.TButton', command=lambda: home()).place(x=80, y=450, height=68,
                                                                               width=600)


def copy():
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    copy_ad = open('copy_address.json', 'r')
    add = json.load(copy_ad)
    copy_ad.close()
    clip.clipboard_append(add[0])
    clip.destroy()
    print('address copied.\n')


def address_():
    thread_a = Thread(target=create_address_page)
    thread_b = Thread(target=create_address)

    thread_a.start()
    thread_b.start()


def send_to_luno(btc, address, desc):
    global in_use
    global sent
    amount = str(btc)

    try:
        if in_use_l:
            time.sleep(2)
        file_a = open('luno_funded_keys.json', 'r')
        keys = json.load(file_a)
        file_a.close()
        key = keys[0]
        print(f'using key pair {key}')
        sec_key = key[0]
        key_id = key[1]
        payload = {'amount': amount, 'currency': 'XBT', 'address': address,
                   'description': desc}
        r = requests.get('https://api.mybitx.com/api/1/send', params=payload)
        print('sending request to luno...')
        rs = requests.post(r.url, auth=(key_id, sec_key)).json()
        print(rs)
        suc = []
        for k, v in rs.items():
            suc.append(k)
            suc.append(v)
        if 'success' in suc:
            global sent

            print('rearranging keys...')
            used_key = keys[0]
            keys.remove(keys[0])
            keys.append(used_key)

            print('re-saving_keys...')
            file_update = open('luno_funded_keys.json', 'w')
            json.dump(keys, file_update)
            file_update.close()

            print('updating_balance...')

            sent = True
            update = float(btc_bal) - float(btc)
            new = f"{update:.7f}"
            file = open('axemo_bal.json', 'w')
            json.dump(float(new), file)
            file.close()

            rec = [desc, "completed", f'-{btc}', address]

            print('saving outgoing transaction data.....')
            file_1 = open('final_send_data_save.json', 'r')
            saved_list = json.load(file_1)
            file_1.close()
            saved_list.insert(0, rec)
            print(saved_list)
            file = open('final_send_data_save.json', 'w')
            json.dump(saved_list, file)
            file.close()
            sent = True
            print(f'transaction of {btc} to {address} completed successfully')

        elif 'Insufficient balance.' in suc:
            print(f'insufficient balance in {keys[0]}')
            print('sending keys to funding queue...')
            file_a = open('luno_awaiting_fund.json', 'r')
            awaiting_keys = json.load(file_a)
            file_a.close()
            awaiting_keys.append(keys[0])

            file_update = open('luno_awaiting_fund.json', 'w')
            json.dump(awaiting_keys, file_update)
            file_update.close()
            print('keys sent successfully.')

            print('removing keys from funded list...')
            keys.remove(keys[0])
            file_update = open('luno_funded_keys.json', 'w')
            json.dump(keys, file_update)
            file_update.close()
            print('keys removed successfully.')

            print('waiting for 1 second...')
            time.sleep(1)

            funding_manager_luno(0)

            print('retrying transaction...')
            send_to_luno(btc, address, desc)

    except IndexError:
        print('No new keys available in funded list!!')
        print('waiting for keys...\n')
        time.sleep(5)
        print('retrying transaction...')
        send_to_luno(btc, address, desc)

    except Exception as e:
        print(e)


def send_coinbase(btc, address, desc, fee):
    print('###############################################')

    global sent
    try:
        file_a = open('coinbase_funded_keys.json', 'r')
        keys = json.load(file_a)
        file_a.close()

        key = keys[0]

        print(f'using key pair {key}...')
        secret = key[0]
        cb_key = key[1]
        cb_id = key[2]
        btc = float(btc)

        client = Client(cb_key, secret)
        r = client.send_money(cb_id, to=address, amount=btc, currency='BTC')

        print(f'SENT {btc}btc to {address} successfully!')

        update = float(btc_bal) - float(btc)
        update = f"{update:.5f}"
        file = open('axemo_bal.json', 'w')
        json.dump(float(update), file)
        file.close()

        print(r)
        suc = []
        for k, v in r.items():
            suc.append(k)
            suc.append(v)

        print(suc)
        if 'completed' in suc:
            global sent

            print('rearranging keys...')
            used_key = keys[0]
            keys.remove(keys[0])
            keys.append(used_key)

            print('re-saving_keys...')
            file_update = open('luno_funded_keys.json', 'w')
            json.dump(keys, file_update)
            file_update.close()

            print('updating_balance...')

            sent = True
            update = float(btc_bal) - float(btc)
            new = f"{update:.7f}"
            file = open('axemo_bal.json', 'w')
            json.dump(float(new), file)
            file.close()
            print(new)

            rec = [desc, "completed", f'-{btc}', address]

            print('saving outgoing transaction data.....')
            file_1 = open('final_send_data_save.json', 'r')
            saved_list = json.load(file_1)
            file_1.close()
            saved_list.insert(0, rec)
            print(saved_list)
            file = open('final_send_data_save.json', 'w')
            json.dump(saved_list, file)
            file.close()

            sent = True
            print(f'transaction of {btc} to {address} completed successfully')

    except IndexError:
        print('No new keys available in funded list!!')
        print('waiting for keys...\n')
        time.sleep(5)
        print('retrying...')
        send_coinbase(btc, address, desc, fee)

    except Exception as e:
        e = str(e)
        print(e)
        if e == "APIError(id=validation_error): You don't have that much.":
            print(f'insufficient funds in {keys[0]}')
            file_a = open('coinbase_funded_keys.json', 'r')
            keys = json.load(file_a)
            file_a.close()

            print('sending keys to funding queue...')
            file_a = open('coinbase_awaiting_fund.json', 'r')
            awaiting_keys = json.load(file_a)
            file_a.close()
            awaiting_keys.append(keys[0])

            file_update = open('coinbase_awaiting_fund.json', 'w')
            json.dump(awaiting_keys, file_update)
            file_update.close()
            print('keys sent sucessfully.')

            print('removing keys from funded list...')
            keys.remove(keys[0])
            file_update = open('coinbase_funded_keys.json', 'w')
            json.dump(keys, file_update)
            file_update.close()
            print('keys removed successfully.')
            print('waiting for 5 seconds...')
            time.sleep(1)

            funding_manager_coinbase(0)

            print('retrying transaction...\n')
            send_coinbase(btc, address, desc, fee)


def funding_manager_luno(trial):
    print('\n########COINBASE FUNDING##############')
    if trial < 5:
        try:
            file_a = open('luno_awaiting_fund.json', 'r')
            a_f = json.load(file_a)
            file_a.close()

            x = a_f[0]

            a = time.time()
            print(f'luno non_funded keys detected\n')

            file_update = open('luno_funded_keys.json', 'r')
            funded = json.load(file_update)
            file_update.close()

            print(f'checking balance of non_funded luno key: {x}...\n')

            payload = {'asset': 'XBT'}
            r = requests.get('https://api.mybitx.com/api/1/balance', params=payload)
            rs = requests.get(r.url, auth=(x[1], x[0])).json()
            old_bal = rs['balance'][0]['balance']

            print(f'balance of {x} = {old_bal}\n')

            balance_sheet_w_id = []
            balance_list = []

            print(f'checking balance of luno funded keys...')

            for i in funded:
                payload = {'asset': 'XBT'}
                r = requests.get('https://api.mybitx.com/api/1/balance', params=payload)
                rs = requests.get(r.url, auth=(i[1], i[0])).json()
                balance = float(rs['balance'][0]['balance'])
                print(balance)
                time.sleep(10)
                balance_sheet_w_id.append([i[0], i[1], balance])
                balance_list.append(balance)
                print(f'balance of {i} = {balance}')

            max_bal = max(balance_list)
            print(max_bal)
            index = balance_list.index(max_bal)
            use_key = balance_sheet_w_id[index]

            print(f'\n{float(use_key[2])}    {float(old_bal)} \n')

            if float(use_key[2]) > float(old_bal):
                print('trying to initiate re-funding with luno...\n')

                try:
                    amount_rf = float(use_key[2]) / 2
                    amount_rf = f"{amount_rf:.8f}"
                    amt_rf = str(amount_rf)
                    print(f'sending {amt_rf} to {x[2]}...\n')

                    payload = {'amount': amt_rf, 'currency': 'XBT', 'address': x[2],
                               'description': 're-fundinng process'}
                    print(f'Transferring {amount_rf} to account: {x[2]}')
                    s = requests.get('https://api.mybitx.com/api/1/send', params=payload)
                    r_f = requests.post(s.url, auth=(use_key[1], use_key[0])).json()
                    print(r_f)

                    suc = []
                    for k, v in r_f.items():
                        suc.append(k)
                        suc.append(v)
                    if 'success' in suc:
                        file_a = open('luno_awaiting_fund.json', 'r')
                        awaiting_keys_2 = json.load(file_a)
                        file_a.close()

                        awaiting_keys_2.remove(x)

                        file_remove = open('luno_awaiting_fund.json', 'w')
                        json.dump(awaiting_keys_2, file_remove)
                        file_remove.close()
                    else:
                        funding_manager_luno()

                except Exception as e:
                    print(e)
                    funding_manager_luno(trial + 1)

            else:
                print('insufficient funds in all luno keys\n')
                print('retrying re-funding with coinbase...\n')
                payload = {'asset': 'XBT'}
                print(f'getting address of {x}...\n')
                r = requests.get('https://api.mybitx.com/api/1/funding_address', params=payload)
                rs = requests.get(r.url, auth=(x[1], x[0])).json()
                btc_address = rs['address']

                print(f'btc address {btc_address}')

                cb_funded = open('coinbase_funded_keys.json', 'r')
                funded = json.load(cb_funded)
                cb_funded.close()

                cb_balance_sheet_w_id = []
                balance_lst = []

                print('checking balance in all coinbase accounts...')
                for a in funded:
                    print(f'checking {a}...')
                    client_a = Client(a[1], a[0])
                    account = client_a.get_account('BTC')
                    bal = float(account['balance']['amount'])
                    cb_balance_sheet_w_id.append([a[0], a[1], a[2], bal])
                    balance_lst.append(bal)
                    print(f'balance of {a}: {bal}\n')

                print(f'balance list: {balance_lst}')
                cb_max_bal = max(balance_lst)
                print(f'max balance in all coinbase accounts = {cb_max_bal}')
                ind = balance_lst.index(cb_max_bal)
                use_key = cb_balance_sheet_w_id[ind]

                try:
                    print('trying to initiate re-funding with coinbase...')

                    amount = cb_max_bal / 2
                    amount = f"{amount:.8f}"
                    print(amount)
                    print('PASS')
                    print(f'btc address {btc_address}')

                    client_b = Client(use_key[1], use_key[0])
                    tx = client_b.send_money(use_key[2], to=btc_address, amount=amount, currency='BTC')
                    print(tx)

                    suc = []
                    for k, v in tx.items():
                        suc.append(k)
                        suc.append(v)

                    print(suc)
                    if 'completed' in suc:
                        file_a = open('coinbase_awaiting_fund.json', 'r')
                        awaiting_keys_2 = json.load(file_a)
                        file_a.close()

                        awaiting_keys_2.remove(x)

                        file_remove = open('coinbase_awaiting_fund.json', 'w')
                        json.dump(awaiting_keys_2, file_remove)
                        file_remove.close()
                    else:
                        funding_manager_luno(trial + 1)

                except Exception as e:
                    print(e)
                    time.sleep(5)
                    funding_manager_luno(trial + 1)

            file_update = open('luno_funded_keys.json', 'r')
            funded = json.load(file_update)
            file_update.close()

            funded.append(x)

            file_update = open('luno_funded_keys.json', 'w')
            json.dump(funded, file_update)
            file_update.close()
            time.sleep(1)

            b = time.time()
            print(f'luno funded keys transfer time: {b - a}\n\n')

        except Exception as e:
            print(e)
            time.sleep(5)
            funding_manager_luno(trial + 1)

    else:
        print('maximum trials exceded')


def funding_manager_coinbase(trial):
    print('\n########COINBASE FUNDING##############')
    if trial < 5:
        try:

            file_a = open('coinbase_awaiting_fund.json', 'r')
            a_f = json.load(file_a)
            file_a.close()

            print(a_f)

            x = a_f[0]

            a = time.time()
            print('coinbase non_funded keys detected\n')

            file_update = open('coinbase_funded_keys.json', 'r')
            funded = json.load(file_update)
            file_update.close()

            print(f'checking balance of non_funded coinbase key: {x}...')

            client_a = Client(x[1], x[0])
            account = client_a.get_account('BTC')
            old_bal = float(account['balance']['amount'])
            print(f'balance of {x} = {old_bal}')

            cb_balance_sheet_w_id = []
            balance_lst = []

            print(f'checking balance of luno funded keys...\n')

            for a in funded:
                print(f'checking {a}...')
                client_a = Client(a[1], a[0])
                account = client_a.get_account('BTC')
                bal = float(account['balance']['amount'])
                cb_balance_sheet_w_id.append([a[0], a[1], a[2], bal])
                balance_lst.append(bal)
                print(f'balance of {a}: {bal}\n')

            print(cb_balance_sheet_w_id)
            print(balance_lst)

            max_bal = max(balance_lst)
            print(max_bal)
            index = balance_lst.index(max_bal)
            use_key = cb_balance_sheet_w_id[index]
            print(use_key)

            print(f'\n{float(use_key[3])}    {float(old_bal)} \n')

            if float(use_key[3]) > float(old_bal):

                print('trying to initiate re-funding with coinbase..\n')
                try:
                    amount = max_bal / 2
                    amount = f"{amount:.8f}"
                    print(amount)
                    print('PASS')
                    print(f'btc address {x[2]}')

                    client_b = Client(use_key[1], use_key[0])
                    tx = client_b.send_money(use_key[2], to=x[3], amount=amount, currency='BTC')
                    print(tx)

                    suc = []
                    for k, v in tx.items():
                        suc.append(k)
                        suc.append(v)

                    print(suc)
                    if 'completed' in suc:
                        file_a = open('coinbase_awaiting_fund.json', 'r')
                        awaiting_keys_2 = json.load(file_a)
                        file_a.close()

                        awaiting_keys_2.remove(x)

                        file_remove = open('coinbase_awaiting_fund.json', 'w')
                        json.dump(awaiting_keys_2, file_remove)
                        file_remove.close()
                    else:
                        funding_manager_coinbase()

                except Exception as e:
                    print(e)
                    funding_manager_coinbase(trial + 1)

            else:
                print('insufficient funds in all coinbase keys\n')
                print('retrying re-funding with luno...\n')

                client = Client(use_key[1], use_key[0])
                address = client.create_address(coinbase_id)
                address = address['address']

                print(f'btc address {address}')

                cb_funded = open('luno_funded_keys.json', 'r')
                funded = json.load(cb_funded)
                cb_funded.close()

                balance_sheet_w_id = []
                balance_list = []

                print('checking balance in all luno accounts...\n')
                for i in funded:
                    print('#############################')
                    payload = {'asset': 'XBT'}
                    r = requests.get('https://api.mybitx.com/api/1/balance', params=payload)
                    rs = requests.get(r.url, auth=(i[1], i[0])).json()
                    balance = float(rs['balance'][0]['balance'])
                    balance_sheet_w_id.append([i[0], i[1], balance])
                    balance_list.append(balance)
                    print(f'balance of luno keys: {i} = {balance}')

                print(f'balance list: {balance_list}')
                cb_max_bal = max(balance_list)
                print(f'max balance in all luno accounts = {cb_max_bal}')
                ind = balance_list.index(cb_max_bal)
                use_key = balance_sheet_w_id[ind]
                print('**************************************')
                print(x)
                try:
                    print('trying to initiate re-funding with luno...')

                    amount_rf = float(use_key[2]) / 2
                    amount_rf = f"{amount_rf:.8f}"
                    amt_rf = str(amount_rf)
                    print(amt_rf)

                    payload = {'amount': amt_rf, 'currency': 'XBT', 'address': address,
                               'description': 're-fundinng process'}
                    print(f'Transferring {amount_rf} to account: {address}')
                    s = requests.get('https://api.mybitx.com/api/1/send', params=payload)
                    r_f = requests.post(s.url, auth=(use_key[1], use_key[0])).json()
                    print(r_f)

                    suc = []
                    for k, v in r_f.items():
                        suc.append(k)
                        suc.append(v)
                    if 'success' in suc:
                        file_a = open('coinbase_awaiting_fund.json', 'r')
                        awaiting_keys_2 = json.load(file_a)
                        file_a.close()

                        awaiting_keys_2.remove(x)

                        file_remove = open('coinbase_awaiting_fund.json', 'w')
                        json.dump(awaiting_keys_2, file_remove)
                        file_remove.close()

                        file_update = open('coinbase_funded_keys.json', 'r')
                        funded = json.load(file_update)
                        file_update.close()

                        funded.append(x)

                        file_update = open('coinbase_funded_keys.json', 'w')
                        json.dump(funded, file_update)
                        file_update.close()
                        time.sleep(1)

                        b = time.time()
                        print(f'coinbase funded keys transfer time: {b - a}\n\n')
                    else:
                        funding_manager_coinbase(trial + 1)

                except Exception as e:
                    print('####################################***********')
                    print(e)
                    funding_manager_coinbase(trial + 1)

        except Exception as e:
            print(e)
            time.sleep(5)
            funding_manager_coinbase(trial + 1)
    else:
        print('maximum refund trials exceeded.')


def tx_list_thread():

    def get_notification_list(url):
        print('getting notifications....')
        r = requests.get(url).json()
        return r

    def save_notification_id(n_list):
        print('saving notifications id...')
        file_1 = open('notif_tx_id.json', 'r')
        old_ids = json.load(file_1)
        file_1.close()

        for i in n_list['data']:
            if i['id'] not in old_ids:
                old_ids.append(i['id'])

                file = open('notif_tx_id.json', 'w')
                json.dump(old_ids, file)
                file.close()
                get_useful_data_url(i)

    def get_useful_data_url(l):
        print('extracting useful data....')
        u_data = [l['id'], l['type'], l['additional_data']['amount']['amount'], l['data']['address']]
        final_tx_confirmation(u_data)

    def final_tx_confirmation(data):
        print('confirming transactions.....')
        bal = float(data[2])
        if bal > 0.00000000:
            print(f'CREDIT ALERT! OF {data[2]}btc FROM {data[3]}\n')

            pending = open('addresses.json', 'r')
            public_ads = json.load(pending)
            pending.close()

            for a in public_ads:
                if a[0] == data[2]:
                    file = open('axemo_bal.json', 'r')
                    old_bal = json.load(file)
                    file.close()

                    new_bal = float(old_bal) + float(data[2])

                    file = open('axemo_bal.json', 'w')
                    json.dump(new_bal, file)
                    file.close()

            final_receive_data_save(data)

    def final_receive_data_save(f_list):
        print('saving incoming transaction data...')
        file_1 = open('final_receive_data_save.json', 'r')
        saved_list = json.load(file_1)
        file_1.close()
        file = open('axemo_bal.json', 'r')
        bal = json.load(file)
        file.close()
        if f_list not in saved_list:
            saved_list.insert(0, f_list)
            file = open('final_receive_data_save.json', 'w')
            json.dump(saved_list, file)
            file.close()
            new_bal = bal + float(f_list[2])
            bal = new_bal
        print('updating balance')
        file = open('axemo_bal.json', 'w')
        json.dump(saved_list, bal)
        file.close()

    def run():
        notification_url = "https://ponzi.herokuapp.com/api/notifications_list"
        x = 0
        while True:
            try:
                a = time.time()
                new_lst = get_notification_list(notification_url)
                save_notification_id(new_lst)

                y = time.time()
                print('finishing round....')
                x += 1
                print(f'round {x} completed')
                print(f'time taken to update transaction list: {y - a}seconds\n\n')

            except Exception as e:
                print(e)
                print('restarting transaction list manager...\n')
                time.sleep(20)
                run()
            time.sleep(20)

    run()


def check_btc_price():
    while True:
        print('checking exchange rates...\n')
        global naira
        price = client.get_buy_price(currency_pair='BTC-NGN')
        ng = float(bt_bal) * float(price['amount'])
        naira = ng
        time.sleep(10)


def thr():
    thread1 = Thread(target=tx_list_thread)
    thread4 = Thread(target=check_btc_price)
    thread1.start()
    thread4.start()


home()
thr()
root.mainloop()
