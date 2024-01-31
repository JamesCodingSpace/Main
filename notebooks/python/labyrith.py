import tkinter as tk
import random

class MazeGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Labyrinth Generator")

        self.size_label = tk.Label(master, text="Labyrinthgröße:")
        self.size_label.pack()

        self.size_entry = tk.Entry(master)
        self.size_entry.pack()

        self.difficulty_label = tk.Label(master, text="Schwierigkeitsstufe:")
        self.difficulty_label.pack()

        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set("easy")

        difficulty_options = ["easy", "medium", "hard"]
        self.difficulty_menu = tk.OptionMenu(master, self.difficulty_var, *difficulty_options)
        self.difficulty_menu.pack()

        self.generate_button = tk.Button(master, text="Labyrinth generieren", command=self.generate_maze)
        self.generate_button.pack()

        self.canvas = tk.Canvas(master, width=500, height=500)
        self.canvas.pack()

    def generate_maze(self):
        size = int(self.size_entry.get())
        difficulty = self.difficulty_var.get()

        maze = self.generate_maze_data(size, difficulty)
        self.draw_maze(maze)

    def generate_maze_data(self, size, difficulty):
        if difficulty == "easy":
            wall_density = 0.1
        elif difficulty == "medium":
            wall_density = 0.3
        elif difficulty == "hard":
            wall_density = 0.5
        else:
            raise ValueError("Ungültige Schwierigkeitsstufe")

        maze = [[0] * size for _ in range(size)]

        # Rand des Labyrinths setzen
        for i in range(size):
            maze[0][i] = maze[size - 1][i] = 1
            maze[i][0] = maze[i][size - 1] = 1

        # Wände im Labyrinth setzen
        for i in range(1, size - 1):
            for j in range(1, size - 1):
                if random.random() < wall_density:
                    maze[i][j] = 1

        # Eingang und Ausgang setzen
        maze[0][1] = maze[size - 1][size - 2] = 0

        return maze

    def draw_maze(self, maze):
        self.canvas.delete("all")

        cell_size = 500 / len(maze)

        for i in range(len(maze)):
            for j in range(len(maze[i])):
                x0, y0 = j * cell_size, i * cell_size
                x1, y1 = (j + 1) * cell_size, (i + 1) * cell_size

                if maze[i][j] == 1:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="black")
                else:
                    self.canvas.create_rectangle(x0, y0, x1, y1, fill="white")

if __name__ == "__main__":
    root = tk.Tk()
    app = MazeGeneratorGUI(root)
    root.mainloop()
