import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

from vars import *
from get_data_from_db import *
from display_graphs import *

class EvaluationOfTestResult(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_evaluation_of_test_result()
    
    def init_evaluation_of_test_result(self):
        self.title('Оценка результатов тестируемых')
        self.geometry('650x500+350+250')
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

        # Сброс переменных для выбора групп и годов
        def reset_group_year_vars():
            group_var.set([])
            year_var.set([])
            group_selected_var.set([])
            year_selected_var.set([])
        
        # Сброс переменных для выбора СТ и ШТ
        def reset_ST_SHT_vars():
            ST_var.set([])
            SHT_var.set([])
            ST_selected_var.set([])
            SHT_selected_var.set([])

        # Сокрытие виджетов для выбора какие СТ/ШТ анализировать
        def del_number_to_analyze():
            number_to_analyze_ST_label.grid_forget()
            number_to_analyze_SHT_label.grid_forget()
            number_to_analyze_combobox.grid_forget()
            number_to_analyze_frame.grid_forget()
            ST_label.grid_forget()
            frame_number_listbox.grid_forget()
            btn_add_ST.grid_forget()
            btn_del_ST.grid_forget()
            ST_selected_label.grid_forget()
            frame_selected_number_listbox.grid_forget()
            SHT_label.grid_forget()
            btn_add_SHT.grid_forget()
            btn_del_SHT.grid_forget()
            SHT_selected_label.grid_forget()
        
        # Сокрытие виджетов для выбора какие группы/года анализировать
        def del_who_to_analyze():
            who_to_analyze_label.grid_forget()
            btn_group.grid_forget()
            btn_year.grid_forget()
            who_to_analyze_frame.grid_forget()
            group_label.grid_forget()
            year_label.grid_forget()
            frame_listbox.grid_forget()
            group_selected_label.grid_forget()
            year_selected_label.grid_forget()
            frame_selected_listbox.grid_forget()
            btn_add_group.grid_forget()
            btn_del_group.grid_forget()
            btn_add_year.grid_forget()
            btn_del_year.grid_forget()
        
        # Сокрытие виджетов для выбора вида и кнопки Показать
        def del_view():
            view_label.grid_forget()
            view_combobox.grid_forget()
            btn_analyze.grid_forget()


        # После выбора что выводить выводится следующий виджет
        def bind_what_to_draw(event):
            del_number_to_analyze()
            del_who_to_analyze()
            del_view()

            cur_analyze.set('')
            cur_view.set('')
            reset_group_year_vars()
            reset_ST_SHT_vars()

            what_to_analyze_label.grid(row=2, column=0, sticky='w')
            analyze_combobox.grid(row=3, column=0, columnspan=2, sticky='w')


        what_to_draw_label = tk.Label(choice_frame, text='Что вывести')
        what_to_draw_label.grid(row=0, column=0, sticky='w')

        cur_draw = tk.StringVar()
        draw_values = ['% УСПЕШНО ПРОЙДЕННЫХ ПО ОДНОМУ СТ/ШТ', '% УСПЕШНО ПРОЙДЕННЫХ ПО НЕСКОЛЬКИМ СТ/ШТ', 'СРЕДНЯЯ ОЦЕНКА ПО ОДНОМУ СТ/ШТ', 'СРЕДНЯЯ ОЦЕНКА ПО НЕСКОЛЬКИМ СТ/ШТ', 'КОЛ-ВО ОЦЕНОК ПО ОДНОМУ СТ/ШТ']
        draw_combobox = ttk.Combobox(choice_frame, textvariable=cur_draw, width=52, values=draw_values)
        draw_combobox.grid(row=1, column=0, columnspan=2, sticky='w')
        draw_combobox.bind('<<ComboboxSelected>>', bind_what_to_draw)


        # После выбора что анализировать выводится следующий виджет
        def bind_what_to_analyze(event):
            del_who_to_analyze()
            del_view()

            cur_number_analyze.set('')
            cur_view.set('')
            reset_group_year_vars()
            reset_ST_SHT_vars()

            if 'ОДНОМУ' in cur_draw.get():
                number_to_analyze_frame.grid_forget()
                number_to_analyze_ST_label.grid_forget()
                number_to_analyze_SHT_label.grid_forget()

                number_to_analyze_combobox.grid(row=5, column=0, columnspan=2, sticky='w')

                # Заполнение данными в зависимости от выбора, что анализировать
                if cur_analyze.get() == 'СЕАНС ТЕСТИРОВАНИЯ':
                    number_to_analyze_ST_label.grid(row=4, column=0, sticky='w')
                    number_to_analyze_combobox['values'] = get_ST()

                elif cur_analyze.get() == 'ШАБЛОН ТЕСТИРОВАНИЯ':
                    number_to_analyze_SHT_label.grid(row=4, column=0, sticky='w')
                    number_to_analyze_combobox['values'] = get_SHT()
                

            elif 'НЕСКОЛЬКИМ' in cur_draw.get():
                number_to_analyze_ST_label.grid_forget()
                number_to_analyze_SHT_label.grid_forget()
                number_to_analyze_combobox.grid_forget()

                number_to_analyze_frame.grid(row=4, column=0, sticky='w')

                if cur_analyze.get() == 'СЕАНС ТЕСТИРОВАНИЯ':
                    SHT_label.grid_forget()
                    SHT_listbox.pack_forget()
                    frame_number_listbox.grid_forget()
                    btn_add_SHT.grid_forget()
                    btn_del_SHT.grid_forget()
                    SHT_selected_label.grid_forget()
                    SHT_selected_listbox.pack_forget()
                    frame_selected_number_listbox.grid_forget()

                    ST_var.set(get_ST())
                    
                    ST_label.grid(row=0, column=0, sticky='w')
                    frame_number_listbox.grid(row=1, rowspan=2, column=0, sticky='w')
                    ST_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
                    scroll_number.config(command=ST_listbox.yview)
                    scroll_number.pack(side=tk.RIGHT, fill=tk.Y)

                    btn_add_ST.grid(row=1, column=1, sticky='w', padx=5)
                    btn_del_ST.grid(row=2, column=1, sticky='w', padx=5)

                    ST_selected_label.grid(row=0, column=2, sticky='w')
                    frame_selected_number_listbox.grid(row=1, rowspan=2, column=2, sticky='w')
                    ST_selected_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
                    scroll_number_selected.config(command=ST_selected_listbox.yview)
                    scroll_number_selected.pack(side=tk.RIGHT, fill=tk.Y)
                
                elif cur_analyze.get() == 'ШАБЛОН ТЕСТИРОВАНИЯ':
                    ST_label.grid_forget()
                    ST_listbox.pack_forget()
                    frame_number_listbox.grid_forget()
                    btn_add_ST.grid_forget()
                    btn_del_ST.grid_forget()
                    ST_selected_label.grid_forget()
                    ST_selected_listbox.pack_forget()
                    frame_selected_number_listbox.grid_forget()

                    SHT_var.set(get_SHT())

                    SHT_label.grid(row=0, column=0, sticky='w')
                    frame_number_listbox.grid(row=1, rowspan=2, column=0, sticky='w')
                    SHT_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
                    scroll_number.config(command=SHT_listbox.yview)
                    scroll_number.pack(side=tk.RIGHT, fill=tk.Y)

                    btn_add_SHT.grid(row=1, column=1, sticky='w', padx=5)
                    btn_del_SHT.grid(row=2, column=1, sticky='w', padx=5)

                    SHT_selected_label.grid(row=0, column=2, sticky='w')
                    frame_selected_number_listbox.grid(row=1, rowspan=2, column=2, sticky='w')
                    SHT_selected_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
                    scroll_number_selected.config(command=SHT_selected_listbox.yview)
                    scroll_number_selected.pack(side=tk.RIGHT, fill=tk.Y)


        what_to_analyze_label = tk.Label(choice_frame, text='Что анализировать')

        cur_analyze = tk.StringVar()
        analyze_combobox = ttk.Combobox(choice_frame, textvariable=cur_analyze, width=30)
        analyze_combobox['values'] = ['СЕАНС ТЕСТИРОВАНИЯ', 'ШАБЛОН ТЕСТИРОВАНИЯ']
        analyze_combobox.bind('<<ComboboxSelected>>', bind_what_to_analyze)


        # После выбора какой ст/шт анализировать выводится следующий виджет
        def bind_number_to_analyze(event):
            del_who_to_analyze()
            del_view()

            cur_view.set('')
            reset_group_year_vars()
            reset_ST_SHT_vars()
            
            who_to_analyze_label.grid(row=6, column=0, sticky='w')
            btn_group.grid(row=7, column=0, sticky='w')
            btn_year.grid(row=7, column=1, sticky='w')


        number_to_analyze_ST_label  = tk.Label(choice_frame, text='Выберите СТ')
        number_to_analyze_SHT_label  = tk.Label(choice_frame, text='Выберите ШТ')

        cur_number_analyze = tk.StringVar()
        number_to_analyze_combobox = ttk.Combobox(choice_frame, textvariable=cur_number_analyze, width=30)
        number_to_analyze_combobox.bind('<<ComboboxSelected>>', bind_number_to_analyze)

        # Фрэйм для красивого вывода при выборе нескольких СТ/ШТ
        number_to_analyze_frame = tk.Frame(choice_frame)
        number_to_analyze_frame.columnconfigure(0, weight=1)
        number_to_analyze_frame.columnconfigure(2, weight=1)

        ST_label = tk.Label(number_to_analyze_frame, text='Выберите СТ')
        SHT_label = tk.Label(number_to_analyze_frame, text='Выберите ШТ')

        ST_var = tk.Variable()
        SHT_var = tk.Variable()

        # Фрэймы для вывода listbox с scrollbar
        frame_number_listbox = tk.Frame(number_to_analyze_frame)
        frame_number_listbox.columnconfigure(0, weight=1)
        scroll_number = tk.Scrollbar(frame_number_listbox, orient=tk.VERTICAL)
        
        frame_selected_number_listbox = tk.Frame(number_to_analyze_frame)
        frame_selected_number_listbox.columnconfigure(0, weight=1)
        scroll_number_selected = tk.Scrollbar(frame_selected_number_listbox, orient=tk.VERTICAL)

        # listbox для выбора СТ
        ST_listbox = tk.Listbox(frame_number_listbox, listvariable=ST_var, selectmode=tk.EXTENDED, height=5)
        ST_listbox.config(yscrollcommand=scroll_number.set)

        # listbox для выбранных СТ
        ST_selected_label = tk.Label(number_to_analyze_frame, text='Выбранные СТ')
        ST_selected_var = tk.Variable(value=[])
        ST_selected_listbox = tk.Listbox(frame_selected_number_listbox, listvariable=ST_selected_var, selectmode=tk.EXTENDED, height=5)
        ST_selected_listbox.config(yscrollcommand=scroll_number_selected.set)

        # listbox для выбора ШТ
        SHT_listbox = tk.Listbox(frame_number_listbox, listvariable=SHT_var, selectmode=tk.EXTENDED, height=5)
        SHT_listbox.config(yscrollcommand=scroll_number.set)

        # listbox для выбранных ШТ
        SHT_selected_label = tk.Label(number_to_analyze_frame, text='Выбранные ШТ')
        SHT_selected_var = tk.Variable(value=[])
        SHT_selected_listbox = tk.Listbox(frame_selected_number_listbox, listvariable=SHT_selected_var, selectmode=tk.EXTENDED, height=5)
        SHT_selected_listbox.config(yscrollcommand=scroll_number_selected.set)


        # Показать выбор кого анализировать
        def show_who_to_analyze():
            del_who_to_analyze()
            del_view()

            cur_view.set('')
            reset_group_year_vars()
            
            who_to_analyze_label.grid(row=6, column=0, sticky='w')
            btn_group.grid(row=7, column=0, sticky='w')
            btn_year.grid(row=7, column=1, sticky='w')


        # Добавление в listbox выбранных СТ
        def add_selected_ST():
            select = list(ST_listbox.curselection())
            select.reverse()
            # ST_list необходим для упорядоченного вывода СТ
            ST_list = list(ST_selected_var.get())
            for i in select:
                ST_list.append(ST_listbox.get(i))
                ST_listbox.delete(i)

            ST_selected_listbox.delete(0, tk.END)
            for ST in sorted(ST_list):
                ST_selected_listbox.insert(tk.END, ST)

            # Если не выбран ни один СТ, то скрываем выбор кого анализировать
            if len(ST_selected_var.get()) == 0:
                del_who_to_analyze()
                del_view()
                cur_view.set('')
                reset_group_year_vars()
            else:
                show_who_to_analyze()

        # Удаление из listbox выбранных СТ
        def del_selected_ST():
            select = list(ST_selected_listbox.curselection())
            select.reverse()
            # ST_list необходим для упорядоченного вывода СТ
            ST_list = list(ST_var.get())
            for i in select:
                ST_list.append(ST_selected_listbox.get(i))
                ST_selected_listbox.delete(i)

            ST_listbox.delete(0, tk.END)
            for ST in sorted(ST_list):
                ST_listbox.insert(tk.END, ST)

            # Если не выбран ни один СТ, то скрываем выбор кого анализировать
            if len(ST_selected_var.get()) == 0:
                del_who_to_analyze()
                del_view()
                cur_view.set('')
                reset_group_year_vars()
            else:
                show_who_to_analyze()


        # Добавление в listbox выбранных ШТ
        def add_selected_SHT():
            select = list(SHT_listbox.curselection())
            select.reverse()

            # SHT_list необходим для упорядоченного вывода ШТ
            SHT_list = list(SHT_selected_var.get())
            for i in select:
                SHT_list.append(SHT_listbox.get(i))
                SHT_listbox.delete(i)

            SHT_selected_listbox.delete(0, tk.END)
            for SHT in sorted(SHT_list):
                SHT_selected_listbox.insert(tk.END, SHT)

            # Если не выбран ни один ШТ, то скрываем выбор кого анализировать
            if len(SHT_selected_var.get()) == 0:
                del_who_to_analyze()
                del_view()
                cur_view.set('')
                reset_group_year_vars()
            else:
                show_who_to_analyze()

        # Удаление из listbox выбранных ШТ
        def del_selected_SHT():
            select = list(SHT_selected_listbox.curselection())
            select.reverse()

            # SHT_list необходим для упорядоченного вывода ШТ
            SHT_list = list(SHT_var.get())
            for i in select:
                SHT_list.append(SHT_selected_listbox.get(i))
                SHT_selected_listbox.delete(i)

            SHT_listbox.delete(0, tk.END)
            for SHT in sorted(SHT_list):
                SHT_listbox.insert(tk.END, SHT)

            # Если не выбран ни один ШТ, то скрываем выбор кого анализировать
            if len(SHT_selected_var.get()) == 0:
                del_who_to_analyze()
                del_view()
                cur_view.set('')
                reset_group_year_vars()
            else:
                show_who_to_analyze()


        # Кнопки для выбора СТ
        btn_add_ST = tk.Button(number_to_analyze_frame, text='>>', command=add_selected_ST)
        btn_del_ST = tk.Button(number_to_analyze_frame, text='<<', command=del_selected_ST)
        # Кнопки для выбора ШТ
        btn_add_SHT = tk.Button(number_to_analyze_frame, text='>>', command=add_selected_SHT)
        btn_del_SHT = tk.Button(number_to_analyze_frame, text='<<', command=del_selected_SHT)


        # Если выбраны группы
        def select_group():
            year_label.grid_forget()
            year_listbox.pack_forget()
            frame_listbox.grid_forget()
            year_selected_label.grid_forget()
            year_selected_listbox.pack_forget()
            frame_selected_listbox.grid_forget()
            btn_add_group.grid_forget()
            btn_del_group.grid_forget()
            btn_add_year.grid_forget()
            btn_del_year.grid_forget()

            del_view()

            cur_view.set('')
            reset_group_year_vars()

            who_to_analyze_frame.grid(row=8, column=0, columnspan=2, sticky='w')

            group_label.grid(row=0, column=0, sticky='w')
            frame_listbox.grid(row=1, rowspan=2, column=0, sticky='w')
            group_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
            scroll.config(command=group_listbox.yview)
            scroll.pack(side=tk.RIGHT, fill=tk.Y)

            btn_add_group.grid(row=1, column=1, sticky='w', padx=5)
            btn_del_group.grid(row=2, column=1, sticky='w', padx=5)

            group_selected_label.grid(row=0, column=2, sticky='w')
            frame_selected_listbox.grid(row=1, rowspan=2, column=2, sticky='w')
            group_selected_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
            scroll_selected.config(command=group_selected_listbox.yview)
            scroll_selected.pack(side=tk.RIGHT, fill=tk.Y)

            if 'ОДНОМУ' in cur_draw.get():
                # Заполнение данными в зависимости от выбора, что анализировать
                if cur_analyze.get() == 'СЕАНС ТЕСТИРОВАНИЯ':
                    # Вызов метода по получению групп из бд, которые проходили СТ. Передаётся название СТ
                    group_var.set(get_groups_ST(cur_number_analyze.get()))
                elif cur_analyze.get() == 'ШАБЛОН ТЕСТИРОВАНИЯ':
                    # Вызов метода по получению групп из бд, которые проходили ШТ. Передаётся номер ШТ
                    group_var.set(get_groups_SHT(cur_number_analyze.get()))
            
            elif 'НЕСКОЛЬКИМ' in cur_draw.get():
                if cur_analyze.get() == 'СЕАНС ТЕСТИРОВАНИЯ':
                    group_var.set(get_groups_ST(ST_selected_var.get()))
                elif cur_analyze.get() == 'ШАБЛОН ТЕСТИРОВАНИЯ':
                    group_var.set(get_groups_SHT(SHT_selected_var.get()))

        # Если выбраны года
        def select_year():
            group_label.grid_forget()
            group_listbox.pack_forget()
            frame_listbox.grid_forget()
            group_selected_label.grid_forget()
            group_selected_listbox.pack_forget()
            frame_selected_listbox.grid_forget()
            btn_add_group.grid_forget()
            btn_del_group.grid_forget()
            btn_add_year.grid_forget()
            btn_del_year.grid_forget()

            del_view()

            cur_view.set('')
            reset_group_year_vars()
            
            if cur_analyze.get() == 'СЕАНС ТЕСТИРОВАНИЯ':
                who_to_analyze_frame.grid_forget()
                showerror(parent=self, title='Ошибка', message='Выбрать года можно только для ШТ')
            else:
                who_to_analyze_frame.grid(row=8, column=0, columnspan=2, sticky='w')

                year_label.grid(row=0, column=0, sticky='w')
                frame_listbox.grid(row=1, rowspan=2, column=0, sticky='w')
                year_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
                scroll.config(command=year_listbox.yview)
                scroll.pack(side=tk.RIGHT, fill=tk.Y)

                btn_add_year.grid(row=1, column=1, sticky='w', padx=5)
                btn_del_year.grid(row=2, column=1, sticky='w', padx=5)

                year_selected_label.grid(row=0, column=2, sticky='w')
                frame_selected_listbox.grid(row=1, rowspan=2, column=2, sticky='w')
                year_selected_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
                scroll_selected.config(command=year_selected_listbox.yview)
                scroll_selected.pack(side=tk.RIGHT, fill=tk.Y)

                if 'ОДНОМУ' in cur_draw.get():
                    # Вызов метода по получению годов из бд, в которые проходили ШТ. Передаётся номер ШТ
                    year_var.set(get_years_SHT(cur_number_analyze.get()))
                
                elif 'НЕСКОЛЬКИМ' in cur_draw.get():
                    year_var.set(get_years_SHT(SHT_selected_var.get()))


        who_to_analyze_label = tk.Label(choice_frame, text='Кого анализировать')
        
        selected_who_to_analyze = tk.StringVar()
        btn_group = tk.Radiobutton(choice_frame, text='Группы', value='Группы', variable=selected_who_to_analyze, command=select_group)
        btn_year = tk.Radiobutton(choice_frame, text='Года', value='Года', variable=selected_who_to_analyze, command=select_year)

        # Фрэйм для красивого вывода
        who_to_analyze_frame = tk.Frame(choice_frame)
        who_to_analyze_frame.columnconfigure(0, weight=1)
        who_to_analyze_frame.columnconfigure(2, weight=1)

        group_label = tk.Label(who_to_analyze_frame, text='Выберите группы')
        year_label = tk.Label(who_to_analyze_frame, text='Выберите года')

        group_var = tk.Variable()
        year_var = tk.Variable()

        # Фрэймы для вывода listbox с scrollbar
        frame_listbox = tk.Frame(who_to_analyze_frame)
        frame_listbox.columnconfigure(0, weight=1)
        scroll = tk.Scrollbar(frame_listbox, orient=tk.VERTICAL)
        
        frame_selected_listbox = tk.Frame(who_to_analyze_frame)
        frame_selected_listbox.columnconfigure(0, weight=1)
        scroll_selected = tk.Scrollbar(frame_selected_listbox, orient=tk.VERTICAL)

        # listbox для выбора групп
        group_listbox = tk.Listbox(frame_listbox, listvariable=group_var, selectmode=tk.EXTENDED, height=5)
        group_listbox.config(yscrollcommand=scroll.set)

        # listbox для выбранных групп
        group_selected_label = tk.Label(who_to_analyze_frame, text='Выбранные группы')
        group_selected_var = tk.Variable(value=[])
        group_selected_listbox = tk.Listbox(frame_selected_listbox, listvariable=group_selected_var, selectmode=tk.EXTENDED, height=5)
        group_selected_listbox.config(yscrollcommand=scroll.set)

        # listbox для выбора годов
        year_listbox = tk.Listbox(frame_listbox, listvariable=year_var, selectmode=tk.EXTENDED, height=5)
        year_listbox.config(yscrollcommand=scroll.set)

        # listbox для выбранных годов
        year_selected_label = tk.Label(who_to_analyze_frame, text='Выбранные года')
        year_selected_var = tk.Variable(value=[])
        year_selected_listbox = tk.Listbox(frame_selected_listbox, listvariable=year_selected_var, selectmode=tk.EXTENDED, height=5)
        year_selected_listbox.config(yscrollcommand=scroll.set)
        
        # Показать выбор вида анализа
        def show_view():
            del_view()
            view_label.grid(row=9, column=0, sticky='w')
            if 'НЕСКОЛЬКИМ' in cur_draw.get() and 'ТАБЛИЦА' not in values_view_combobox:
                values_view_combobox.append('ТАБЛИЦА')
            elif 'ОДНОМУ' in cur_draw.get() and 'ТАБЛИЦА' in values_view_combobox:
                values_view_combobox.remove('ТАБЛИЦА')

            view_combobox['values'] = values_view_combobox
            view_combobox.grid(row=10, column=0, sticky='w')
            btn_analyze.grid(row=11, column=0, sticky='w', pady=5)


        # Добавление в listbox выбранных групп
        def add_selected_group():
            select = list(group_listbox.curselection())
            select.reverse()
            
            # group_list необходим для упорядоченного вывода групп
            group_list = list(group_selected_var.get())
            for i in select:
                group_list.append(group_listbox.get(i))
                group_listbox.delete(i)

            group_selected_listbox.delete(0, tk.END)
            for group in sorted(group_list):
                group_selected_listbox.insert(tk.END, group)

            # Если не выбран ни одна группа, то скрываем выбор вида анализа
            if len(group_selected_var.get()) == 0:
                del_view()
            else:
                show_view()

        # Удаление из listbox выбранных групп
        def del_selected_group():
            select = list(group_selected_listbox.curselection())
            select.reverse()
            
            # group_list необходим для упорядоченного вывода групп
            group_list = list(group_var.get())
            for i in select:
                group_list.append(group_selected_listbox.get(i))
                group_selected_listbox.delete(i)

            group_listbox.delete(0, tk.END)
            for group in sorted(group_list):
                group_listbox.insert(tk.END, group)

            # Если не выбран ни одна группа, то скрываем выбор вида анализа
            if len(group_selected_var.get()) == 0:
                del_view()
            else:
                show_view()


        # Добавление в listbox выбранных годов
        def add_selected_year():
            select = list(year_listbox.curselection())
            select.reverse()
            
            # year_list необходим для упорядоченного вывода групп
            year_list = list(year_selected_var.get())
            for i in select:
                year_list.append(year_listbox.get(i))
                year_listbox.delete(i)

            year_selected_listbox.delete(0, tk.END)
            for year in sorted(year_list):
                year_selected_listbox.insert(tk.END, year)

            # Если не выбран ни один год, то скрываем выбор вида анализа
            if len(year_selected_var.get()) == 0:
                del_view()
            else:
                show_view()

        # Удаление из listbox выбранных годов
        def del_selected_year():
            select = list(year_selected_listbox.curselection())
            select.reverse()
            
            # year_list необходим для упорядоченного вывода групп
            year_list = list(year_var.get())
            for i in select:
                year_list.append(year_selected_listbox.get(i))
                year_selected_listbox.delete(i)

            year_listbox.delete(0, tk.END)
            for year in sorted(year_list):
                year_listbox.insert(tk.END, year)

            # Если не выбран ни один год, то скрываем выбор вида анализа
            if len(year_selected_var.get()) == 0:
                del_view()
            else:
                show_view()


        # Кнопки для выбора групп
        btn_add_group = tk.Button(who_to_analyze_frame, text='>>', command=add_selected_group)
        btn_del_group = tk.Button(who_to_analyze_frame, text='<<', command=del_selected_group)
        # Кнопки для выбора годов
        btn_add_year = tk.Button(who_to_analyze_frame, text='>>', command=add_selected_year)
        btn_del_year = tk.Button(who_to_analyze_frame, text='<<', command=del_selected_year)
        
        view_label = tk.Label(choice_frame, text='Вид')
        cur_view = tk.StringVar()
        values_view_combobox = ['ГРАФИК', 'ДИАГРАММА']
        view_combobox = ttk.Combobox(choice_frame, textvariable=cur_view, width=30)


        def get_params_to_display(is_one):
            if cur_analyze.get() == 'СЕАНС ТЕСТИРОВАНИЯ':
                is_ST = True
                is_group = True
                if is_one:
                    marks = get_marks_groups_one_ST(cur_number_analyze.get(), group_selected_var.get())
                else:
                    marks = get_marks_groups_many_ST(ST_selected_var.get(), group_selected_var.get())
            
            elif cur_analyze.get() == 'ШАБЛОН ТЕСТИРОВАНИЯ':
                is_ST = False
                if selected_who_to_analyze.get() == 'Группы':
                    is_group = True
                    if is_one:
                        marks = get_marks_groups_one_SHT(cur_number_analyze.get(), group_selected_var.get())
                    else:
                        marks = get_marks_groups_many_SHT(SHT_selected_var.get(), group_selected_var.get())

                elif selected_who_to_analyze.get() == 'Года':
                    is_group = False
                    if is_one:
                        marks = get_marks_years_one_SHT(cur_number_analyze.get(), year_selected_var.get())
                    else:
                        marks = get_marks_years_many_SHT(SHT_selected_var.get(), year_selected_var.get())

            return marks, is_ST, is_group

        def display_graphs():
            match cur_draw.get():
                case '% УСПЕШНО ПРОЙДЕННЫХ ПО ОДНОМУ СТ/ШТ':
                    marks, is_ST, is_group = get_params_to_display(True)
                    is_graph = True if cur_view.get() == 'ГРАФИК' else False
                    passed_one_st(cur_number_analyze.get(), marks, is_ST, is_group, is_graph)

                case '% УСПЕШНО ПРОЙДЕННЫХ ПО НЕСКОЛЬКИМ СТ/ШТ':
                    marks, is_ST, is_group = get_params_to_display(False)
                    passed_many_st(marks, is_ST, is_group, cur_view.get())

                case 'СРЕДНЯЯ ОЦЕНКА ПО ОДНОМУ СТ/ШТ':
                    marks, is_ST, is_group = get_params_to_display(True)
                    is_graph = True if cur_view.get() == 'ГРАФИК' else False
                    avg_score_one_st(cur_number_analyze.get(), marks, is_ST, is_group, is_graph)
                    
                case 'СРЕДНЯЯ ОЦЕНКА ПО НЕСКОЛЬКИМ СТ/ШТ':
                    marks, is_ST, is_group = get_params_to_display(False)
                    avg_score_many_st(marks, is_ST, is_group, cur_view.get())
                    
                case 'КОЛ-ВО ОЦЕНОК ПО ОДНОМУ СТ/ШТ':
                    marks, is_ST, is_group = get_params_to_display(True)
                    is_graph = True if cur_view.get() == 'ГРАФИК' else False
                    count_score_one_st(cur_number_analyze.get(), marks, is_ST, is_group, is_graph)


        btn_analyze = tk.Button(choice_frame, text='Показать', command=display_graphs)


        # Очистка всех виджетов
        def del_all():
            what_to_analyze_label.grid_forget()
            analyze_combobox.grid_forget()

            del_number_to_analyze()
            del_who_to_analyze()
            del_view()

            cur_draw.set('')
            cur_view.set('')
            reset_group_year_vars()


        btn_del_all = tk.Button(choice_frame, text='Очистить', command=del_all)
        btn_del_all.grid(row=11, column=2, padx=5, pady=5)