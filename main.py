import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import uuid
from utils import  initialize_session_state,initial_page_config

#initial_page_config("EQ Management Dashboard")

# [Sample Data - 集中管理所有示例数据]
pending_eqs = [
    {"id": "PCB-2024-0128", "client": "Deltec DE, Furth (Wolf GmbH)", "date": "2024-01-28", "priority": "High", "color": "#ef4444"},
    {"id": "PCB-2024-0127", "client": "Siedle DE, Furtwangen", "date": "2024-01-27", "priority": "Medium", "color": "#facc15"},
    {"id": "PCB-2024-0126", "client": "ifm DE, Tettnang", "date": "2024-01-26", "priority": "Low", "color": "#34d399"},
]
recent_questions = pd.DataFrame([
    {"client": "Deltec DE, Furth", "question": "Outer layer Copper Thickness", "dueDate": "2024-02-01", "details": "Request clarification on copper thickness for outer layers (35µm or 70µm)."},
    {"client": "Siedle DE, Furtwangen", "question": "Propose to change the dielectric thickness", "dueDate": "2024-02-02", "details": "Suggest increasing dielectric thickness to 0.2mm for better insulation."},
    {"client": "ifm DE, Tettnang", "question": "To use soldermask Rongda H9100 8G01", "dueDate": "2024-02-03", "details": "Confirm compatibility of Rongda H9100 8G01 soldermask with current PCB design."},
])
status_data = {"Reviewing": 35, "Pending": 45, "Closed": 20}

# [Click Handler Function for Pending EQs]
def card_clicked(eq_id):
    """
    处理 Pending EQs 卡片点击事件，显示详细信息
    :param eq_id: 点击的 EQ ID
    """
    print('clicked', eq_id)



# [Main Content]
#st.markdown("<div style='padding: 24px;'>", unsafe_allow_html=True)

# [Pending EQs Section]
st.markdown("<h2 style='font-size: 1.25rem; font-weight: 600; margin-bottom: 16px;'>Pending EQs 待解决问题</h2>", unsafe_allow_html=True)
cols = st.columns(3)
for i, eq in enumerate(pending_eqs):
    with cols[i % 3]:
        with st.container():
            card_id = str(uuid.uuid4())
            st.markdown(f"""
                <div class='card' id='{card_id}' data-eq-id="{eq['id']}" onclick='window.StreamlitAPI.clickCard("{card_id}", this.dataset.eqId)'>
                    <div style='display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;'>
                        <p style='font-weight: 500;'>{eq['id']}</p>
                        <span style='background-color: {eq['color']}; color: white; padding: 2px 8px; border-radius: 4px; font-size: 12px;'>{eq['priority']}</span>
                    </div>
                    <p style='color: #4b5563; font-size: 14px;'>{eq['client']}</p>
                    <p style='color: #9ca3af; font-size: 12px;'>{eq['date']}</p>
                </div>
            """, unsafe_allow_html=True)
            # [Handle card click via session state]
            if st.session_state.get(f"card_clicked_{card_id}", False):
                card_clicked(eq['id'])
                # [Clear the state to allow re-clicking]
                st.session_state[f"card_clicked_{card_id}"] = False

# [EQ Status Tracking and Recent Questions]
col1, col2 = st.columns(2)

# [EQ Status Chart]
with col1:
    st.markdown("<h2 style='font-size: 1.25rem; font-weight: 600; margin-bottom: 16px;'>EQs Status Tracking 问题状态追踪</h3>", unsafe_allow_html=True)
    fig = go.Figure(data=[
        go.Pie(
            labels=list(status_data.keys()),
            values=list(status_data.values()),
            hole=0.75,
            marker_colors=["#fb923c", "#10b981", "#1e3a8a"],
            textinfo="label+percent",
            hoverinfo="label+percent+value"
        )
    ])
    fig.update_layout(
        showlegend=True,
        legend=dict(orientation="h", yanchor="bottom", y=-0.2, xanchor="center", x=0.5),
        margin=dict(t=0, b=0, l=0, r=0)
    )
    st.plotly_chart(fig, use_container_width=True)

# [Recent Questions List - 使用 st.expander 实现折叠/展开]
with col2:
    st.markdown("<h2 style='font-size: 1.25rem; font-weight: 600; margin-bottom: 16px;'>Recent Questions 最新问题展示</h3>", unsafe_allow_html=True)
    st.markdown("<div class='list-container'>", unsafe_allow_html=True)
    for idx, row in recent_questions.iterrows():
        with st.expander(row['client'], expanded=False):  # 空标题，样式通过 CSS 控制
            # [Expander 标题部分，使用 .list-item 样式]
            st.markdown(f"""
                <div class='list-item-content'>
                    <p class='client'> <strong>{row['client']}</strong></p>
                    <p class='due-date'>{row['dueDate']}</p>
                </div>
            """, unsafe_allow_html=True)
            # [Expander 内容部分，使用 .details 样式]
            st.markdown(f"""
                <div>
                    <p><strong>Detail:     </strong> {row['details']}</p>
                </div>
            """, unsafe_allow_html=True)
            col0,col1 = st.columns([4,1])
            col1.button("查看完整详情", key=f"view_details_{idx}", help="查看完整问题详情", on_click=card_clicked, args=(row['client'],))
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# [JavaScript for Pending EQs click handling]
st.html("""
    <script>
        window.StreamlitAPI = {
            clickCard: function(cardId, eqId) {
                // [Update session state for card click]
                window.parent.Streamlit.setComponentValue({ cardId: cardId, eqId: eqId });
                window.parent.Streamlit.navigationFrameChanged();
            }
        };
        // [Prevent multiple event bindings]
        if (!window.clickBound) {
            document.querySelectorAll('.card').forEach(card => {
                card.addEventListener('click', () => {
                    const cardId = card.id;
                    const eqId = card.dataset.eqId;
                    window.StreamlitAPI.clickCard(cardId, eqId);
                });
            });
            window.clickBound = true;
        }
    </script>
""")

# [Handle Pending EQs clicks]
if "clicked" in st.session_state:
    card_id = st.session_state.clicked.get("cardId")
    eq_id = st.session_state.clicked.get("eqId")
    if card_id and eq_id:
        st.session_state[f"card_clicked_{card_id}"] = True
        del st.session_state.clicked