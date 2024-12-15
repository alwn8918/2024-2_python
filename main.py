import tkinter as tk
from tkinter import ttk
import subprocess

KNAPSACK_OPTIONS = ['Fractional Knapsack', '0-1 Knapsack']
ALGORITHM_OPTIONS = ['Greedy', 'Dynamic Programming', 'Branch and Bound']

# function
def buildGUI():
    # knapsack 선택
    option_frame = ttk.Frame(win)
    
    knapsack_label = ttk.Label(option_frame, text='Knapsack 선택: ')
    knapsack_label.grid(row=0, column=0)

    global knapsack_option
    knapsack_option = tk.IntVar(value=-1)
    for i in range(2):
        knapsack_button = ttk.Radiobutton(option_frame,
                                          text=KNAPSACK_OPTIONS[i],
                                          value=i,
                                          variable=knapsack_option,
                                          command=knapsack_button_handler)
        knapsack_button.grid(row=i, column=1, sticky='w')

    # 알고리즘 선택
    algorithm_label = ttk.Label(option_frame, text='알고리즘 선택: ')
    algorithm_label.grid(row=3, column=0)

    global algorithm_buttons
    global algorithm_option
    algorithm_option = tk.IntVar(value=-1)
    algorithm_buttons = []
    for i in range(3):
        algorithm_button = ttk.Radiobutton(option_frame,
                                           text=ALGORITHM_OPTIONS[i],
                                           value=i,
                                           variable=algorithm_option,
                                           command=algorithm_button_handler,
                                           state=tk.DISABLED)
        algorithm_button.grid(row=i+3, column=1, sticky='w')
        algorithm_buttons.append(algorithm_button)

    option_frame.pack(pady=5)

    # 배낭 용량
    knapsack_frame = ttk.Frame(win)
    capacity_label = ttk.Label(knapsack_frame, text='배낭 용량: ')
    capacity_label.grid(row=0, column=0)

    global capacity
    capacity = tk.IntVar()
    input_capacity = ttk.Entry(knapsack_frame, textvariable=capacity)
    input_capacity.grid(row=0, column=1, columnspan=2)

    # 물건 개수
    number_label = ttk.Label(knapsack_frame, text='물건 개수: ')
    number_label.grid(row=1, column=0)

    global number
    number = tk.IntVar()
    input_number = ttk.Entry(knapsack_frame, textvariable=number, width=10)
    input_number.grid(row=1, column=1)

    number_button = ttk.Button(knapsack_frame, text='확인', command=number_button_handler)
    number_button.grid(row=1, column=2)

    knapsack_frame.pack(pady=5)

    # 물건 정보
    global item_frame
    item_frame = ttk.Frame(win)
    item_frame.pack(pady=5)

    # 완료 버튼
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
    knapsack_weight = capacity.get()
    knapsack_amount = number.get()
        
    items_data = []
    for item in items:
        name = item['name'].get()
        profit = item['profit'].get()
        weight = item['weight'].get()
        items_data.append([name, profit, weight])
            
    # Fractional + Greedy
    if knapsack_option.get() == 0 and algorithm_option.get() == 0:
        # 기존 greedy.py 수정
        try:
            with open('greedy.py', 'r') as f:
                lines = f.readlines()
            
            with open('greedy.py', 'w') as f:
                for line in lines:
                    if line.startswith('knapsack_weight'):
                        f.write(f'knapsack_weight = {knapsack_weight}\n')
                    elif line.startswith('knapsack_amount'):
                        f.write(f'knapsack_amount = {knapsack_amount}\n')
                    elif line.startswith('knapsack'):
                        f.write(f'knapsack = {items_data}\n')
                    else:
                        f.write(line)
        except FileNotFoundError:
            print("greedy.py 파일이 존재하지 않습니다.")
            return

        # greedy.py 실행
        try:
            result = subprocess.run(['python3', 'greedy.py'], check=True, capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(e.stderr)

    # 0-1 + dynamic programming
    if knapsack_option.get() == 1 and algorithm_option.get() == 1:
        # 기존 dynamic_programming.py 수정
        try:
            with open('dynamic_programming.py', 'r') as f:
                lines = f.readlines()
            
            with open('dynamic_programming.py', 'w') as f:
                for line in lines:
                    if line.startswith('knapsack_weight'):
                        f.write(f'knapsack_weight = {knapsack_weight}\n')
                    elif line.startswith('knapsack_amount'):
                        f.write(f'knapsack_amount = {knapsack_amount}\n')
                    elif line.startswith('knapsack'):
                        f.write(f'knapsack = {items_data}\n')
                    else:
                        f.write(line)
        except FileNotFoundError:
            print("dynamic_programming.py 파일이 존재하지 않습니다.")
            return

        # dynamic_programming.py 실행
        try:
            result = subprocess.run(['python3', 'dynamic_programming.py'], check=True, capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(e.stderr)


def number_button_handler():
    for widget in item_frame.winfo_children():
        widget.destroy()

    global items
    items = []
    for i in range(number.get()):
        item = {}

        # 물건 이름
        name_label = ttk.Label(item_frame, text=f'{i+1}. 이름')
        name_label.grid(row=i, column=0)

        item["name"] = tk.StringVar()
        input_name = ttk.Entry(item_frame, textvariable=item["name"], width=10)
        input_name.grid(row=i, column=1)

        # 물건 값어치
        profit_label = ttk.Label(item_frame, text='값어치')
        profit_label.grid(row=i, column=2)

        item["profit"] = tk.IntVar()
        input_profit = ttk.Entry(item_frame, textvariable=item["profit"], width=10)
        input_profit.grid(row=i, column=3)

        # 물건 무게
        weight_label = ttk.Label(item_frame, text='무게')
        weight_label.grid(row=i, column=4)

        item["weight"] = tk.IntVar()
        input_weight = ttk.Entry(item_frame, textvariable=item["weight"], width=10)
        input_weight.grid(row=i, column=5)

        items.append(item)

# main program
win = tk.Tk()
win.title('Knapsack Program')
win.geometry('500x400')
buildGUI()

win.mainloop()
