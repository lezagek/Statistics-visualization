import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# % УСПЕШНО ПРОЙДЕННЫХ ПО ОДНОМУ СТ/ШТ
def passed_one_st(ST_name, marks, is_ST, is_group, is_graph):
    passed_one_st_vis = []
    who_to_analyze_list = []

    # Проходимся по каждой группе/году
    for group in marks:
        # Сортируем оценки
        marks[group] = sorted(marks[group])
        # Находим 3 (успешно пройдено при оценке >=3 )
        if 3 in marks[group]:
            ind = marks[group].index(3)
        elif 4 in marks[group]:
            ind = marks[group].index(4)
        elif 5 in marks[group]:
            ind = marks[group].index(5)
        else:
            ind = len(marks[group])

        # Узнаём процент успешно пройденных
        passed = (len(marks[group]) - ind) / len(marks[group]) * 100
        passed_one_st_vis.append(passed)

        who_to_analyze_list.append(group)

    fig, ax = plt.subplots()
    fig.set_size_inches(10,5)
    
    # График или диаграмма
    if is_graph:
        plt.plot(range(len(passed_one_st_vis)), passed_one_st_vis, marker='o')
    else:
        plt.bar(range(len(passed_one_st_vis)), passed_one_st_vis, edgecolor='black')

    # , rotation=45 если понадобится повернуть подписи
    plt.xticks(range(len(passed_one_st_vis)), who_to_analyze_list)
    plt.ylim(0, 110)
    plt.xlabel(f'{"Группа" if is_group else "Года"}')
    plt.ylabel('%')
    what_to_analyze = 'СТ' if is_ST else 'ШТ'
    who_to_analyze = 'групп' if is_group else 'годов'
    plt.title(f'% успешно пройденных {what_to_analyze} {ST_name} у {who_to_analyze} \n{", ".join(who_to_analyze_list)}')

    for i, avg_score in enumerate(passed_one_st_vis):
        plt.text(i, avg_score, f'{avg_score:.2f}', ha='center', va='bottom')

    plt.show()


# % УСПЕШНО ПРОЙДЕННЫХ ПО НЕСКОЛЬКИМ СТ/ШТ
def passed_many_st(marks, is_ST, is_group, view):
    passed_many_st_vis = {}
    who_to_analyze_set = set()
    count_ST = 0
    ST_name = []

    # Проходимся по каждому СТ/ШТ
    for ST in marks:
        passed_many_st_vis[ST] = []
        count_ST += 1
        ST_name.append(str(ST))

        # Проходимся по каждой группе/году
        for group in marks[ST]:
            # Сортируем оценки
            marks[ST][group] = sorted(marks[ST][group])
            # Находим 3 (успешно пройдено при оценке >=3 )
            if 3 in marks[ST][group]:
                ind = marks[ST][group].index(3)
            elif 4 in marks[ST][group]:
                ind = marks[ST][group].index(4)
            elif 5 in marks[ST][group]:
                ind = marks[ST][group].index(5)
            else:
                ind = len(marks[ST][group])

            # Узнаём процент успешно пройденных
            if len(marks[ST][group]) != 0:
                passed = (len(marks[ST][group]) - ind) / len(marks[ST][group]) * 100
            else:
                passed = 0
            passed_many_st_vis[ST].append(round(passed, 2))

            who_to_analyze_set.add(group)

    ind = np.arange(1, len(who_to_analyze_set) + 1)
    width = 1 / (count_ST + 1)

    fig, ax = plt.subplots()
    fig.set_size_inches(10,5)

    what_to_analyze = 'СТ' if is_ST else 'ШТ'
    
    match view:
        case 'ГРАФИК':
            for ST in passed_many_st_vis:
                plt.plot(range(len(passed_many_st_vis[ST])), passed_many_st_vis[ST], marker='o', label=f'{what_to_analyze} {ST}')

                for j, passed_score in enumerate(passed_many_st_vis[ST]):
                    plt.text(j, passed_score, f'{passed_score:.2f}', ha='center', va='bottom')
            
            plt.xticks(range(len(passed_many_st_vis[ST])), sorted(list(who_to_analyze_set)))
            plt.ylim(0, 110)
            plt.xlabel(f'{"Группа" if is_group else "Года"}')
            plt.ylabel('%')
            plt.legend()

        case 'ДИАГРАММА':
            i = 1
            for ST in passed_many_st_vis:
                plt.bar(ind + (i - (count_ST + 1)/2) * width, passed_many_st_vis[ST], width, label=f'{what_to_analyze} {ST}')
                
                for j, passed_score in enumerate(passed_many_st_vis[ST]):
                    plt.text(j + 1 + (i - (count_ST + 1)/2) * width, passed_score, f'{passed_score:.2f}', ha='center', va='bottom')
                
                i += 1
            
            plt.xticks(range(1, len(passed_many_st_vis[ST]) + 1), sorted(list(who_to_analyze_set)))
            plt.ylim(0, 110)
            plt.xlabel(f'{"Группа" if is_group else "Года"}')
            plt.ylabel('%')
            plt.legend()

        case 'ТАБЛИЦА':
            ax.axis('off')
            df = pd.DataFrame.from_dict(passed_many_st_vis)
            ax.table(cellText=df.values, colLabels=df.columns, rowLabels=sorted(list(who_to_analyze_set)), loc='center')
    
    
    who_to_analyze = 'групп' if is_group else 'годов'
    plt.title(f'% успешно пройденных {what_to_analyze} {", ".join(ST_name)} у {who_to_analyze} \n{", ".join(who_to_analyze_set)}')

    plt.show()


