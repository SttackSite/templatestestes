import streamlit as st

def render():
    # URL da imagem do seu template (Substitua pela sua)
    url_imagem_referencia = "https://sua-url-aqui.com/imagem-do-template.png"

    # ─────────────────────────────────────────────────────────────────────────────
    # CSS PARA ROLAMENTO INDEPENDENTE E AJUSTES DE COLUNA
    # ─────────────────────────────────────────────────────────────────────────────
    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        /* Remove margens e fixa altura da visualização */
        [data-testid="stAppViewContainer"] {{
            padding: 0 !important;
        }}
        
        /* Estilização da Coluna do Formulário (Esquerda) */
        [data-testid="column"]:nth-child(1) {{
            background: #ffffff;
            height: 100vh;
            overflow-y: auto !important;
            padding: 24px !important;
            border-right: 1px solid #e2e8f0;
        }}

        /* Estilização da Coluna da Imagem (Direita) */
        [data-testid="column"]:nth-child(2) {{
            background: #f1f5f9;
            height: 100vh;
            overflow-y: auto !important;
            padding: 0 !important; /* Ponta a ponta */
        }}

        /* Esconde elementos padrão do Streamlit */
        [data-testid="stHeader"], [data-testid="stToolbarActions"],
        [data-testid="stDecoration"], footer {{ display: none !important; }}

        .panel-title {{ font-size: 18px; font-weight: 700; color: #1a1a2e; margin-bottom: 4px; }}
        .panel-subtitle {{ font-size: 13px; color: #64748b; margin-bottom: 20px; }}
        .section-label {{ font-size: 11px; font-weight: 700; text-transform: uppercase; color: #94a3b8; margin: 20px 0 8px 0; border-bottom: 1px solid #f1f5f9; }}
        
        /* Ajuste do botão */
        .stButton > button {{
            background: linear-gradient(135deg, #0066FF, #0052CC) !important;
            color: white !important;
            width: 100% !important;
            border-radius: 8px !important;
        }}

        /* Estilo da imagem full */
        .template-preview-img {{
            width: 100%;
            height: auto;
            display: block;
        }}
    </style>
    """, unsafe_allow_html=True)

    # ─────────────────────────────────────────────────────────────────────────────
    # LAYOUT
    # ─────────────────────────────────────────────────────────────────────────────
    
    col_form, col_preview = st.columns([1, 2], gap="small")

    with col_form:
        st.markdown('<div class="panel-title">✏️ Editor de Template</div>', unsafe_allow_html=True)
        st.markdown('<div class="panel-subtitle">Template 1 — Agência Digital</div>', unsafe_allow_html=True)

        # -- SEÇÕES DO FORMULÁRIO --
        st.markdown('<div class="section-label">⚙️ Configuração Geral</div>', unsafe_allow_html=True)
        page_title = st.text_input("Título da aba", "Agência Digital")
        
        st.markdown('<div class="section-label">🎨 Cores</div>', unsafe_allow_html=True)
        cor_primaria = st.color_picker("Cor principal", "#0066FF")
        
        st.markdown('<div class="section-label">🦸 Hero (Principal)</div>', unsafe_allow_html=True)
        hero_titulo = st.text_input("Título", "Transforme seu Negócio")
        hero_desc = st.text_area("Descrição", "Soluções completas...", height=100)

        # Adicione aqui os demais st.text_input que você já tinha...
        # Repita o padrão para os 35 templates mudando apenas os inputs

        st.markdown("---")
        if st.button("✅ Finalizar e Enviar"):
            st.success("Informações enviadas para nossa equipe!")

    with col_preview:
        # Renderiza a imagem de ponta a ponta
        # Usamos HTML para garantir que não haja margens laterais do Streamlit
        st.markdown(f"""
            <img src="{url_imagem_referencia}" class="template-preview-img">
        """, unsafe_allow_html=True)

# Lembre-se que o app.py continua chamando o render() desse arquivo.
