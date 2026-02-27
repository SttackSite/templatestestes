import streamlit as st
import importlib.util
import os

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÃO DA PÁGINA
# ─────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Editor de Templates Profissional",
    page_icon="✏️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 1. PEGAR O TEMPLATE PELA URL
# Exemplo: ?template=template1
query_params = st.query_params
template_nome = query_params.get("template", "template1") # 'template1' é o padrão

# 2. FUNÇÃO PARA CARREGAR O ARQUIVO DE CONFIGURAÇÃO DO TEMPLATE
def carregar_config_template(nome):
    caminho = f"templates/{nome}.py"
    if not os.path.exists(caminho):
        st.error(f"Template '{nome}' não encontrado.")
        return None
    
    spec = importlib.util.spec_from_file_location("modulo_template", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo.config # Retorna o dicionário de dados

config_template = carregar_config_template(template_nome)

if config_template:
    # ─────────────────────────────────────────────────────────────────────────
    # CSS GLOBAL DO EDITOR (Mantido do seu original)
    # ─────────────────────────────────────────────────────────────────────────
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        html, body, [data-testid="stAppViewContainer"] { font-family: 'Inter', sans-serif; background: #f4f6fb; }
        [data-testid="stHeader"], [data-testid="stToolbarActions"], [data-testid="stDecoration"], footer { display: none !important; }
        .editor-panel { background: #ffffff; border-right: 1px solid #e2e8f0; height: 100vh; overflow-y: auto; padding: 24px 20px; }
        .preview-panel { height: 100vh; overflow-y: auto; background: #f8faff; }
        .section-label { font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; color: #94a3b8; margin: 20px 0 8px 0; padding-bottom: 6px; border-bottom: 1px solid #f1f5f9; }
        .panel-title { font-size: 18px; font-weight: 700; color: #1a1a2e; }
        .panel-subtitle { font-size: 13px; color: #64748b; margin-bottom: 20px; }
        .stButton > button { background: linear-gradient(135deg, #0066FF, #0052CC) !important; color: white !important; width: 100% !important; border-radius: 8px !important; }
    </style>
    """, unsafe_allow_html=True)

    col_form, col_preview = st.columns([1, 2], gap="small")

    with col_form:
        st.markdown(f'<div class="panel-title">✏️ Editor de Template</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="panel-subtitle">{config_template["nome_exibicao"]}</div>', unsafe_allow_html=True)

        # ── CONFIGURAÇÃO GERAL ────────────────────────────────────────────────────
        st.markdown('<div class="section-label">⚙️ Configuração Geral</div>', unsafe_allow_html=True)
        page_title = st.text_input("Título da aba", config_template["default_title"])
        cor_primaria = st.color_picker("Cor principal", config_template["default_color"])
        
        # ── NAVBAR ────────────────────────────────────────────────────────────────
        st.markdown('<div class="section-label">🔝 Navegação</div>', unsafe_allow_html=True)
        navbar_logo = st.text_input("Logo", "🚀 AGÊNCIA")
        
        # ── HERO ──────────────────────────────────────────────────────────────────
        st.markdown('<div class="section-label">🦸 Hero</div>', unsafe_allow_html=True)
        hero_titulo_antes = st.text_input("Título (Parte 1)", "Transforme seu Negócio com")
        hero_titulo_destaque = st.text_input("Título (Destaque)", "Estratégia Digital")
        hero_subtitulo = st.text_area("Subtítulo", "Soluções completas de marketing digital...")

        # ── DINÂMICA DE CARDS ─────────────────────────────────────────────────────
        st.markdown('<div class="section-label">🃏 Serviços / Cards</div>', unsafe_allow_html=True)
        cards = []
        for i in range(1, 4): # Exemplo simplificado para 3 cards
            with st.expander(f"Card {i}"):
                icon = st.text_input(f"Ícone {i}", "🚀", key=f"i_{i}")
                title = st.text_input(f"Título {i}", f"Serviço {i}", key=f"t_{i}")
                desc = st.text_area(f"Descrição {i}", "Descrição curta...", key=f"d_{i}")
                cards.append((icon, title, desc))

        if st.button("✅ Finalizar e Enviar"):
            st.success("Dados enviados com sucesso!")

    with col_preview:
        # Lógica de renderização do HTML (Mantida a sua estrutura de f-strings)
        cards_html = "".join([f'<div class="feature-card"><div class="feature-icon">{c[0]}</div><h3>{c[1]}</h3><p>{c[2]}</p></div>' for c in cards])
        
        # Aqui você usa as variáveis capturadas no form para preencher seu template HTML
        # Vou simplificar para o exemplo não ficar gigante:
        html_preview = f"""
        <style>
            body {{ font-family: sans-serif; color: #333; }}
            .hero {{ text-align: center; padding: 50px; background: white; }}
            .highlight {{ color: {cor_primaria}; }}
            .feature-card {{ border: 1px solid #eee; padding: 20px; margin: 10px; border-radius: 10px; display: inline-block; width: 200px; }}
        </style>
        <div class="hero">
            <h1>{hero_titulo_antes} <span class="highlight">{hero_titulo_destaque}</span></h1>
            <p>{hero_subtitulo}</p>
            <div class="grid">{cards_html}</div>
        </div>
        """
        st.components.v1.html(html_preview, height=800, scrolling=True)
