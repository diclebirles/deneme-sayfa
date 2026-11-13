import streamlit as st

st.title("Merhaba!")
st.write("Bu bizim ilk deneme sayfamız.")

isim = st.text_input("Adınız nedir?")
if isim:
    st.write("Hoş geldin,", isim)
sayi = st.slider("Bir sayı seçin", 1, 100, 50)
st.write("Seçtiğiniz sayının karesi:", sayi * sayi)
