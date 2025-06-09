from abc import ABC, abstractmethod
import random
import string

class Senha(ABC):
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.valor = ""

    @abstractmethod
    def gerar(self):
        pass

    @abstractmethod
    def validar(self):
        pass

class SenhaSimples(Senha):
    def gerar(self):
        caracteres = string.ascii_letters
        self.valor = ''.join(random.choices(caracteres, k=self.tamanho))
        return self.valor

    def validar(self):
        return self.valor.isalpha() and len(self.valor) == self.tamanho

class SenhaComplexa(Senha):
    def gerar(self):
        caracteres = string.ascii_letters + string.digits + string.punctuation
        while True:
            tentativa = ''.join(random.choices(caracteres, k=self.tamanho))
            self.valor = tentativa
            if self.validar():
                break
        return self.valor

    def validar(self):
        tem_letra = any(c.isalpha() for c in self.valor)
        tem_numero = any(c.isdigit() for c in self.valor)
        tem_simbolo = any(c in string.punctuation for c in self.valor)
        return tem_letra and tem_numero and tem_simbolo and len(self.valor) == self.tamanho

class SenhaEmailPessoal(Senha):
    def gerar(self):
        letras = random.choices(string.ascii_letters, k=self.tamanho - 2)
        simbolo = random.choice("!@#$.")
        numero = random.choice(string.digits)
        todos = letras + [simbolo, numero]
        random.shuffle(todos)
        self.valor = ''.join(todos)
        return self.valor

    def validar(self):
        tem_letra = any(c.isalpha() for c in self.valor)
        tem_numero = sum(c.isdigit() for c in self.valor) >= 1
        tem_simbolo = sum(1 for c in self.valor if c in "!@#$.") == 1
        return tem_letra and tem_numero and tem_simbolo and len(self.valor) == self.tamanho

class SenhaTemporal(Senha):
    def gerar(self):
        base = string.ascii_letters + string.digits
        simbolos = ".!#?"
        corpo = ''.join(random.choices(base, k=self.tamanho - 2))
        simbolo = random.choice(simbolos)
        digito = random.choice(string.digits)
        self.valor = corpo + simbolo + digito + "_tmp"
        return self.valor

    def validar(self):
        simbolos = ".!#?"
        return (
            len(self.valor) == self.tamanho + 4 and
            self.valor[-4:] == "_tmp" and
            self.valor[-5] in string.digits and
            self.valor[-6] in simbolos
        )
