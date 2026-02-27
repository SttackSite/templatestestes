import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/site/main/1.png"

# ─────────────────────────────────────────────────────────────────────────────
# NOME DO TEMPLATE (exibido no cabeçalho do painel)
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_NAME = "Template 1 — Agência Digital"


def render():
    """
    Renderiza o editor do Template 1.
    Chame esta função a partir do appmain.py:

        import editor_template1
        editor_template1.render()
    """

    # ── CSS do painel ────────────────────────────────────────────────────────
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Inter', sans-serif;
            background: #f4f6fb;
        }
        [data-testid="stHeader"], [data-testid="stToolbarActions"],
        [data-testid="stDecoration"], footer { display: none !important; }

        .panel-title   { font-size: 18px; font-weight: 700; color: #1a1a2e; margin-bottom: 4px; }
        .panel-subtitle{ font-size: 13px; color: #64748b; margin-bottom: 20px; }
        .section-label {
            font-size: 11px; font-weight: 700; text-transform: uppercase;
            letter-spacing: 1px; color: #94a3b8;
            margin: 20px 0 8px 0; padding-bottom: 6px;
            border-bottom: 1px solid #f1f5f9;
        }
        .stButton > button {
            background: linear-gradient(135deg, #0066FF, #0052CC) !important;
            color: white !important; border: none !important;
            border-radius: 8px !important; font-weight: 600 !important;
            padding: 10px 24px !important; width: 100% !important;
            margin-top: 12px !important;
        }
        .stButton > button:hover {
            transform: translateY(-1px) !important;
            box-shadow: 0 4px 12px rgba(0,102,255,0.3) !important;
        }
        /* Painel esquerdo com scroll próprio */
        [data-testid="column"]:first-child > div:first-child {
            height: calc(100vh - 80px);
            overflow-y: auto;
            padding-right: 8px;
        }
        /* Imagem do template com scroll próprio */
        .template-img-wrapper {
            height: calc(100vh - 80px);
            overflow-y: auto;
            border-radius: 12px;
            border: 1px solid #e2e8f0;
            background: #f8faff;
        }
        .template-img-wrapper img {
            width: 100%;
            display: block;
        }
        .img-caption {
            font-size: 12px; color: #94a3b8; text-align: center;
            padding: 8px 0 4px;
        }
    </style>
    """, unsafe_allow_html=True)

    col_form, col_preview = st.columns([1, 2], gap="medium")

    # ── PAINEL ESQUERDO: FORMULÁRIO ──────────────────────────────────────────
    with col_form:
        st.markdown(f'<div class="panel-title">✏️ Editor de Template</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="panel-subtitle">{TEMPLATE_NAME}</div>', unsafe_allow_html=True)

        # ── Configuração Geral ────────────────────────────────────────────────
        st.markdown('<div class="section-label">⚙️ Configuração Geral</div>', unsafe_allow_html=True)
        page_title = st.text_input("Título da aba do navegador", "Agência Digital - Transforme seu Negócio")
        page_icon  = st.text_input("Ícone da aba (emoji)", "🚀")

        # ── Cores ─────────────────────────────────────────────────────────────
        st.markdown('<div class="section-label">🎨 Cores</div>', unsafe_allow_html=True)
        cor_primaria = st.color_picker("Cor principal (botões, destaques)", "#0066FF")
        cor_texto    = st.color_picker("Cor dos textos", "#1a1a1a")
        cor_subtexto = st.color_picker("Cor dos subtextos", "#666666")

        # ── Navbar ────────────────────────────────────────────────────────────
        st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)
        navbar_logo    = st.text_input("Logo / Nome da marca", "🚀 AGÊNCIA")
        navbar_link1   = st.text_input("Link 1 — Texto", "Serviços")
        navbar_link2   = st.text_input("Link 2 — Texto", "Sobre")
        navbar_link3   = st.text_input("Link 3 — Texto", "Contato")
        navbar_cta_txt = st.text_input("Botão CTA — Texto", "Começar")
        navbar_cta_url = st.text_input("Botão CTA — URL", "https://www.google.com/")

        # ── Hero ──────────────────────────────────────────────────────────────
        st.markdown('<div class="section-label">🦸 Hero (Seção Principal)</div>', unsafe_allow_html=True)
        hero_titulo_antes    = st.text_input("Título — Parte 1 (antes do destaque)", "Transforme seu Negócio com")
        hero_titulo_destaque = st.text_input("Título — Parte 2 (em destaque colorido)", "Estratégia Digital")
        hero_subtitulo       = st.text_area("Subtítulo", "Soluções completas de marketing digital que aumentam suas vendas e presença online", height=80)
        hero_btn1_txt        = st.text_input("Botão 1 — Texto", "Solicitar Consultoria")
        hero_btn1_url        = st.text_input("Botão 1 — URL", "https://www.google.com/")
        hero_btn2_txt        = st.text_input("Botão 2 — Texto", "Ver Portfólio")
        hero_btn2_url        = st.text_input("Botão 2 — URL", "https://www.google.com/")

        # ── Estatísticas ──────────────────────────────────────────────────────
        st.markdown('<div class="section-label">📊 Estatísticas do Hero</div>', unsafe_allow_html=True)
        stat1_num = st.text_input("Estatística 1 — Número", "500+")
        stat1_lbl = st.text_input("Estatística 1 — Label", "Clientes Satisfeitos")
        stat2_num = st.text_input("Estatística 2 — Número", "10+")
        stat2_lbl = st.text_input("Estatística 2 — Label", "Anos de Experiência")
        stat3_num = st.text_input("Estatística 3 — Número", "300%")
        stat3_lbl = st.text_input("Estatística 3 — Label", "Crescimento Médio")

        # ── Serviços / Cards ──────────────────────────────────────────────────
        st.markdown('<div class="section-label">🃏 Serviços / Cards</div>', unsafe_allow_html=True)
        secao_titulo    = st.text_input("Título da seção — Parte 1", "Nossos")
        secao_destaque  = st.text_input("Título da seção — Destaque", "Serviços")
        secao_descricao = st.text_area("Descrição da seção", "Oferecemos soluções completas de marketing digital para impulsionar seu negócio", height=60)

        cards = []
        defaults = [
            ("📱", "Social Media",       "Gerenciamento completo de suas redes sociais com estratégia de conteúdo"),
            ("🎯", "Publicidade Digital", "Campanhas otimizadas em Google Ads e Facebook para máximo ROI"),
            ("📊", "Análise de Dados",    "Relatórios detalhados e insights para melhorar seu desempenho"),
            ("🌐", "SEO & Conteúdo",      "Otimização para buscas e criação de conteúdo de alta qualidade"),
            ("💻", "Web Design",          "Websites modernos e responsivos que convertem visitantes em clientes"),
            ("📧", "Email Marketing",     "Campanhas de email personalizadas que geram resultados"),
        ]
        for i, (icon_d, title_d, desc_d) in enumerate(defaults, start=1):
            with st.expander(f"Card {i} — {title_d}"):
                icon  = st.text_input(f"Ícone {i}",     icon_d,  key=f"t1_icon_{i}")
                title = st.text_input(f"Título {i}",    title_d, key=f"t1_title_{i}")
                desc  = st.text_area(f"Descrição {i}", desc_d,  key=f"t1_desc_{i}", height=70)
                cards.append((icon, title, desc))

        # ── CTA ───────────────────────────────────────────────────────────────
        st.markdown('<div class="section-label">📣 Seção CTA</div>', unsafe_allow_html=True)
        cta_titulo  = st.text_input("CTA — Título",    "Pronto para Transformar seu Negócio?")
        cta_subtxt  = st.text_input("CTA — Subtítulo", "Agende uma consultoria gratuita com nossos especialistas")
        cta_btn_txt = st.text_input("CTA — Botão Texto", "Agendar Agora")
        cta_btn_url = st.text_input("CTA — Botão URL",   "https://www.google.com/")

        # ── Footer ────────────────────────────────────────────────────────────
        st.markdown('<div class="section-label">🔻 Footer</div>', unsafe_allow_html=True)
        footer_txt = st.text_input("Texto do footer", "© 2026 Agência Digital. Todos os direitos reservados.")

        # ── Observações livres ────────────────────────────────────────────────
        st.markdown('<div class="section-label">📝 Observações</div>', unsafe_allow_html=True)
        observacoes = st.text_area(
            "Algo que não encontrou acima? Descreva aqui",
            placeholder="Ex: quero mudar a fonte, adicionar uma seção de FAQ, remover o botão X...",
            height=100,
        )

        # ── Enviar ────────────────────────────────────────────────────────────
        st.markdown("---")
        if st.button("✅ Finalizar e Enviar para a Equipe", key="t1_send"):
            # Monte aqui o resumo e envie por e-mail / salve em banco / etc.
            st.success("✅ Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
            st.balloons()

    # ── PAINEL DIREITO: IMAGEM DO TEMPLATE ──────────────────────────────────
    with col_preview:
        st.markdown(
            '<p class="img-caption">📌 Referência visual do template — role para ver o site completo</p>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}" alt="Preview do template" /></div>',
            unsafe_allow_html=True,
        )


# ─────────────────────────────────────────────────────────────────────────────
# EXECUÇÃO DIRETA (para testar isoladamente: streamlit run editor_template1.py)
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    st.set_page_config(
        page_title=f"Editor — {TEMPLATE_NAME}",
        page_icon="✏️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
