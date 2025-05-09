# config.py
# 页面配置
APP_CONFIG = {
    "page_layout": "wide",
    "logo_path": "images/starteam-logo.png",
    "logo_size": "Large",
    "pages": {
        "faq": {"title": "FAQ - STARTEAM Global"},
        "eq_search": {"title": "EQ Searching Page"},
        "create_eq": {"title": "Create EQ - STARTEAM Global"},
        "translator": {"title": "Create EQ - Translator"},
        "dashboard": {"title": "EQ Management Dashboard"}
    }
}

# 状态图标
STATUS_ICONS = {
    "Closed": "✅",
    "Pending": "🔄",
    "Reviewing": "⏳"
}

# 语言配置
LANGUAGES = {
    "zh-CN": "简体中文",
    "zh-TW": "繁體中文",
    "de": "Deutsch",
    "en": "English"
}

# 国际化消息
MESSAGES = {
    "zh-CN": {
        "searchKeyword": "搜索客户名称、客户 P/N...",
        "searchItemCode": "搜索项目代码/STG P/N...",
        "allStatus": "所有状态",
        "allFactories": "所有工厂",
        "engineerTeam": "工程师团队",
        "engineerName": "工程师姓名",
        "csName": "客服姓名",
        "noDataFound": "未找到数据",
        "previous": "上一页",
        "next": "下一页",
        "page": "页",
        "of": "共",
        "perPage": "每页",
        "backToDashboard": "返回仪表板",
        "selectAll": "全选",
        "image": "图片",
        "translateText": "翻译文本",
        "translateDocument": "翻译文档",
        "translateImage": "翻译图片",
        "translateWeb": "翻译网页",
        "sourceLang": "源语言",
        "targetLang": "目标语言",
        "swapLang": "交换语言",
        "inputText": "输入要翻译的文本...",
        "uploadDocument": "上传文档（.docx、.pdf、.txt）",
        "uploadImage": "上传图片（.jpg、.png）",
        "inputUrl": "输入网页 URL",
        "noTextExtracted": "未提取到文本",
        "translationFailed": "翻译失败",
        "usageInstructions": """
            **使用说明：**
            - 选择源语言和目标语言（或选择“自动检测”源语言）。
            - 在相应标签页中输入文本、上传文档、上传图片或输入网页 URL。
            - 点击相应的“翻译”按钮查看翻译结果。
            - 使用 🔄 按钮交换语言。
        """,
        "languageSelect": "选择语言",
        "createNewCase": "创建新案例",
        "editEQ": "编辑 EQ",
        "exportEQ": "导出 EQ",
        "eqInformation": "EQ 信息",
        "questionDescription": "问题描述",
        "uploadImage": "上传相关图片",
        "finalDescription": "最终描述",
        "engineerSuggestion": "工程师建议",
        "attachments": "附件",
        "save": "保存",
        "delete": "删除",
        "addQuestion": "添加问题",
        "exportAndSend": "导出并发送",
        "pendingIssues": "待解决问题",
        "statusTracking": "问题状态追踪",
        "recentQuestions": "最新问题展示",
        "viewDetails": "查看完整详情",
        "faq_title": "常见问题 - STARTEAM Global",
        "eq_search_title": "EQ 搜索页面",
        "create_eq_title": "创建 EQ - STARTEAM Global",
        "translator_title": "创建 EQ - 翻译器",
        "dashboard_title": "EQ 管理仪表板"
    },
    "zh-TW": {
        "searchKeyword": "搜尋客戶名稱、客戶 P/N...",
        "searchItemCode": "搜尋項目代碼/STG P/N...",
        "allStatus": "所有狀態",
        "allFactories": "所有工廠",
        "engineerTeam": "工程師團隊",
        "engineerName": "工程師姓名",
        "csName": "客服姓名",
        "noDataFound": "未找到資料",
        "previous": "上一頁",
        "next": "下一頁",
        "page": "頁",
        "of": "共",
        "perPage": "每頁",
        "backToDashboard": "返回儀表板",
        "selectAll": "全選",
        "image": "圖片",
        "translateText": "翻譯文本",
        "translateDocument": "翻譯文件",
        "translateImage": "翻譯圖片",
        "translateWeb": "翻譯網頁",
        "sourceLang": "源語言",
        "targetLang": "目標語言",
        "swapLang": "交換語言",
        "inputText": "輸入要翻譯的文本...",
        "uploadDocument": "上傳文件（.docx、.pdf、.txt）",
        "uploadImage": "上傳圖片（.jpg、.png）",
        "inputUrl": "輸入網頁 URL",
        "noTextExtracted": "未提取到文本",
        "translationFailed": "翻譯失敗",
        "usageInstructions": """
            **使用說明：**
            - 選擇源語言和目標語言（或選擇“自動檢測”源語言）。
            - 在相應標籤頁中輸入文本、上傳文件、上傳圖片或輸入網頁 URL。
            - 點擊相應的“翻譯”按鈕查看翻譯結果。
            - 使用 🔄 按鈕交換語言。
        """,
        "languageSelect": "選擇語言",
        "createNewCase": "創建新案例",
        "editEQ": "編輯 EQ",
        "exportEQ": "導出 EQ",
        "eqInformation": "EQ 資訊",
        "questionDescription": "問題描述",
        "uploadImage": "上傳相關圖片",
        "finalDescription": "最終描述",
        "engineerSuggestion": "工程師建議",
        "attachments": "附件",
        "save": "儲存",
        "delete": "刪除",
        "addQuestion": "新增問題",
        "exportAndSend": "導出並發送",
        "pendingIssues": "待解決問題",
        "statusTracking": "問題狀態追蹤",
        "recentQuestions": "最新問題展示",
        "viewDetails": "查看完整詳情",
        "faq_title": "常見問題 - STARTEAM Global",
        "eq_search_title": "EQ 搜尋頁面",
        "create_eq_title": "創建 EQ - STARTEAM Global",
        "translator_title": "創建 EQ - 翻譯器",
        "dashboard_title": "EQ 管理儀表板"
    },
    "de": {
        "searchKeyword": "Kundenname, Kunden P/N suchen...",
        "searchItemCode": "Artikelcode/STG P/N suchen...",
        "allStatus": "Alle Status",
        "allFactories": "Alle Werke",
        "engineerTeam": "Ingenieurteam",
        "engineerName": "Ingenieurname",
        "csName": "Kundendienstname",
        "noDataFound": "Keine Daten gefunden",
        "previous": "Vorherige",
        "next": "Nächste",
        "page": "Seite",
        "of": "von",
        "perPage": "pro Seite",
        "backToDashboard": "Zurück zum Dashboard",
        "selectAll": "Alle auswählen",
        "image": "Bild",
        "translateText": "Text übersetzen",
        "translateDocument": "Dokument übersetzen",
        "translateImage": "Bild übersetzen",
        "translateWeb": "Webseite übersetzen",
        "sourceLang": "Quellsprache",
        "targetLang": "Zielsprache",
        "swapLang": "Sprachen tauschen",
        "inputText": "Zu übersetzenden Text eingeben...",
        "uploadDocument": "Dokument hochladen (.docx, .pdf, .txt)",
        "uploadImage": "Bild hochladen (.jpg, .png)",
        "inputUrl": "Web-URL eingeben",
        "noTextExtracted": "Kein Text extrahiert",
        "translationFailed": "Übersetzung fehlgeschlagen",
        "usageInstructions": """
            **Gebrauchsanweisung:**
            - Wählen Sie die Quell- und Zielsprache (oder wählen Sie „Automatische Erkennung“ für die Quellsprache).
            - Geben Sie Text ein, laden Sie ein Dokument, ein Bild hoch oder geben Sie eine Web-URL in der entsprechenden Registerkarte ein.
            - Klicken Sie auf die entsprechende „Übersetzen“-Schaltfläche, um die Ergebnisse anzuzeigen.
            - Verwenden Sie die 🔄 Schaltfläche, um die Sprachen zu tauschen.
        """,
        "languageSelect": "Sprache wählen",
        "createNewCase": "Neuen Fall erstellen",
        "editEQ": "EQ bearbeiten",
        "exportEQ": "EQ exportieren",
        "eqInformation": "EQ-Informationen",
        "questionDescription": "Problem Beschreibung",
        "uploadImage": "Zusätzliche Bilder hochladen",
        "finalDescription": "Endgültige Beschreibung",
        "engineerSuggestion": "Vorschlag des Ingenieurs",
        "attachments": "Anhänge",
        "save": "Speichern",
        "delete": "Löschen",
        "addQuestion": "Frage hinzufügen",
        "exportAndSend": "Exportieren und senden",
        "pendingIssues": "Ausstehende Probleme",
        "statusTracking": "Statusverfolgung",
        "recentQuestions": "Neueste Fragen",
        "viewDetails": "Vollständige Details anzeigen",
        "faq_title": "Häufig gestellte Fragen - STARTEAM Global",
        "eq_search_title": "EQ-Suchseite",
        "create_eq_title": "EQ erstellen - STARTEAM Global",
        "translator_title": "EQ erstellen - Übersetzer",
        "dashboard_title": "EQ-Management-Dashboard"
    },
    "en": {
        "searchKeyword": "Search Customer Name, Customer P/N...",
        "searchItemCode": "Search Item Code/STG P/N...",
        "allStatus": "All Status",
        "allFactories": "All Factories",
        "engineerTeam": "Engineer Team",
        "engineerName": "Engineer Name",
        "csName": "CS Name",
        "noDataFound": "No data found",
        "previous": "Previous",
        "next": "Next",
        "page": "Page",
        "of": "of",
        "perPage": "per page",
        "backToDashboard": "Back to Dashboard",
        "selectAll": "Select All",
        "image": "Image",
        "translateText": "Translate Text",
        "translateDocument": "Translate Document",
        "translateImage": "Translate Image",
        "translateWeb": "Translate Web",
        "sourceLang": "Source Language",
        "targetLang": "Target Language",
        "swapLang": "Swap Languages",
        "inputText": "Input text to translate...",
        "uploadDocument": "Upload document (.docx, .pdf, .txt)",
        "uploadImage": "Upload image (.jpg, .png)",
        "inputUrl": "Input web URL",
        "noTextExtracted": "No text extracted",
        "translationFailed": "Translation failed",
        "usageInstructions": """
            **Usage Instructions:**
            - Select source and target languages (or choose "Auto Detect" for source).
            - Enter text, upload a document, upload an image, or input a web URL in the respective tab.
            - Click the corresponding "Translate" button to view results.
            - Use the 🔄 button to swap languages.
        """,
        "languageSelect": "Select Language",
        "createNewCase": "Create New Case",
        "editEQ": "Edit EQ",
        "exportEQ": "Export EQ",
        "eqInformation": "EQ Information",
        "questionDescription": "Question Description",
        "uploadImage": "Upload Related Images",
        "finalDescription": "Final Description",
        "engineerSuggestion": "Engineer Suggestion",
        "attachments": "Attachments",
        "save": "Save",
        "delete": "Delete",
        "addQuestion": "Add Question",
        "exportAndSend": "Export and Send",
        "pendingIssues": "Pending Issues",
        "statusTracking": "Status Tracking",
        "recentQuestions": "Recent Questions",
        "viewDetails": "View Full Details",
        "faq_title": "FAQ - STARTEAM Global",
        "eq_search_title": "EQ Searching Page",
        "create_eq_title": "Create EQ - STARTEAM Global",
        "translator_title": "Create EQ - Translator",
        "dashboard_title": "EQ Management Dashboard"
    }
}

# 日期格式
DATE_FORMAT = "%Y-%m-%d"

# 翻译相关配置
TRANSLATOR_CONFIG = {
    "languages": ["Auto Detect", "English", "Chinese (Simplified)", "German", "French", "Japanese"],
    "file_types": ["docx", "pdf", "txt", "jpg", "png"]
}