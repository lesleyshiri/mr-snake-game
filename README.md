# Mr Snake Game 🐍

A classic Snake game built with Pygame featuring multiple speed levels, high score tracking, and both mouse and keyboard controls.

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

- **Multiple Speed Levels**: Choose from Very Slow, Slow, Medium, Fast, and Very Fast
- **High Score System**: Tracks your top 5 scores across sessions
- **Dual Control Options**: Play with keyboard arrows or mouse controls
- **Modern UI**: Glass-style buttons with hover effects
- **Custom Graphics**: Striped snake design with 3D-style apple
- **Wraparound Gameplay**: Snake wraps around screen edges
- **Persistent Storage**: High scores saved to local file

## Installation

### Prerequisites

- Python 3.7 or higher
- Pygame library

### Setup

1. Clone the repository:
```bash
git clone https://github.com/lesleyshiri/mr-snake-game.git
cd mr-snake-game
```

2. Install dependencies:
```bash
pip install pygame
```

3. Update the background image path in the code:
```python
IMAGE_PATH = r"path/to/your/background/image.png"
```

## How to Play

1. Run the game:
```bash
python snake_game.py
```

2. **Main Menu Options**:
   - **NEW GAME (1 or Enter)**: Start a new game
   - **HIGH SCORE (2)**: View top 5 high scores
   - **SPEED**: Click to cycle through speed presets
   - **END GAME (3 or ESC)**: Exit the game

3. **Game Controls**:
   - **Arrow Keys**: Control snake direction (Up, Down, Left, Right)
   - **Mouse**: Click and hold to steer snake toward cursor
   - **ESC or Menu Button**: Return to main menu

4. **Game Over Options**:
   - **R**: Replay game at current speed
   - **M or ESC**: Return to main menu

## Game Mechanics

- Snake grows by one segment each time it eats food
- Game ends when snake collides with itself
- Snake wraps around screen edges (no wall collision)
- Score increases by 1 for each food item eaten
- High scores are automatically saved

## Configuration

You can customize the game by modifying these constants in the code:

```python
WIDTH, HEIGHT = 600, 500          # Window dimensions
CELL_SIZE = 20                    # Grid cell size
SPEED_PRESETS = [                 # Speed options (label, FPS)
    ("Very Slow", 1),
    ("Slow", 3),
    ("Medium", 5),
    ("Fast", 10),
    ("Very Fast", 15),
]
```

## File Structure

```
mr-snake-game/
│
├── snake_game.py          # Main game file
├── highscore.txt          # High scores (auto-generated)
├── background.png         # Background image (not included)
├── README.md              # This file
└── LICENSE                # MIT License
```

## Technical Details

- **Built with**: Python 3.x and Pygame
- **Graphics**: Custom-rendered shapes with transparency effects
- **Data Persistence**: Text file storage for high scores
- **UI Design**: Bootstrap-inspired color scheme with glass morphism
- **Performance**: Configurable FPS from 1 to 15

## Requirements

```
pygame>=2.0.0
```

## Known Issues

- Background image path must be manually configured
- Game requires valid image file at specified path to run

## Future Enhancements

- [ ] Add sound effects and background music
- [ ] Implement power-ups and obstacles
- [ ] Add multiplayer support
- [ ] Create level progression system
- [ ] Add more snake skin options
- [ ] Include sample background images

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Lesley Shiri**
- GitHub: [@lesleyshiri](https://github.com/lesleyshiri)
- MBA Candidate at Clarkson University

## Acknowledgments

- Built as a Python mini-project
- Inspired by the classic Nokia Snake game
- Uses Pygame community resources and documentation

---

**Enjoy the game! 🎮🐍**
