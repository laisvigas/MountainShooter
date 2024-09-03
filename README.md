# <img src="https://github.com/laisvigas/MountainShooter/blob/master/asset/Level1Bg3.png" width="50" height="50" alt="Level1Bg3 Logo"> Mountain Shooter <img src="https://github.com/laisvigas/MountainShooter/blob/master/asset/Level1Bg3.png" width="50" height="50" alt="Level1Bg3 Logo">

**Mountain Shooter** is a **2D Shooter Game** built using Python and Pygame. The game was developed with a professor as part of the **Applied Programming Language** course in the undergraduate program for **Digital Games** at **UNINTER**. It features three levels with various player controls, enemy AI, background animations, and score management. Additionally, I independently developed some functionalities as part of the course's final exercise.

## Key Features

### 1. Game Initialization and Setup
- Initializes the game window with specified dimensions.
- Loads and plays background music and sound effects.
- Initializes game entities, including players, enemies, and backgrounds, based on the selected game mode and level.

### 2. Menu System
- Provides a main menu with multiple options:
  - Start a new game (Single-player, 2-player cooperative, 2-player competitive).
  - View high scores.
  - Exit the game.
- Allows navigation through menu options using keyboard input.

### 3. Player Controls and Mechanics
- Players can move in four directions using keyboard keys.
- Players can shoot projectiles to defeat enemies.
- Supports two players with separate controls and shooting mechanics.
  - Controls for the first player: Arrow keys to move and M to shoot.
  - Controls for the second player: WASD to move and Z to shoot.

### 4. Enemy AI and Behavior
- Three types of enemies, with distinct behaviors.
- The first two enemies move horizontally only.
- The third enemy, encountered in level three, moves both horizontally and vertically, changing direction upon reaching screen boundaries.
- Enemies can shoot projectiles at players.

### 5. Background Animation
- Animated scrolling backgrounds for each level using the parallax concept.
- Backgrounds are loaded dynamically based on the current game level.

### 6. Collision Detection and Scoring
- Detects collisions between player shots and enemy shots.
- Manages health and damage for entities upon collisions.
- Updates player scores based on enemy defeats.

### 7. Level Progression
- The game is divided into three levels, with the third level lasting twice as long as the first two.
- Players progress to the next level upon completing the current level.
- Each level has a timeout mechanism; players must survive within the given time to progress.

### 8. Score Management
- Scores are saved to an SQLite database.
- Players can enter their names upon completing the game to save their scores.
- Displays the top 10 high scores on the score screen.

### 9. Entity Factory and Mediator
- Factory design pattern used to dynamically create game entities.
- Mediator pattern to manage interactions and collisions between game entities.

### 10. Assets Management
- Utilizes various assets such as images and sounds stored in the `assets` folder.
- Dynamically loads images and sounds based on the game state.

## <img src="https://github.com/laisvigas/MountainShooter/blob/master/asset/Level2Bg3.png" width="50" height="50" alt="Level1Bg3 Logo"> Personal Implementations <img src="https://github.com/laisvigas/MountainShooter/blob/master/asset/Level2Bg3.png" width="50" height="50" alt="Level1Bg3 Logo">

The following features were implemented independently:

1. **Menu Customization**:
   - The menu displays my name name in one of the corners of the screen.

2. **Level 3 Implementation**:
   - **Level Sequencing**: Level 3 appears after Level 2 and before the final score screen.
   - **Score Continuity**: Level 3 maintains the cumulative score from levels 1 and 2.
   - **Extended Duration**: Level 3 has a duration twice that of levels 1 and 2. For example, if levels 1 and 2 last 20 seconds each, level 3 lasts 40 seconds.
   - **Unique Background**: Level 3 has a different background from levels 1 and 2, featuring a parallax effect.
   - **Unique Soundtrack**: Level 3 plays a different song from levels 1 and 2.

3. **Enemy3 Specific Features**:
   - **Exclusive to Level 3**: Level 3 exclusively generates 'Enemy3' only.
   - **Unique Movement Behavior**:
     - On the **horizontal axis (x-axis)**, 'Enemy3' moves from right to left across the screen.
     - On the **vertical axis (y-axis)**, 'Enemy3' moves up and down continuously:
       - When 'Enemy3' reaches the bottom edge of the screen, it reverses direction and moves up at normal speed.
       - When 'Enemy3' reaches the top edge of the screen, it changes direction to move down at twice its normal speed.
   - **Shooting and Damage**: 'Enemy3' has the ability to shoot projectiles and cause damage to the player, similar to other enemies in the game.

## How to Run the Game

1. Install Python and Pygame.
2. Run the main game script:

   ```bash
   python main.py

Thank you for exploring **Mountain Shooter**! This game was a challenging yet rewarding project that combined creativity and programming skills to bring a classic 2D shooter experience to life.
