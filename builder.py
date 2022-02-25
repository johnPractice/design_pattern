from abc import ABC , abstractmethod
from typing import Any


class Product1():
    def __init__(self) -> None:
        self.parts=[]
    def add(self,part:Any)->None:
        self.parts.append(part)
    def list_parts(self)->None:
        print(f"Product parts: {', '.join(self.parts)}", end="")

class Builder(ABC):
    @property
    @abstractmethod
    def product(self)->None:
        pass

    @property
    @abstractmethod
    def product_part_a(self)->None:
        pass
    
    @property
    @abstractmethod
    def product_part_b(self)->None:
        pass

    @property
    @abstractmethod
    def product_part_c(self)->None:
        pass

class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        self.reset()
    def reset(self):
        self._product=Product1()

    @property
    def product(self) -> Product1:
        product=self._product
        self.reset()
        return product
    def product_part_a(self) -> None:
        self._product.add("PartA1")

    def product_part_b(self) -> None:
        self._product.add("PartB1")

    def product_part_c(self) -> None:
        self._product.add("PartC1")

class Director:
    def __init__(self) -> None:
        self._builder=None
    @property
    def builder(self)->Builder:
        return self._builder
    
    @builder.setter
    def builder(self,builder:Builder)->None:
        self._builder:Builder=builder

    def build_minimal_viable_product(self) -> None:
        self.builder.product_part_a()

    def build_full_featured_product(self) -> None:
        self._builder.product_part_a()
        self._builder.product_part_b()
        self._builder.product_part_c()


if __name__ == "__main__":
    """
    The client code creates a builder object, passes it to the director and then
    initiates the construction process. The end result is retrieved from the
    builder object.
    """

    director = Director()
    builder = ConcreteBuilder1()
    director.builder = builder

    print("Standard basic product: ")
    director.build_minimal_viable_product()
    builder.product.list_parts()

    print("\n")

    print("Standard full featured product: ")
    director.build_full_featured_product()
    builder.product.list_parts()

    print("\n")

    # Remember, the Builder pattern can be used without a Director class.
    print("Custom product: ")
    builder.product_part_a()
    builder.product_part_b()
    builder.product.list_parts()