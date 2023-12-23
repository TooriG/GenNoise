import streamlit as st
import numpy as np
from PIL import Image
import io
import zipfile

# Streamlitアプリのタイトルを設定
st.title('Batch RGB Random Noise Image Generator')

# ユーザーが画像のサイズと枚数を指定できるように入力を受け取る
width = st.number_input('Enter width', min_value=1, value=768)
height = st.number_input('Enter height', min_value=1, value=768)
num_images = st.number_input('Enter number of images to generate', min_value=1, value=24)

# 生成された画像を格納するリスト
generated_images = []

# 'Generate' ボタンを追加
if st.button('Generate'):
    # 生成された画像を保存するためのバイト配列
    bytes_io = io.BytesIO()

    # ZIPファイルを作成
    with zipfile.ZipFile(bytes_io, 'w') as zip_file:
        for i in range(num_images):
            # ランダムノイズ画像を生成
            noise = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
            image = Image.fromarray(noise)
            generated_images.append(image)  # 画像をリストに追加
            img_byte_arr = io.BytesIO()
            image.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()

            # ZIPファイルに画像を追加
            zip_file.writestr(f'noise_image_{i+1}.png', img_byte_arr)

    # ダウンロードボタンを作成し、ユーザーがZIPファイルをダウンロードできるようにする
    st.download_button(
        label="Download Images as ZIP",
        data=bytes_io.getvalue(),
        file_name='noise_images.zip',
        mime='application/zip'
    )

    # 生成された画像を表示
    for idx, img in enumerate(generated_images, 1):
        st.image(img, caption=f'Image {idx}', use_column_width=True)
