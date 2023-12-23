import streamlit as st
import numpy as np
from PIL import Image

# Streamlitアプリのタイトルを設定
st.title('RGB Random Noise Image Generator')

# ユーザーがサイズを指定できるように入力を受け取る
width = st.number_input('Enter width', min_value=1, value=768)
height = st.number_input('Enter height', min_value=1, value=768)

# 'Generate' ボタンを追加
if st.button('Generate'):
    # ランダムノイズ画像を生成
    noise = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    image = Image.fromarray(noise)

    # 画像を表示
    st.image(image, caption='Random RGB Noise Image', use_column_width=True)
