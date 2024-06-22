import streamlit as st
import datetime
import pandas as pd
from vnstock3 import Vnstock

# add logo
st.image('https://upload.wikimedia.org/wikipedia/commons/7/77/Streamlit-logo-primary-colormark-darktext.png', width = 80)
st.title("Trang tổng quan")
st.markdown('---')

# add 2 columns layout
col1, col2 = st.columns(2)

with col1:
    # input stock symbol
    symbol = st.text_input('Enter a stock symbol', 'VCI')
## add date as the second

with col2:
    start_date= st.date_input("chọn ngày bắt đầu", datetime.date(2022,1,2)).strftime('%Y-%m-%d')
    
# datetime yesterday
yesterday = (datetime.date.today()-datetime.timedelta(days=1)).strftime('%Y-%m-%d')

st.write('start_date', start_date)
st.write('yesterday_date', yesterday)

# get stock data
stock = Vnstock().stock(symbol=symbol, source='VCI')
history_df = stock.quote.history(start=start_date, end=yesterday)

# conver time
history_df['time'] = pd.to_datetime(history_df['time'])
# set time to be index
history_df = history_df.set_index('time')

# price_chart= history_df.viz.combo(bar_data='volume',
#              line_data='close',
#              title='Giá đóng cửa và khối lượng giao dịch - Hợp đồng tương lai VN30F1M',
#              left_ylabel='Volume (M)', right_ylabel='Price (K)',
#              figsize=(10, 6),
#              color_palette='stock',
#              palette_shuffle=True)

line_col, bar_col = st.columns(2)


with line_col:
    # display the price_chart
    st.line_chart(history_df['close'])
with bar_col:
    # add a bar chart for volume
    st.bar_chart(history_df['volume'])


# add an expander
with st.expander("Xem du lieu"):
    st.dataframe(history_df)