import tkinter as tk
from tkinter import ttk

from vars import *

class EvaluationOfTestResult(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_evaluation_of_test_result()
    
    def init_evaluation_of_test_result(self):
        self.title('Оценка результатов тестируемых')
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

        tk.Label(info_frame, text='СТ - СЕАНС ТЕСТИРОВАНИЯ \nШТ - ШАБЛОН ТЕСТА \nШТЗ - ШАБЛОН ТЕСТОВОГО ЗАДАНИЯ', bg='#D9D9D9').grid(row=0, column=0, sticky='w')

        # table_frame = tk.Frame(self, bd=10)
        # table_frame.grid(row=1, column=0, sticky='wesn')

        what_to_draw_label = tk.Label(choice_frame, text='Что вывести')
        what_to_draw_label.grid(row=0, column=0, sticky='w')

        cur_draw = tk.StringVar()
        draw_values = ['% УСПЕШНО ПРОЙДЕННЫХ СТ/ШТ/ШТЗ', 'СРЕДНЯЯ ОЦЕНКА ПО НЕСКОЛЬКИМ СТ/ШТ', 'СРЕДНЯЯ ОЦЕНКА ПО ОДНОМУ СТ/ШТ']
        draw_combobox = ttk.Combobox(choice_frame, textvariable=cur_draw, width=45, values=draw_values)
        draw_combobox.grid(row=1, column=0, sticky='w')

        what_to_analyze_label = tk.Label(choice_frame, text='Что анализировать')
        what_to_analyze_label.grid(row=2, column=0, sticky='w')

        cur_analyze = tk.StringVar()
        analyze_combobox = ttk.Combobox(choice_frame, textvariable=cur_analyze, width=30)
        # analyze_combobox['values'] = взять инфу из бд СТ/ШТ/ШТЗ
        analyze_combobox.grid(row=3, column=0, sticky='w')

        number_to_analyze_label = tk.Label(choice_frame, text='Какой СТ/ШТ/ШТЗ анализировать')
        number_to_analyze_label.grid(row=4, column=0, sticky='w')

        cur_number_analyze = tk.StringVar()
        number_analyze_combobox = ttk.Combobox(choice_frame, textvariable=cur_number_analyze, width=30)
        # number_analyze_combobox['values'] = взять инфу из бд номер ст/шт/штз
        number_analyze_combobox.grid(row=5, column=0, sticky='w')

        view_label = tk.Label(choice_frame, text='Вид')
        view_label.grid(row=6, column=0, sticky='w')

        cur_view = tk.StringVar()
        view_combobox = ttk.Combobox(choice_frame, textvariable=cur_view, width=30)
        # view_combobox['values'] = взять инфу из бд таблица/график/диаграмма
        view_combobox.grid(row=7, column=0, sticky='w')

        # Добавить выбор группы/годов

        # После добавления группы/годов поменять row
        btn_analyze = tk.Button(choice_frame, text='Показать')
        btn_analyze.grid(row=8, column=0, sticky='w', pady=5)

        # После добавления группы/годов поменять row
        btn_del = tk.Button(choice_frame, text='Очистить')
        btn_del.grid(row=8, column=1, padx=5, pady=5)

        # tk.Label(info_frame, text='СТ - СЕАНС ТЕСТИРОВАНИЯ', bg='#D9D9D9').grid(row=0, column=0, sticky='w')
        # tk.Label(info_frame, text='ШТ - ШАБЛОН ТЕСТА', bg='#D9D9D9').grid(row=1, column=0, sticky='w')
        # tk.Label(info_frame, text='ШТЗ - ШАБЛОН ТЕСТОВОГО ЗАДАНИЯ', bg='#D9D9D9').grid(row=2, column=0, sticky='w')

        