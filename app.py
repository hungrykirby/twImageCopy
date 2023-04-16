import os
import shutil
import pandas as pd

# CSVファイルの読み込み
csv_file = "images.csv"
df = pd.read_csv(csv_file)

# カレントディレクトリ内にoutputフォルダを作成
output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 画像をコピーし、ファイル名を変更
for index, row in df.iterrows():
    index_str = f"{row[0]:04}"  # ゼロ埋め4桁のindex
    image_path = row[1]  # 画像のパス
    _, ext = os.path.splitext(image_path)  # 画像の拡張子

    new_filename = f"{index_str}{ext}"  # 新しいファイル名
    new_path = os.path.join(output_folder, new_filename)  # 新しいパス

    shutil.copy(image_path, new_path)  # 画像をコピー

print("画像のコピーが完了しました。")
