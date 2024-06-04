import tkinter as tk
from tkinter import ttk, font
from PIL import Image, ImageTk

import pandas as pd
import numpy as np

from vars import *
from get_data_from_db import *

class TestQualityAssessment(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_evaluation_of_test_result()
    
    def init_evaluation_of_test_result(self):
        self.title('Оценка качества теста')
        self.state('zoomed')
        self.resizable(False, False)
        self.config(bg='#FFFFFF')

        self.grab_set()
        self.focus_set()

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=2)
        self.grid_rowconfigure(3, weight=2)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)

        back_frame = tk.Frame(self, bd=10, bg='#FFFFFF')
        back_frame.grid(row=0, column=0, columnspan=2, sticky='we')

        # Загрузка изображения и присвоение к back_label
        back_photo = ImageTk.PhotoImage(Image.open("Кнопки/Назад.png"))
        back_label = tk.Label(back_frame, bg='#FFFFFF')
        back_label.image = back_photo  # Сохраняем ссылку на изображение, чтобы оно не удалилось из памяти
        back_label.configure(image=back_photo)
        back_label.grid()

        # Привязываем событие нажатия на картинку к вызову self.destroy()
        back_label.bind('<Button-1>', lambda event: self.destroy())


        # Фрэйм для выбора параметров
        choice_frame = tk.Frame(self, bd=10, bg='#FFFFFF')
        choice_frame.grid(row=1, column=0, sticky='wen')

        # Фрэйм для подсказки
        help_frame = tk.Frame(self, bd=10, bg='#FFFFFF')
        help_frame.grid(row=1, column=1, sticky='en', padx=10)

        # Фрэйм для изначальной таблицы
        table_frame = tk.Frame(self, bd=10, bg='#FFFFFF')
        table_frame.grid(row=2, column=0, sticky='wen')

        # Фрэйм для отсортированной таблицы
        sorted_table_frame = tk.Frame(self, bd=10, bg='#FFFFFF')
        sorted_table_frame.grid(row=3, column=0, sticky='wen')

        # Фрэйм для рекомендаций
        info_frame = tk.Frame(self, bd=10)
        info_frame.grid(row=2, rowspan=2, column=1, sticky='wen', padx=10, pady=10)

        # Фрэйм для итога
        result_frame = tk.Frame(self, bd=10)
        result_frame.grid(row=4, column=0, columnspan=2, sticky='wesn', padx=10, pady=10)


        # Загрузка изображения и присвоение к help_label
        help_photo = ImageTk.PhotoImage(Image.open("Кнопки/Подсказка.png"))
        help_label = tk.Label(help_frame, bg='#FFFFFF')
        help_label.image = help_photo  # Сохраняем ссылку на изображение, чтобы оно не удалилось из памяти
        help_label.configure(image=help_photo)
        help_label.grid(row=0, column=0, sticky='w')

        # Создаем пользовательский шрифт
        custom_font = font.Font(family="Golos", size=12)

        # После выбора что анализировать выводится следующий виджет
        def bind_what_to_analyze(event):
            number_to_analyze_ST_label.grid_forget()
            number_to_analyze_SHT_label.grid_forget()
            number_analyze_combobox.grid_forget()
            analyze_label.grid_forget()

            cur_number_analyze.set('')
            number_analyze_combobox.grid(row=1, column=1, sticky='w', padx=20)

            # Заполнение данными в зависимости от выбора, что анализировать
            if cur_analyze.get() == 'Сеанс тестирования':
                number_to_analyze_ST_label.grid(row=0, column=1, sticky='w', padx=20)
                number_analyze_combobox['values'] = get_ST()

            elif cur_analyze.get() == 'Шаблон тестирования':
                number_to_analyze_SHT_label.grid(row=0, column=1, sticky='w', padx=20)
                number_analyze_combobox['values'] = get_SHT()


        # Загрузка изображения и присвоение к what_to_analyze_label
        what_to_analyze_photo = ImageTk.PhotoImage(Image.open("Кнопки/Что_анализировать.png"))
        what_to_analyze_label = tk.Label(choice_frame, bg='#FFFFFF')
        what_to_analyze_label.image = what_to_analyze_photo  # Сохраняем ссылку на изображение, чтобы оно не удалилось из памяти
        what_to_analyze_label.configure(image=what_to_analyze_photo)
        what_to_analyze_label.grid(row=0, column=0, sticky='w')

        cur_analyze = tk.StringVar()
        analyze_values = ['Сеанс тестирования', 'Шаблон тестирования']
        analyze_combobox = ttk.Combobox(choice_frame, textvariable=cur_analyze, width=25, values=analyze_values, font=custom_font)
        analyze_combobox.grid(row=1, column=0, sticky='w', padx= 5)
        analyze_combobox.bind('<<ComboboxSelected>>', bind_what_to_analyze)


        # После выбора какой ст/шт анализировать выводится кнопка
        def bind_number_to_analyze(event):
            analyze_label.grid(row=2, column=0, sticky='w', padx=5, pady=5)


        # Загрузка изображения и присвоение к number_to_analyze_ST_label
        number_to_analyze_ST_photo = ImageTk.PhotoImage(Image.open("Кнопки/Выберите_сеанс_тестирования.png"))
        number_to_analyze_ST_label = tk.Label(choice_frame, bg='#FFFFFF')
        number_to_analyze_ST_label.image = number_to_analyze_ST_photo  # Сохраняем ссылку на изображение, чтобы оно не удалилось из памяти
        number_to_analyze_ST_label.configure(image=number_to_analyze_ST_photo)

        # Загрузка изображения и присвоение к number_to_analyze_ST_label
        number_to_analyze_SHT_photo = ImageTk.PhotoImage(Image.open("Кнопки/Выберите_шаблон_тестирования.png"))
        number_to_analyze_SHT_label = tk.Label(choice_frame, bg='#FFFFFF')
        number_to_analyze_SHT_label.image = number_to_analyze_SHT_photo  # Сохраняем ссылку на изображение, чтобы оно не удалилось из памяти
        number_to_analyze_SHT_label.configure(image=number_to_analyze_SHT_photo)

        cur_number_analyze = tk.StringVar()
        number_analyze_combobox = ttk.Combobox(choice_frame, textvariable=cur_number_analyze, width=35, font=custom_font)
        number_analyze_combobox.bind('<<ComboboxSelected>>', bind_number_to_analyze)


        def analyze():
            if cur_analyze.get() == 'Сеанс тестирования':
                ST_id = cur_number_analyze.get()
                ST_id = ST_id[ST_id.find('(') + 1 : ST_id.find(')')]
                marks = get_marks_ST(ST_id)
                data = {}
                tasks = set()
                ind = ''

                for mark in marks:
                    if mark[0] != ind:
                        data[mark[0]] = []
                        ind = mark[0]
                        
                    data[mark[0]].append(round(mark[1], 2))
                    tasks.add(mark[2])
                
                tasks = sorted(list(tasks))

                print(data)
                print(tasks)

                df = pd.DataFrame(data=data, index=tasks)
                df.loc['Xi'] = (df.sum())
                df = df.T
                df.loc['Ri'] = (df.sum())
                df.loc['Ri', 'Xi'] = np.nan
                print(df)

                # Создание таблицы
                tree = ttk.Treeview(table_frame)
                tree['columns'] = tuple(df.columns)

                # Вертикальный скролл
                vert_scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
                vert_scrollbar.pack(side="right", fill="y")
                tree.configure(yscrollcommand=vert_scrollbar.set)

                # Горизонтальный скролл
                horiz_scrollbar = ttk.Scrollbar(table_frame, orient="horizontal", command=tree.xview)
                horiz_scrollbar.pack(side="bottom", fill="x")
                tree.configure(xscrollcommand=horiz_scrollbar.set)

                # Добавление заголовков столбцов
                tree.column('#0', width=40, anchor='c')
                for col in df.columns:
                    tree.column(col, width=50, anchor='e')
                tree.heading('#0', text='')
                for col in df.columns:
                    tree.heading(col, text=col)

                # Заполнение таблицы данными из DataFrame с округлением
                for index, row in df.iterrows():
                    values = []
                    for value in row:
                        if isinstance(value, (int, float)):
                            value = round(value, 3)
                            values.append(str(value))
                        else:
                            values.append(str(value))
                    tree.insert('', 'end', text=str(index), values=tuple(values))

                # Размещение таблицы и скроллбаров в окне
                tree.pack(side="left", fill="both", expand=True)
                vert_scrollbar.pack(side="right", fill="y")
                horiz_scrollbar.pack(side="bottom", fill="x")

                # Вычитание и деление на кол-во студентов
                df.loc['Wj'] = (10 - df.loc['Ri'])
                df.loc['pj'] = (df.loc['Ri'] / 10)
                df.loc['qj'] = (1 - df.loc['pj'])
                df.loc['pjqj'] = (df.loc['pj'] * df.loc['qj'])

                # Сортировка столбцов по убыванию значений в строке Ri
                df = df.sort_values('Ri', axis=1, ascending=False)
                # Сортировка строк по убыванию значений в столбце Xi
                df = df.sort_values('Xi', ascending=False)

                df = df.fillna('')
                print(df)


                # Создание отсортированной таблицы
                sorted_tree = ttk.Treeview(sorted_table_frame)
                sorted_tree['columns'] = tuple(df.columns)

                # Вертикальный скролл
                sorted_vert_scrollbar = ttk.Scrollbar(sorted_table_frame, orient="vertical", command=sorted_tree.yview)
                sorted_vert_scrollbar.pack(side="right", fill="y")
                sorted_tree.configure(yscrollcommand=sorted_vert_scrollbar.set)

                # Горизонтальный скролл
                sorted_horiz_scrollbar = ttk.Scrollbar(sorted_table_frame, orient="horizontal", command=sorted_tree.xview)
                sorted_horiz_scrollbar.pack(side="bottom", fill="x")
                sorted_tree.configure(xscrollcommand=sorted_horiz_scrollbar.set)

                # Добавление заголовков столбцов
                sorted_tree.column('#0', width=40, anchor='c')
                for col in df.columns:
                    sorted_tree.column(col, width=50, anchor='e')
                sorted_tree.heading('#0', text='')
                for col in df.columns:
                    sorted_tree.heading(col, text=col)

                # Заполнение таблицы данными из DataFrame с округлением
                for index, row in df.iterrows():
                    values = []
                    for value in row:
                        if isinstance(value, (int, float)):
                            value = round(value, 3)
                            values.append(str(value))
                        else:
                            values.append(str(value))
                    sorted_tree.insert('', 'end', text=str(index), values=tuple(values))

                # Размещение таблицы и скроллбаров в окне
                sorted_tree.pack(side="left", fill="both", expand=True)
                sorted_vert_scrollbar.pack(side="right", fill="y")
                sorted_horiz_scrollbar.pack(side="bottom", fill="x")

                tk.Label(result_frame, text='ИТОГ', font=custom_font).grid(row=0, column=0, sticky='w')
                tk.Label(result_frame, text='Следует пересмотреть', font=custom_font).grid(row=1, column=0, sticky='w')



            elif cur_analyze.get() == 'Шаблон тестирования':
                pass


        # btn_analyze = tk.Button(choice_frame, text='Анализировать', command=analyze)

        # Загрузка изображения и присвоение к analyze_label
        analyze_photo = ImageTk.PhotoImage(Image.open("Кнопки/Анализировать.png"))
        analyze_label = tk.Label(choice_frame, bg='#FFFFFF')
        analyze_label.image = analyze_photo  # Сохраняем ссылку на изображение, чтобы оно не удалилось из памяти
        analyze_label.configure(image=analyze_photo)

        # Привязываем событие нажатия на картинку к вызову analyze
        analyze_label.bind('<Button-1>', lambda event: analyze())


        # Очистка всех виджетов
        def del_all():
            number_to_analyze_ST_label.grid_forget()
            number_to_analyze_SHT_label.grid_forget()
            number_analyze_combobox.grid_forget()
            analyze_label.grid_forget()

            cur_analyze.set('')
            cur_number_analyze.set('')


        # Загрузка изображения и присвоение к del_label
        del_photo = ImageTk.PhotoImage(Image.open("Кнопки/Очистить.png"))
        del_label = tk.Label(choice_frame, bg='#FFFFFF')
        del_label.image = del_photo  # Сохраняем ссылку на изображение, чтобы оно не удалилось из памяти
        del_label.configure(image=del_photo)
        del_label.grid(row=2, column=1, sticky='w', padx=10, pady=5)

        # Привязываем событие нажатия на картинку к вызову del_all
        del_label.bind('<Button-1>', lambda event: del_all())