import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

#Load datasets
hour_df = pd.read_csv('/Users/zoyavyraa/Downloads/hour_cleaned.csv')
day_df = pd.read_csv('/Users/zoyavyraa/Downloads/day_cleaned.csv')

#Judul aplikasi
st.title("Analisis Penyewaan Sepeda")

#Membuat selectbox
selected_option = st.selectbox("Home", ["Datasets", "Analysis", "Conclusion"])

if selected_option == "Datasets":

    tab1, tab2 = st.tabs(["Hour Dataset", "Day Dataset"])
    with tab1:
        st.write(hour_df)
        if st.button("Tampilkan Rangkuman Parameter"):
            st.image('/Users/zoyavyraa/Desktop/Rangkuman parameter hour.png')


    with tab2:
        st.write(day_df)
        if st.button("Tampilkan Rangkuman Parameter "):
            st.image('/Users/zoyavyraa/Desktop/Rangkuman parameter day.png')

elif selected_option == "Analysis":

    col1, col2 = st.columns(2)
    with col1:
        st.write(
            '''
            Kategori Musim:
            1. Spring
            2. Summer
            3. Fall
            4. Winter
            '''
        )

    with col2:
        st.write(
            '''
            Kategori Cuaca
            1. Clear
            2. Mist
            3. Light Rain
            4. Heavy Rain/Snow
            '''
        )
    st.header("Analisis Untuk Melihat Bagaimana Musim Mempengaruhi Sepeda:")

    st.divider()
    st.subheader("**Hasil Analisis**:")
    st.write(pd.DataFrame({
        "Jumlah Penyewa": ["", 471.348, 918.589, "1.061.129", 841.613],
        "Cuaca Terbanyak": ["", "Clear", "Clear", "Clear", "Clear"],
    }))
    chart_data = pd.DataFrame({
        "Season": ["Spring", "Summer", "Fall", "Winter"],
        "Value": [1.402, 1.297, 1.477, 1.408],
    })
    st.bar_chart(chart_data.set_index("Season"))

    with st.expander("**Penjelasan**"):
        st.write(
                """
                Pelanggan terbanyak sebesar 1.061.229 adalah di musim gugur (Fall), 
                 dan rata-rata cuaca cerah menjadi favorit pelanggan
                 """)
        
    st.divider()
    st.header("Analisis Untuk Melihat Hari Pelanggan Menyewa Sepeda:")

    col1, col2 = st.columns(2)
    with col1: 
        st.write("Hari Libur")
        st.write(pd.DataFrame({
        "Nama Hari": ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"],
        "Jumlah Penyewa": [105, 15, 1, 1, 2, 2, 105],
    }))
        st.write("Total: 213 Penyewa")

    with col2: 
        st.write("Hari Kerja")
        st.write(pd.DataFrame({
        "Nama Hari": ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"],
        "Jumlah Penyewa": [90, 103, 103, 102, 102, 0, 0],
    }))
        st.write("Total: 500 Penyewa")
    
    chart_data = pd.DataFrame({
    "Day": ["Hari Kerja Minggu", "Hari Kerja Senin", "Hari Kerja Selasa", "Hari Kerja Rabu", "Hari Kerja Kamis", "Hari Kerja Jumat", "Hari Kerja Sabtu",
            "Hari Libur Minggu", "Hari Libur Senin", "Hari Libur Selasa", "Hari Libur Rabu", "Hari Libur Kamis", "Hari Libur Jumat", "Hari Libur Sabtu"],
    "Value": [90, 103, 103, 102, 102, 0, 0, 105, 15, 1, 1, 2, 2, 105]
    })

# Mengatur "Day" sebagai indeks DataFrame
    chart_data.set_index("Day", inplace=True)

# Menampilkan line chart
    st.line_chart(chart_data)

    with st.expander("**Penjelasan**"):
        st.write("""
                 Pelanggan lebih memilih untuk merental di hari kerja,
                 dengan hari terbanyak di Senin-Kamis
                 """
                 )

elif selected_option == "Conclusion":
    st.markdown(
            """
            Berdasarkan seluruh analisis yang telah dilakukan, untuk menjawab pertanyaan berikut:
            1. Bagaimana tren penggunaan sepeda dipengaruhi oleh perubahan cuaca dan musim?
                Berdasarkan analisis yang telah dilakukan, didapati hasil bahwa perentalan terbanyak pada periode 2011 hingga 2012, dilakukan pada musim ke 3 atau musim gugur (Fall), dengan jumlah total sepeda sebanyak 1.061.129 buah. Diikuti dengan kedua terbanyak di musim panas sebanyak 918.589 buah sepeda, kemudian musim salju dengan 841.613 buah sepeda, dan yang terakhir pada musim semi dengan 471.348 buah sepeda. Kemudian rata-rata orang merental sepeda di cuaca cerah (clear). Sehingga, dapat disimpulkan bahwa musim dan cuaca memiliki pengaruh signifikan.
            2.  Bagaimana pengaruh penyewaan sepeda pada hari kerja dan pada bukan hari kerja?
            Berdasarkan analisis perbandingan antara perentalan sepeda pada hari kerja dan bukan hari kerja, dari total keseluruhan 731 hari,didapatkan bahwa sebanyak 500 hari pelanggan merental sepeda di hari kerja daripada pelanggan merental sepeda di hari libur, sebanyak 231 hari sepeda keluar. Hari kerja di mulai Senin-Kamis rata-rata banyak pelanggan merental sepeda, namun pada hari libur, rata-rata pelangggan merental sepeda di hari Minggu dan Jumat Kesimpulannya, lebih banyak orang merental sepeda di hari kerja pada Senin-Kamis daripada di hari libur pada Minggu dan Jumat.
            """
                )
