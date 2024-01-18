import db_connection


@db_connection.handle_connection
def get_all_questions(cursor):
    cursor.execute("SELECT title, description FROM questions")
    result = cursor.fetchall()
    return result


@db_connection.handle_connection
def get_all_questions_with_answers(cursor):
    cursor.execute("""
        select q.title, count(a.answer_id) as number_of_answers from answers a
        join questions q on q.question_id = a.question_id
        group by q.title, a.question_id
        order by a.question_id  
    """)
    result = cursor.fetchall()
    return result


@db_connection.handle_connection
def get_question_with_answers(cursor, index):
    cursor.execute(f"""
        select q.title, q.description, a.description from questions q
        join answers a on a.question_id = q.question_id
        where q.question_id = {index}
    """)
    result = cursor.fetchall()
    return result