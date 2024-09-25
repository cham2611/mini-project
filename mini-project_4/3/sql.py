# sql 와 csv 연결
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
               CREATE TABLE IF NOT EXISTS games_2d (
               name VARCHAR(255),
               genres VARCHAR(255),
               image VARCHAR(255),
               releasedate DATETIME,
               price INT,
               reviewtext LONGTEXT,
               reviewscore BOOL,
               language VARCHAR(255),
               author BIGINT ,
               playtime_at_review INT , 
               timestamp_created DATETIME
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example = pd.read_csv('2d.csv')


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
        row['language'] if pd.notna(row['language']) else None,
        row['author'] if pd.notna(row['author']) else None,
        row['playtime_at_review'] if pd.notna(row['playtime_at_review']) else None,
        row['timestamp_created'] if pd.notna(row['timestamp_created']) else None
    )

    cursor.execute("""
               INSERT INTO games_2d (name, genres, image, releasedate, price, reviewtext, reviewscore, language, author,playtime_at_review,timestamp_created)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """, data_tuple)

connection.commit()
# ------------------------------------------------------------------------------------
cursor.execute("""
               CREATE TABLE IF NOT EXISTS games_3d (
               name VARCHAR(255),
               genres VARCHAR(255),
               image VARCHAR(255),
               releasedate DATETIME,
               price INT,
               reviewtext LONGTEXT,
               reviewscore BOOL,
               language VARCHAR(255),
               author BIGINT ,
               playtime_at_review INT , 
               timestamp_created DATETIME
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example2 = pd.read_csv('3d.csv')


# 데이터베이스에 데이터 삽입
for index, row in Example2.iterrows():
    data_tuple = (
        row['game_name'] if pd.notna(row['game_name']) else None,
        row['game_genres'] if pd.notna(row['game_genres']) else None,
        row['game_image'] if pd.notna(row['game_image']) else None,
        row['game_release_date'] if pd.notna(row['game_release_date']) else None,  # NaT를 None으로 처리
        row['game_price'],
        row['review_text'] if pd.notna(row['review_text']) else None,
        row['review_score'] if pd.notna(row['review_score']) else None,
        row['language'] if pd.notna(row['language']) else None,
        row['author'] if pd.notna(row['author']) else None,
        row['playtime_at_review'] if pd.notna(row['playtime_at_review']) else None,
        row['timestamp_created'] if pd.notna(row['timestamp_created']) else None
    )

    cursor.execute("""
               INSERT INTO games_3d (name, genres, image, releasedate, price, reviewtext, reviewscore, language, author,playtime_at_review,timestamp_created)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """, data_tuple)
    

connection.commit()

# ------------------------------------------------------------------------------------
cursor.execute("""
               CREATE TABLE IF NOT EXISTS games_Action (
               name VARCHAR(255),
               genres VARCHAR(255),
               image VARCHAR(255),
               releasedate DATETIME,
               price INT,
               reviewtext LONGTEXT,
               reviewscore BOOL,
               language VARCHAR(255),
               author BIGINT ,
               playtime_at_review INT , 
               timestamp_created DATETIME
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example3 = pd.read_csv('Action.csv')


# 데이터베이스에 데이터 삽입
for index, row in Example3.iterrows():
    data_tuple = (
        row['game_name'] if pd.notna(row['game_name']) else None,
        row['game_genres'] if pd.notna(row['game_genres']) else None,
        row['game_image'] if pd.notna(row['game_image']) else None,
        row['game_release_date'] if pd.notna(row['game_release_date']) else None,  # NaT를 None으로 처리
        row['game_price'],
        row['review_text'] if pd.notna(row['review_text']) else None,
        row['review_score'] if pd.notna(row['review_score']) else None,
        row['language'] if pd.notna(row['language']) else None,
        row['author'] if pd.notna(row['author']) else None,
        row['playtime_at_review'] if pd.notna(row['playtime_at_review']) else None,
        row['timestamp_created'] if pd.notna(row['timestamp_created']) else None
    )

    cursor.execute("""
               INSERT INTO games_Action (name, genres, image, releasedate, price, reviewtext, reviewscore, language, author,playtime_at_review,timestamp_created)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """, data_tuple)
    

connection.commit()

# ------------------------------------------------------------------------------------
cursor.execute("""
               CREATE TABLE IF NOT EXISTS games_Adventure (
               name VARCHAR(255),
               genres VARCHAR(255),
               image VARCHAR(255),
               releasedate DATETIME,
               price INT,
               reviewtext LONGTEXT,
               reviewscore BOOL,
               language VARCHAR(255),
               author BIGINT ,
               playtime_at_review INT , 
               timestamp_created DATETIME
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example4 = pd.read_csv('Adventure.csv')


# 데이터베이스에 데이터 삽입
for index, row in Example4.iterrows():
    data_tuple = (
        row['game_name'] if pd.notna(row['game_name']) else None,
        row['game_genres'] if pd.notna(row['game_genres']) else None,
        row['game_image'] if pd.notna(row['game_image']) else None,
        row['game_release_date'] if pd.notna(row['game_release_date']) else None,  # NaT를 None으로 처리
        row['game_price'],
        row['review_text'] if pd.notna(row['review_text']) else None,
        row['review_score'] if pd.notna(row['review_score']) else None,
        row['language'] if pd.notna(row['language']) else None,
        row['author'] if pd.notna(row['author']) else None,
        row['playtime_at_review'] if pd.notna(row['playtime_at_review']) else None,
        row['timestamp_created'] if pd.notna(row['timestamp_created']) else None
    )

    cursor.execute("""
               INSERT INTO games_Adventure (name, genres, image, releasedate, price, reviewtext, reviewscore, language, author,playtime_at_review,timestamp_created)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """, data_tuple)

connection.commit()
# ------------------------------------------------------------------------------------
cursor.execute("""
               CREATE TABLE IF NOT EXISTS games_Atmospheric (
               name VARCHAR(255),
               genres VARCHAR(255),
               image VARCHAR(255),
               releasedate DATETIME,
               price INT,
               reviewtext LONGTEXT,
               reviewscore BOOL,
               language VARCHAR(255),
               author BIGINT ,
               playtime_at_review INT , 
               timestamp_created DATETIME
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example5 = pd.read_csv('Atmospheric.csv')


# 데이터베이스에 데이터 삽입
for index, row in Example5.iterrows():
    data_tuple = (
        row['game_name'] if pd.notna(row['game_name']) else None,
        row['game_genres'] if pd.notna(row['game_genres']) else None,
        row['game_image'] if pd.notna(row['game_image']) else None,
        row['game_release_date'] if pd.notna(row['game_release_date']) else None,  # NaT를 None으로 처리
        row['game_price'],
        row['review_text'] if pd.notna(row['review_text']) else None,
        row['review_score'] if pd.notna(row['review_score']) else None,
        row['language'] if pd.notna(row['language']) else None,
        row['author'] if pd.notna(row['author']) else None,
        row['playtime_at_review'] if pd.notna(row['playtime_at_review']) else None,
        row['timestamp_created'] if pd.notna(row['timestamp_created']) else None
    )

    cursor.execute("""
               INSERT INTO games_Atmospheric (name, genres, image, releasedate, price, reviewtext, reviewscore, language, author,playtime_at_review,timestamp_created)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """, data_tuple)

connection.commit()

# ------------------------------------------------------------------------------------
cursor.execute("""
               CREATE TABLE IF NOT EXISTS games_Casual (
               name VARCHAR(255),
               genres VARCHAR(255),
               image VARCHAR(255),
               releasedate DATETIME,
               price INT,
               reviewtext LONGTEXT,
               reviewscore BOOL,
               language VARCHAR(255),
               author BIGINT ,
               playtime_at_review INT , 
               timestamp_created DATETIME
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example6 = pd.read_csv('Casual.csv')


# 데이터베이스에 데이터 삽입
for index, row in Example6.iterrows():
    data_tuple = (
        row['game_name'] if pd.notna(row['game_name']) else None,
        row['game_genres'] if pd.notna(row['game_genres']) else None,
        row['game_image'] if pd.notna(row['game_image']) else None,
        row['game_release_date'] if pd.notna(row['game_release_date']) else None,  # NaT를 None으로 처리
        row['game_price'],
        row['review_text'] if pd.notna(row['review_text']) else None,
        row['review_score'] if pd.notna(row['review_score']) else None,
        row['language'] if pd.notna(row['language']) else None,
        row['author'] if pd.notna(row['author']) else None,
        row['playtime_at_review'] if pd.notna(row['playtime_at_review']) else None,
        row['timestamp_created'] if pd.notna(row['timestamp_created']) else None
    )

    cursor.execute("""
               INSERT INTO games_Casual (name, genres, image, releasedate, price, reviewtext, reviewscore, language, author,playtime_at_review,timestamp_created)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """, data_tuple)

connection.commit()

# ------------------------------------------------------------------------------------
cursor.execute("""
               CREATE TABLE IF NOT EXISTS games_co_op (
               name VARCHAR(255),
               genres VARCHAR(255),
               image VARCHAR(255),
               releasedate DATETIME,
               price INT,
               reviewtext LONGTEXT,
               reviewscore BOOL,
               language VARCHAR(255),
               author BIGINT ,
               playtime_at_review INT , 
               timestamp_created DATETIME
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example7 = pd.read_csv('co_op.csv')


# 데이터베이스에 데이터 삽입
for index, row in Example7.iterrows():
    data_tuple = (
        row['game_name'] if pd.notna(row['game_name']) else None,
        row['game_genres'] if pd.notna(row['game_genres']) else None,
        row['game_image'] if pd.notna(row['game_image']) else None,
        row['game_release_date'] if pd.notna(row['game_release_date']) else None,  # NaT를 None으로 처리
        row['game_price'],
        row['review_text'] if pd.notna(row['review_text']) else None,
        row['review_score'] if pd.notna(row['review_score']) else None,
        row['language'] if pd.notna(row['language']) else None,
        row['author'] if pd.notna(row['author']) else None,
        row['playtime_at_review'] if pd.notna(row['playtime_at_review']) else None,
        row['timestamp_created'] if pd.notna(row['timestamp_created']) else None
    )

    cursor.execute("""
               INSERT INTO games_co_op (name, genres, image, releasedate, price, reviewtext, reviewscore, language, author,playtime_at_review,timestamp_created)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """, data_tuple)

connection.commit()

# ------------------------------------------------------------------------------------
cursor.execute("""
               CREATE TABLE IF NOT EXISTS games_fisrt_person (
               name VARCHAR(255),
               genres VARCHAR(255),
               image VARCHAR(255),
               releasedate DATETIME,
               price INT,
               reviewtext LONGTEXT,
               reviewscore BOOL,
               language VARCHAR(255),
               author BIGINT ,
               playtime_at_review INT , 
               timestamp_created DATETIME
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example8 = pd.read_csv('first_person.csv')


# 데이터베이스에 데이터 삽입
for index, row in Example8.iterrows():
    data_tuple = (
        row['game_name'] if pd.notna(row['game_name']) else None,
        row['game_genres'] if pd.notna(row['game_genres']) else None,
        row['game_image'] if pd.notna(row['game_image']) else None,
        row['game_release_date'] if pd.notna(row['game_release_date']) else None,  # NaT를 None으로 처리
        row['game_price'],
        row['review_text'] if pd.notna(row['review_text']) else None,
        row['review_score'] if pd.notna(row['review_score']) else None,
        row['language'] if pd.notna(row['language']) else None,
        row['author'] if pd.notna(row['author']) else None,
        row['playtime_at_review'] if pd.notna(row['playtime_at_review']) else None,
        row['timestamp_created'] if pd.notna(row['timestamp_created']) else None
    )

    cursor.execute("""
               INSERT INTO games_fisrt_person (name, genres, image, releasedate, price, reviewtext, reviewscore, language, author,playtime_at_review,timestamp_created)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """, data_tuple)

connection.commit()

# ------------------------------------------------------------------------------------
cursor.execute("""
               CREATE TABLE IF NOT EXISTS games_Indie (
               name VARCHAR(255),
               genres VARCHAR(255),
               image VARCHAR(255),
               releasedate DATETIME,
               price INT,
               reviewtext LONGTEXT,
               reviewscore BOOL,
               language VARCHAR(255),
               author BIGINT ,
               playtime_at_review INT , 
               timestamp_created DATETIME
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example9 = pd.read_csv('Indie.csv')


# 데이터베이스에 데이터 삽입
for index, row in Example9.iterrows():
    data_tuple = (
        row['game_name'] if pd.notna(row['game_name']) else None,
        row['game_genres'] if pd.notna(row['game_genres']) else None,
        row['game_image'] if pd.notna(row['game_image']) else None,
        row['game_release_date'] if pd.notna(row['game_release_date']) else None,  # NaT를 None으로 처리
        row['game_price'],
        row['review_text'] if pd.notna(row['review_text']) else None,
        row['review_score'] if pd.notna(row['review_score']) else None,
        row['language'] if pd.notna(row['language']) else None,
        row['author'] if pd.notna(row['author']) else None,
        row['playtime_at_review'] if pd.notna(row['playtime_at_review']) else None,
        row['timestamp_created'] if pd.notna(row['timestamp_created']) else None
    )

    cursor.execute("""
               INSERT INTO games_Indie (name, genres, image, releasedate, price, reviewtext, reviewscore, language, author,playtime_at_review,timestamp_created)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """, data_tuple)

connection.commit()

# ------------------------------------------------------------------------------------
cursor.execute("""
               CREATE TABLE IF NOT EXISTS games_Multiplayer (
               name VARCHAR(255),
               genres VARCHAR(255),
               image VARCHAR(255),
               releasedate DATETIME,
               price INT,
               reviewtext LONGTEXT,
               reviewscore BOOL,
               language VARCHAR(255),
               author BIGINT ,
               playtime_at_review INT , 
               timestamp_created DATETIME
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example10 = pd.read_csv('Multiplayer.csv')


# 데이터베이스에 데이터 삽입
for index, row in Example10.iterrows():
    data_tuple = (
        row['game_name'] if pd.notna(row['game_name']) else None,
        row['game_genres'] if pd.notna(row['game_genres']) else None,
        row['game_image'] if pd.notna(row['game_image']) else None,
        row['game_release_date'] if pd.notna(row['game_release_date']) else None,  # NaT를 None으로 처리
        row['game_price'],
        row['review_text'] if pd.notna(row['review_text']) else None,
        row['review_score'] if pd.notna(row['review_score']) else None,
        row['language'] if pd.notna(row['language']) else None,
        row['author'] if pd.notna(row['author']) else None,
        row['playtime_at_review'] if pd.notna(row['playtime_at_review']) else None,
        row['timestamp_created'] if pd.notna(row['timestamp_created']) else None
    )

    cursor.execute("""
               INSERT INTO games_Multiplayer (name, genres, image, releasedate, price, reviewtext, reviewscore, language, author,playtime_at_review,timestamp_created)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """, data_tuple)

connection.commit()

# ------------------------------------------------------------------------------------
cursor.execute("""
               CREATE TABLE IF NOT EXISTS games_openworld (
               name VARCHAR(255),
               genres VARCHAR(255),
               image VARCHAR(255),
               releasedate DATETIME,
               price INT,
               reviewtext LONGTEXT,
               reviewscore BOOL,
               language VARCHAR(255),
               author BIGINT ,
               playtime_at_review INT , 
               timestamp_created DATETIME
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example11 = pd.read_csv('openworld.csv')


# 데이터베이스에 데이터 삽입
for index, row in Example11.iterrows():
    data_tuple = (
        row['game_name'] if pd.notna(row['game_name']) else None,
        row['game_genres'] if pd.notna(row['game_genres']) else None,
        row['game_image'] if pd.notna(row['game_image']) else None,
        row['game_release_date'] if pd.notna(row['game_release_date']) else None,  # NaT를 None으로 처리
        row['game_price'],
        row['review_text'] if pd.notna(row['review_text']) else None,
        row['review_score'] if pd.notna(row['review_score']) else None,
        row['language'] if pd.notna(row['language']) else None,
        row['author'] if pd.notna(row['author']) else None,
        row['playtime_at_review'] if pd.notna(row['playtime_at_review']) else None,
        row['timestamp_created'] if pd.notna(row['timestamp_created']) else None
    )

    cursor.execute("""
               INSERT INTO games_openworld (name, genres, image, releasedate, price, reviewtext, reviewscore, language, author,playtime_at_review,timestamp_created)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """, data_tuple)

connection.commit()

# ------------------------------------------------------------------------------------
cursor.execute("""
               CREATE TABLE IF NOT EXISTS games_RPG (
               name VARCHAR(255),
               genres VARCHAR(255),
               image VARCHAR(255),
               releasedate DATETIME,
               price INT,
               reviewtext LONGTEXT,
               reviewscore BOOL,
               language VARCHAR(255),
               author BIGINT ,
               playtime_at_review INT , 
               timestamp_created DATETIME
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example12 = pd.read_csv('RPG.csv')


# 데이터베이스에 데이터 삽입
for index, row in Example12.iterrows():
    data_tuple = (
        row['game_name'] if pd.notna(row['game_name']) else None,
        row['game_genres'] if pd.notna(row['game_genres']) else None,
        row['game_image'] if pd.notna(row['game_image']) else None,
        row['game_release_date'] if pd.notna(row['game_release_date']) else None,  # NaT를 None으로 처리
        row['game_price'],
        row['review_text'] if pd.notna(row['review_text']) else None,
        row['review_score'] if pd.notna(row['review_score']) else None,
        row['language'] if pd.notna(row['language']) else None,
        row['author'] if pd.notna(row['author']) else None,
        row['playtime_at_review'] if pd.notna(row['playtime_at_review']) else None,
        row['timestamp_created'] if pd.notna(row['timestamp_created']) else None
    )

    cursor.execute("""
               INSERT INTO games_RPG (name, genres, image, releasedate, price, reviewtext, reviewscore, language, author,playtime_at_review,timestamp_created)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """, data_tuple)

connection.commit()

# ------------------------------------------------------------------------------------
cursor.execute("""
               CREATE TABLE IF NOT EXISTS games_Simulation (
               name VARCHAR(255),
               genres VARCHAR(255),
               image VARCHAR(255),
               releasedate DATETIME,
               price INT,
               reviewtext LONGTEXT,
               reviewscore BOOL,
               language VARCHAR(255),
               author BIGINT ,
               playtime_at_review INT , 
               timestamp_created DATETIME
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example13 = pd.read_csv('Simulation.csv')


# 데이터베이스에 데이터 삽입
for index, row in Example13.iterrows():
    data_tuple = (
        row['game_name'] if pd.notna(row['game_name']) else None,
        row['game_genres'] if pd.notna(row['game_genres']) else None,
        row['game_image'] if pd.notna(row['game_image']) else None,
        row['game_release_date'] if pd.notna(row['game_release_date']) else None,  # NaT를 None으로 처리
        row['game_price'],
        row['review_text'] if pd.notna(row['review_text']) else None,
        row['review_score'] if pd.notna(row['review_score']) else None,
        row['language'] if pd.notna(row['language']) else None,
        row['author'] if pd.notna(row['author']) else None,
        row['playtime_at_review'] if pd.notna(row['playtime_at_review']) else None,
        row['timestamp_created'] if pd.notna(row['timestamp_created']) else None
    )

    cursor.execute("""
               INSERT INTO games_Simulation (name, genres, image, releasedate, price, reviewtext, reviewscore, language, author,playtime_at_review,timestamp_created)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """, data_tuple)

connection.commit()

# ------------------------------------------------------------------------------------
cursor.execute("""
               CREATE TABLE IF NOT EXISTS games_SinglePlayer (
               name VARCHAR(255),
               genres VARCHAR(255),
               image VARCHAR(255),
               releasedate DATETIME,
               price INT,
               reviewtext LONGTEXT,
               reviewscore BOOL,
               language VARCHAR(255),
               author BIGINT ,
               playtime_at_review INT , 
               timestamp_created DATETIME
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example14 = pd.read_csv('SinglePlayer.csv')


# 데이터베이스에 데이터 삽입
for index, row in Example14.iterrows():
    data_tuple = (
        row['game_name'] if pd.notna(row['game_name']) else None,
        row['game_genres'] if pd.notna(row['game_genres']) else None,
        row['game_image'] if pd.notna(row['game_image']) else None,
        row['game_release_date'] if pd.notna(row['game_release_date']) else None,  # NaT를 None으로 처리
        row['game_price'],
        row['review_text'] if pd.notna(row['review_text']) else None,
        row['review_score'] if pd.notna(row['review_score']) else None,
        row['language'] if pd.notna(row['language']) else None,
        row['author'] if pd.notna(row['author']) else None,
        row['playtime_at_review'] if pd.notna(row['playtime_at_review']) else None,
        row['timestamp_created'] if pd.notna(row['timestamp_created']) else None
    )

    cursor.execute("""
               INSERT INTO games_SinglePlayer (name, genres, image, releasedate, price, reviewtext, reviewscore, language, author,playtime_at_review,timestamp_created)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """, data_tuple)

connection.commit()

# ------------------------------------------------------------------------------------
cursor.execute("""
               CREATE TABLE IF NOT EXISTS games_story (
               name VARCHAR(255),
               genres VARCHAR(255),
               image VARCHAR(255),
               releasedate DATETIME,
               price INT,
               reviewtext LONGTEXT,
               reviewscore BOOL,
               language VARCHAR(255),
               author BIGINT ,
               playtime_at_review INT , 
               timestamp_created DATETIME
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example15 = pd.read_csv('story.csv')


# 데이터베이스에 데이터 삽입
for index, row in Example15.iterrows():
    data_tuple = (
        row['game_name'] if pd.notna(row['game_name']) else None,
        row['game_genres'] if pd.notna(row['game_genres']) else None,
        row['game_image'] if pd.notna(row['game_image']) else None,
        row['game_release_date'] if pd.notna(row['game_release_date']) else None,  # NaT를 None으로 처리
        row['game_price'],
        row['review_text'] if pd.notna(row['review_text']) else None,
        row['review_score'] if pd.notna(row['review_score']) else None,
        row['language'] if pd.notna(row['language']) else None,
        row['author'] if pd.notna(row['author']) else None,
        row['playtime_at_review'] if pd.notna(row['playtime_at_review']) else None,
        row['timestamp_created'] if pd.notna(row['timestamp_created']) else None
    )

    cursor.execute("""
               INSERT INTO games_story (name, genres, image, releasedate, price, reviewtext, reviewscore, language, author,playtime_at_review,timestamp_created)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """, data_tuple)

connection.commit()

# ------------------------------------------------------------------------------------
cursor.execute("""
               CREATE TABLE IF NOT EXISTS games_Strategy (
               name VARCHAR(255),
               genres VARCHAR(255),
               image VARCHAR(255),
               releasedate DATETIME,
               price INT,
               reviewtext LONGTEXT,
               reviewscore BOOL,
               language VARCHAR(255),
               author BIGINT ,
               playtime_at_review INT , 
               timestamp_created DATETIME
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example16 = pd.read_csv('Strategy.csv')


# 데이터베이스에 데이터 삽입
for index, row in Example16.iterrows():
    data_tuple = (
        row['game_name'] if pd.notna(row['game_name']) else None,
        row['game_genres'] if pd.notna(row['game_genres']) else None,
        row['game_image'] if pd.notna(row['game_image']) else None,
        row['game_release_date'] if pd.notna(row['game_release_date']) else None,  # NaT를 None으로 처리
        row['game_price'],
        row['review_text'] if pd.notna(row['review_text']) else None,
        row['review_score'] if pd.notna(row['review_score']) else None,
        row['language'] if pd.notna(row['language']) else None,
        row['author'] if pd.notna(row['author']) else None,
        row['playtime_at_review'] if pd.notna(row['playtime_at_review']) else None,
        row['timestamp_created'] if pd.notna(row['timestamp_created']) else None
    )

    cursor.execute("""
               INSERT INTO games_Strategy (name, genres, image, releasedate, price, reviewtext, reviewscore, language, author,playtime_at_review,timestamp_created)
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
               """, data_tuple)

connection.commit()

# 장르 테이블 작성 

cursor.execute("""
               CREATE TABLE IF NOT EXISTS gennres (
               genres VARCHAR(255) 
               );
               """) 
connection.commit()

cursor.execute("""
        INSERT INTO gennres (genres)
        VALUES ('2d'),('3d'),('action'),('adventure'),('atmospheric'),('casual'),('co_op'),('first_person')
               ,('indie'),('multiplayer'),('openworld'),('rpg'),('simulation'),('singleplayer'),('story'),('strategy')
        """)


connection.commit()

# 커서와 연결 종료
cursor.close()
connection.close()