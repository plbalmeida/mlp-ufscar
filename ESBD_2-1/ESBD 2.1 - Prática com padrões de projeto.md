# ESBD 2.1 - Prática com padrões de projeto

- Suponha um sistema de geração de rotas seguras. O App deve gerar uma rota que se classifica em “altamente segura”, “segura” e “aceitável”. Como a rota deve/pode ser alterada à medida que o pedestre caminha, o sistema deve ser capaz de trocar o nível de segurança da rota em tempo de execução. Assim, ora a rota se caracteriza como “altamente segura”, ora como “segura” e ora como “aceitável”.
- Elabore um projeto que reflita essa dinamicidade do sistema
- ## Observações
    - Como a memória do dispositivo é limitada, deve-se cuidar para que não haja sobrecarga de objetos desnecessários em memória
- ## Forma de resolução
    - Diagrama de classe UML
    - Trechos de código (pseudo-código) das partes importantes

A seguir será aplicado o sistema em Python utilizando os padrões de projeto Singleton e Strategy. O Singleton garantirá que apenas uma instância do gerador de rotas seja criada, enquanto o Strategy permitirá a troca de níveis de segurança da rota em tempo de execução.

``` python
from abc import ABC, abstractmethod

class SecurityLevel(ABC):

    @abstractmethod
    def generate_route(self):
        pass
```

O bloco de código acima define uma classe abstrata chamada `SecurityLevel`. Essa classe utiliza o módulo abc (Abstract Base Classes) em Python para definir uma interface que outras classes concretas devem implementar.

A classe SecurityLevel herda de ABC, que é uma metaclass fornecida pelo módulo abc. Isso torna a classe abstrata e impede que seja instanciada diretamente.

A classe `SecurityLevel` possui um método abstrato chamado `generate_route`. O decorador @abstractmethod indica que esse método deve ser implementado por todas as classes que herdam de SecurityLevel. Caso contrário, essas classes também serão consideradas abstratas e não poderão ser instanciadas. Essa é uma maneira de impor a implementação do método em todas as subclasses concretas, garantindo que elas sigam a mesma interface.

```python
class HighlySecure(SecurityLevel):

    def generate_route(self):
        return "Rota altamente segura"


class Secure(SecurityLevel):

    def generate_route(self):
        return "Rota segura"


class Acceptable(SecurityLevel):

    def generate_route(self):
        return "Rota aceitável"
```

O bloco de código acima define três classes concretas - `HighlySecure`, `Secure` e `Acceptable` - que herdam da classe abstrata `SecurityLevel`. Essas classes representam diferentes níveis de segurança na geração de rotas seguras e implementam o padrão Strategy.

Cada uma dessas classes concretas implementa o método `generate_route`, que é um método abstrato definido na classe base `SecurityLevel`. O método `generate_route` retorna uma string indicando qual tipo de rota foi gerada, dependendo do nível de segurança.

Essas classes são usadas em conjunto com a classe do bloco de código a seguir, a `RouteGenerator` para definir a estratégia de geração de rotas em tempo real. Através do método `set_security_level` da classe `RouteGenerator`, você pode alterar a estratégia de geração de rotas e obter diferentes níveis de segurança.

```python
class RouteGenerator:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self._security_level = None

    def set_security_level(self, security_level):
        self._security_level = security_level

    def generate_route(self):
        return self._security_level.generate_route()
```

A classe `RouteGenerator` implementa o padrão Singleton, garantindo que apenas uma instância da classe seja criada durante a execução do programa. Essa classe possui o atributo `_security_level`, que armazena a estratégia atual para a geração de rotas seguras. A estratégia é definida pelo padrão Strategy, conforme apresentado anteriormente.

Segue uma análise detalhada das partes do código dessa classe:

1. `_instance = None`: Essa linha define um atributo de classe `_instance`, que armazena a única instância do RouteGenerator.

2. `__new__(cls)`: Este método especial é chamado quando uma nova instância da classe é criada. Ele recebe a classe como argumento `(cls)`. Neste método, verificamos se a instância da classe já existe `(cls._instance)`. Se não existir, criamos a instância usando `super().__new__(cls)`. Caso contrário, retornamos a instância existente. Isso garante que apenas uma instância da classe seja criada.

3. `__init__(self)`: Este é o construtor da classe. Ele inicializa o atributo `_security_level` como **None**. Esse atributo armazenará a estratégia de geração de rotas.

4. `set_security_level(self, security_level)`: Este método permite definir a estratégia de geração de rotas (nível de segurança). Ele aceita um objeto de uma classe que implementa a interface `SecurityLevel` e define o atributo `_security_level` como esse objeto.

5. `generate_route(self)`: Este método utiliza a estratégia atual armazenada em `_security_level` para gerar uma rota. Ele chama o método `generate_route` do objeto `_security_level` e retorna o resultado.

Com essa classe é criada uma única instância de `RouteGenerator`, assim como é definida diferentes estratégias de geração de rotas em tempo de execução usando o método `set_security_level` gerarando rotas com o método `generate_route`. Isso é útil para lidar com diferentes níveis de segurança e trocar a estratégia em tempo real conforme necessário.

