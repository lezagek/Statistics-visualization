import tkinter as tk
from tkinter import ttk

from vars import *
from get_data_from_db import *

class TestQualityAssessment(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_evaluation_of_test_result()
    
    def init_evaluation_of_test_result(self):
        self.title('Оценка качества теста')
        # self.attributes('-fullscreen', True)
        # self.geometry('650x450+350+250')
        # self.resizable(False, False)

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


        # После выбора что анализировать выводится следующий виджет
        def bind_what_to_analyze(event):
            number_to_analyze_ST_label.grid_forget()
            number_to_analyze_SHT_label.grid_forget()
            number_analyze_combobox.grid_forget()
            btn_analyze.grid_forget()

            cur_number_analyze.set('')
            number_analyze_combobox.grid(row=1, column=1, sticky='w', padx=5)

            # Заполнение данными в зависимости от выбора, что анализировать
            if cur_analyze.get() == 'СЕАНС ТЕСТИРОВАНИЯ':
                number_to_analyze_ST_label.grid(row=0, column=1, sticky='w', padx=5)
                number_analyze_combobox['values'] = get_ST()

            elif cur_analyze.get() == 'ШАБЛОН ТЕСТИРОВАНИЯ':
                number_to_analyze_SHT_label.grid(row=0, column=1, sticky='w', padx=5)
                number_analyze_combobox['values'] = get_SHT()


        what_to_analyze_label = tk.Label(choice_frame, text='Что анализировать')
        what_to_analyze_label.grid(row=0, column=0, sticky='w')

        cur_analyze = tk.StringVar()
        analyze_values = ['СЕАНС ТЕСТИРОВАНИЯ', 'ШАБЛОН ТЕСТИРОВАНИЯ']
        analyze_combobox = ttk.Combobox(choice_frame, textvariable=cur_analyze, width=30, values=analyze_values)
        analyze_combobox.grid(row=1, column=0, sticky='w', padx= 5)
        analyze_combobox.bind('<<ComboboxSelected>>', bind_what_to_analyze)


        # После выбора какой ст/шт анализировать выводится кнопка
        def bind_number_to_analyze(event):
            btn_analyze.grid(row=2, column=0, sticky='w', pady=5)


        number_to_analyze_ST_label  = tk.Label(choice_frame, text='Выберите СТ')
        number_to_analyze_SHT_label  = tk.Label(choice_frame, text='Выберите ШТ')

        cur_number_analyze = tk.StringVar()
        number_analyze_combobox = ttk.Combobox(choice_frame, textvariable=cur_number_analyze, width=30)
        number_analyze_combobox.bind('<<ComboboxSelected>>', bind_number_to_analyze)

        btn_analyze = tk.Button(choice_frame, text='Анализировать')


        # Очистка всех виджетов
        def del_all():
            number_to_analyze_ST_label.grid_forget()
            number_to_analyze_SHT_label.grid_forget()
            number_analyze_combobox.grid_forget()
            btn_analyze.grid_forget()

            cur_analyze.set('')
            cur_number_analyze.set('')


        btn_del = tk.Button(choice_frame, text='Очистить', command=del_all)
        btn_del.grid(row=2, column=1, sticky='w', padx=5, pady=5)


        # Тестовая таблица
        frame = tk.Frame(self, bd=10)
        frame.grid(row=2, column=0, sticky='wen')

        # Создание и настройка виджета Treeview для отображения таблицы
        table = ttk.Treeview(frame, columns=('A Scores', 'B Scores'))
        table.heading('#0', text='Index')
        table.heading('A Scores', text='A Scores')
        table.heading('B Scores', text='B Scores')
        
        # Вставка данных в таблицу
        data = [[100, 95], [90, 85], [80, 75], [90, 95]]
        for i, (a_score, b_score) in enumerate(data, start=1):
            table.insert('', 'end', text=str(i), values=(a_score, b_score))
        
        # Упаковка виджета Treeview и запуск главного цикла Tkinter
        table.pack(expand=True, fill=tk.BOTH)