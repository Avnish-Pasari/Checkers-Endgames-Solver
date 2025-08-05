# Checkers Endgame Solver ♟️

A Python AI program that solves **Checkers endgame puzzles** using **Alpha-Beta Pruning** with a depth-limited search and a custom evaluation function.   

---

## 📖 About the Project

This solver plays both sides of a Checkers endgame, making optimal moves for **Red** and **Black** using **alpha-beta pruning**.  
The goal is to always find a winning sequence of moves (if possible) or play optimally given the board state.

The implementation also uses optimizations such as:
- **Node Ordering** (explore promising moves first for deeper pruning)  
- **State Caching** (avoid recomputing repeated board states)  
- **Custom Evaluation Function** (for non-terminal states)  

---

## 🕹️ Game Rules Implemented

- Board size: **8×8 grid**  
- Pieces:
  - `r`: red piece  
  - `R`: red king  
  - `b`: black piece  
  - `B`: black king  
  - `.`: empty square  
- **Red always moves first**.  
- **Moves**:
  - Normal pieces move diagonally forward (Red = up, Black = down)  
  - Kings move diagonally in both directions  
  - Jumps are mandatory  
  - Multi-jumps are required when available  
- **Promotion**: A piece becomes a king when it reaches the opponent’s back row  
- **Game End**: One player wins when the opponent has no legal moves or no pieces  

---

## ⚙️ Features

- Implements **Alpha-Beta Pruning** for efficient minimax search  
- Configurable **depth limit** for pruning  
- Utility-based **evaluation function** for non-terminal states  
- Supports **multi-jumps** and **mandatory captures**  
- Handles **king promotions** correctly  
- Outputs the full sequence of board states from the initial configuration to the game’s end  

---

## 🛠️ Tech Stack

- **Language**: Python 3  
- **Core Algorithms**: Minimax Search, Alpha-Beta Pruning  
- **Optimizations**: Node Ordering, State Caching  
- **Environment**: Linux
