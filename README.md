# 🏓 Pong Game in Python (Turtle)

A classic **Pong** arcade game remake using Python's built-in `turtle` module. Two players can control paddles to keep the ball in play. First to reach the winning score wins the game!

## 📜 Description

This game is a digital version of the original Pong arcade game. Two players control paddles on either side of the screen and try to bounce the ball back and forth. Missing the ball gives the opponent a point. The first player to reach the winning score is declared the winner.

## 🎮 Controls

| Player | Move Up | Move Down |
| ------ | ------- | --------- |
| Left   | `W`     | `S`       |
| Right  | `↑`     | `↓`       |


## 📁 File Structure

pong_game/
│
├── main.py             # Main game loop and logic
├── paddle_bar.py       # Paddle class definition
├── circle.py           # Ball class with movement and collision behavior
├── scoreboard.py       # Scoreboard class to track and display scores
└── README.md           # Project documentation
```

## 🧠 Features

* Two-player paddle control
* Ball bounces off walls and paddles
* Points awarded for missed ball
* Scoreboard updates in real-time
* Declares a winner when a player reaches the target score

## ⚙️ Requirements

* Python 3.x
* No external libraries; uses built-in `turtle` and `time`

## ▶️ How to Run

Ensure all files are in the same directory. Run the game using:

```bash
python main.py
```

## 🏆 Winning Condition

The first player to reach the score defined by `score.winner_score` (default usually 5 or 10) is declared the winner. The game then displays the winner message and stops.

## 📌 Notes

* The paddle and ball collision detection uses distance and x-position checks.
* The ball resets to the center after every miss.
* Timing and speed can be adjusted via `time.sleep()` for smoother gameplay.
