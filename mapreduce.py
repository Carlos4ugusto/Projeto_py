from mrjob.job import MRJob #Importa a biblioteca mrjob que permite criar jobs MapReduce em Python para processamento distribuído de dados.
import re #Importa a biblioteca re que fornece suporte para expressões regulares em Python, útil para manipulação e busca de padrões em strings.

palavra_regex = re.compile(r"[\w']+") #Compila uma expressão regular que corresponde a palavras, incluindo letras, números e apóstrofos.


class QuantidadePalavras(MRJob):
    def mapper(self, _, linha): 
        for p in palavra_regex.findall(linha): #Encontra todas as palavras na linha usando a expressão regular compilada.
            yield (p.lower(), 1) #Emite cada palavra em minúsculas junto com o valor 1, indicando uma ocorrência da palavra.

    def reducer(self, p, qtd): #Agrega os valores emitidos pelo mapper para cada palavra.
        yield (p, sum(qtd)) #Emite a palavra junto com a soma total de suas ocorrências.


if __name__ == '__main__':
    QuantidadePalavras.run()
 