# ─────────────────────────────────────────────────────────────────────────────
    # CSS PARA ROLAMENTO INDEPENDENTE (VERSÃO FORÇADA)
    # ─────────────────────────────────────────────────────────────────────────────
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        /* 1. Reset total da página e containers superiores */
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {{
            height: 100vh !important;
            overflow: hidden !important;
            margin: 0;
            padding: 0;
        }}

        /* 2. Seleciona o container das colunas e remove o scroll dele */
        [data-testid="stHorizontalBlock"] {{
            height: 100vh !important;
            overflow: hidden !important;
            gap: 0 !important;
        }}

        /* 3. A MÁGICA: Aplica scroll individual nos containers internos das colunas */
        [data-testid="column"]:nth-child(1) > div {{
            height: 100vh !important;
            overflow-y: auto !important;
            padding: 40px 24px !important;
            background-color: white;
            border-right: 1px solid #e2e8f0;
        }}

        [data-testid="column"]:nth-child(2) > div {{
            height: 100vh !important;
            overflow-y: auto !important;
            padding: 0 !important;
            background-color: #f1f5f9;
        }}

        /* 4. Esconde elementos padrão */
        [data-testid="stHeader"], [data-testid="stToolbarActions"],
        [data-testid="stDecoration"], footer {{ display: none !important; }}

        /* Estilo da imagem para garantir que ela não quebre o layout */
        .template-preview-img {{
            width: 100%;
            height: auto;
            display: block;
        }}

        /* Barra de rolagem personalizada (Opcional, mas fica mais bonito) */
        [data-testid="column"] > div::-webkit-scrollbar {{
            width: 6px;
        }}
        [data-testid="column"] > div::-webkit-scrollbar-thumb {{
            background: #cbd5e1;
            border-radius: 10px;
        }}
    </style>
    """, unsafe_allow_html=True)
