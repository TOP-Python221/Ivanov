import sqlite3


def index():
        db_command = []
        db_text = []
        with sqlite3.connect('..\service\db.sqlite3') as db:
                cursor = db.cursor()
                query = """ SELECT * FROM sitebot_listcommand"""
                cursor.execute(query)
                
                for r in cursor:
                        db_command.append(r[1])
                        db_text.append(r[2])

        return db_command, db_text

def message_save(text_message, id_author, mes=None):
        id_com = None
        with sqlite3.connect('..\service\db.sqlite3') as db:
                title = text_message[1:].split()[0]
                cursor = db.cursor()
                vals = cursor.execute("SELECT id, title FROM sitebot_listcommand WHERE title=?", (title, )).fetchone()
                id_com = vals[0]

        with sqlite3.connect('..\service\db.sqlite3') as db:
                cursor = db.cursor()
                params = (id_com, id_author, mes)
                query1 = """ INSERT INTO  sitebot_messageuser(command_id, author_id, text) VALUES(?, ?, ?) """
                cursor.execute(query1, params)
                db.commit()

def save_chat(id_tg_user, name, first_name, user_name, mes, text):
       with sqlite3.connect('..\service\db.sqlite3') as db:
                cursor = db.cursor()
                vals = cursor.execute("SELECT id, id_tg_user FROM sitebot_tguser WHERE id_tg_user=?", (id_tg_user, )).fetchone()
                if vals:
                        print('Значение есть ', vals)
                        id_author = vals[0]
                        message_save(text, id_author, mes)
                else:
                        print('Значения нет')
                        params = (id_tg_user, name, first_name, user_name)
                        query1 = """ INSERT INTO  sitebot_tguser(id_tg_user, name, first_name, user_name) VALUES(?, ?, ?, ?) """
                        cursor.execute(query1, params)
                        db.commit()
                        vals = cursor.execute("SELECT id, id_tg_user FROM sitebot_tguser WHERE id_tg_user=?", (id_tg_user, )).fetchone()
                        id_author = vals[0]
                        message_save(text, id_author, mes)

if __name__ == "__main__":
    print("Hello, World!")