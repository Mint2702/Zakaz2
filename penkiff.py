companies = {}


class Client:
    def __init__(self, name: str):
        self.actives = {}
        self.name = name

    def buy(self, value: float, company: str) -> None:
        if self.actives.get(company) is None:
            self.actives[company] = value
        else:
            self.actives[company] += value
        if companies.get(company) is None:
            companies[company] = 1

    def sell(self, value: float, company: str) -> None:
        if self.actives.get(company) is not None:
            if self.actives[company] > value:
                self.actives[company] -= value
            else:
                self.actives[company] = 0
        if companies.get(company) is None:
            companies[company] = 1

    def get_balance(self):
        balance = 0
        for active in self.actives.items():
            balance += companies.get(active[0]) * active[1]
        print(round(balance))


class Clients:
    def __init__(self) -> None:
        self.names = []
        self.clients = []

    def add(self, client: Client) -> None:
        self.clients.append(client)
        self.names.append(client.name)

    def get_by_name(self, name: str):
        for client in self.clients:
            if client.name == name:
                return client


def inc(value: float, company: str) -> None:
    value = 1 + value / 100
    companies[company] *= value


def dec(value: float, company: str) -> None:
    value = 1 - value / 100
    companies[company] *= value


n = int(input())
clients = Clients()

for i in range(n):
    operation = str(input()).split(" ")
    operation_name = operation[0]
    if operation_name == "BUY":
        client_name = operation[1]
        company = operation[2]
        value = float(operation[3])
        if client_name in clients.names:
            client = clients.get_by_name(client_name)
        else:
            client = Client(client_name)
            clients.add(client)
        client.buy(value, company)
    elif operation_name == "SELL":
        client_name = operation[1]
        company = operation[2]
        value = float(operation[3])
        if client_name in clients.names:
            client = clients.get_by_name(client_name)
        else:
            client = Client(client_name)
            clients.add(client)
        client.sell(value, company)
    elif operation_name == "PRICE_RAISE":
        value = float(operation[2])
        company = operation[1]
        if companies.get(company) is not None:
            inc(value, company)
    elif operation_name == "PRICE_FALL":
        value = float(operation[2])
        company = operation[1]
        if companies.get(company) is not None:
            dec(value, company)
    elif operation_name == "BALANCE":
        client_name = operation[1]
        if client_name in clients.names:
            client = clients.get_by_name(client_name)
            client.get_balance()
        else:
            print(0)
