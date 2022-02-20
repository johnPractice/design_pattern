from abc import ABC ,abstractmethod

# Abstract Products class 
class AbstractProductA(ABC):
    @abstractmethod
    def usfule_methode_a(self)->str:
        pass
class AbstractProductB(ABC):
    @abstractmethod
    def usfule_methode_b(self)->str:
        pass

# Abstract Factory Class
class AbstractFactory(ABC):
    # create product A
    @abstractmethod
    def create_product_a(self)->AbstractProductA:
        pass
    # create product B
    @abstractmethod
    def create_product_b(self)->AbstractProductB:
        pass


# product Implementation
class ConcreateProductA1(AbstractProductA):
    def usfule_methode_a(self) -> str:
        return 'this is product A1'
class ConcreateProductA2(AbstractProductA):
    def usfule_methode_a(self) -> str:
        return 'this is product A2'

class ConcreateProductB1(AbstractProductB):
    def usfule_methode_b(self) -> str:
        return 'this is product B1'
class ConcreateProductB2(AbstractProductB):
    def usfule_methode_b(self) -> str:
        return 'this is product B2'


# Concreate Factory
class ConcreateFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreateProductA1()
    def create_product_b(self) -> AbstractProductB:
        return ConcreateProductB1()

class ConcreateFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreateProductA2()
    def create_product_b(self) -> AbstractProductB:
        return ConcreateProductB2()
    
def client_code(factory:AbstractFactory)->None:
    prodcut_a=factory.create_product_a()
    print(prodcut_a.usfule_methode_a())


def main():
    client_code(ConcreateFactory1())
    client_code(ConcreateFactory2())

if __name__=="__main__":
    main()