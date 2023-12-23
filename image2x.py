import streamlit as st
import numpy as np
from PIL import Image

# Streamlitアプリのタイトル
st.title('RGBランダムノイズ画像生成器')

# ユーザーがサイズを指定できるように入力を受け取る
width = st.number_input('幅を入力してください', min_value=1, value=256)
height = st.number_input('高さを入力してください', min_value=1, value=256)

# ランダムノイズ画像を生成
noise = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
image = Image.fromarray(noise)

# 画像を表示
st.image(image, caption='ランダムRGBノイズ画像', use_column_width=True)
