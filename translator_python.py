import cv2
from pyzbar.pyzbar import decode
import streamlit as st

# CSS styling for the app
st.markdown(
    """
    <style>
    .title {
        font-size: 36px;
        color: #333;
        text-align: center;
        margin-bottom: 50px;
    }
    .button {
        font-size: 18px;
        background-color: #4CAF50;
        color: white;
        padding: 12px 20px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        transition: background-color 0.3s;
    }
    .button:hover {
        background-color: #45a049;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def qr_code_scanner():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        a = 0
        decoded_objects = decode(gray)
        for obj in decoded_objects:
            a += 1
            st.success(obj.data.decode('utf-8'))
        if a != 0:
            break
    cap.release()
    cv2.destroyAllWindows()

# Streamlit app
st.markdown('<h1 class="title">QR Scanner</h1>', unsafe_allow_html=True)
if st.button("Scan", key="scan_button"):
    qr_code_scanner()
