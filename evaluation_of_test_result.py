import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

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

        tk.Label(info_frame, text='СТ - СЕАНС ТЕСТИРОВАНИЯ \nШТ - ШАБЛОН ТЕСТА', bg='#D9D9D9').grid(row=0, column=0, sticky='w')

        def reset_group_year_vars():
            group_var.set(const_group_var)
            year_var.set(const_year_var)
            group_selected_var.set([])
            year_selected_var.set([])

        # После выбора что выводить выводиться следующий виджет
        def bind_what_to_draw(event):
            number_to_analyze_label.grid_forget()
            number_analyze_combobox.grid_forget()
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
            view_label.grid_forget()
            view_combobox.grid_forget()
            btn_analyze.grid_forget()

            cur_analyze.set('')
            cur_view.set('')
            reset_group_year_vars()

            what_to_analyze_label.grid(row=2, column=0, sticky='w')
            analyze_combobox.grid(row=3, column=0, columnspan=2, sticky='w')


        what_to_draw_label = tk.Label(choice_frame, text='Что вывести')
        what_to_draw_label.grid(row=0, column=0, sticky='w')

        cur_draw = tk.StringVar()
        draw_values = ['% УСПЕШНО ПРОЙДЕННЫХ ПО ОДНОМУ СТ/ШТ', '% УСПЕШНО ПРОЙДЕННЫХ ПО НЕСКОЛЬКИМ СТ/ШТ', 'СРЕДНЯЯ ОЦЕНКА ПО ОДНОМУ СТ/ШТ', 'СРЕДНЯЯ ОЦЕНКА ПО НЕСКОЛЬКИМ СТ/ШТ', 'КОЛ-ВО ОЦЕНОК ПО ОДНОМУ СТ/ШТ', 'КОЛ-ВО ОЦЕНОК ПО НЕСКОЛЬКИМ СТ/ШТ']
        draw_combobox = ttk.Combobox(choice_frame, textvariable=cur_draw, width=52, values=draw_values)
        draw_combobox.grid(row=1, column=0, columnspan=2, sticky='w')
        draw_combobox.bind('<<ComboboxSelected>>', bind_what_to_draw)


        # После выбора что анализировать выводиться следующий виджет
        def bind_what_to_analyze(event):
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
            view_label.grid_forget()
            view_combobox.grid_forget()
            btn_analyze.grid_forget()

            cur_number_analyze.set('')
            cur_view.set('')
            reset_group_year_vars()

            number_to_analyze_label.grid(row=4, column=0, sticky='w')
            number_analyze_combobox.grid(row=5, column=0, columnspan=2, sticky='w')


        what_to_analyze_label = tk.Label(choice_frame, text='Что анализировать')

        cur_analyze = tk.StringVar()
        analyze_combobox = ttk.Combobox(choice_frame, textvariable=cur_analyze, width=30)
        analyze_combobox['values'] = ['СТ', 'ШТ']
        analyze_combobox.bind('<<ComboboxSelected>>', bind_what_to_analyze)


        # После выбора какой ст/шт анализировать выводиться следующий виджет
        def bind_number_to_analyze(event):
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
            view_label.grid_forget()
            view_combobox.grid_forget()
            btn_analyze.grid_forget()

            cur_view.set('')
            reset_group_year_vars()
            
            who_to_analyze_label.grid(row=6, column=0, sticky='w')
            btn_group.grid(row=7, column=0, sticky='w')
            btn_year.grid(row=7, column=1, sticky='w')


        number_to_analyze_label = tk.Label(choice_frame, text='Какой СТ/ШТ анализировать')

        cur_number_analyze = tk.StringVar()
        number_analyze_combobox = ttk.Combobox(choice_frame, textvariable=cur_number_analyze, width=30)
        # Данные как пример. Позже необходимо брать из бд
        number_analyze_combobox['values'] = ['1', '2', '3']
        number_analyze_combobox.bind('<<ComboboxSelected>>', bind_number_to_analyze)


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
            view_label.grid_forget()
            view_combobox.grid_forget()
            btn_analyze.grid_forget()

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
            view_label.grid_forget()
            view_combobox.grid_forget()
            btn_analyze.grid_forget()

            cur_view.set('')
            reset_group_year_vars()
            
            if cur_analyze.get() == 'СТ':
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


        # Добавить выбор группы/годов
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
        # Данные как пример. Позже необходимо брать из бд
        group_var = tk.Variable(value=const_group_var)
        year_var = tk.Variable(value=const_year_var)

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


        # Скрыть выбор вида анализа
        def hide_view():
            view_label.grid_forget()
            view_combobox.grid_forget()
            btn_analyze.grid_forget()
        
        # Показать выбор вида анализа
        def show_view():
            hide_view()
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
            for i in select:
                group_selected_listbox.insert(tk.END, group_listbox.get(i))
                group_listbox.delete(i)

            # Если не выбран ни одна группа, то скрываем выбор вида анализа
            if len(group_selected_var.get()) == 0:
                hide_view()
            else:
                show_view()

        # Удаление из listbox выбранных групп
        def del_selected_group():
            select = list(group_selected_listbox.curselection())
            select.reverse()
            for i in select:
                group_listbox.insert(tk.END, group_selected_listbox.get(i))
                group_selected_listbox.delete(i)

            # Если не выбран ни одна группа, то скрываем выбор вида анализа
            if len(group_selected_var.get()) == 0:
                hide_view()
            else:
                show_view()


        # Добавление в listbox выбранных годов
        def add_selected_year():
            select = list(year_listbox.curselection())
            select.reverse()
            for i in select:
                year_selected_listbox.insert(tk.END, year_listbox.get(i))
                year_listbox.delete(i)

            # Если не выбран ни один год, то скрываем выбор вида анализа
            if len(year_selected_var.get()) == 0:
                hide_view()
            else:
                show_view()

        # Удаление из listbox выбранных годов
        def del_selected_year():
            select = list(year_selected_listbox.curselection())
            select.reverse()
            for i in select:
                year_listbox.insert(tk.END, year_selected_listbox.get(i))
                year_selected_listbox.delete(i)

            # Если не выбран ни один год, то скрываем выбор вида анализа
            if len(year_selected_var.get()) == 0:
                hide_view()
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

        btn_analyze = tk.Button(choice_frame, text='Показать')


        def del_all():
            what_to_analyze_label.grid_forget()
            analyze_combobox.grid_forget()
            number_to_analyze_label.grid_forget()
            number_analyze_combobox.grid_forget()
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
            view_label.grid_forget()
            view_combobox.grid_forget()
            btn_analyze.grid_forget()

            cur_draw.set('')
            cur_view.set('')
            reset_group_year_vars()


        btn_del_all = tk.Button(choice_frame, text='Очистить', command=del_all)
        btn_del_all.grid(row=11, column=2, padx=5, pady=5)