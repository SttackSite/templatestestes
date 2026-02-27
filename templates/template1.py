import streamlit as st

def render():
    # URL da imagem do seu template
    url_imagem_referencia = "https://raw.githubusercontent.com/SttackSite/site/main/1.png"

    # ─────────────────────────────────────────────────────────────────────────────
    # CSS PARA ROLAMENTO INDEPENDENTE (FIX)
    # ─────────────────────────────────────────────────────────────────────────────
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        /* 1. Remove o scroll da página principal e remove paddings extras */
        html, body, [data-testid="stAppViewContainer"] {{
            overflow: hidden !important;
            height: 100vh;
            margin: 0;
            padding: 0 !important;
        }}

        /* 2. Força o container das colunas a ocupar a tela cheia */
        [data-testid="stHorizontalBlock"] {{
            height: 100vh;
            gap: 0 !important;
        }}

        /* 3. Estilização da Coluna 1 (Editor) */
        [data-testid="column"]:nth-child(1) {{
            height: 100vh !important;
            overflow-y: auto !important;
            padding: 30px 24px !important;
            background-color: white;
            border-right: 1px solid #e2e8f0;
        }}

        /* 4. Estilização da Coluna 2 (Preview Imagem) */
        [data-testid="column"]:nth-child(2) {{
            height: 100vh !important;
            overflow-y: auto !important;
            padding: 0 !important;
            background-color: #f1f5f9;
        }}

        /* Esconde elementos padrão do Streamlit */
        [data-testid="stHeader"], [data-testid="stToolbarActions"],
        [data-testid="stDecoration"], footer {{ display: none !important; }}

        /* Estilos de Texto e Componentes */
        .panel-title {{ font-size: 18px; font-weight: 700; color: #1a1a2e; margin-bottom: 4px; }}
        .panel-subtitle {{ font-size: 13px; color: #64748b; margin-bottom: 20px; }}
        .section-label {{ font-size: 11px; font-weight: 700; text-transform: uppercase; color: #94a3b8; margin: 25px 0 10px 0; border-bottom: 1px solid #f1f5f9; padding-bottom: 5px; }}
        
        .stButton > button {{
            background: linear-gradient(135deg, #0066FF, #0052CC) !important;
            color: white !important;
            width: 100% !important;
            border-radius: 8px !important;
            border: none !important;
            padding: 10px !important;
            font-weight: 600 !important;
        }}

        .template-preview-img {{
            width: 100%;
            height: auto;
            display: block;
        }}

        /* Estilização fina da barra de rolagem para ficar elegante */
        ::-webkit-scrollbar {{ width: 6px; }}
        ::-webkit-scrollbar-track {{ background: transparent; }}
        ::-webkit-scrollbar-thumb {{ background: #cbd5e1; border-radius: 10px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: #94a3b8; }}
    </style>
    """, unsafe_allow_html=True)

    # ─────────────────────────────────────────────────────────────────────────────
    # LAYOUT
    # ─────────────────────────────────────────────────────────────────────────────
    
    # Ajustei a proporção para [1, 2.5] para a imagem ter mais destaque
    col_form, col_preview = st.columns([1, 2.5])

    with col_form:
        st.markdown('<div class="panel-title">✏️ Editor de Template</div>', unsafe_allow_html=True)
        st.markdown('<div class="panel-subtitle">Template 1 — Agência Digital</div>', unsafe_allow_html=True)

        st.markdown('<div class="section-label">⚙️ Configuração Geral</div>', unsafe_allow_html=True)
        page_title = st.text_input("Título da aba", "Agência Digital", key="pt")
        
        st.markdown('<div class="section-label">🎨 Cores</div>', unsafe_allow_html=True)
        cor_primaria = st.color_picker("Cor principal", "#0066FF", key="cp")
        
        st.markdown('<div class="section-label">🦸 Hero (Principal)</div>', unsafe_allow_html=True)
        hero_titulo = st.text_input("Título", "Transforme seu Negócio", key="ht")
        hero_desc = st.text_area("Descrição", "Soluções completas...", height=100, key="hd")

        # Espaçador apenas para testar o scroll da esquerda
        for i in range(10):
             st.markdown(f'<div class="section-label">Seção Extra {i+1}</div>', unsafe_allow_html=True)
             st.text_input(f"Campo de Teste {i+1}", key=f"test_{i}")

        st.markdown("---")
        if st.button("✅ Finalizar e Enviar"):
            st.success("Informações enviadas!")

    with col_preview:
        # Imagem ocupando 100% da largura da coluna com scroll independente
        st.markdown(f'<img src="{url_imagem_referencia}" class="template-preview-img">', unsafe_allow_html=True)

# Lembre-se que o app.py chama render()
