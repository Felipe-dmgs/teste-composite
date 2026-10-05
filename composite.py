from abc import ABC, abstractmethod


class Interface(ABC):

    @abstractmethod
    def get_price(self) -> float:
        pass

    def add(self, component: "Interface") -> None:
        raise NotImplementedError(
            "Operação add() não é suportada neste elemento."
        )

    def remove(self, component: "Interface") -> None:
        raise NotImplementedError(
            "Operação remove() não é suportada neste elemento."
        )


class Composite(Interface):

    def __init__(self):
        self.children: list[Interface] = []

    def add(self, component: Interface) -> None:
        self.children.append(component)

    def remove(self, component: Interface) -> None:
        if component in self.children:
            self.children.remove(component)

    def get_price(self) -> float:
        return sum(child.get_price() for child in self.children)


class Leaf(Interface):

    def __init__(self, price: float = 5):
        self.price = price

    def get_price(self) -> float:
        return self.price


# --- Teste de Execução ---
folha1 = Leaf(5)
folha2 = Leaf(5)
folha3 = Leaf(5)
folha4 = Leaf(5)
folha5 = Leaf(5)

caixa = Composite()
caixa.add(folha1)
caixa.add(folha2)
print("Preço caixa 1:", caixa.get_price())  # Output: 10

caixa2 = Composite()
caixa2.add(folha3)
caixa2.add(folha4)
caixa2.add(folha5)
print("Preço caixa 2:", caixa2.get_price())  # Output: 15

caixa.add(caixa2)  # Aninhando um Composite em outro

print("Preço caixa 1:", caixa.get_price())

caixa.remove(folha1)

print("Preço total após remoção e aninhamento:", caixa.get_price())  # Output: 20