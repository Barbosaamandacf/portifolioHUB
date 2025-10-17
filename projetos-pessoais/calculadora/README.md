#  Calculadora em Python

Este projeto é uma calculadora simples feita em Python, com duas formas de uso:  
- Uma versão em linha de comando (`calculadora.py`)  
- Uma versão com interface gráfica (`calculadora_front.py`), feita com Tkinter.

A ideia foi criar algo direto e fácil de usar, servindo tanto para treinar conceitos básicos de Python quanto para ter um projetinho funcional no dia a dia.

---

##  O que dá pra fazer

- Somar  
- Subtrair  
- Multiplicar  
- Dividir (com proteção contra divisão por zero)  

Na versão de terminal, você escolhe a opção pelo menu.  
Na versão gráfica, é só preencher os dois campos e clicar no botão da operação.

---

##  Requisitos

- Ter o **Python 3** instalado  
- O Tkinter já vem junto com o Python (Windows, Linux e macOS), então não precisa instalar nada extra.

---

##  Como rodar

### Linha de comando
```bash
python calculadora.py
```

### Interface gráfica
```bash
python calculadora_front.py
```

---

## 📸 Exemplos

### No terminal:
```
CALCULADORA
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
5 - Sair
Escolha uma opção: 1
Digite o primeiro número: 10
Digite o segundo número: 5
Resultado: 15.0
```

### Na interface gráfica:
Uma janelinha aparece, você coloca os dois números, clica na operação e o resultado aparece logo embaixo.

---

##  Estrutura do projeto

```
├── calculadora.py         # versão em terminal
├── calculadora_front.py   # versão em interface gráfica (Tkinter)
```

---


##  Autor

Feito como exercício e também como forma de mostrar o básico de Python rodando de formas diferentes (terminal e GUI).  
