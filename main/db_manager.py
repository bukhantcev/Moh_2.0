# import sqlite3
# from datetime import datetime
#
#
#
# # Создаем таблицу Users
# # cursor.execute('''
# # CREATE TABLE IF NOT EXISTS Users (
# # id INTEGER PRIMARY KEY,
# # username TEXT NOT NULL,
# # email TEXT NOT NULL,
# # age INTEGER
# # )
# # ''')
# # cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# # print(cursor.fetchall())
# class Events:
#     table_name = 'forms_event'
#     def events(self):
#         connection = sqlite3.connect('db.sqlite3')
#         cursor = connection.cursor()
#         cursor.execute(f'SELECT * FROM {self.table_name}')
#         events = cursor.fetchall()
#         return events
#     def get_name(self):
#         connection = sqlite3.connect('db.sqlite3')
#         cursor = connection.cursor()
#         result = []
#         cursor.execute(f'SELECT name FROM {self.table_name}')
#         events = cursor.fetchall()
#         for i in events:
#             result.append(i[0])
#         connection.commit()
#         connection.close()
#         return result
#     def get_date(self):
#         connection = sqlite3.connect('db.sqlite3')
#         cursor = connection.cursor()
#         result = []
#         cursor.execute(f'SELECT date FROM {self.table_name}')
#         events = cursor.fetchall()
#         for i in events:
#             result.append(datetime.strptime(str(i[0]).split(' ')[0], "%Y-%m-%d").date())
#         connection.commit()
#         connection.close()
#         return result
#     def get_time(self):
#         connection = sqlite3.connect('db.sqlite3')
#         cursor = connection.cursor()
#         result = []
#         cursor.execute(f'SELECT date FROM {self.table_name}')
#         events = cursor.fetchall()
#         for i in events:
#             result.append(f'{str(i[0]).split(' ')[1].split(':')[0]}:{str(i[0]).split(' ')[1].split(':')[1]}')
#         connection.commit()
#         connection.close()
#         return result
#     def get_staff(self):
#         connection = sqlite3.connect('db.sqlite3')
#         cursor = connection.cursor()
#         result = []
#         cursor.execute(f'SELECT staff FROM {self.table_name}')
#         events = cursor.fetchall()
#         for i in events:
#             result.append(i[0])
#         connection.commit()
#         connection.close()
#         return result
#     def get_type(self):
#         connection = sqlite3.connect('db.sqlite3')
#         cursor = connection.cursor()
#         result = []
#         cursor.execute(f'SELECT type FROM {self.table_name}')
#         events = cursor.fetchall()
#         for i in events:
#             result.append(i[0])
#         connection.commit()
#         connection.close()
#         return result
#     def get_location(self):
#         connection = sqlite3.connect('db.sqlite3')
#         cursor = connection.cursor()
#         result = []
#         cursor.execute(f'SELECT location FROM {self.table_name}')
#         events = cursor.fetchall()
#         for i in events:
#             result.append(i[0])
#         connection.commit()
#         connection.close()
#         return result
#
#
#
# #______________________________________________TABLE EVENTS________________________________________________
#
#
