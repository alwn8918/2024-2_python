import tkinter as tk
from tkinter import ttk

KNAPSACK_OPTIONS = ['Fractional Knapsack', '0-1 Knapsack']
ALGORITHM_OPTIONS = ['Greedy', 'Dynamic Programming', 'Branch and Bound']

# function
def buildGUI():
    # knapsack 선택
    knapsack_label = ttk.Label(win, text='Knapsack 선택')
    knapsack_label.pack()

    global knapsack_option
    knapsack_option = tk.IntVar(value=-1)
    for i in range(2):
        knapsack_button = ttk.Radiobutton(win,
                                          text=KNAPSACK_OPTIONS[i],
                                          value=i,
                                          variable=knapsack_option,
                                          command=knapsack_button_handler)
        knapsack_button.pack()

    # 알고리즘 선택
    algorithm_label = ttk.Label(win, text='알고리즘 선택')
    algorithm_label.pack()

    global algorithm_buttons
    global algorithm_option
    algorithm_option = tk.IntVar(value=-1)
    algorithm_buttons = []
    for i in range(3):
        algorithm_button = ttk.Radiobutton(win,
                                           text=ALGORITHM_OPTIONS[i],
                                           value=i,
                                           variable=algorithm_option,
                                           command=algorithm_button_handler,
                                           state=tk.DISABLED)
        algorithm_button.pack()
        algorithm_buttons.append(algorithm_button)

    complete_button = ttk.Button(win, text='완료', command=complete_button_handler)
    complete_button.pack(side=tk.BOTTOM)

def knapsack_button_handler():
    selected_knapsack = knapsack_option.get()
    if selected_knapsack == 0:  # Fractional Knapsack
        algorithm_buttons[0].config(state=tk.NORMAL)
        algorithm_buttons[1].config(state=tk.DISABLED)
        algorithm_buttons[2].config(state=tk.DISABLED)
    elif selected_knapsack == 1:  # 0-1 Knapsack
        algorithm_buttons[0].config(state=tk.DISABLED)
        algorithm_buttons[1].config(state=tk.NORMAL)
        algorithm_buttons[2].config(state=tk.NORMAL)

def algorithm_button_handler():
    pass

def complete_button_handler():
    print('Knapsack:', KNAPSACK_OPTIONS[knapsack_option.get()])
    print('Algorithm:', ALGORITHM_OPTIONS[algorithm_option.get()])

# main program
win = tk.Tk()
win.title('Knapsack Program')
win.geometry('300x200')
buildGUI()

win.mainloop()
