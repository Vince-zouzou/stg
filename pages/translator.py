import streamlit as st
import docx
import PyPDF2
from PIL import Image
import pytesseract
from models import TranslationResult
from config import MESSAGES, TRANSLATOR_CONFIG
from utils import initial_page_config
from components import render_language_selector

# 初始化页面
#initial_page_config("translator")

# 模拟翻译函数（无 API）
def mock_translate(text, source_lang, target_lang):
    """
    模拟翻译逻辑
    :param text: 输入文本
    :param source_lang: 源语言
    :param target_lang: 目标语言
    :return: TranslationResult 对象
    """
    if not text:
        return TranslationResult(source_text=text, translated_text="", source_lang=source_lang, target_lang=target_lang)
    # 模拟翻译：添加语言标签
    translated_text = f"[翻译] {text} (从 {source_lang} 到 {target_lang})"
    return TranslationResult(source_text=text, translated_text=translated_text, source_lang=source_lang, target_lang=target_lang)

# 缓存支持的文件类型和语言
@st.cache_data
def get_translator_config():
    """
    缓存翻译器配置
    :return: 文件类型和语言列表
    """
    return TRANSLATOR_CONFIG

# 标题
st.header("翻译器")

# 语言选择
source_lang, target_lang = render_language_selector(lang="zh-CN")

# 标签页
tab1, tab2, tab3, tab4 = st.tabs(["文本", "文档", "图片", "网页"])

# 文本翻译
with tab1:

    input_text = st.text_area(MESSAGES["zh-CN"]["inputText"], height=150, placeholder="在此输入...")
    if st.button(MESSAGES["zh-CN"]["translateText"]):
        with st.container():
            if input_text:
                with st.spinner("正在翻译..."):
                    result = mock_translate(input_text, source_lang, target_lang)
                    st.text_area("翻译结果:", value=result.translated_text, height=150)
            else:
                st.warning("请输入要翻译的文本。")

# 文档翻译
with tab2:

    uploaded_file = st.file_uploader(MESSAGES["zh-CN"]["uploadDocument"], type=TRANSLATOR_CONFIG["file_types"][:3])
    if uploaded_file and st.button(MESSAGES["zh-CN"]["translateDocument"]):
        with st.container():
            try:
                if uploaded_file.type == "application/pdf":
                    pdf_reader = PyPDF2.PdfReader(uploaded_file)
                    text = "".join([page.extract_text() for page in pdf_reader.pages])
                elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                    doc = docx.Document(uploaded_file)
                    text = "\n".join([para.text for para in doc.paragraphs])
                elif uploaded_file.type == "text/plain":
                    text = uploaded_file.read().decode("utf-8")
                else:
                    st.error("不支持的文件类型。")
                    text = None

                if text:
                    with st.spinner("正在翻译..."):
                        result = mock_translate(text, source_lang, target_lang)
                        st.text_area("翻译结果:", value=result.translated_text, height=300)
            except Exception as e:
                st.error(f"{MESSAGES['zh-CN']['translationFailed']}: {str(e)}")

# 图片翻译
with tab3:

    uploaded_image = st.file_uploader(MESSAGES["zh-CN"]["uploadImage"], type=TRANSLATOR_CONFIG["file_types"][3:])
    if uploaded_image and st.button(MESSAGES["zh-CN"]["translateImage"]):
        with st.container():
            try:
                image = Image.open(uploaded_image)
                text = pytesseract.image_to_string(image)
                if text:
                    with st.spinner("正在翻译..."):
                        result = mock_translate(text, source_lang, target_lang)
                        st.text_area("提取的文本:", value=text, height=150)
                        st.text_area("翻译结果:", value=result.translated_text, height=150)
                else:
                    st.warning(MESSAGES["zh-CN"]["noTextExtracted"])
            except Exception as e:
                st.error(f"{MESSAGES['zh-CN']['translationFailed']}: {str(e)}")

# 网页翻译
with tab4:

    url = st.text_input(MESSAGES["zh-CN"]["inputUrl"], placeholder="https://example.com")
    if url and st.button(MESSAGES["zh-CN"]["translateWeb"]):
        with st.container():
            # 模拟网页文本提取（无 API）
            text = f"模拟网页内容: {url}"
            with st.spinner("正在翻译..."):
                result = mock_translate(text, source_lang, target_lang)
                st.text_area("翻译结果:", value=result.translated_text, height=300)

# 使用说明
st.markdown(MESSAGES["zh-CN"]["usageInstructions"], unsafe_allow_html=True)