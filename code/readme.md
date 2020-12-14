**Linguagem de Programação Utilizada**
- Python 3.9.0 (necessário instalar biblioteca Flask-RESTful através do comando 'pip install Flask-RESTful')


Esta API REST permite ao usuário enviar textos de entrada e gera como resultado o vucabulário formado pelas palavras dos textos (ignorando repetições, case, pontuação e palavras que não agragam valor ao vacabulário do texto chamadas *stopwords*) e um vetor de repetição que conta quantas vezes cada termo daquele vocabulário aparece no texto. Considera os seguintes cenários:\

**1. o vocabulário é composto de palavras isoladas;**\
Exemplo:\
texto1: “Falar é fácil. Mostre-me o código.”\
texto2: “É fácil escrever código. Difícil é escrever código que funcione.”\
Vocabulário:
1. falar
2. é
3. fácil
4. mostre
5. me
6. o
7. código
8. escrever
9. difícil
10. que
11. funcione

Vetor de repetição:\
texto1: [1,1,1,1,1,1,1,0,0,0,0]\
texto2: [0,2,1,0,0,0,2,2,1,1,1]

**2. o vocabulário é composto de grupos de duas palavras em sequência (2-gram);**
Exemplo:\
Considerando os mesmos textos 1 e 2, o vocabulário seria:
1. falar é
2. é fácil
3. fácil mostre
4. mostre me
5. me o
6. o código
7. fácil escrever
8. escrever código
9. código difícil
10. difícil é
11. é escrever
12. código que
13. que funcione

Vetor de repetição:\
texto1: [1,1,1,1,1,1,0,0,0,0,0,0,0]\
texto2: [0,1,0,0,0,0,1,2,1,1,1,1,1]

e assim por diante (podendo trabalhar com sequências n-gram sendo n um número natural inteiro diferente de zero).

**Envio de textos**
- Para testar a API nessa versão inicial o envio de textos deve ser feito no formato JSON:
```json
{
    "id": 1,
    "content": "Falar é fácil. Mostre-me o código."
}
```
sendo 'id' o identificador único do texto e 'content' seu conteúdo. O texto será enviado utilizando o seguinte método:\
POST host:port/text\
com o body da requisição sendo como descrito acima.


**Vocabulário n-gram**
- O usuário poderar solicitar o vocabulário n-gram através do seguinte método:\
GET host:port/vocabulary/<int:gram>\
sendo gram um inteiro que define como as palavras serão agregadas no 
