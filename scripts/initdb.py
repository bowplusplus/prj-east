import pandas as pd
import duckdb

# テストデータのDataFrameを作成
data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "age": [25, 30, 35, 40, 45]
}
df = pd.DataFrame(data)

# DuckDBファイルへの接続（ファイルが存在しない場合は新規作成される）
con = duckdb.connect('test.duckdb')

# テーブルがまだ存在しない場合は作成
con.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name VARCHAR, age INTEGER)")

# DataFrameの各行をテーブルに挿入
# executemanyメソッドを使用
con.executemany("INSERT INTO users (id, name, age) VALUES (?, ?, ?)", df.values.tolist())

# 挿入したデータを確認
result = con.execute("SELECT * FROM users").fetchdf()
print(result)

# 接続を閉じる
con.close()
