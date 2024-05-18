import matplotlib.pyplot as plt
import numpy as np

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


# КОЛ-ВО ОЦЕНОК ПО ОДНОМУ СТ/ШТ
# def count_score_one_st(ST_name, marks, is_ST, is_group, is_graph):
#     who_to_analyze_list = []
#     all_scores = [score for sublist in avg_score_one_st.values() for score in sublist]

#     unique_scores, count_scores = np.unique(all_scores, return_counts=True)

#     print(unique_scores)
#     print(count_scores)

#     plt.plot(unique_scores, count_scores, marker='o')
#     plt.xticks(range(1, 6))

#     for x, y in zip(unique_scores, count_scores):
#         plt.text(x, y, f'{y}', ha='center', va='bottom')
#     plt.xlabel('Оценка')
#     plt.ylabel('Кол-во студентов')
#     plt.title('Кол-во оценок за СТ №1 у групп \nБ9120-09.03.04, Б9121-09.03.04, Б9122-09.03.04')

#     plt.show()