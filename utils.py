# utils.py
import streamlit as st
import pandas as pd
from config import APP_CONFIG, MESSAGES, LANGUAGES, DATE_FORMAT

def initial_page_config(page_key):
    """
    初始化页面特定配置，包括 session state 和全局 CSS
    :param page_key: 页面键，用于确定当前页面
    """
    # 初始化 session state
    if "language" not in st.session_state:
        st.session_state.language = "zh-CN"  # 默认简体中文
    if "current_page" not in st.session_state:
        st.session_state.current_page = page_key  # 跟踪当前页面

    # 获取当前语言
    lang = st.session_state.language

    # 加载全局 CSS
    with open("styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def initialize_session_state(keys_defaults):
    """
    初始化 session state 键值对
    :param keys_defaults: 字典，包含键和默认值
    """
    for key, default in keys_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default

def render_pagination(total_items, page_size, page_key, lang="zh-CN"):
    """
    渲染分页控件
    :param total_items: 数据总条数
    :param page_size: 每页显示条数
    :param page_key: session state 中的页面键
    :param lang: 语言（zh-CN, zh-TW, de, en）
    :return: 总页数
    """
    total_pages = max(1, (total_items + page_size - 1) // page_size)
    col_prev, col_page, col_next, col_label, col_pages = st.columns([1, 2, 1, 2, 1])
    with col_prev:
        if st.button(MESSAGES[lang]["previous"], disabled=st.session_state[page_key] <= 1):
            st.session_state[page_key] -= 1
    with col_page:
        st.write(f"{MESSAGES[lang]['page']} {st.session_state[page_key]} {MESSAGES[lang]['of']} {total_pages}")
    with col_next:
        if st.button(MESSAGES[lang]["next"], disabled=st.session_state[page_key] >= total_pages):
            st.session_state[page_key] += 1
    with col_pages:
        st.write(MESSAGES[lang]["perPage"])
    with col_label:
        new_page_size = st.selectbox(
            MESSAGES[lang]["perPage"], [10, 20, 50, 100],
            index=[10, 20, 50, 100].index(st.session_state.get("page_size", page_size)),
            label_visibility='collapsed'
        )
        if new_page_size != st.session_state.get("page_size"):
            st.session_state.page_size = new_page_size
            st.session_state[page_key] = 1
    return total_pages

def filter_dataframe(df, filters, date_column="changed", date_format=DATE_FORMAT):
    """
    根据过滤条件筛选 DataFrame
    :param df: 输入 DataFrame
    :param filters: 字典，包含过滤条件
    :param date_column: 日期列名
    :param date_format: 日期格式
    :return: 筛选后的 DataFrame
    """
    filtered_df = df.copy()
    if filters.get("keyword"):
        mask = filtered_df[["customer", "customerPN", "project"]].apply(
            lambda x: x.str.contains(filters["keyword"], case=False, na=False)).any(axis=1)
        filtered_df = filtered_df[mask]
    if filters.get("item_code"):
        filtered_df = filtered_df[filtered_df["pn"].str.contains(filters["item_code"], case=False, na=False)]
    if filters.get("start_date"):
        filtered_df = filtered_df[pd.to_datetime(filtered_df[date_column], format=date_format) >= pd.to_datetime(filters["start_date"])]
    if filters.get("end_date"):
        filtered_df = filtered_df[pd.to_datetime(filtered_df[date_column], format=date_format) <= pd.to_datetime(filters["end_date"])]
    if filters.get("status"):
        filtered_df = filtered_df[filtered_df["eqStatus"] == filters["status"]]
    if filters.get("factory"):
        filtered_df = filtered_df[filtered_df["factory"] == filters["factory"]]
    return filtered_df