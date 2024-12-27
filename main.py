import streamlit as st
from streamlit.elements.widgets.time_widgets import TimeInputSerde
with st.form('Chọn ngày trong tuần'):
  dates = ('Thứ Hai' , 'Thứ Ba' , 'Thứ Tư', 'Thứ Năm', 'Thứ Sáu')
  option_date = st.selectbox('Bạn muốn chọn cho ngày nào?', dates)
  tiets = ('1', '2', '3', '4', '5', '6', '7', '8')
  option_tiet = st.selectbox('Bạn thích chọn tiết mấy?', tiets)
  mons = ('Toán', 'Anh', 'Văn', 'Sử & địa', 'Khoa học', 'Giáo dục Thể chất', 'Bơi lội', 'Công nghệ', 'Giáo dục công dân', 'Giáo dục địa phương', 'Công nghệ', 'Công nghệ thông tin ')
  option_mon = st.selectbox('Bạn thích chọn môn nào?', mons)
  thoi_khoa_bieu = {'Ngày:' : option_date, 'Tiết:' : option_tiet, 'Môn:' : option_mon}
  submitted = st.form_submit_button("Xác nhận")
  if submitted:
    st.write('Bạn đã chọn:')
    for x,y in thoi_khoa_bieu.items():
      st.write(x,y)
print_thoi_khoa_bieu = st.checkbox('In thời khoá biểu')
if print_thoi_khoa_bieu:
  ans = ''
  for x in thoi_khoa_bieu:
    ans += str(x) + '' + str(thoi_khoa_bieu[x]) + '\n'
  st.download_button('In hoá đơn', ans)