# СРЕДНЯЯ ОЦЕНКА ПО ОДНОМУ СТ/ШТ
def avg_score_one_st(ST_name, marks, is_ST, is_group, is_graph):
    avg_score_one_st_vis = []
    who_to_analyze_list = []

    # Проходимся по каждой группе/году
    for group in marks:
        avg_score_one_st_vis.append(np.mean(marks[group]))
        who_to_analyze_list.append(group)

    fig, ax = plt.subplots()
    fig.set_size_inches(10,5)

    # График или диаграмма
    if is_graph:
        plt.plot(range(len(avg_score_one_st_vis)), avg_score_one_st_vis, marker='o')
    else:
        plt.bar(range(len(avg_score_one_st_vis)), avg_score_one_st_vis, edgecolor='black')

    plt.xticks(range(len(avg_score_one_st_vis)), who_to_analyze_list)
    plt.yticks(range(7))

    plt.xlabel(f'{"Группа" if is_group else "Года"}')
    plt.ylabel('Средняя оценка')
    what_to_analyze = 'СТ' if is_ST else 'ШТ'
    who_to_analyze = 'групп' if is_group else 'годов'
    plt.title(f'Средняя оценка за {what_to_analyze} {ST_name} у {who_to_analyze} \n{", ".join(who_to_analyze_list)}')

    for i, avg_score in enumerate(avg_score_one_st_vis):
        plt.text(i, avg_score, f'{avg_score:.2f}', ha='center', va='bottom')

    plt.show()


