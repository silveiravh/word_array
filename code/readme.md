**Linguagem de Programação Utilizada**
- Python 3.9.0 (necessário instalar biblioteca Flask-RESTful através do comando 'pip install Flask-RESTful')

Esta API REST permite ao usuário enviar textos de entrada e gera como resultado o vucabulário formado pelas palavras do texto e o vetor de palavras para cada arquivo considerando os cenários:
1. o vocabulário é composto de palavras isoladas;
2. o vocabulário é composto de grupos de duas palavras em sequência (2-gram);
3. o vocabulário é composto de grupos de três palavras em sequência (3-gram);
e assim por diante (podendo trabalhar com sequências n-gram sendo n um número natural inteiro diferente de zero).

**Envio de textos**
- Para testar a API nessa versão inicial o envio de textos deve ser feito no formato JSON:
```json
{
    "id": 1,
    "content": "Falar é fácil. Mostre-me o código."
}
```
sendo 'id' o identificador único do texto e 'content' seu conteúdo. O texto será enviado utilizando o seguinte método:
POST host:port/text
com o body da requisição sendo como descrito acima.

