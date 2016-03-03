# Stock Market Game

## Abstract

In the Stock Market Game, users will be able to invest virtual money into the NASDAQ stock market. Users will also be able to make transactions, select, and display the price data.

## Background

I have seen stock investing games and know what features are necessary that can be helpful. The Programming language I am familiar with is Python, and I am experienced with Python GUI And APIs. However, it was a pretty small project and it did not require many APIs. 

## Significance

In economics classes, teachers and professors often assign a stock investing project. From what I saw, the software they are using for the project is missing features such as price data graph and stock finding functions. The proposed game will give people a chance to spend time and find promising stocks and engage with the project. This project will also give me an opportunity to learn more about Object-Oriented programing and how to find and use APIs, libraries, and documentations more efficiently. Through this project, I aspire to become a better programmer.

## Deliverables

### Skeleton:
**I will create prototype to demonstrate manually pulling data using the stock market API that I have selected**
- Data includes:
- The current price, and a corresponding time
- The change of the price from the beginning to the end

**The GUI will demonstrate**
- Generating a graph populated with hard coded data
- Widgets such as, buttons, text input, and labels

### Basic:
**I will build a text based command line game. In this game the player can:**
- Start the game with $5000
- Buy and sell stock
- Check the list of stocks that they own
- Check the amount of money that respective user owns
- Check the name and symbol of existing stocks in the NASDAQ
- Save the game

### Solid:
**Solid features will include:**
- A GUI that replaces the command line interface
- The player can select a stock at any time and check the change of its respective price graph.
- Stock price graph generation

### Awesome:
**Awesome features include:**
- Difficulty setting feature
- In easy mode:
- game will be the same as the game in solid.
- In hard mode: 
- user will start the game with $2500
- user will pay fees (10% of the price) and taxes (10% of the price) for every transition	

## Tools

There are a number of APIs and libraries which could be helpful in building the game. I found the library called GTK which has built in widgets such as buttons, menus, and labels. For stock market API, I am going to use Yahoo-Finance which lets me pull stock data such as current price, and the historical data of the chosen stock. Also, I am going to use matplotlib to display the price movement graph of the stock. 

## Problems

I still have a hard time with separating functions into different classes. To resolve this problem, I am going to review the UML diagram for my code and check if classes and functions are keeping the single responsibility priciple. Another problem is that I am not completely familar with the API I am going to use for this project. In order to solve this problem, I am going to read more documentation to figure out what kind of features are in the chosen API and do lots of testing to find out how they behave.

## References

**Yahoo-Finance:**

[1] Pypi.python.org, "yahoo-finance 1.2.1 : Python Package Index", 2016. [Online]. Available: https://pypi.python.org/pypi/yahoo-finance/1.2.1. [Accessed: 27- Jan- 2016]

**Matplotlib:**
[2] Matplotlib.org, "Pyplot tutorial — Matplotlib 1.5.1 documentation", 2016. [Online]. Available: http://matplotlib.org/users/pyplot_tutorial.html. [Accessed: 17- Feb- 2016].

**Gosu:**
[3] Gosu-lang.github.io, "The Gosu Programming Language", 2016. [Online]. Available: https://gosu-lang.github.io/. [Accessed: 17- Feb- 2016].

**GTK:**
[4] Python-gtk-3-tutorial.readthedocs.org, "The Python GTK+ 3 Tutorial — Python GTK+ 3 Tutorial 3.4 documentation", 2016. [Online]. Available: https://python-gtk-3-tutorial.readthedocs.org/en/latest/. [Accessed: 17- Feb- 2016].

**Python Argparse:**
[5] Docs.python.org, "16.4. argparse — Parser for command-line options, arguments and sub-commands — Python 3.5.1 documentation", 2016. [Online]. Available: https://docs.python.org/3/library/argparse.html. [Accessed: 17- Feb- 2016].