# СРЕДНЯЯ ОЦЕНКА ПО НЕСКОЛЬКИМ СТ/ШТ
def avg_score_many_st(marks, is_ST, is_group, view):
    avg_score_many_st_vis = {}
    who_to_analyze_set = set()
    count_ST = 0
    ST_name = []
    # print(marks)
    # Проходимся по каждому СТ/ШТ
    for ST in marks:
        # print(ST)
        # print(marks[ST])
        avg_score_many_st_vis[ST] = []
        count_ST += 1
        ST_name.append(str(ST))

        # Проходимся по каждой группе/году
        for group in marks[ST]:
            # print(group)
            # print(marks[ST][group])

            # Как тест. Возможно потом убрать. Ровнее выстраиваются диаграммы, но не понятны графики.
            if len(marks[ST][group]) == 0:
                avg_score_many_st_vis[ST].append(0)
            else:
                avg_score_many_st_vis[ST].append(round(np.mean(marks[ST][group]), 2))
            who_to_analyze_set.add(group)

    ind = np.arange(1, len(who_to_analyze_set) + 1)
    width = 1 / (count_ST + 1)

    fig, ax = plt.subplots()
    fig.set_size_inches(10,5)

    what_to_analyze = 'СТ' if is_ST else 'ШТ'

    match view:
        case 'ГРАФИК':
            for ST in avg_score_many_st_vis:
                plt.plot(range(len(avg_score_many_st_vis[ST])), avg_score_many_st_vis[ST], marker='o', label=f'{what_to_analyze} {ST}')

                for j, avg_score in enumerate(avg_score_many_st_vis[ST]):
                    plt.text(j, avg_score, f'{avg_score:.2f}', ha='center', va='bottom')
            
            plt.xticks(range(len(avg_score_many_st_vis[ST])), sorted(list(who_to_analyze_set)))
            plt.yticks(range(7))
            plt.xlabel(f'{"Группа" if is_group else "Года"}')
            plt.ylabel('Средняя оценка')
            plt.legend()

        case 'ДИАГРАММА':
            i = 1
            for ST in avg_score_many_st_vis:
                # print(ind + (i - (count_ST + 1)/2) * width, avg_score_many_st_vis[ST])
                plt.bar(ind + (i - (count_ST + 1)/2) * width, avg_score_many_st_vis[ST], width, label=f'{what_to_analyze} {ST}')

                for j, avg_score in enumerate(avg_score_many_st_vis[ST]):
                    plt.text(j + 1 + (i - (count_ST + 1)/2) * width, avg_score, f'{avg_score:.2f}', ha='center', va='bottom')
                i += 1

            plt.xticks(range(1, len(avg_score_many_st_vis[ST]) + 1), sorted(list(who_to_analyze_set)))
            plt.yticks(range(7))
            plt.xlabel(f'{"Группа" if is_group else "Года"}')
            plt.ylabel('Средняя оценка')
            plt.legend()

        case 'ТАБЛИЦА':
            ax.axis('off')
            df = pd.DataFrame.from_dict(avg_score_many_st_vis)
            df = df.fillna('-')
            ax.table(cellText=df.values, colLabels=df.columns, rowLabels=sorted(list(who_to_analyze_set)), loc='center')

    who_to_analyze = 'групп' if is_group else 'годов'
        
    plt.title(f'Средняя оценка за {what_to_analyze} {", ".join(ST_name)} у {who_to_analyze} \n{", ".join(who_to_analyze_set)}')

    plt.show()


# КОЛ-ВО ОЦЕНОК ПО ОДНОМУ СТ/ШТ
def count_score_one_st(ST_name, marks, is_ST, is_group, is_graph):
    who_to_analyze_list = []
    count_scores = {}
    count_group = 0

     # Проходимся по каждой группе/году
    for group in marks:
        count_scores[group] = [0, 0, 0, 0, 0]
        count_group += 1
        who_to_analyze_list.append(group)

        # Считаем кол-во оценок для каждой группы
        for mark in marks[group]:
            count_scores[group][mark - 1] += 1

    # До 6, так как 5 оценок
    ind = np.arange(1, 6)
    width = 1 / (count_group + 1)

    fig, ax = plt.subplots()
    fig.set_size_inches(15,5)

    what_to_analyze = 'СТ' if is_ST else 'ШТ'
    who_to_analyze = 'групп' if is_group else 'годов'

    if is_graph:
        for group in count_scores:
            plt.plot(range(len(count_scores[group])), count_scores[group], marker='o', label=f'{group}')

            for j, count in enumerate(count_scores[group]):
                plt.text(j, count, f'{count:.2f}', ha='center', va='bottom')
        plt.xticks(range(5))

    else:
        i = 1
        for group in count_scores:
            plt.bar(ind + (i - (count_group + 1)/2) * width, count_scores[group], width, label=f'{group}')

            for j, count in enumerate(count_scores[group]):
                plt.text(j + 1 + (i - (count_group + 1)/2) * width, count, f'{count:.2f}', ha='center', va='bottom')
            i += 1
        plt.xticks(range(1, 6))

    plt.xlabel('Оценка')
    plt.ylabel('Кол-во студентов')
    plt.title(f'Кол-во оценок за {what_to_analyze} {ST_name} у {who_to_analyze} \n{", ".join(who_to_analyze_list)}')
    plt.legend()
    plt.show()