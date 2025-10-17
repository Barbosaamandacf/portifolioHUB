# Jogo de Adivinhação em Python

Este é um joguinho simples feito em Python, onde o computador escolhe um número secreto entre **1 e 10** e você precisa acertar.  
Foi feito em duas versões para mostrar como a mesma ideia pode ser usada tanto no terminal quanto em uma interface gráfica.

---

## Como funciona

- O programa sorteia um número secreto de **1 a 10**  
- Você tenta adivinhar digitando o palpite  
- O jogo dá dicas:  
  - Se o número é **maior**  
  - Se o número é **menor**  
- Quando você acerta, aparece uma mensagem de parabéns 🎉

---

## O que você precisa

- Ter o **Python 3** instalado  
- O Tkinter já vem junto com o Python, então não precisa instalar nada extra para rodar a versão gráfica

---

## Como jogar

### Versão no terminal
Abra o terminal na pasta do projeto e rode:
```bash
python jogo_adivinhacao.py
```

Exemplo:
```
JOGO DE ADIVINHAÇÃO
Estou pensando em um número de 1 a 10...
Qual é o seu palpite? 4
O número secreto é MAIOR.
Qual é o seu palpite? 7
🎉 Parabéns! Você acertou!
```

### Versão com interface gráfica
Abra o terminal e rode:
```bash
python jogo_adivinhacao_front.py
```
Vai abrir uma janelinha com um campo de texto para digitar o palpite e um botão para verificar.

---

## Estrutura do projeto

```
├── jogo_adivinhacao.py        # versão no terminal
├── jogo_adivinhacao_front.py  # versão com interface gráfica (Tkinter)
```

---

## Ideias para melhorar

- Permitir escolher o intervalo (ex: 1 a 100)  
- Contar e mostrar o número de tentativas  
- Exibir um histórico dos palpites  
- Criar um ranking de jogadores  

---

## Sobre o projeto

Foi feito como exercício de programação em Python, servindo tanto para treinar lógica de repetição e condição quanto para experimentar com interface gráfica usando Tkinter.
