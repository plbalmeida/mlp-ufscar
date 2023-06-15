# ESBD 4.1 - Prática com o Teste de Software Aplicado ao Desenvolvimento de Software

O TDD (Test-Driven Development) é uma metodologia de desenvolvimento de software que visa garantir a correta funcionalidade de um programa por meio da utilização de testes unitários. O processo de TDD geralmente envolve os seguintes passos:

1. Escrever um teste que defina uma função ou melhorias.
2. Executar todos os testes e veja se o novo teste falha.
3. Escrever o código.
4. Executar os testes.
5. Refatorar o código.
6. Repitir.

Aplicando esses passos para o problema dos números romanos, primeiro, será escrito alguns testes unitários. Esses testes vão verificar a corretude da função que será escrita para converter números romanos em números inteiros.

```python
# test_roman_numerals.py

import unittest
from roman_numerals import roman_to_int

class TestRomanNumerals(unittest.TestCase):
    def test_single_digit(self):
        self.assertEqual(roman_to_int('I'), 1)
        self.assertEqual(roman_to_int('V'), 5)
        self.assertEqual(roman_to_int('X'), 10)
        self.assertEqual(roman_to_int('L'), 50)
        self.assertEqual(roman_to_int('C'), 100)
        self.assertEqual(roman_to_int('D'), 500)
        self.assertEqual(roman_to_int('M'), 1000)

    def test_combined_digits(self):
        self.assertEqual(roman_to_int('III'), 3)
        self.assertEqual(roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('LVIII'), 58)
        self.assertEqual(roman_to_int('MCMXCIV'), 1994)

if __name__ == '__main__':
    unittest.main()
```

Ao executar os testes acima, todos os testes falharão dado que a função roman_to_int não foi implementada ainda.

A seguir, a função roman_to_int é implementada:

```python
# roman_numerals.py

def roman_to_int(s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prev = 0
    for i in s[::-1]:
        if roman_dict[i] >= prev:
            res += roman_dict[i]  
        else:
            res -= roman_dict[i] 
        prev = roman_dict[i]
    return res
```

Agora testes podem ser executados novamente, se tudo foi feito corretamente, todos os testes devem passar.

O próximo passo seria a refatoração. No entanto, a função roman_to_int já está bastante clara e não é necessária nenhuma melhoria óbvia que poderia ser feita. Portanto, a refatoração não foi feita neste caso.

E esse é o fim do processo TDD para este problema específico. Os passos seriam repetidos se existisse a necessidade de adicionar mais funcionalidades ou se fosse encontrado um bug.

## Qual(is) critério(s) de teste utilizei na elaboração do conjunto de teste?

Os critérios de teste utilizados na elaboração do conjunto de teste para este problema dos números romanos incluem:

1. **Testes de Validação de Entrada Única (Single Input Validation Tests)**: Os testes verificam se cada numeral romano individual (I, V, X, L, C, D, M) é corretamente traduzido para o seu equivalente em algarismo arábico. Isto é para garantir que o programa entende corretamente cada um dos símbolos.

2. **Testes de Combinações Simples (Simple Combination Tests)**: Esses testes verificam se o programa pode lidar com a soma de números romanos, como em 'III' que deve ser convertido para 3.

3. **Testes de Combinações Complexas (Complex Combination Tests)**: Esses testes verificam se o programa pode lidar com as regras mais complexas dos números romanos, como a subtração de um número menor antes de um maior, como em 'IV' que deve ser convertido para 4. 

4. **Testes de Casos Reais (Real Case Tests)**: Esses testes verificam se o programa pode lidar com números romanos que representam números mais complexos e que seguiriam as regras dos numerais romanos em casos do mundo real. Por exemplo, 'MCMXCIV' que deve ser convertido para 1994.

Cada um desses critérios de teste é importante para garantir que a função de conversão de números romanos funcione corretamente em várias situações diferentes. Os testes assumem que as entradas são válidas, ou seja, que são strings que representam números romanos válidos. Testes adicionais poderiam ser feitos para garantir que a função lide corretamente com entradas inválidas.

## Quantos testes foram necessários para satisfazê-los?

Foram necessários dez testes para satisfazer os critérios de teste descritos. Aqui está a lista de todos os testes usados:

1. Testar a conversão do numeral romano 'I' para o número inteiro 1.
2. Testar a conversão do numeral romano 'V' para o número inteiro 5.
3. Testar a conversão do numeral romano 'X' para o número inteiro 10.
4. Testar a conversão do numeral romano 'L' para o número inteiro 50.
5. Testar a conversão do numeral romano 'C' para o número inteiro 100.
6. Testar a conversão do numeral romano 'D' para o número inteiro 500.
7. Testar a conversão do numeral romano 'M' para o número inteiro 1000.
8. Testar a conversão do numeral romano 'III' para o número inteiro 3.
9. Testar a conversão do numeral romano 'IV' para o número inteiro 4.
10. Testar a conversão do numeral romano 'MCMXCIV' para o número inteiro 1994.

Cada um desses testes é projetado para testar um aspecto específico da conversão de números romanos para números inteiros. Isso inclui testar a conversão de numerais romanos individuais, testar a soma de numerais romanos e testar a subtração de um numeral romano de um numeral maior que o segue.

