### PPNJJ Team Activity: Random Quote Generator App(with OOP & API)

##### OBJECTIVES
- Display random quote locally(Console or GUI)
- Serve quite via **Flask API** and **ngrok** for other teams
- use **object oriented- programming** (class and object) to manage quotes
- Make the API consumable by other teams
- Utilize **Github** and **Git** for collaborations
- Make README.md on your Github with proper documentation on how your app works and how to use it

### Random Quote Generator App
##### Introduction
- This app displays random quotes with the use of **Flask API** and **ngrok** that other teams/users can use through a provided **URL**.

##### Process
- First we created a program using *random* *module*.
- After that, we created the Quote and QuoteManager class.
- The Quote class seperates the text and author for proper labeling and returns a readable **JSON** format.
- On the other hand, the QuoteManager compiles the quotes and returns a **random quote**.
- After doing this, the program can now run **locally** by using console/terminal.
- We then proceeded using **ngrok** and **FlaskAPI** to make the program into an **API** that can run through a link.
- By using the obtained link it will provide a random quote in a **JSON** format. This link can also used in a seperate program to get a random quote.
  
##### Installation and How to Use Instructions
- Install our Application and Run on Vscode.
- Open terminal and run the command **Api.py / API File** and **ngrok http 500** on seperate terminals.


