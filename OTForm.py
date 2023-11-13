import streamlit as st
import datetime

sites = ('高雄', '公司', '南科', '台中', '美光', '新竹', '林口')
st.title(':male-mechanic:裝機輸入表單:male-mechanic:')

title = st.text_input('', placeholder='地點 機台名稱 裝機/拉線 ex.台中台積MDP裝機', label_visibility='hidden')
d = st.date_input('出工日期', datetime.date.today(), format='YYYY/MM/DD')
got = st.time_input('出發時間', datetime.time(9, 0), step=300)
ont = st.time_input('進廠時間', datetime.time(9, 30), step=300)
offt = st.time_input('離廠時間', datetime.time(18, 0), step=300)
ot = st.number_input('OT', min_value=0.0, step=0.5)
if ot == 0.0:
    ot = ''
rest = ''
if st.checkbox('中午未休息?'):
    rest = st.radio('', ['休半時', '未休息'], label_visibility='collapsed')
lunch = st.radio('餐費', [1, 2], index=0)
night = st.checkbox('過夜')
night = 1 if night else ''
if night:
    hotel = st.text_input('請輸入飯店名稱', placeholder='ex.豪美商旅')
else:
    hotel = ''
# open staff txt file
slist = []
with open('staff.txt', 'r', encoding='UTF-8') as file_object:
    staff = file_object.readlines()
    for s in staff:
        slist.append(s.strip('\n'))
    drivers = ' '.join(st.multiselect('開車人員', slist))
    siton = ' '.join(st.multiselect('坐車人員', slist))
    goself = ' '.join(st.multiselect('自行出發', slist))

col1, col2, col3 = st.columns(3)
with col1:
    site1 = st.selectbox('地點1', sites, index=1, key='公司')
with col2:
    site2 = st.selectbox('地點2', sites, index=2, key='南科')
with col3:
    way = st.radio('', ['去程', '回程', '來回'], label_visibility='collapsed')
remark = st.text_area('備註')
st.divider()
content = f'{title}\n'\
           f'日期:{d.strftime("%m/%d")}\n'\
           f'出發:{got.strftime("%H:%M")}\n'\
           f'進廠:{ont.strftime("%H:%M")}\n'\
           f'離廠:{offt.strftime("%H:%M")}\n'\
           f'OT:{ot}\n'\
           f'餐費:{lunch}\n'\
           f'住宿:{night}\n'\
           f'坐車:{siton}\n'\
           f'開車:{drivers}\n'\
           f'自行前往:{goself}\n'\
           f'里程:{site1}-{site2} {way}\n'\
           f'備註:中午{rest} {hotel} {remark}\n'

st.code(content, language='basic')
