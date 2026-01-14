import streamlit as st
from PIL import Image
import numpy as np
import joblib
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans

# 1. Cấu hình trang - PHẢI ĐẶT ĐẦU TIÊN
st.set_page_config(page_title="AI Personal Color", layout="wide")

# 2. CSS CHUYÊN SÂU - Ẩn khung mặc định và tạo Glassmorphism
st.markdown("""
    <style>
    /* Ẩn các khoảng trắng thừa của Streamlit */
    .block-container {
        padding-top: 2rem !important;
        max-width: 95% !important;
    }

    /* Thiết lập nền Gradient động cho toàn trang */
    .stApp {
        background: radial-gradient(circle at top left, #e0eafc, #cfdef3);
    }

    /* Tạo khối Glassmorphism bao quanh toàn bộ nội dung */
    .main-card {
        background: rgba(255, 255, 255, 0.3);
        backdrop-filter: blur(25px);
        -webkit-backdrop-filter: blur(25px);
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 40px;
        padding: 50px;
        box-shadow: 0 25px 50px rgba(0,0,0,0.1);
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    /* Tiêu đề rực rỡ */
    .main-header {
        font-size: 3.5rem;
        font-weight: 900;
        text-align: center;
        background: linear-gradient(90deg, #FF4B4B, #FF8000);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 30px;
    }

    /* Kết quả mùa nổi bật */
    .season-result {
        color: #00796B;
        font-size: 4rem;
        font-weight: 800;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.05);
    }

    /* Thẻ màu Swatch kiểu mẫu */
    .swatch-item {
        height: 160px;
        width: 100%;
        border-radius: 20px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-weight: bold;
        text-shadow: 0 2px 5px rgba(0,0,0,0.3);
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
        margin-top: 20px;
    }

    /* Làm mượt ảnh tải lên */
    .stImage img {
        border-radius: 30px;
        box-shadow: 0 15px 30px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Tiêu đề
st.markdown('<div class="main-header">✨ Personal Color Analysis AI</div>', unsafe_allow_html=True)

# 4. Bố cục Layout 2 cột lớn
# Chúng ta bọc toàn bộ trong một container glassmorphism
st.markdown('<div class="main-card">', unsafe_allow_html=True)

col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.subheader("📸 Tải ảnh phân tích")
    uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"], label_visibility="collapsed")
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, use_container_width=True)
    else:
        # Placeholder nếu chưa có ảnh
        st.info("👈 Hãy tải ảnh chân dung rõ mặt lên nhé!")

with col_right:
    if uploaded_file:
        # Giả lập kết quả (Bạn thay bằng code dự đoán của mình)
        season = "Summer"

        st.markdown(f"<h3>Bạn thuộc mùa:</h3>", unsafe_allow_html=True)
        st.markdown(f'<div class="season-result">{season} 💎</div>', unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:1.2rem; color:#555;'>Dựa trên sắc tố da và mắt, đây là những màu sắc giúp bạn tỏa sáng nhất.</p>",
            unsafe_allow_html=True)

        st.write("---")

        # Bảng màu gợi ý
        st.markdown("<b>🎨 Palette gợi ý:</b>", unsafe_allow_html=True)
        palette = ["#ADD8E6", "#87CEFA", "#B0C4DE", "#E6E6FA", "#6B5B95"]
        cols = st.columns(len(palette))
        for i, color in enumerate(palette):
            with cols[i]:
                st.markdown(f'<div class="swatch-item" style="background-color: {color};">{color}</div>',
                            unsafe_allow_html=True)

        # Thêm các nút chức năng bên dưới
        st.markdown("<br>", unsafe_allow_html=True)
        btn_col1, btn_col2 = st.columns(2)
        with btn_col1:
            st.button("📥 Tải bảng màu PDF")
        with btn_col2:
            st.markdown("<p style='padding-top:10px;'>Chia sẻ: 🔵 📸 🐦</p>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Đóng main-card