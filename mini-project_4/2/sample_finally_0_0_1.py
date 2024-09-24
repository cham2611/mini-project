import mysql.connector
import pandas as pd

connection = mysql.connector.connect(
    user = "root",
    password= "0000",
    host ="127.0.0.1",
    port = "3306",
)
cursor = connection.cursor()


cursor.execute('CREATE DATABASE IF NOT EXISTS exdatabase;')
connection.commit()


cursor.execute('USE exdatabase;')
connection.commit()


cursor.execute("""
               CREATE TABLE IF NOT EXISTS ex (
               name VARCHAR(255),
               genres VARCHAR(255),
               image VARCHAR(255),
               releasedate DATETIME,
               price INT,
               reviewtext LONGTEXT,
               reviewscore BOOL,
               language VARCHAR(255)
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example = pd.read_csv('finally.csv')


# 데이터베이스에 데이터 삽입
for index, row in Example.iterrows():
    data_tuple = (
        row['game_name'] if pd.notna(row['game_name']) else None,
        row['game_genres'] if pd.notna(row['game_genres']) else None,
        row['game_image'] if pd.notna(row['game_image']) else None,
        row['game_release_date'] if pd.notna(row['game_release_date']) else None,  # NaT를 None으로 처리
        row['game_price'],
        row['review_text'] if pd.notna(row['review_text']) else None,
        row['review_score'] if pd.notna(row['review_score']) else None,
        row['language'] if pd.notna(row['language']) else None
    )

    cursor.execute("""
               INSERT INTO ex (name, genres, image, releasedate, price, reviewtext, reviewscore, language)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
               """, data_tuple)

connection.commit()

# 커서와 연결 종료
cursor.close()
connection.close()