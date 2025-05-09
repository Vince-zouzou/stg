# create.py
import streamlit as st
from datetime import datetime
import uuid
from utils import initial_page_config, initialize_session_state
from config import DATE_FORMAT

# 初始化页面
#initial_page_config("create_eq")

# 初始化 session state
initialize_session_state({
    "current_eq": None,
    "questions": []
})

def searching(final_description):
    pass

# 函数：渲染 Question 编辑界面
def render_question_form(index=None):
    with st.expander(f'问题 {index+1}', expanded=True):
        question = st.text_area("问题描述", value=st.session_state.questions[index].get("question", "") if index is not None else "", key=f"question_{index}")
        image = st.file_uploader("上传相关图片 (请注意Gerber File不可使用)", type=["jpg", "jpeg", "png"], key=f"image_{index}")
        if image is not None:
            st.image(image, caption="已上传图片", use_column_width=True)
        elif index is not None and st.session_state.questions[index].get("image"):
            for img in st.session_state.questions[index].get("image", []):
                st.image(img, caption="已上传图片", use_column_width=True)
        final_description = st.text_area("最终描述", value=st.session_state.questions[index].get("final_description", "") if index is not None else "", key=f"final_description_{index}")
        search = st.button("搜索", key=f"search_{index}")
        if search: searching(final_description)
        st.text_input("工程师建议", value=st.session_state.questions[index].get("answer", "") if index is not None else "", key=f"answer_{index}")
        attachments = st.file_uploader("附件", type=["jpg", "jpeg", "png"], key=f"attachments_{index}", accept_multiple_files=True)
        col0, col1 = st.columns(2)
        if col0.button("保存", key=f"save_{index}"):
            st.session_state.questions[index] = {
                "question": question,
                "image": [image] if image else [],
                "final_description": final_description,
                "answer": st.session_state.get(f"answer_{index}", "")
            }
        if col1.button("删除", key=f"delete_{index}"):
            if 0 <= index < len(st.session_state.questions):
                st.session_state.questions.pop(index)
                st.rerun()

# EQ Information Card
with st.container(border=True):
    st.subheader("EQ 信息")
    col1, col2 = st.columns(2)

    with col1:
        customer_name = st.text_input("客户名称", value=st.session_state.current_eq.get("customer_name", "") if st.session_state.current_eq else "")
        stg_pn = st.text_input("STG P/N", value=st.session_state.current_eq.get("stg_pn", "") if st.session_state.current_eq else "")
        factory_engineer = st.text_input("工厂工程师", value=st.session_state.current_eq.get("factory_engineer", "") if st.session_state.current_eq else "")
        via_options = [
            "绿油全塞：IPC 4761 Type VI-b,Plug with solder mask",
            "绿油半塞+全塞：IPC 4761 Type VI-a+b,Plug with solder mask",
            "树脂塞孔+电镀填平：IPC 4761 Type VII, Resin plugged and capped",
            "树脂塞孔+双面开窗：IPC 4761 Type V. Plug with resin",
            "没有塞孔：No via plugging needed"
        ]
        via_plugging_type = st.selectbox(
            "塞孔类型",
            via_options,
            index=via_options.index(st.session_state.current_eq.get("via_plugging_type", via_options[0])) if st.session_state.current_eq and st.session_state.current_eq.get("via_plugging_type") in via_options else 0
        )
        base_material = st.text_input("基材", value=st.session_state.current_eq.get("base_material", "") if st.session_state.current_eq else "")

    with col2:
        customer_pn = st.text_input("客户 P/N", value=st.session_state.current_eq.get("customer_pn", "") if st.session_state.current_eq else "")
        factory_pn = st.text_input("工厂 P/N", value=st.session_state.current_eq.get("factory_pn", "") if st.session_state.current_eq else "")
        issue_date = st.date_input(
            "日期",
            value=datetime.strptime(st.session_state.current_eq.get("issue_date", datetime.today().strftime(DATE_FORMAT)), DATE_FORMAT) if st.session_state.current_eq and st.session_state.current_eq.get("issue_date") else datetime.today()
        )
        panel_size = st.text_input("交货板尺寸 (mm*mm)", value=st.session_state.current_eq.get("panel_size", "") if st.session_state.current_eq else "")
        solder_mask = st.text_input("阻焊层", value=st.session_state.current_eq.get("solder_mask", "") if st.session_state.current_eq else "")

    status = st.session_state.current_eq.get("status", "Reviewing") if st.session_state.current_eq else "Reviewing"
    st.selectbox(
        "状态",
        ["Reviewing", "Pending", "Closed"],
        index=["Reviewing", "Pending", "Closed"].index(status),
        disabled=True
    )

# Question Part
with st.container(border=True, key="question_part"):
    for i in range(len(st.session_state.questions)):
        render_question_form(i)
    if st.button("添加问题"):
        st.session_state.questions.append({"question": "", "answer": ""})
        st.rerun()

# Export and Send
if st.button("导出并发送"):
    if not all([customer_name, customer_pn, stg_pn, factory_pn, factory_engineer, via_plugging_type, panel_size, base_material, solder_mask]):
        st.error("请填写所有必填字段。")
    elif not st.session_state.questions:
        st.error("请至少添加一个问题。")
    else:
        with st.spinner("正在导出并发送..."):
            if status == "Reviewing":
                st.session_state.current_eq = {
                    "id": f"EQ-{datetime.today().year}-{len(st.session_state.get('eq_list', [])) + 1:03d}",
                    "customer_name": customer_name,
                    "customer_pn": customer_pn,
                    "stg_pn": stg_pn,
                    "factory_pn": factory_pn,
                    "factory_engineer": factory_engineer,
                    "issue_date": issue_date.strftime(DATE_FORMAT),
                    "created_date": datetime.today().strftime(DATE_FORMAT),
                    "status": "Pending",
                    "questions": st.session_state.questions,
                    "via_plugging_type": via_plugging_type,
                    "panel_size": panel_size,
                    "base_material": base_material,
                    "solder_mask": solder_mask
                }
                st.session_state.setdefault("eq_list", []).append(st.session_state.current_eq)
                st.session_state.questions = []
                st.success("EQ 已导出并发送！")
            elif status == "Pending":
                st.success("待处理问题已导出！")
            elif status == "Closed":
                st.success("客户回复已保存！")

# 自动保存指示器
st.write(f"草稿已自动保存于: {datetime.now().strftime('%H:%M:%S')}")
