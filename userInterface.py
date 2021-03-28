import tkinter
from tkinter import *
from algorithms import algorithms

class user_interface:
  def __init__(self, master):
    frame = Frame(master)
    frame.pack()
    self.labelUpper = Label(frame, text = "How many uppercase letters:")
    self.labelUpper.grid(row = 0, column = 0, padx = 20, pady = 20)
    self.entUpper = Entry(frame, width = 22)
    self.entUpper.grid(row = 0, column = 1, padx = 20, pady = 20, sticky = W)

    self.labelMid = Label(frame, text = "How many lowercase letters:")
    self.labelMid.grid(row = 1, column = 0, padx = 20, pady = 20, sticky = W)
    self.entMid = Entry(frame, width = 22)
    self.entMid.grid(row = 1, column = 1, padx = 20, pady = 20, sticky = W)

    self.labelThird = Label(frame, text = "How many digits:")
    self.labelThird.grid(row = 2, column = 0, padx = 20, pady = 20, sticky = W)
    self.entThird = Entry(frame, width = 22)
    self.entThird.grid(row = 2, column = 1, padx = 20, pady = 20, sticky = W)

    self.labelBot = Label(frame, text = "How many special characters:")
    self.labelBot.grid(row = 3, column = 0, padx = 20, pady = 20, sticky = W)
    self.entBot = Entry(frame, width = 22)
    self.entBot.grid(row = 3, column = 1, padx = 20, pady = 20, sticky = W)

    self.buttonExecute = Button(frame, text = 'Generate Password', command = self.getAnswers)
    self.buttonExecute.grid(row = 4, column = 0, padx = 5, pady = 18, sticky = W)

    self.entPas = Entry(frame, width = 22)
    self.entPas.grid(row = 4, column = 1, padx = 20, pady = 20, sticky = W)

  def getAnswers(self):
    arr = []
    arr.append(self.entUpper.get())
    arr.append(self.entMid.get())
    arr.append(self.entThird.get())
    arr.append(self.entBot.get())
    algorithm = algorithms(arr)
    
    password = algorithm.randoms()
    self.entPas.delete(0, END)
    self.entPas.insert(0, password)