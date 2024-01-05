import sqlite3


def main():
    # 连接到数据库（如果不存在，则会被创建）
    connection = sqlite3.connect('example.db')

    # 创建一个游标对象，用于执行SQL语句
    cursor = connection.cursor()

    # 创建一个表格
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    # 插入一些数据
    cursor.execute("INSERT INTO users (username, email) VALUES (?, ?)", ('JohnDoe', 'john@example.com'))

    # 提交事务（将写入的改变保存到数据库）
    connection.commit()

    # 查询数据
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # 关闭连接
    connection.close()


def execute():
    connection = sqlite3.connect('example.db')  
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    
if __name__ == '__main__':
    # main()
    execute()
