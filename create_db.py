import sqlite3

# Устанавливаем соединение с базой данных
conn = sqlite3.connect('db.sqlite')
cursor = conn.cursor()

cursor.executescript(
    '''
        CREATE TABLE teacher (
            teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            teacher_name VARCHAR(50),
            teacher_login VARCHAR(50),
            teacher_password VARCHAR(50)
        );

        INSERT INTO teacher (teacher_name, teacher_login, teacher_password)
        VALUES 
            ('Остроухова Светлана Николаевна', 'ostroukhova.sn', 'aaaa'),
            ('Крестникова Ольга Александровна', 'krestnikova.oa', 'bbbb'),
            ('Иваненко Юрий Сергеевич', 'ivanenko.ys', 'cccc'),
            ('Симаков Валентин Константинович', 'simakov.vk', 'dddd');


        CREATE TABLE student_group (
            group_id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_name CHAR(15) UNIQUE,
            group_majority VARCHAR(10)
        );

        INSERT INTO student_group (group_name, group_majority)
        VALUES 
            ('Б9120-09.03.04','прогин'),
            ('Б9121-09.03.04','прогин'),
            ('Б9122-09.03.04','прогин'),
            ('Б9123-09.03.04','прогин');


        CREATE TABLE education_year (
            education_year_id INTEGER PRIMARY KEY,
            teacher_id INTEGER,
            group_id INTEGER,

            FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id) ON DELETE CASCADE,
            FOREIGN KEY (group_id) REFERENCES student_group(group_id) ON DELETE CASCADE
        );

        INSERT INTO education_year (teacher_id, group_id)
        VALUES 
            (1, 1),
            (2, 2);


        CREATE TABLE subgroup (
            subgroup_id INTEGER PRIMARY KEY AUTOINCREMENT,
            group_id INTEGER,
            subgroup_num INTEGER,
            teacher_id INTEGER,

            FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id) ON DELETE CASCADE,
            FOREIGN KEY (group_id) REFERENCES student_group(group_id) ON DELETE CASCADE
        );

        INSERT INTO subgroup (group_id, subgroup_num, teacher_id)
        VALUES 
            (1,1,1),
            (1,2,1),
            (2,1,2),
            (2,2,2),
            (3,1,1),
            (3,2,2),
            (4,1,1),
            (4,2,2);


        CREATE TABLE student (
            student_id INTEGER PRIMARY KEY,
            student_name VARCHAR(50),
            subgroup_id INTEGER,
            student_login VARCHAR(50),
            student_password VARCHAR(50),

            FOREIGN KEY (subgroup_id) REFERENCES subgroup(subgroup_id) ON DELETE CASCADE
        );


        INSERT INTO student (student_name, subgroup_id, student_login, student_password)
        VALUES 
            ('Доржиев Арсалан Сенгэевич',1,'dorzhiev.as','aaaa'),
            ('Чемериская Елизавета Вячеславовна',1,'chemeriskaya.ev','bbbb'),
            ('Шулятьев Артём Андреевич',1,'shulyatev.aa','cccc'),
            ('Аюров Роман Сергеевич',2,'aurov.rs','dddd'),
            ('Борщевский Иван Олегович',2,'borschevsky.io','eeee'),
            ('Жигжитов Этигэл Сэнгэевич',3,'zhigzhitov.es','ffff'),
            ('Корогод Дмитрий Александрович',3,'korogod','gggg'),
            ('Лысенко Алексей Алексеевич',4,'lysenko.aa','hhhh'),
            ('Майоров Сергей Владимирович',4,'mayorov.sv','jjjj'),
            ('Мищенко Александра Андреевна',5,'mischenko.aa','kkkk'),
            ('Перфильева Дарья Вадимовна',5,'perfileva.dv','llll'),
            ('Полянская Эвелина Олеговна',6,'polyanskaya.eo','mmmm'),
            ('Пяткин Алексей Витальевич',6,'pyatkin.av','nnnn'),
            ('Седых Анна Дмитриевна',6,'sedykh.ad','oooo'),
            ('Сусоева Анна Дмитриевна',7,'susoeva.ad','pppp'),
            ('Федоров Артур Максимович',7,'fedorov.am','rrrr'),
            ('Худоногов Сергей Вячеславович',8,'khudonogov.sv','ssss'),
            ('Широкова Софья Сергеевна',8,'shirokova.ss','tttt');


        CREATE TABLE key_template (
            key_template_id INTEGER PRIMARY KEY,
            key_template_name VARCHAR(10)
        );

        INSERT INTO key_template (key_template_name)
        VALUES 
            ('Числовой'),
            ('Строковый');


        CREATE TABLE tree_type (
            tree_type_id INTEGER PRIMARY KEY,
            tree_type_name CHAR(3)
        );

        INSERT INTO tree_type (tree_type_name)
        VALUES 
            ('БДП'),
            ('АВЛ');


        CREATE TABLE tree_template (
            tree_template_id INTEGER PRIMARY KEY AUTOINCREMENT,
            tree_type_id INTEGER,
            key_template_id INTEGER,
            tree_template_height INTEGER,
            tree_template_keys_amount INTEGER,
            tree_template_difficulty FLOAT,
            teacher_id INTEGER,
            tree_structure VARCHAR(40),

            FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id) ON DELETE CASCADE,
            FOREIGN KEY (tree_type_id) REFERENCES tree_type(tree_type_id) ON DELETE CASCADE,
            FOREIGN KEY (key_template_id) REFERENCES key_template(key_template_id) ON DELETE CASCADE
        );


        CREATE TABLE input_template (
            input_template_id INTEGER PRIMARY KEY AUTOINCREMENT,
            is_tree INTEGER
        );

        INSERT INTO input_template(is_tree) 
        VALUES 
            (0),
            (1);


        CREATE TABLE output_template (
            output_template INTEGER PRIMARY KEY AUTOINCREMENT,
            is_tree INTEGER
        );


        INSERT INTO output_template(is_tree) 
        VALUES 
            (0),
            (1);


        CREATE TABLE suboperation_template (
            suboperation_template_id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_template_id INTEGER,
            output_template_id INTEGER,
            suboperation_template_difficulty FLOAT,
            suboperation_text VARCHAR(80),

            FOREIGN KEY (input_template_id) REFERENCES input_template(input_template_id) ON DELETE CASCADE,
            FOREIGN KEY (output_template_id) REFERENCES output_template(output_template_id) ON DELETE CASCADE
        );


        INSERT INTO suboperation_template (input_template_id, output_template_id, suboperation_template_difficulty, suboperation_text)
        VALUES
            (2, 2, 0.2, 'Выберите ключи в соответствии с алгоритмом обхода в глубину'),
            (2, 2, 0.2, 'Выберите ключи в соответствии с алгоритмом обхода в ширину'),
            (2, 1, 0.1, 'Выберите узел - место вставки'),
            (2, 1, 0.1, 'Выберите направление вставки: вставить влево или вправо'),
            (2, 1, 0.5, 'Выберите тройку узлов, участвующих в балансировке, если она необходима'),
            (2, 1, 0.2, 'Выберите тип поворота из предложенных вариантов'),
            (2, 1, 0.1, 'Выберите удаляемый узел'),
            (2, 1, 0.2, 'Выберите узел-замену, если это необходимо (замена на минимальный справа)'),
            (2, 1, 0.2, 'Выберите узел-замену, если это необходимо (замена на максимальный слева)');


        CREATE TABLE operation_template (
            operation_template_id INTEGER PRIMARY KEY AUTOINCREMENT,
            operation_name VARCHAR(20),
            input_template_id INTEGER,
            output_template_id INTEGER,
            operation_template_difficulty FLOAT,
            operation_text VARCHAR(80),
            tree_type_id INTEGER,

            FOREIGN KEY (input_template_id) REFERENCES input_template(input_template_id) ON DELETE CASCADE,
            FOREIGN KEY (output_template_id) REFERENCES output_template(output_template_id) ON DELETE CASCADE,
            FOREIGN KEY (tree_type_id) REFERENCES tree_type(tree_type_id) ON DELETE CASCADE
        );


        INSERT INTO operation_template (operation_name, input_template_id, output_template_id, operation_template_difficulty, operation_text, tree_type_id)
        VALUES
            ('Обход в глубину', 2, 2, 0.2, 'Выполните обход дерева в глубину', 1),
            ('Обход в глубину', 2, 2, 0.2, 'Выполните обход дерева в глубину', 2),
            ('Обход в ширину', 2, 2, 0.2, 'Выполните обход дерева в ширину', 1),
            ('Обход в ширину', 2, 2, 0.2, 'Выполните обход дерева в ширину', 2),
            ('Добавление узла с повторением слева', 2, 2, 0.3, 'Выполните добавление узла', 1),
            ('Добавление узла с повторением справа', 2, 2, 0.3, 'Выполните добавление узла', 1),
            ('Добавление узла с без повторения слева', 2, 2, 0.3, 'Выполните добавление узла', 1),
            ('Добавление узла с без повторения справа', 2, 2, 0.3, 'Выполните добавление узла', 1),
            ('Добавление узла слева', 2, 2, 0.3, 'Выполните добавление узла', 2),
            ('Добавление узла справа', 2, 2, 0.3, 'Выполните добавление узла', 2),
            ('Удаление узла с заменой на мин. справа', 2, 2, 0.4, 'Выполните удаление узла', 1),
            ('Удаление узла с заменой на макс. слева', 2, 2, 0.4, 'Выполните удаление узла', 1),
            ('Удаление узла с заменой на мин. справа', 2, 2, 0.5, 'Выполните удаление узла', 2),
            ('Удаление узла с заменой на макс. слева', 2, 2, 0.5, 'Выполните удаление узла', 2);


        CREATE TABLE operation_suboperation_template (
            operation_template_id INTEGER,
            suboperation_template_id INTEGER,
            
            PRIMARY KEY (operation_template_id, suboperation_template_id),
            FOREIGN KEY (operation_template_id) REFERENCES operation_template(operation_template_id) ON DELETE CASCADE,
            FOREIGN KEY (suboperation_template_id) REFERENCES suboperation_template(suboperation_template_id) ON DELETE CASCADE
        );

        INSERT INTO operation_suboperation_template (operation_template_id, suboperation_template_id)
        VALUES
            (1, 1),
            (2, 1),
            (3, 2),
            (4, 2),
            (5, 3),
            (5, 4),
            (6, 3),
            (6, 4),
            (7, 3),
            (7, 4),
            (8, 3),
            (8, 4),
            (9, 3),
            (9, 4),
            (9, 5),
            (9, 6),
            (10, 3),
            (10, 4),
            (10, 5),
            (10, 6),
            (11, 7),
            (11, 8),
            (12, 7),
            (12, 9),
            (13, 7),
            (13, 8),
            (13, 5),
            (13, 6),
            (14, 7),
            (14, 9),
            (14, 5),
            (14, 6);


        CREATE TABLE formula_task (
            formula_task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            formula_task_body VARCHAR(80)
        );

        INSERT INTO formula_task (formula_task_body)
        VALUES
            ('sum([1/(mi + 1) for mi in mi_s])/n');


        CREATE TABLE task_template (
            task_template_id INTEGER PRIMARY KEY AUTOINCREMENT,
            formula_task_id INTEGER,
            task_template_difficulty FLOAT,
            teacher_id INTEGER,
            tree_template_id INTEGER,
            operation_template_id INTEGER,
            node_index INTEGER,

            FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id) ON DELETE CASCADE,
            FOREIGN KEY (formula_task_id) REFERENCES formula_task(formula_task_id) ON DELETE CASCADE,
            FOREIGN KEY (operation_template_id) REFERENCES operation_template(operation_template_id) ON DELETE CASCADE,
            FOREIGN KEY (tree_template_id) REFERENCES tree_template(tree_template_id) ON DELETE CASCADE
        );


        CREATE TABLE test_template (
            test_template_id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_template_difficulty FLOAT,
            teacher_id INTEGER,

            FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id) ON DELETE CASCADE
        );


        CREATE TABLE test_task_template (
            test_task_template_id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_template_id INTEGER,
            task_template_id INTEGER,

            FOREIGN KEY (test_template_id) REFERENCES test_template(test_template_id) ON DELETE CASCADE,
            FOREIGN KEY (task_template_id) REFERENCES task_template(task_template_id) ON DELETE CASCADE
        );


        CREATE TABLE formula_test (
            formula_test_id INTEGER PRIMARY KEY AUTOINCREMENT,
            formula_test_body VARCHAR(80)
        );

        INSERT INTO formula_test(formula_test_body)
        VALUES
            ('B/sum(zi_s) * sum([ri * zi for ri, zi in zip(ri_s, zi_s)])');


        CREATE TABLE testing_session (
            testing_session_id INTEGER PRIMARY KEY AUTOINCREMENT,
            testing_session_name VARCHAR(30),
            testing_session_date DATE,
            testing_session_begin_time TIME,
            testing_session_end_time TIME,
            formula_test_id INTEGER,
            teacher_id INTEGER,
            test_template_id INTEGER,
            test_template_bar INTEGER,

            FOREIGN KEY (test_template_id) REFERENCES test_template(test_template_id) ON DELETE CASCADE,
            FOREIGN KEY (teacher_id) REFERENCES teacher(teacher_id) ON DELETE CASCADE,
            FOREIGN KEY (formula_test_id) REFERENCES formula_test(formula_test_id) ON DELETE CASCADE
        );


        CREATE TABLE student_testing_session (
            student_testing_session_id INTEGER PRIMARY KEY AUTOINCREMENT,
            testing_session_id INTEGER,
            student_id INTEGER,

            FOREIGN KEY (testing_session_id) REFERENCES testing_session(testing_session_id) ON DELETE CASCADE,
            FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE
        );
    '''
)