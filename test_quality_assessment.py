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

        # Создаем пользовательский шрифт
        custom_font = font.Font(family="Golos", size=12)

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
        help_frame.grid(row=1, column=1, sticky='en')

        # Фрэйм для изначальной таблицы
        table_frame = tk.Frame(self, bd=10, bg='#FFFFFF')

        # Фрэйм для отсортированной таблицы
        sorted_table_frame = tk.Frame(self, bd=10, bg='#FFFFFF')

        # Фрэйм для рекомендаций
        info_frame = tk.Frame(self, bd=10)

        # Текст рекомендаций
        good_stud_label = tk.Label(info_frame, font=custom_font)
        bad_stud_label = tk.Label(info_frame, font=custom_font)
        dif_label = tk.Label(info_frame, font=custom_font)

        # Фрэйм для итога
        result_frame = tk.Frame(self, bd=10)

        # Текст итога
        result_label = tk.Label(result_frame, text='ИТОГ', font=custom_font)
        reconsider_label = tk.Label(result_frame, text='Следует пересмотреть', font=custom_font)
        result_stud_label = tk.Label(result_frame, font=custom_font)
        result_dif_label = tk.Label(result_frame, font=custom_font)

        # Таблицы
        tree = ttk.Treeview(table_frame)
        vert_scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=tree.yview)
        horiz_scrollbar = ttk.Scrollbar(table_frame, orient="horizontal", command=tree.xview)
        sorted_tree = ttk.Treeview(sorted_table_frame)
        sorted_vert_scrollbar = ttk.Scrollbar(sorted_table_frame, orient="vertical", command=sorted_tree.yview)
        sorted_horiz_scrollbar = ttk.Scrollbar(sorted_table_frame, orient="horizontal", command=sorted_tree.xview)

        # Загрузка изображения и присвоение к help_label
        help_photo = ImageTk.PhotoImage(Image.open("Текст/Подсказка.png"))
        help_label = tk.Label(help_frame, bg='#FFFFFF')
        help_label.image = help_photo  # Сохраняем ссылку на изображение, чтобы оно не удалилось из памяти
        help_label.configure(image=help_photo)
        help_label.grid(row=0, column=0, sticky='w')

        def reset_number_to_analyze():
            number_to_analyze_ST_label.grid_forget()
            number_to_analyze_SHT_label.grid_forget()
            number_analyze_combobox.grid_forget()
            analyze_label.grid_forget()

            cur_number_analyze.set('')

        def reset_all():
            table_frame.grid_forget()
            tree.pack_forget()
            vert_scrollbar.pack_forget()
            horiz_scrollbar.pack_forget()
            sorted_table_frame.grid_forget()
            sorted_tree.pack_forget()
            sorted_vert_scrollbar.pack_forget()
            sorted_horiz_scrollbar.pack_forget()
            info_frame.grid_forget()
            good_stud_label.grid_forget()
            bad_stud_label.grid_forget()
            dif_label.grid_forget()
            result_frame.grid_forget()
            result_label.grid_forget()
            reconsider_label.grid_forget()
            result_stud_label.grid_forget()
            result_dif_label.grid_forget()


        # После выбора что анализировать выводится следующий виджет
        def bind_what_to_analyze(event):
            reset_number_to_analyze()
            reset_all()

            number_analyze_combobox.grid(row=1, column=1, sticky='w', padx=20)

            # Заполнение данными в зависимости от выбора, что анализировать
            if cur_analyze.get() == 'Сеанс тестирования':
                number_to_analyze_ST_label.grid(row=0, column=1, sticky='w', padx=20)
                number_analyze_combobox['values'] = get_ST()

            elif cur_analyze.get() == 'Шаблон тестирования':
                number_to_analyze_SHT_label.grid(row=0, column=1, sticky='w', padx=20)
                number_analyze_combobox['values'] = get_SHT()


        # Загрузка изображения и присвоение к what_to_analyze_label
        what_to_analyze_photo = ImageTk.PhotoImage(Image.open("Текст/Что_анализировать.png"))
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
            reset_all()

            analyze_label.grid(row=2, column=0, sticky='w', padx=5, pady=5)


        # Загрузка изображения и присвоение к number_to_analyze_ST_label
        number_to_analyze_ST_photo = ImageTk.PhotoImage(Image.open("Текст/Выберите_сеанс_тестирования.png"))
        number_to_analyze_ST_label = tk.Label(choice_frame, bg='#FFFFFF')
        number_to_analyze_ST_label.image = number_to_analyze_ST_photo  # Сохраняем ссылку на изображение, чтобы оно не удалилось из памяти
        number_to_analyze_ST_label.configure(image=number_to_analyze_ST_photo)

        # Загрузка изображения и присвоение к number_to_analyze_SHT_label
        number_to_analyze_SHT_photo = ImageTk.PhotoImage(Image.open("Текст/Выберите_шаблон_тестирования.png"))
        number_to_analyze_SHT_label = tk.Label(choice_frame, bg='#FFFFFF')
        number_to_analyze_SHT_label.image = number_to_analyze_SHT_photo  # Сохраняем ссылку на изображение, чтобы оно не удалилось из памяти
        number_to_analyze_SHT_label.configure(image=number_to_analyze_SHT_photo)

        cur_number_analyze = tk.StringVar()
        number_analyze_combobox = ttk.Combobox(choice_frame, textvariable=cur_number_analyze, width=35, font=custom_font)
        number_analyze_combobox.bind('<<ComboboxSelected>>', bind_number_to_analyze)


        def analyze():
            table_frame.grid(row=2, column=0, sticky='wen')
            sorted_table_frame.grid(row=3, column=0, sticky='wen')
            info_frame.grid(row=2, rowspan=2, column=1, sticky='wen', padx=10, pady=10)
            result_frame.grid(row=4, column=0, columnspan=2, sticky='wesn', padx=10, pady=10)

            if cur_analyze.get() == 'Сеанс тестирования':
                ST_id = cur_number_analyze.get()
                ST_id = ST_id[ST_id.find('(') + 1 : ST_id.find(')')]
                marks = get_marks_ST(ST_id)
                data = {}
                tasks = []
                ind = ''
                first_id = marks[0][0]
                num_stud = 0
                task_difficulty = {}

                text_good_stud = ''
                text_bad_stud = ''

                text_result_stud = ''
                text_result_dif = ''

                for mark in marks:
                    if mark[0] != ind:
                        data[mark[0]] = []
                        ind = mark[0]
                        num_stud += 1
                        
                    data[mark[0]].append(round(mark[1], 2))
                    if ind == first_id:
                        tasks.append(mark[2])
                        task_difficulty[mark[2]] = mark[3]
                

                print(data)
                print(tasks)
                print(num_stud)
                
                # Пока не надо. Считаем, что повторов не может быть
                # Переименование ШТЗ, если есть повторы
                # for i in range(len(tasks)):
                #     last_index = len(tasks) - 1 - list(reversed(tasks)).index(tasks[i])
                #     if i != last_index:
                #         new_ind = 1
                #         for j in range(i, last_index + 1):
                #             tasks[j] = f'{str(tasks[j])}.{new_ind}'
                #             new_ind += 1
                
                # print(tasks)
                print(task_difficulty)

                df = pd.DataFrame(data=data, index=tasks)
                df.loc['Xi'] = (df.sum())
                df = df.T
                df.loc['Ri'] = (df.sum())
                df.loc['Ri', 'Xi'] = np.nan
                print(df)


                # Создание таблицы
                for item in tree.get_children():
                    tree.delete(item)
                tree['columns'] = tuple(df.columns)

                # Вертикальный скролл
                vert_scrollbar.pack(side="right", fill="y")
                tree.configure(yscrollcommand=vert_scrollbar.set)

                # Горизонтальный скролл
                horiz_scrollbar.pack(side="bottom", fill="x")
                tree.configure(xscrollcommand=horiz_scrollbar.set)

                # Добавление заголовков столбцов
                tree.column('#0', anchor='c')
                for col in df.columns:
                    tree.column(col, anchor='e')
                tree.heading('#0', text='')
                for col in df.columns:
                    tree.heading(col, text=col)

                # Заполнение таблицы данными из DataFrame с округлением
                for index, row in df.fillna('').iterrows():
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

                print(df['Xi'])
                print(df[df['Xi'] >= len(tasks) * 0.8].index)
                print(df.loc['Ri'][df.loc['Ri'] >= num_stud * 0.8].index)
                
                # Пока считать, что выполнили задание отлично = 80%
                # Рекомендации по студентам, выполнивших все задания
                ind_good_stud = df[df['Xi'] >= len(tasks) * 0.8].index
                if len(ind_good_stud) > 1:
                    text_good_stud = f'Испытуемые {", ".join(ind_good_stud)} успешно выполнили все задания теста. \nТест не дает информации об испытуемых, за исключением того, \nчто для них все задания слишком легкие.'
                    # Расчёт нового Ri
                    for ind in ind_good_stud:
                        row_values = df.loc[ind, :]
                        df.loc['Ri'] = df.loc['Ri'] - row_values
                    
                    # Удаление студентов
                    df = df.drop(ind_good_stud)
                    num_stud -= len(ind_good_stud)
                    
                elif len(ind_good_stud) == 1:
                    text_good_stud = f'Испытуемый {ind_good_stud[0]} успешно выполнил все задания теста. \nТест не дает информации об испытуемом, за исключением того, \nчто для него все задания слишком легкие.'
                    # Расчёт нового Ri
                    row_values = df.loc[ind_bad_stud[0], :]
                    df.loc['Ri'] = df.loc['Ri'] - row_values

                    # Удаление студентов
                    df = df.drop(ind_good_stud)
                    num_stud -= 1
                
                if text_good_stud != '':
                    good_stud_label['text'] = text_good_stud
                    good_stud_label.grid(row=0, column=0, sticky='w')
                

                # Рекомендации по студентам, не выполнивших ни одно задание
                ind_bad_stud = df[df['Xi'] < len(tasks) * 0.6].index
                if len(ind_bad_stud) > 1:
                    text_bad_stud += f'Испытуемые {", ".join(ind_bad_stud)} не прошли ни одно задание теста. \nТест не дает информации об испытуемых, за исключением того, \nчто для них все задания слишком сложные.'
                    # Расчёт нового Ri
                    for ind in ind_bad_stud:
                        row_values = df.loc[ind, :]
                        df.loc['Ri'] = df.loc['Ri'] - row_values

                    # Удаление студентов
                    df = df.drop(ind_bad_stud)
                    num_stud -= len(ind_bad_stud)

                elif len(ind_bad_stud) == 1:
                    text_bad_stud += f'Испытуемый {ind_bad_stud[0]} не прошёл ни одно задание теста. \nТест не дает информации об испытуемом, за исключением того, \nчто для него все задания слишком сложные.'
                    # Расчёт нового Ri
                    row_values = df.loc[ind_bad_stud[0], :]
                    df.loc['Ri'] = df.loc['Ri'] - row_values
                    
                    # Удаление студентов
                    df = df.drop(ind_bad_stud)
                    num_stud -= 1
                    
                if text_bad_stud != '':
                    bad_stud_label['text'] = text_bad_stud
                    bad_stud_label.grid(row=1, column=0, sticky='w')

                
                print(df.loc['Ri'][df.loc['Ri'] >= num_stud * 0.8].index)




                # Вычитание и деление на кол-во студентов
                df.loc['Wj'] = (num_stud - df.loc['Ri'])
                df.loc['pj'] = (df.loc['Ri'] / num_stud)
                df.loc['qj'] = (1 - df.loc['pj'])
                df.loc['pjqj'] = (df.loc['pj'] * df.loc['qj'])

                # Сортировка столбцов по убыванию значений в строке Ri
                df = df.sort_values('Ri', axis=1, ascending=False)
                # Сортировка строк по убыванию значений в столбце Xi
                df = df.sort_values('Xi', ascending=False)

                df = df.fillna('')
                print(df)


                # Создание отсортированной таблицы
                for item in sorted_tree.get_children():
                    sorted_tree.delete(item)
                sorted_tree['columns'] = tuple(df.columns)

                # Вертикальный скролл
                sorted_vert_scrollbar.pack(side="right", fill="y")
                sorted_tree.configure(yscrollcommand=sorted_vert_scrollbar.set)

                # Горизонтальный скролл
                sorted_horiz_scrollbar.pack(side="bottom", fill="x")
                sorted_tree.configure(xscrollcommand=sorted_horiz_scrollbar.set)

                # Добавление заголовков столбцов
                sorted_tree.column('#0', anchor='c')
                for col in df.columns:
                    sorted_tree.column(col, anchor='e')
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


                print(task_difficulty)
                ind_dif = []
                # Если сложность задания не соответсвует действительности, то запоминаем задание
                for task in task_difficulty:
                    print(round(df.loc['qj', task], 2))
                    if round(df.loc['qj', task], 2) > task_difficulty[task] + 0.1 or round(df.loc['qj', task], 2) < task_difficulty[task] - 0.1:
                        ind_dif.append(tuple([task, task_difficulty[task], round(df.loc['qj', task], 2)]))
                    
                print(ind_dif)

                if len(ind_dif) == 1:
                    dif_label['text'] = f'У шаблона тестового задания {ind_dif[0][0]} следует изменить сложность (с {ind_dif[0][1]} на [{round(ind_dif[0][2] - 0.1, 2)}, {round(ind_dif[0][2] + 0.1, 2)}])'
                    dif_label.grid(row=2, column=0, sticky='w')
                elif len(ind_dif) > 1:
                    num_task_list = []
                    dif_task_list = []
                    for ind in ind_dif:
                        num_task_list.append(str(ind[0]))
                        dif_task_list.append(f'(у {ind[0]} с {ind[1]} на [{round(ind[2] - 0.1, 2)}, {round(ind[2] + 0.1, 2)}])')
                    dif_task_text = '\n'.join(dif_task_list)
                    dif_label['text'] = f'У шаблонов тестовых заданий {", ".join(num_task_list)} следует изменить сложность \n {dif_task_text}'
                    dif_label.grid(row=2, column=0, sticky='w')

                # Итог
                result_label.grid(row=0, column=0, sticky='w')

                res_list = []
                for ind in ind_good_stud:
                    stud = get_stud(ind)
                    res_list.append(f'испытуемого {ind} {stud[0][0]} {stud[0][1]} ({stud[0][2]})')
                for ind in ind_bad_stud:
                    stud = get_stud(ind)
                    res_list.append(f'испытуемого {ind} {stud[0][0]} {stud[0][1]} ({stud[0][2]})')
                
                
                print(res_list)    
                text_result_stud = '\n'.join(res_list)

                # Добавить проверку на задания
                if text_result_stud != '':
                    reconsider_label.grid(row=1, column=0, sticky='w')
                    result_stud_label['text'] = text_result_stud
                    result_stud_label.grid(row=2, column=0, sticky='w')
                
                res_list = []
                for ind in ind_dif:
                    res_list.append(f'шаблон тестового задания {ind[0]}')

                text_result_dif = '\n'.join(res_list)

                if text_result_dif != '':
                    reconsider_label.grid(row=1, column=0, sticky='w')
                    result_dif_label['text'] = text_result_dif
                    result_dif_label.grid(row=3, column=0, sticky='w')


            elif cur_analyze.get() == 'Шаблон тестирования':
                pass


        # Загрузка изображения и присвоение к analyze_label
        analyze_photo = ImageTk.PhotoImage(Image.open("Кнопки/Анализировать.png"))
        analyze_label = tk.Label(choice_frame, bg='#FFFFFF')
        analyze_label.image = analyze_photo  # Сохраняем ссылку на изображение, чтобы оно не удалилось из памяти
        analyze_label.configure(image=analyze_photo)

        # Привязываем событие нажатия на картинку к вызову analyze
        analyze_label.bind('<Button-1>', lambda event: analyze())


        # Очистка всех виджетов
        def del_all():
            reset_number_to_analyze()
            reset_all()

            cur_analyze.set('')


        # Загрузка изображения и присвоение к del_label
        del_photo = ImageTk.PhotoImage(Image.open("Кнопки/Очистить.png"))
        del_label = tk.Label(choice_frame, bg='#FFFFFF')
        del_label.image = del_photo  # Сохраняем ссылку на изображение, чтобы оно не удалилось из памяти
        del_label.configure(image=del_photo)
        del_label.grid(row=2, column=1, sticky='w', padx=10, pady=5)

        # Привязываем событие нажатия на картинку к вызову del_all
        del_label.bind('<Button-1>', lambda event: del_all())