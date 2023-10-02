import streamlit as st
import datetime

sites = ('高雄', '公司', '南科', '台中', '美光', '新竹', '林口')
st.title('這是一個裝機輸入表單')

d = st.date_input('出工日期', datetime.date.today(), format='YYYY/MM/DD')
got = st.time_input('出發時間', datetime.time(9, 0), step=300)
ont = st.time_input('進廠時間', datetime.time(9, 30), step=300)
offt = st.time_input('離廠時間', datetime.time(18, 0), step=300)
lunch = st.radio('餐費', [100, 200], index=0)
night = st.checkbox('過夜')
if night:
    hotel = st.text_input('請輸入飯店名稱', placeholder='ex.豪美商旅')
else:
    hotel = ''
# open staff csv ile
slist = []
with open('staff.txt', 'r', encoding='UTF-8' ) as file_object:
    staff = file_object.readlines()
    for s in staff:
        slist.append(s.strip('\n'))
    drivers = st.multiselect('開車人員', slist)
    siton = st.multiselect('坐車人員', slist)
    goself = st.multiselect('自行出發', slist)

col1, col2, col3 = st.columns(3)
with col1:
   site1 = st.selectbox('地點1', sites, index=1, key='公司')
with col2:
   site2 = st.selectbox('地點2', sites, index=2, key='南科')
with col3:
   way = st.radio('', ['去程', '回程', '來回'], label_visibility='collapsed')

st.write(f'test component: {d.strftime("%Y/%m/%d"), got.strftime("%H:%M"), ont.strftime("%H:%M"), offt.strftime("%H:%M"), lunch, night, hotel, drivers, siton, goself, site1, site2, way}')
