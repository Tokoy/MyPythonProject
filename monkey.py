#!/usr/bin/env python
# coding=utf-8
from Tkinter import *
import tkMessageBox, sys
from random import randint

class Grid(object):
    #设置画布属性
    def __init__(self, master=None, window_width=250, window_height=500, grid_width=50, offset=10):
        self.height = window_height
        self.width = window_width
        self.grid_width = grid_width
        self.offset = offset
        self.grid_x = self.width / self.grid_width
        self.grid_y = self.height / self.grid_width
        self.bg = "#EBEBEB"
        self.canvas = Canvas(master, width=self.width + 2 * self.offset, height=self.height + 2 * self.offset,
                             bg=self.bg)
        self.canvas.pack()
        self.grid_list()

    #绘制方块
    def draw(self, pos, color, ):
        x = pos[0] * self.grid_width + self.offset
        y = pos[1] * self.grid_width + self.offset
        self.canvas.create_rectangle(x, y, x + self.grid_width, y + self.grid_width, fill=color, outline=self.bg)

    #设置数组
    def grid_list(self):
        grid_list = []
        for y in range(0, self.grid_y):
            for x in range(0, self.grid_x):
                grid_list.append((x, y))
        self.grid_list = grid_list


class Obstacles(object):
    #设置障碍物属性
    def __init__(self, Grid):
        self.grid = Grid
        self.color = "#23D978"
        self.set_pos()

    #生成障碍物位置
    def set_pos(self):
        x = randint(0, 4)
        y = 0
        self.pos = (x, y)

    #绘制障碍物
    def display(self):
        self.grid.draw(self.pos, self.color)


class Monkey(object):
    #设置属性
    def __init__(self, Grid):
        self.grid = Grid
        self.body = (2, 9)
        self.status = ['run', 'stop']
        self.direction = "Up"
        self.speed = 300
        self.color = "#5FA8D9"
        self.obstacles = Obstacles(self.grid)
        self.display_obstacles()
        self.gameover = False
        self.score = 0

    #判断障碍物是否在画布里面
    def available_grid(self):
        return [i for i in self.grid.grid_list if i not in self.obstacles.pos]

    #改变前进方向
    def change_direction(self, direction):
        self.direction = direction

    #绘制主方块
    def display(self):
            self.grid.draw(self.body, self.color)

    #显示障碍物
    def display_obstacles(self):
            self.obstacles.display()

    #行动，默认的向前
    def move(self):
        obstacleshead = self.obstacles.pos
        monkeyhead=self.body
        if self.direction == 'Up':
            new = (obstacleshead[0], obstacleshead[1] + 1)
        # elif self.direction == 'Down':
        #     new = (head[0], head[1] + 1)
        elif self.direction == 'Left':
            new = (monkeyhead[0] - 1, monkeyhead[1])
        elif self.direction == 'Right':
            new = (monkeyhead[0] + 1, monkeyhead[1])
        else:
            new = (obstacleshead[0], obstacleshead[1] + 1)

        # 如果障碍物位置和头位置不一致
        if not monkeyhead == obstacleshead:
            self.grid.draw(obstacleshead, self.grid.bg)
            self.score += 1
        else:
            self.status.reverse()
            self.gameover = True
        self.obstacles.pos = new
        if not new in self.available_grid():
            self.display_obstacles()
        else:
            self.grid.draw(new, color=self.obstacles.color)

class MonkeyGame(Frame):
    #静态绘制好视图
    def __init__(self, master=None, *args, **kwargs):
        Frame.__init__(self, master)
        self.master = master
        self.grid = Grid(master=master, *args, **kwargs)
        self.monkey=Monkey(self.grid)
        self.bind_all("<KeyRelease>", self.key_release)
        self.monkey.display()

    def key_release(self, event):
        key = event.keysym
        key_dict = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if key_dict.has_key(key) and not key == key_dict[self.monkey.direction]:
            self.monkey.change_direction(key)
            self.monkey.move()
        elif key == 'p':
            self.monkey.status.reverse()

    def run(self):
        if not self.monkey.status[0] == 'stop':
            self.monkey.move()
        if self.monkey.gameover == True:
            message = tkMessageBox.showinfo("Game Over", "your score: %d" % self.monkey.score)
            if message == 'ok':
                sys.exit()
        self.after(self.monkey.speed, self.run)

if __name__ == '__main__':
    root = Tk()
    monkey = MonkeyGame(root)
    monkey.run()
    monkey.mainloop()
