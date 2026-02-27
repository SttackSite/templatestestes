import streamlit as st

def render():
    # URL da imagem do seu template
    url_imagem_referencia = "https://raw.githubusercontent.com/SttackSite/site/main/1.png"

    # ─────────────────────────────────────────────────────────────────────────────
    # CSS PARA ROLAMENTO INDEPENDENTE FORÇADO
    # ─────────────────────────────────────────────────────────────────────────────
    st.markdown(f"""
    <style>
        /* 1. Trava o scroll da página principal */
        html, body, [data-testid="stAppViewContainer"] {{
            overflow: hidden !important;
            height: 100vh !important;
            margin: 0 !important;
            padding: 0 !important;
        }}

        /* 2. Configura o container das colunas para ocupar altura total */
        [data-testid="stHorizontalBlock"] {{
            height: 100vh !important;
        }}

        /* 3. Aplica scroll individual nos blocos internos das colunas */
        /* Selecionamos o primeiro container interno de cada coluna */
        [data-testid="column"]:nth-child(1) > div:first-child {{
            height: 100vh !important;
            overflow-y: auto !important;
            overflow-x: hidden !important;
            padding: 40px 24px !important;
            background-color: white !important;
            border-right: 1px solid #e2e8f0 !important;
        }}

        [data-testid="column"]:nth-child(2) > div:first-child {{
            height: 100vh !important;
            overflow-y: auto !important;
            overflow-x: hidden !important;
            padding: 0 !important;
            background-color: #f1f5f9 !important;
        }}

        /* Esconde elementos nativos do Streamlit */
        [data-testid="stHeader"], [data-testid="stToolbarActions"], 
        [data-testid="stDecoration"], footer {{ display: none !important; }}

        /* Estilo da Imagem Full */
        .template-preview-img {{
            width: 100%;
            display: block;
        }}

        /* Scrollbar elegante */
        [data-testid="column"] > div::-webkit-scrollbar {{ width: 6px; }}
        [data-testid="column"] > div::-webkit-scrollbar-thumb {{ background: #cbd5e1; border-radius: 10px; }}
        
        /* Ajustes de componentes editor */
        .panel-title {{ font-size: 18px; font-weight: 700; color: #1a1a2e; }}
        .section-label {{ font-size: 11px; font-weight: 700; text-transform: uppercase; color: #94a3b8; margin-top: 25px; border-bottom: 1px solid #f1f5f9; }}
    </style>
    """, unsafe_allow_html=True)

    # ─────────────────────────────────────────────────────────────────────────────
    # CONTEÚDO
    # ─────────────────────────────────────────────────────────────────────────────
    
    col_form, col_preview = st.columns([1, 2.5])

    with col_form:
        st.markdown('<div class="panel-title">✏️ Editor de Template</div>', unsafe_allow_html=True)
        st.markdown('<p style="color:#64748b; font-size:13px;">Template 1 — Agência Digital</p>', unsafe_allow_html=True)

        st.markdown('<div class="section-label">⚙️ Configuração Geral</div>', unsafe_allow_html=True)
        st.text_input("Título da aba", "Agência Digital", key="t_aba")
        st.color_picker("Cor principal", "#0066FF", key="c_pri")

        st.markdown('<div class="section-label">🦸 Hero Section</div>', unsafe_allow_html=True)
        st.text_input("Título Principal", "Transforme seu Negócio", key="t_hero")
        st.text_area("Descrição", "Soluções completas...", height=100, key="d_hero")

        # Gerando campos extras apenas para testar o scroll da esquerda
        for i in range(15):
            st.text_input(f"Campo extra {i+1}", key=f"extra_{i}")

        st.markdown("---")
        if st.button("✅ Finalizar e Enviar"):
            st.success("Enviado!")

    with col_preview:
        # Imagem com link do GitHub
        st.markdown(f'<img src="{url_imagem_referencia}" class="template-preview-img">', unsafe_allow_html=True)
