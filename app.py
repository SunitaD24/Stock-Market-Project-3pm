import streamlit as st
from utils import StockAPI


def get_stock_api():
    return StockAPI

client = get_stock_api()

def search_company(company):
    return client.search_symbol(company)



#set the header title
st.set_page_config(page_title="Stock Market App")
