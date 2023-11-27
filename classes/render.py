from typing import Tuple, List
import matplotlib.pyplot as plt
import os


class Render:
    def __init__(self, old_vertices: List[Tuple], new_vertices: List[Tuple]) -> None:
        self.old_vertices = old_vertices
        self.new_vertices = new_vertices

    def render_overlay(self):
        plt.clf()
        x_coords = [vertice[0] for vertice in self.old_vertices + self.new_vertices]
        y_coords = [vertice[1] for vertice in self.old_vertices + self.new_vertices]
        plt.plot(x_coords, y_coords, marker="o")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)
        plt.title("Old polygon")
        if not os.path.exists("./results"):
            os.mkdir("./results")
        plt.savefig("results/render_overlay.png")

    def render_subplot(self):
        plt.clf()
        old_x_coords = [vertice[0] for vertice in self.old_vertices]
        old_y_coords = [vertice[1] for vertice in self.old_vertices]
        new_x_coords = [vertice[0] for vertice in self.new_vertices]
        new_y_coords = [vertice[1] for vertice in self.new_vertices]
        plt.subplot(1, 2, 1)
        plt.plot(old_x_coords, old_y_coords, marker="o")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)
        plt.title("Old polygon")

        plt.subplot(1, 2, 2)
        plt.plot(new_x_coords, new_y_coords, marker="o")
        plt.xlabel("X-axis")
        plt.ylabel("Y-axis")
        plt.grid(True)
        plt.title("New polygon")
        if not os.path.exists("./results"):
            os.mkdir("./results")
        plt.savefig("results/render_subplot.png")