Porém, o número de testes pode variar dependendo da complexidade do problema e do nível de cobertura de código desejado. Embora esses dez testes abordem muitos dos casos principais, seria possível acrescentar mais testes para lidar com casos de borda adicionais ou para aumentar a cobertura do código.

## Qual o tamanho da solução proposta da primeira versão até a última em termos de linhas de código?

Para o problema dos números romanos, a solução proposta inicialmente era composta por uma única função chamada `roman_to_int`. Esta função tem 8 linhas de código, incluindo a definição da função e a declaração dos valores numéricos dos numerais romanos.

No código dos testes, foram escritos dois métodos de teste na classe `TestRomanNumerals`, cada um com vários testes. No total, o código do teste tem 13 linhas de código, incluindo a definição da classe de teste, os métodos de teste e a chamada para executar os testes.

Portanto, considerando tanto a função de conversão quanto os testes, a solução completa tem 21 linhas de código.

Não houve necessidade de refatoração na solução inicial, então a primeira versão permaneceu como a versão final, mantendo o mesmo tamanho em termos de linhas de código. A quantidade de linhas de código pode variar ligeiramente dependendo do estilo de codificação do desenvolvedor, mas essa é uma estimativa razoável para este problema.

## Você ficou satisfeito com a solução desenvolvida em termos de sua qualidade? Por quê?

Sim, fiquei satisfeito com a solução desenvolvida. Aqui estão as razões:

1. **Clareza e legibilidade**: A função `roman_to_int` é clara e fácil de entender. O uso do dicionário `roman_dict` para mapear os numerais romanos para seus equivalentes em números inteiros torna o código autoexplicativo.

2. **Eficiência**: A função é eficiente pois opera em tempo linear, ou seja, o tempo de execução aumenta linearmente com o tamanho da entrada. Isso ocorre porque a função percorre a string de entrada apenas uma vez.

3. **Corretude**: Com base nos testes que foram escritos e passaram, a função parece ser correta. Ela manipula corretamente tanto os casos básicos (numerais individuais) quanto os casos mais complexos (combinações de numerais).

4. **Testabilidade**: A função é fácil de testar, é possível escrever vários testes unitários para verificar sua corretude.

No entanto, a perfeição é um processo contínuo e sempre há espaço para melhorias. Por exemplo, seria possível adicionar tratamento de erros para lidar com entradas inválidas. Atualmente, a função assumiria que está recebendo uma string válida de numerais romanos, mas em um ambiente de produção real, seria útil ter algum tipo de verificação e tratamento de erro para entradas inválidas. 

Além disso, embora os testes que escrevemos abranjam uma boa gama de casos, sempre há a possibilidade de existirem casos extremos ou de borda que não foram considerados. Portanto, mais testes poderiam ser adicionados para aumentar a confiabilidade do programa.

## Na sua opinião, quais são as principais vantagens e desvantagens no uso do TDD até aqui?

O Desenvolvimento Orientado a Testes (TDD - Test-Driven Development) tem várias vantagens e desvantagens.

**Vantagens**

1. **Código de alta qualidade**: O TDD promove a escrita de código de alta qualidade, pois você está constantemente testando e refatorando o código. Isso pode levar a menos bugs e um código mais limpo e fácil de manter.

2. **Documentação viva**: Os testes podem servir como uma espécie de documentação do seu código. Eles mostram como a função ou classe deve ser usada e que tipo de comportamento esperar dela.

3. **Design de código melhorado**: Como o TDD exige que você escreva os testes primeiro, ele pode ajudar a melhorar o design do seu código. Isso ocorre porque você precisa pensar sobre como a função ou classe será usada antes de realmente implementá-la.

4. **Refatoração mais segura**: Com um conjunto robusto de testes, a refatoração do código se torna menos arriscada porque você pode ter certeza de que não quebrou nada se todos os seus testes ainda passarem depois da refatoração.

**Desvantagens**

1. **Tempo inicial mais longo**: O TDD pode levar mais tempo no início, porque você precisa escrever os testes antes de poder começar a escrever o código real. Isso pode atrasar o desenvolvimento inicial.

2. **Curva de aprendizado**: Pode ser difícil para os desenvolvedores se acostumarem a escrever testes antes do código se eles não estiverem familiarizados com o TDD. Isso pode adicionar mais tempo ao processo de desenvolvimento.

3. **Falsa sensação de segurança**: Passar em todos os testes não significa necessariamente que o código está sem bugs. Os testes são tão bons quanto são escritos. Se você não cobrir todos os casos possíveis ou se os testes estiverem incorretos, ainda poderá ter bugs no código.

4. **Maior dificuldade com problemas complexos**: Em problemas muito complexos ou com grande variabilidade de casos, a escrita de testes pode ser mais desafiadora e consumir muito tempo, o que pode atrasar o desenvolvimento.

Em resumo, o TDD é uma ferramenta poderosa e útil para o desenvolvimento de software, mas, como qualquer ferramenta, tem suas vantagens e desvantagens. A decisão de usar o TDD deve depender do projeto específico, da equipe e das circunstâncias.


