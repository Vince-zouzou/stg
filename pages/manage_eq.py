import streamlit as st
import pandas as pd
from models import EQ
from config import MESSAGES, DATE_FORMAT
from utils import initial_page_config, filter_dataframe
from components import render_data_table, render_filter_controls

# 初始化页面
#initial_page_config("eq_search")

# 缓存示例数据
@st.cache_data
def load_eqs():
    return [
        EQ(id="057539", eqStatus="1. EQ to customer", prodData="For approval", paste="Required", last="days(5)", changed="2025-01-09", pn="QEN1007583-A00", techClass="Standard", spe="Sensodec SA", customer="Sensodec SA", endCustomer="NA–Not available", customerPN="527.1P1018", project="BH 4.5 Screw Compressor", factory="JST", selected=False, image="images/starteam-logo.png"),
        EQ(id="076263", eqStatus="1. EQ to customer", prodData="For record list", paste="", last="70", changed="2025-02-09", pn="QEN1002549-A03", techClass="Standard", spe="", customer="Clipped SA", endCustomer="NA–Not available", customerPN="1000C80200-1", project="BH 4.5 Screw Compressor", factory="JST", selected=False, image="images/starteam-logo.png"),
        EQ(id="076264", eqStatus="2. EQ confirmed", prodData="In progress", paste="Required", last="35", changed="2025-03-09", pn="QEN1002550-A01", techClass="Advanced", spe="MechCorp", customer="MechCorp GmbH", endCustomer="BioSolutions Ltd", customerPN="MC-2025-10", project="Medical Imaging System", factory="TYN", selected=False, image="images/starteam-logo.png"),
        EQ(id="076265", eqStatus="3. EQ completed", prodData="Completed", paste="", last="42", changed="2025-04-09", pn="QEN1002551-A02", techClass="Standard", spe="", customer="ElectroPro Inc", endCustomer="Automotive Solutions", customerPN="EP-5422-B", project="Electric Vehicle Controller", factory="GZ", selected=False, image="images/starteam-logo.png"),
        EQ(id="076266", eqStatus="1. EQ to customer", prodData="For approval", paste="Required", last="28", changed="2025-05-09", pn="QEN1002552-A00", techClass="Complex", spe="TechVision", customer="TechVision AG", endCustomer="Smart Home Solutions", customerPN="TV-2025-SH1", project="Smart Home Hub", factory="SZ", selected=False, image="images/starteam-logo.png")
    ]

# 加载数据
eqs = load_eqs()
df = pd.DataFrame([vars(eq) for eq in eqs])

# 函数：创建新案例
def create_new_case():
    """
    处理创建新案例的点击事件
    """
    st.switch_page("pages/create.py")

# 函数：编辑 EQ
def edit_eq(selected_rows):
    """
    处理编辑 EQ 的点击事件
    :param selected_rows: 选中的行数据
    """
    if len(selected_rows) == 1:
        st.switch_page("pages/create.py")
    else:
        st.error("请仅选择一个 EQ 进行编辑。")
# 函数：导出 EQ
def export_eq(selected_rows):
    """
    处理导出 EQ 的点击事件
    :param selected_rows: 选中的行数据
    """
    if not selected_rows.empty:
        with st.spinner(f"正在导出 {len(selected_rows)} 个 EQ..."):
            csv = selected_rows.to_csv(index=False)
            st.download_button(
                label="下载 CSV",
                data=csv,
                file_name="exported_eqs.csv",
                mime="text/csv",
                key="download_csv"
            )
            st.success(f"{len(selected_rows)} 个 EQ 已导出！")
    else:
        st.error("请至少选择一个 EQ 进行导出。")

# 过滤控件
st.subheader("搜索 EQ")
filters = {}
filters = render_filter_controls(filters, lang="zh-CN")

# 数据过滤
filtered_df = filter_dataframe(df, filters)

# 表格渲染
column_config = {
    "selected": st.column_config.CheckboxColumn("选择", default=False),
    "image": st.column_config.ImageColumn(label=MESSAGES["zh-CN"]["image"], width="medium"),
    "id": st.column_config.TextColumn("ID"),
    "eqStatus": st.column_config.TextColumn("EQ 状态"),
    "prodData": st.column_config.TextColumn("生产数据"),
    "paste": st.column_config.TextColumn("Paste"),
    "last": st.column_config.TextColumn("持续时间"),
    "changed": st.column_config.TextColumn("变更日期"),
    "pn": st.column_config.TextColumn("P/N"),
    "techClass": st.column_config.TextColumn("技术分类"),
    "spe": st.column_config.TextColumn("SPE"),
    "customer": st.column_config.TextColumn("客户"),
    "endCustomer": st.column_config.TextColumn("最终客户"),
    "customerPN": st.column_config.TextColumn("客户 P/N"),
    "project": st.column_config.TextColumn("项目"),
    "factory": st.column_config.TextColumn("工厂")
}

# 渲染表格，启用按钮区域
button_callbacks = {
    "create": create_new_case,
    "edit": edit_eq,
    "export": export_eq
}
edited_df = render_data_table(
    filtered_df,
    column_config,
    lang="zh-CN",
    table_key="eq_table",
    show_buttons=True,
    button_callbacks=button_callbacks
)

# 返回仪表板按钮
if st.button(MESSAGES["zh-CN"]["backToDashboard"]):
    st.write("正在跳转到仪表板...")