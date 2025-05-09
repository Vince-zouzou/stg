import streamlit as st
from collections import Counter
from models import FAQ
from config import STATUS_ICONS, MESSAGES, APP_CONFIG
from utils import initial_page_config, initialize_session_state
from datetime import datetime

# 初始化页面
#initial_page_config("faq")

# 获取当前语言
lang = st.session_state.get("language", "zh-CN")

# 缓存示例数据
@st.cache_data
def load_faqs():
    return [
        FAQ(similarity=95, question="HDI板层压工艺中，如何优化压合温度曲线以提高产品良率？", date="2024-01-15", customer="Siedle", status="Closed", stg="STG-1001", image="images/starteam-logo.png", questions="Q-1001"),
        FAQ(similarity=88, question="高频PCB阻抗测试中出现较大偏差，可能的原因及解决方案？", date="2024-01-15", customer="Deltec", status="Pending", stg="STG-2001", image=["images/starteam-logo.png", "images/starteam-logo.png"], questions="Q-1001"),
        FAQ(similarity=82, question="多层板钻孔后出现毛刺，如何调整工艺参数？", date="2024-01-14", customer="ifm", status="Pending", stg="STG-3002", image=None, questions="Q-1001"),
        FAQ(similarity=80, question="层压后出现鼓包的原因分析？", date="2024-01-14", customer="Others", status="Closed", stg="STG-4003", image="images/starteam-logo.png", questions="Q-1001"),
        FAQ(similarity=90, question="沉金工艺中出现颜色不均匀的问题，如何优化？", date="2024-01-13", customer="Pilz", status="Reviewing", stg="STG-5004", image=["images/starteam-logo.png", "images/starteam-logo.png", "images/starteam-logo.png"], questions="Q-1001"),
    ]

faqs = load_faqs()

# 初始化 session state
initialize_session_state({"selected_customer": "All Customers"})

# 两列布局
col1, col2 = st.columns([1, 3])

# 左侧列：客户筛选
with col1:
    st.header("按客户筛选")
    customer_counts = Counter([faq.customer for faq in faqs])
    top_customers = customer_counts.most_common(5)
    unique_customers = list(set([faq.customer for faq in faqs]))

    selected_customer = st.selectbox(
        "选择客户", 
        ["All Customers"] + unique_customers, 
        index=0 if st.session_state.selected_customer == "All Customers" else unique_customers.index(st.session_state.selected_customer) + 1,
        key="customer_select"
    )
    
    if selected_customer != st.session_state.selected_customer:
        st.session_state.selected_customer = selected_customer
        st.rerun()

    for customer, count in top_customers:
        if st.button(f"{customer} ({count})", key=f"btn_{customer}"):
            st.session_state.selected_customer = customer
            st.rerun()

# 右侧列：FAQ 内容
with col2:
    # 使用 MESSAGES 中的 faq_title，若不存在则回退到 APP_CONFIG
    title = MESSAGES[lang].get("faq_title", APP_CONFIG["pages"]["faq"]["title"])
    st.title(title)

    # 过滤栏
    filter_col1, filter_col2, filter_col3, filter_col4, filter_col5 = st.columns([2, 2, 2, 2, 2])
    with filter_col1:
        keyword = st.text_input("关键词", key="keyword")
    with filter_col2:
        start_date = st.date_input("开始日期", value=None, key="start_date")
    with filter_col3:
        end_date = st.date_input("结束日期", value=None, key="end_date")
    with filter_col4:
        status = st.selectbox("状态", ["All Statuses", "Closed", "Pending", "Reviewing"], key="status")
    with filter_col5:
        stg_pn = st.text_input("STG P/N", key="stg_pn")
    
    search_button = st.button("🔍 搜索", key="search_button")

    # 筛选 FAQ
    filtered_faqs = faqs
    if st.session_state.selected_customer != "All Customers":
        filtered_faqs = [faq for faq in filtered_faqs if faq.customer == st.session_state.selected_customer]
    if keyword:
        filtered_faqs = [faq for faq in filtered_faqs if keyword.lower() in faq.question.lower()]
    if start_date:
        filtered_faqs = [faq for faq in filtered_faqs if datetime.strptime(faq.date, "%Y-%m-%d").date() >= start_date]
    if end_date:
        filtered_faqs = [faq for faq in filtered_faqs if datetime.strptime(faq.date, "%Y-%m-%d").date() <= end_date]
    if status != "All Statuses":
        filtered_faqs = [faq for faq in filtered_faqs if faq.status == status]
    if stg_pn:
        filtered_faqs = [faq for faq in filtered_faqs if stg_pn.lower() in faq.stg.lower()]

    # 延迟加载 FAQ 内容
    with st.container():
        if filtered_faqs:
            for faq in filtered_faqs:
                with st.expander(f"{faq.question} - 相似度: {faq.similarity}%"):
                    st.markdown(f"""
                        <div class="faq-card">
                            <div class="details">
                                <span>{faq.date}</span> | 
                                <span>客户：{faq.customer}</span> | 
                                <span>状态：{faq.status} {STATUS_ICONS[faq.status]}</span> | 
                                <span>STG P/N：{faq.stg}</span>
                            </div>
                            <div class="details">{faq.questions}</div>
                        </div>
                    """, unsafe_allow_html=True)
                    
                    if faq.image:
                        if isinstance(faq.image, list):
                            for img in faq.image:
                                st.image(img, caption="FAQ Image")
                        else:
                            st.image(faq.image, caption="FAQ Image")
        else:
            st.write(MESSAGES[lang]["noDataFound"])