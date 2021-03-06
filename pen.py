COMP = {}


class Client_one:
    def __init__(self, name):
        self.name = name
        self.invest = {}

    def sell(self, value, company):
        if self.invest.get(company) is not None:
            if self.invest[company] > value:
                self.invest[company] -= value
            else:
                self.invest[company] = 0
        if COMP.get(company) is None:
            COMP[company] = 1

    def get_balance(self):
        balance = 0
        for active in self.invest.items():
            balance += COMP.get(active[0]) * active[1]
        print(round(balance))

    def buy(self, value, company):
        if self.invest.get(company) is None:
            self.invest[company] = value
        else:
            self.invest[company] += value
        if COMP.get(company) is None:
            COMP[company] = 1


class Clients_all:
    def __init__(self):
        self.clients = []
        self.names = []

    def get_by_name(self, name):
        for client in self.clients:
            if client.name == name:
                return client

    def add(self, client: Client_one):
        self.clients.append(client)
        self.names.append(client.name)


def raise_inv(value, company):
    value = 1 + value / 100
    COMP[company] *= value


def fall(value, company):
    value = 1 - value / 100
    COMP[company] *= value


def inp():
    global clients
    n = int(input())
    clients = Clients_all()
    return n


n = inp()


def operation_run(operation):
    operation_name = operation[0]
    if operation_name == "BUY":
        client_name = operation[1]
        company = operation[2]
        value = float(operation[3])
        if client_name in clients.names:
            client = clients.get_by_name(client_name)
        else:
            client = Client_one(client_name)
            clients.add(client)
        client.buy(value, company)
    elif operation_name == "SELL":
        client_name = operation[1]
        company = operation[2]
        value = float(operation[3])
        if client_name in clients.names:
            client = clients.get_by_name(client_name)
        else:
            client = Client_one(client_name)
            clients.add(client)
        client.sell(value, company)
    elif operation_name == "PRICE_RAISE":
        value = float(operation[2])
        company = operation[1]
        if COMP.get(company) is not None:
            raise_inv(value, company)
    elif operation_name == "PRICE_FALL":
        value = float(operation[2])
        company = operation[1]
        if COMP.get(company) is not None:
            fall(value, company)
    elif operation_name == "BALANCE":
        client_name = operation[1]
        if client_name in clients.names:
            client = clients.get_by_name(client_name)
            client.get_balance()
        else:
            print(0)


for i in range(n):
    operation = str(input()).split(" ")
    operation_run(operation)
