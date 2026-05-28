# 🔢 Guess The Number Game

A fun Python terminal game where you try to crack a randomly generated number within a set range. With hints to guide each guess, it's a simple but satisfying exercise in logic and deduction.

![Python](https://img.shields.io/badge/Python-100%25-blue)

## 🎮 About the Game

The computer picks a secret number within a defined range, and it's your job to guess it. After each attempt, you get feedback — too high, too low, or spot on. Use the clues to narrow down your guesses and find the number in as few tries as possible!

Great for beginners learning Python and for anyone who enjoys a quick mental challenge.

## ✨ Features

- Random number generation for a fresh game every time
- Clear feedback after each guess (too high / too low / correct)
- Configurable number range
- Tracks the number of attempts taken
- Minimal dependencies — runs with standard Python

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your system

Check your Python version:
```bash
python --version
```

### Installation

```bash
git clone https://github.com/iamparrish/Guess-The-Number-Game.git
cd Guess-The-Number-Game
```

### Run the Game

```bash
python "Guess The Number.py"
```

## 🕹️ How to Play

1. The game generates a random number within a specified range (e.g., 1–100).
2. Enter your guess when prompted.
3. The game tells you if your guess is **too high**, **too low**, or **correct**.
4. Keep guessing until you find the number!
5. Your total number of attempts is shown when you win.

**Example:**

```
Guess a number between 1 and 100: 50
Too high! Try again.

Guess a number between 1 and 100: 25
Too low! Try again.

Guess a number between 1 and 100: 37
🎉 Correct! You got it in 3 attempts!
```

## 🗂️ Project Structure

```
Guess-The-Number-Game/
├── Guess The Number.py    # Main game script
└── README.md
```

## 🛠️ Built With

- **Python 3** — Game logic, random number generation, and user input handling

## 🤝 Contributing

Suggestions and improvements are always welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## 👤 Author

**iamparrish**
- GitHub: [@iamparrish](https://github.com/iamparrish)
