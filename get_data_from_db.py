import sqlite3

# Получение всех СТ
def get_ST():
    ST = []
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()

    query = '''SELECT testing_session_name 
                FROM testing_session'''
    cursor.execute(query)

    for name in cursor.fetchall():
        ST.append(name[0])
    
    conn.commit()
    conn.close()

    return ST

# Получение всех ШТ
def get_SHT():
    SHT = []
    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()

    query = '''SELECT test_template_id 
                FROM test_template'''
    cursor.execute(query)

    for name in cursor.fetchall():
        SHT.append(name[0])
    
    conn.commit()
    conn.close()

    return SHT

# Получение названий групп, которые проходили конкретный СТ
def get_groups_ST(name_ST):
    groups = []

    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()

    query = '''SELECT DISTINCT group_name
                FROM testing_session
                LEFT JOIN test USING (testing_session_id)
                LEFT JOIN student USING (student_id)
                LEFT JOIN subgroup USING (subgroup_id)
                LEFT JOIN student_group USING (group_id)
                WHERE testing_session_name = :p_name'''
    cursor.execute(query, {'p_name': name_ST})

    for name in cursor.fetchall():
        groups.append(name[0])
    
    conn.commit()
    conn.close()

    return groups

# Получение названий групп, которые проходили конкретный ШТ
def get_groups_SHT(num_SHT):
    groups = []

    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()

    query = '''SELECT DISTINCT group_name
                FROM test
                LEFT JOIN student USING (student_id)
                LEFT JOIN subgroup USING (subgroup_id)
                LEFT JOIN student_group USING (group_id)
                WHERE test_template_id = :p_num'''
    cursor.execute(query, {'p_num': num_SHT})

    for name in cursor.fetchall():
        groups.append(name[0])
    
    conn.commit()
    conn.close()

    return groups

# Получение годов, в которые проходили конкретный ШТ
def get_years_SHT(num_SHT):
    years = []

    conn = sqlite3.connect('db.sqlite')
    cursor = conn.cursor()

    query = '''SELECT DISTINCT strftime('%Y', testing_session_date)
                FROM testing_session
                WHERE test_template_id = :p_num'''
    cursor.execute(query, {'p_num': num_SHT})

    for year in cursor.fetchall():
        years.append(year[0])
    
    conn.commit()
    conn.close()

    return years