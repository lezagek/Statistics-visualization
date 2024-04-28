import tkinter as tk
from tkinter import ttk
import sqlite3

from vars import *

from evaluation_of_test_result import EvaluationOfTestResult
from test_quality_assessment import TestQualityAssessment

# Главное окно
class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        btn_frame = tk.Frame()
        btn_frame.grid(row=0, column=0)

        btn_open_test_quality = tk.Button(btn_frame, text='Оценка качества теста', command=self.open_test_quality, width=20)
        btn_open_test_quality.grid(sticky='we', pady=10)

        btn_open_test_result = tk.Button(btn_frame, text='Оценка результатов \nтестируемых', command=self.open_test_result)
        btn_open_test_result.grid(sticky='we', pady=10)

    # Открытие оценки качества теста
    def open_test_quality(self):
        TestQualityAssessment()
    
    # Открытие оценки результатов тестируемых
    def open_test_result(self):
        EvaluationOfTestResult()



if __name__ == '__main__':
    app = Main(root)
    app.grid()
    root.title('ЯDraw')
    root.geometry('650x450+300+200')
    root.resizable(False, False)
    root.config()
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.mainloop()