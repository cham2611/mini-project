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
               reviewscore VARCHAR(255),
               language VARCHAR(255)
               );
               """) 
connection.commit()

# 데이터프레임을 읽어옵니다.
Example = pd.read_csv('ex1.csv')

# 데이터프레임의 날짜 열 변환 함수 정의
def parse_date(date_str):
    try:
        # 'Sep 19, 2024' 형식
        return pd.to_datetime(date_str, format='%b %d, %Y')
    except ValueError:
        pass
    try:
        # '19 Sep, 2024' 형식
        return pd.to_datetime(date_str, format='%d %b, %Y')
    except ValueError:
        pass
    return pd.NaT  # 변환할 수 없는 경우 NaT 반환


# 데이터프레임의 날짜 열 변환
Example['game_release_date'] = Example['game_release_date'].apply(parse_date)



# 숫자만 추출하는 함수
def extract_numbers(price_str):
    if isinstance(price_str, str):  # price_str이 문자열인지 확인
        # 숫자를 저장할 빈 문자열
        numbers = ''
        
        # 문자열을 하나씩 검사
        for char in price_str:
            # 각 문자가 숫자이거나 쉼표일 경우
            if char.isdigit() or char == ',':
                # numbers 문자열에 추가
                numbers += char
                
        # 쉼표를 제거하고 숫자 문자열을 정수로 변환
        return int(numbers.replace(',', '')) if numbers else 0  # 가격 정보가 없을 경우 0 반환
    return 0  # 문자열이 아닐 경우 0 반환

# 'game_price' 열 변환
Example['game_price'] = Example['game_price'].replace('가격 정보 없음', '0')  # 가격 정보가 없는 경우 0으로 대체
Example['game_price'] = Example['game_price'].apply(extract_numbers)  # 각 가격 문자열에 대해 함수 적용




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