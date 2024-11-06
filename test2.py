import streamlit as st
"규담 vs 현민"
who = st.radio(
    "누가 이길까요?",
    [":rainbow[갓규담]", "***현민***"],
    captions=[
        "규담이가 바름",
        "현민이가 이김",
    ],
)
import random
gwin = bool(random.randint(0,1))
if st.button("승부 예측 결과보기"):
    if who == ":rainbow[갓규담]":
        "규담 선택"
        if gwin :
            "맞췄습니다."
        else :
            "틀렸습니다."
    elif who == "***현민***":
        "현민 선택"
        if not gwin :
            "맞췄습니다."
        else :
            "틀렸습니다."
    else :
        "둘 중 하나는 선택해"
