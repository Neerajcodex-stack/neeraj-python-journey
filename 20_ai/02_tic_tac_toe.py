# 



import tkinter as tk
import random

# Define Snake and Food classes
class Snake:
    def __init__(self, head):
        self.head = head
        self.body = [head]
        self.direction = (0, 1)  # moving down by default

    def move(self):
        new_head = (self.head[0] + self.direction[0], self.head[1] + self.direction[1])
        self.body.insert(0, new_head)
        self.head = new_head
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def __len__(self):
        return len(self.body)

class Food:
    def __init__(self, coordinates):
        self.coordinates = coordinates

    def is_eaten(self, snake):
        return snake.head == self.coordinates

def start_game():
    root = tk.Tk()
    root.title("Snake Game")

    grid_width = 20
    grid_height = 20
    cell_size = 20

    canvas_width = grid_width * cell_size
    canvas_height = grid_height * cell_size

    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
    canvas.pack()

    snake = Snake((10, 10))
    for _ in range(4):
        snake.body.append((snake.head[0], snake.head[1] - (_ + 1)))

    def random_food():
        while True:
            pos = (random.randint(0, grid_width - 1), random.randint(0, grid_height - 1))
            if pos not in snake.body:
                return pos

    food = Food(random_food())

    score = [0]
    game_active = [True]

    def draw():
        canvas.delete("all")
        # Draw snake
        for x, y in snake.body:
            canvas.create_rectangle(x * cell_size, y * cell_size,
                                   (x + 1) * cell_size, (y + 1) * cell_size,
                                   fill="green")
        # Draw food
        fx, fy = food.coordinates
        canvas.create_oval(fx * cell_size, fy * cell_size,
                           (fx + 1) * cell_size, (fy + 1) * cell_size,
                           fill="red")
        canvas.create_text(40, 10, fill="white", text=f"Score: {score[0]}", anchor="nw")

    def move_snake():
        if not game_active[0]:
            return
        snake.move()
        # Check collision with walls
        x, y = snake.head
        if x < 0 or y < 0 or x >= grid_width or y >= grid_height:
            game_active[0] = False
            canvas.create_text(canvas_width // 2, canvas_height // 2, fill="white", text="Game Over", font=("Arial", 24))
            return
        # Check collision with self
        if snake.head in snake.body[1:]:
            game_active[0] = False
            canvas.create_text(canvas_width // 2, canvas_height // 2, fill="white", text="Game Over", font=("Arial", 24))
            return
        # Check food
        if food.is_eaten(snake):
            snake.grow()
            score[0] += 1
            food.coordinates = random_food()
        draw()
        root.after(100, move_snake)

    def on_key(event):
        key = event.keysym
        if key == "Up" and snake.direction != (0, 1):
            snake.direction = (0, -1)
        elif key == "Down" and snake.direction != (0, -1):
            snake.direction = (0, 1)
        elif key == "Left" and snake.direction != (1, 0):
            snake.direction = (-1, 0)
        elif key == "Right" and snake.direction != (-1, 0):
            snake.direction = (1, 0)

    root.bind("<Key>", on_key)
    draw()
    move_snake()
    root.mainloop()

if __name__ == "__main__":
    start_game()

