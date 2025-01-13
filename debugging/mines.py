#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(f"{y:2}", end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')
                else:
                    print('.', end=' ')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # Check if the coordinates are within bounds and not revealed yet
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True  # Simply return True for invalid coordinates
        if self.revealed[y][x]:
            return True  # No need to reveal a cell that's already revealed
        
        if (y * self.width + x) in self.mines:
            return False
        
        self.revealed[y][x] = True
        if self.count_mines_nearby(x, y) == 0:
            # Using an explicit stack to avoid recursion depth issues
            to_check = [(x, y)]
            while to_check:
                cx, cy = to_check.pop()
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                            self.revealed[ny][nx] = True
                            if self.count_mines_nearby(nx, ny) == 0:
                                to_check.append((nx, ny))
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input(f"Enter x coordinate (0-{self.width - 1}): "))
                y = int(input(f"Enter y coordinate (0-{self.height - 1}): "))
                
                # Validation des coordonnées
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print(f"Invalid coordinates. Please enter values within the range 0-{self.width - 1} for x and 0-{self.height - 1} for y.")
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()

