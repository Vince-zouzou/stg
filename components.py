import streamlit as st
import pandas as pd
from utils import render_pagination
from config import MESSAGES, TRANSLATOR_CONFIG

def render_data_table(df, column_config, page_size=10, table_key="data_table", lang="en", show_buttons=False, button_callbacks=None):
    """
    渲染带分页和选择框的数据表格，支持按钮区域和固定列顺序
    :param df: 数据 DataFrame
    :param column_config: 表格列配置
    :param page_size: 每页显示条数
    :param table_key: 表格唯一键
    :param lang: 语言（en 或 zh）
    :param show_buttons: 是否显示按钮区域（用于 manage_eq.py）
    :param button_callbacks: 按钮回调函数字典，包含 create、edit、export
    :return: 编辑后的 DataFrame
    """
    # 初始化 session state
    if "page" not in st.session_state:
        st.session_state.page = 1
    if "page_size" not in st.session_state:
        st.session_state.page_size = page_size
    if "select_all" not in st.session_state:
        st.session_state.select_all = False
    if "selected_rows" not in st.session_state:
        st.session_state.selected_rows = pd.DataFrame(columns=df.columns)

    # 确保 selected 和 image 列存在并位于前两列
    if "selected" not in df.columns:
        df.insert(0, "selected", False)
    else:
        df = df[["selected"] + [col for col in df.columns if col != "selected"]]

    if "image" not in df.columns:
        df.insert(1, "image", "images/starteam-logo.png")
    else:
        df = df[["selected", "image"] + [col for col in df.columns if col not in ["selected", "image"]]]

    # 分页计算
    
    start_idx = (st.session_state.page - 1) * st.session_state.page_size
    end_idx = start_idx + st.session_state.page_size
    paginated_df = df.iloc[start_idx:end_idx].copy()

    # 按钮区域（仅 manage_eq.py）
    if show_buttons:
        col_buttons = st.columns(4)
        with col_buttons[0]:
            select_all = st.checkbox(MESSAGES[lang]["selectAll"], value=st.session_state.select_all, key=f"select_all_{table_key}")
        with col_buttons[1]:
            if st.button("创建新案例", key=f"create_{table_key}"):
                if button_callbacks and "create" in button_callbacks:
                    button_callbacks["create"]()
        with col_buttons[2]:
            if st.button("编辑 EQ", key=f"edit_{table_key}"):
                if button_callbacks and "edit" in button_callbacks:
                    button_callbacks["edit"](st.session_state.selected_rows)
        with col_buttons[3]:
            if st.button("导出 EQ", key=f"export_{table_key}"):
                if button_callbacks and "export" in button_callbacks:
                    button_callbacks["export"](st.session_state.selected_rows)
    else:
        select_all = st.checkbox(MESSAGES[lang]["selectAll"], value=st.session_state.select_all, key=f"select_all_{table_key}")

    # 更新全选状态
    if select_all:
        paginated_df["selected"] = True
        st.session_state.select_all = True
    else:
        paginated_df["selected"] = False
        st.session_state.select_all = False

    # 渲染表格
    with st.container():
        if paginated_df.empty:
            st.write(MESSAGES[lang]["noDataFound"])
            return paginated_df
        edited_df = st.data_editor(
            paginated_df,
            column_config=column_config,
            hide_index=True,
            use_container_width=True,
            key=table_key
        )

        # 更新全选状态
        if edited_df["selected"].all() and len(edited_df) > 0:
            st.session_state.select_all = True
        elif not edited_df["selected"].any():
            st.session_state.select_all = False

        # 更新 selected 列
        paginated_df["selected"] = edited_df["selected"]
        st.session_state.selected_rows = paginated_df[paginated_df["selected"] == True]
        #print(st.session_state.selected_rows)
        #st.rerun()

        return paginated_df

def render_filter_controls(filters, lang="en"):
    """
    渲染过滤控件
    :param filters: 过滤条件字典
    :param lang: 语言（en 或 zh）
    :return: 更新后的过滤条件
    """
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        filters["keyword"] = st.text_input(MESSAGES[lang]["searchKeyword"], value=filters.get("keyword", ""))
    with col2:
        filters["start_date"] = st.date_input("Start Date", value=filters.get("start_date"))
    with col3:
        filters["end_date"] = st.date_input("End Date", value=filters.get("end_date"))
    with col4:
        filters["status"] = st.selectbox(MESSAGES[lang]["allStatus"], ["", "1. EQ to customer", "2. EQ confirmed", "3. EQ completed"], index=0)
    with col5:
        filters["factory"] = st.selectbox(MESSAGES[lang]["allFactories"], ["", "JST", "TYN", "GZ", "SZ"])

    col6, col7, col8, col9 = st.columns(4)
    with col6:
        filters["item_code"] = st.text_input(MESSAGES[lang]["searchItemCode"], value=filters.get("item_code", ""))
    with col7:
        filters["engineer_team"] = st.selectbox(MESSAGES[lang]["engineerTeam"], ["", "Team A", "Team B", "Team C"])
    with col8:
        filters["engineer_name"] = st.selectbox(MESSAGES[lang]["engineerName"], ["", "John Doe", "Alice Chan", "Felix Zhang"])
    with col9:
        filters["cs_name"] = st.selectbox(MESSAGES[lang]["csName"], ["", "Emily Wong", "Chris Liu", "Nina Yeung"])

    return filters

def render_language_selector(lang="en"):
    """
    渲染翻译语言选择控件
    :param lang: 语言（en 或 zh）
    :return: 源语言、目标语言
    """
    col1, col2, col3 = st.columns([2, 1, 2])
    with col1:
        source_lang = st.selectbox(MESSAGES[lang]["sourceLang"], options=TRANSLATOR_CONFIG["languages"], index=0)
    with col3:
        target_lang = st.selectbox(MESSAGES[lang]["targetLang"], options=TRANSLATOR_CONFIG["languages"], index=2)

    return source_lang, target_lang