import tkinter as tk
from tkinter import ttk

from vars import *

class TestQualityAssessment(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_evaluation_of_test_result()
    
    def init_evaluation_of_test_result(self):
        self.title('Оценка качества теста')
        self.geometry('650x450+350+250')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)

        back_frame = tk.Frame(self, bd=10)
        back_frame.grid(row=0, column=0, columnspan=2, sticky='we')

        btn_back = tk.Button(back_frame, text='Назад', command=lambda: self.destroy())
        btn_back.grid()

        choice_frame = tk.Frame(self, bd=10)
        choice_frame.grid(row=1, column=0, sticky='wen')

        info_frame = tk.Frame(self, bd=10, bg='#D9D9D9')
        info_frame.grid(row=1, column=1, sticky='en', padx=10)

        tk.Label(info_frame, text='СТ - СЕАНС ТЕСТИРОВАНИЯ \nШТ - ШАБЛОН ТЕСТА', bg='#D9D9D9').grid(row=0, column=0, sticky='w')

        what_to_analyze_label = tk.Label(choice_frame, text='Что анализировать')
        what_to_analyze_label.grid(row=0, column=0, sticky='w')

        cur_analyze = tk.StringVar()
        analyze_values = ['СТ', 'ШТ']
        analyze_combobox = ttk.Combobox(choice_frame, textvariable=cur_analyze, width=30, values=analyze_values)
        analyze_combobox.grid(row=1, column=0, sticky='w')

        number_to_analyze_label = tk.Label(choice_frame, text='Какой СТ/ШТ анализировать')
        number_to_analyze_label.grid(row=2, column=0, sticky='w')

        cur_number_analyze = tk.StringVar()
        number_analyze_combobox = ttk.Combobox(choice_frame, textvariable=cur_number_analyze, width=30)
        # number_analyze_combobox['values'] = взять инфу из бд номер ст/шт/штз
        number_analyze_combobox.grid(row=3, column=0, sticky='w')

        btn_analyze = tk.Button(choice_frame, text='Анализировать')
        btn_analyze.grid(row=4, column=0, sticky='w', pady=5)

        btn_del = tk.Button(choice_frame, text='Очистить')
        btn_del.grid(row=4, column=1, padx=5, pady=5)