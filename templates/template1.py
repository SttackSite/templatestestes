import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/site/main/1.png"

# ─────────────────────────────────────────────────────────────────────────────
# NOME DO TEMPLATE (exibido no cabeçalho do painel)
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_NAME = "Template 1 — Agência Digital"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init_state():
    """Inicializa os valores padrão no session_state na primeira execução."""
    if "t1_nav_links" not in st.session_state:
        st.session_state.t1_nav_links = [
            {"texto": "Serviços", "url": "#features"},
            {"texto": "Sobre",    "url": "#cta"},
            {"texto": "Contato",  "url": "#footer"},
        ]
    if "t1_hero_btns" not in st.session_state:
        st.session_state.t1_hero_btns = [
            {"texto": "Solicitar Consultoria", "url": "https://www.google.com/", "estilo": "primário"},
            {"texto": "Ver Portfólio",          "url": "https://www.google.com/", "estilo": "secundário"},
        ]
    if "t1_stats" not in st.session_state:
        st.session_state.t1_stats = [
            {"numero": "500+", "label": "Clientes Satisfeitos"},
            {"numero": "10+",  "label": "Anos de Experiência"},
            {"numero": "300%", "label": "Crescimento Médio"},
        ]
    if "t1_cards" not in st.session_state:
        st.session_state.t1_cards = [
            {"icone": "📱", "titulo": "Social Media",       "descricao": "Gerenciamento completo de suas redes sociais com estratégia de conteúdo"},
            {"icone": "🎯", "titulo": "Publicidade Digital", "descricao": "Campanhas otimizadas em Google Ads e Facebook para máximo ROI"},
            {"icone": "📊", "titulo": "Análise de Dados",    "descricao": "Relatórios detalhados e insights para melhorar seu desempenho"},
            {"icone": "🌐", "titulo": "SEO & Conteúdo",      "descricao": "Otimização para buscas e criação de conteúdo de alta qualidade"},
            {"icone": "💻", "titulo": "Web Design",          "descricao": "Websites modernos e responsivos que convertem visitantes em clientes"},
            {"icone": "📧", "titulo": "Email Marketing",     "descricao": "Campanhas de email personalizadas que geram resultados"},
        ]


def render():
    """
    Renderiza o editor do Template 1.
    Chame esta função a partir do appmain.py:

        import editor_template1
        editor_template1.render()
    """
    _init_state()

    # ── CSS global ───────────────────────────────────────────────────────────
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Inter', sans-serif;
            background: #f4f6fb;
        }
        [data-testid="stHeader"], [data-testid="stToolbarActions"],
        [data-testid="stDecoration"], footer { display: none !important; }

        .panel-title    { font-size: 18px; font-weight: 700; color: #1a1a2e; margin-bottom: 4px; }
        .panel-subtitle { font-size: 13px; color: #64748b; margin-bottom: 16px; }
        .section-label  {
            font-size: 11px; font-weight: 700; text-transform: uppercase;
            letter-spacing: 1px; color: #94a3b8;
            margin: 20px 0 8px 0; padding-bottom: 6px;
            border-bottom: 1px solid #f1f5f9;
        }
        .item-card {
            background: white;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 12px 14px;
            margin-bottom: 8px;
        }
        /* Botão principal (enviar) */
        div[data-testid="stButton"]:has(button[kind="primary"]) button {
            background: linear-gradient(135deg, #0066FF, #0052CC) !important;
            color: white !important; border: none !important;
            border-radius: 8px !important; font-weight: 600 !important;
            padding: 10px 24px !important; width: 100% !important;
            margin-top: 12px !important;
        }
        /* Botão de adicionar */
        .add-btn button {
            background: #f0f7ff !important;
            color: #0066FF !important;
            border: 1px dashed #0066FF !important;
            border-radius: 8px !important;
            font-size: 13px !important;
            font-weight: 500 !important;
            width: 100% !important;
            margin: 4px 0 12px 0 !important;
        }
        /* Botão de remover */
        .remove-btn button {
            background: #fff5f5 !important;
            color: #e53e3e !important;
            border: 1px solid #fed7d7 !important;
            border-radius: 6px !important;
            font-size: 12px !important;
            padding: 2px 10px !important;
        }
        /* Imagem do template */
        .template-img-wrapper {
            height: calc(100vh - 120px);
            overflow-y: auto;
            border-radius: 12px;
            border: 1px solid #e2e8f0;
            background: #f8faff;
        }
        .template-img-wrapper img { width: 100%; display: block; }
        .img-caption {
            font-size: 12px; color: #94a3b8;
            text-align: center; padding: 6px 0 4px;
        }
    </style>
    """, unsafe_allow_html=True)

    col_form, col_preview = st.columns([1, 2], gap="medium")

    # ════════════════════════════════════════════════════════════════════════
    # PAINEL ESQUERDO — FORMULÁRIO
    # ════════════════════════════════════════════════════════════════════════
    with col_form:
        st.markdown(f'<div class="panel-title">✏️ Editor de Template</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="panel-subtitle">{TEMPLATE_NAME}</div>', unsafe_allow_html=True)

        with st.container(height=720, border=False):

            # ── Configuração Geral ────────────────────────────────────────────
            st.markdown('<div class="section-label">⚙️ Configuração Geral</div>', unsafe_allow_html=True)
            page_title = st.text_input("Título da aba do navegador", "Agência Digital - Transforme seu Negócio")
            page_icon  = st.text_input("Ícone da aba (emoji)", "🚀")

            # ── Cores ─────────────────────────────────────────────────────────
            st.markdown('<div class="section-label">🎨 Cores</div>', unsafe_allow_html=True)
            cor_primaria = st.color_picker("Cor principal (botões, destaques)", "#0066FF")
            cor_texto    = st.color_picker("Cor dos textos", "#1a1a1a")
            cor_subtexto = st.color_picker("Cor dos subtextos", "#666666")

            # ── Navbar ────────────────────────────────────────────────────────
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)
            navbar_logo = st.text_input("Logo / Nome da marca", "🚀 AGÊNCIA")

            # Links da navbar (dinâmicos)
            st.caption("Links do menu")
            for i, link in enumerate(st.session_state.t1_nav_links):
                with st.container():
                    c1, c2, c3 = st.columns([3, 3, 1])
                    with c1:
                        st.session_state.t1_nav_links[i]["texto"] = st.text_input(
                            "Texto", link["texto"], key=f"t1_nl_txt_{i}", label_visibility="collapsed",
                            placeholder="Texto do link"
                        )
                    with c2:
                        st.session_state.t1_nav_links[i]["url"] = st.text_input(
                            "URL", link["url"], key=f"t1_nl_url_{i}", label_visibility="collapsed",
                            placeholder="URL"
                        )
                    with c3:
                        if len(st.session_state.t1_nav_links) > 1:
                            if st.button("🗑", key=f"t1_nl_del_{i}", help="Remover link"):
                                st.session_state.t1_nav_links.pop(i)
                                st.rerun()

            with st.container():
                if st.button("＋ Adicionar link ao menu", key="t1_nl_add"):
                    st.session_state.t1_nav_links.append({"texto": "Novo Link", "url": "#"})
                    st.rerun()

            navbar_cta_txt = st.text_input("Botão CTA — Texto", "Começar")
            navbar_cta_url = st.text_input("Botão CTA — URL", "https://www.google.com/")

            # ── Hero ──────────────────────────────────────────────────────────
            st.markdown('<div class="section-label">🦸 Hero (Seção Principal)</div>', unsafe_allow_html=True)
            hero_titulo_antes    = st.text_input("Título — Parte 1 (antes do destaque)", "Transforme seu Negócio com")
            hero_titulo_destaque = st.text_input("Título — Parte 2 (em destaque colorido)", "Estratégia Digital")
            hero_subtitulo       = st.text_area("Subtítulo", "Soluções completas de marketing digital que aumentam suas vendas e presença online", height=80)

            # Botões do hero (dinâmicos)
            st.caption("Botões do hero")
            for i, btn in enumerate(st.session_state.t1_hero_btns):
                with st.container():
                    c1, c2, c3, c4 = st.columns([3, 3, 2, 1])
                    with c1:
                        st.session_state.t1_hero_btns[i]["texto"] = st.text_input(
                            "Texto", btn["texto"], key=f"t1_hb_txt_{i}", label_visibility="collapsed",
                            placeholder="Texto do botão"
                        )
                    with c2:
                        st.session_state.t1_hero_btns[i]["url"] = st.text_input(
                            "URL", btn["url"], key=f"t1_hb_url_{i}", label_visibility="collapsed",
                            placeholder="URL"
                        )
                    with c3:
                        st.session_state.t1_hero_btns[i]["estilo"] = st.selectbox(
                            "Estilo", ["primário", "secundário"], key=f"t1_hb_style_{i}",
                            index=0 if btn["estilo"] == "primário" else 1,
                            label_visibility="collapsed"
                        )
                    with c4:
                        if len(st.session_state.t1_hero_btns) > 1:
                            if st.button("🗑", key=f"t1_hb_del_{i}", help="Remover botão"):
                                st.session_state.t1_hero_btns.pop(i)
                                st.rerun()

            if st.button("＋ Adicionar botão ao hero", key="t1_hb_add"):
                st.session_state.t1_hero_btns.append({"texto": "Novo Botão", "url": "#", "estilo": "primário"})
                st.rerun()

            # ── Estatísticas ──────────────────────────────────────────────────
            st.markdown('<div class="section-label">📊 Estatísticas do Hero</div>', unsafe_allow_html=True)
            for i, stat in enumerate(st.session_state.t1_stats):
                with st.container():
                    c1, c2, c3 = st.columns([2, 4, 1])
                    with c1:
                        st.session_state.t1_stats[i]["numero"] = st.text_input(
                            "Número", stat["numero"], key=f"t1_st_num_{i}", label_visibility="collapsed",
                            placeholder="Ex: 500+"
                        )
                    with c2:
                        st.session_state.t1_stats[i]["label"] = st.text_input(
                            "Label", stat["label"], key=f"t1_st_lbl_{i}", label_visibility="collapsed",
                            placeholder="Descrição"
                        )
                    with c3:
                        if len(st.session_state.t1_stats) > 1:
                            if st.button("🗑", key=f"t1_st_del_{i}", help="Remover estatística"):
                                st.session_state.t1_stats.pop(i)
                                st.rerun()

            if st.button("＋ Adicionar estatística", key="t1_st_add"):
                st.session_state.t1_stats.append({"numero": "0", "label": "Nova Métrica"})
                st.rerun()

            # ── Serviços / Cards ──────────────────────────────────────────────
            st.markdown('<div class="section-label">🃏 Serviços / Cards</div>', unsafe_allow_html=True)
            secao_titulo    = st.text_input("Título da seção — Parte 1", "Nossos")
            secao_destaque  = st.text_input("Título da seção — Destaque", "Serviços")
            secao_descricao = st.text_area("Descrição da seção", "Oferecemos soluções completas de marketing digital para impulsionar seu negócio", height=60)

            for i, card in enumerate(st.session_state.t1_cards):
                with st.expander(f"Card {i+1} — {card['titulo']}"):
                    c1, c2 = st.columns([1, 8])
                    with c1:
                        st.session_state.t1_cards[i]["icone"] = st.text_input(
                            "Ícone", card["icone"], key=f"t1_cd_ico_{i}", label_visibility="collapsed"
                        )
                    with c2:
                        st.session_state.t1_cards[i]["titulo"] = st.text_input(
                            "Título", card["titulo"], key=f"t1_cd_tit_{i}", label_visibility="collapsed"
                        )
                    st.session_state.t1_cards[i]["descricao"] = st.text_area(
                        "Descrição", card["descricao"], key=f"t1_cd_dsc_{i}", height=70, label_visibility="collapsed"
                    )
                    if len(st.session_state.t1_cards) > 1:
                        if st.button(f"🗑 Remover card {i+1}", key=f"t1_cd_del_{i}"):
                            st.session_state.t1_cards.pop(i)
                            st.rerun()

            if st.button("＋ Adicionar card de serviço", key="t1_cd_add"):
                st.session_state.t1_cards.append({
                    "icone": "⭐", "titulo": "Novo Serviço",
                    "descricao": "Descrição do novo serviço"
                })
                st.rerun()

            # ── CTA ───────────────────────────────────────────────────────────
            st.markdown('<div class="section-label">📣 Seção CTA</div>', unsafe_allow_html=True)
            cta_titulo  = st.text_input("CTA — Título",      "Pronto para Transformar seu Negócio?")
            cta_subtxt  = st.text_input("CTA — Subtítulo",   "Agende uma consultoria gratuita com nossos especialistas")
            cta_btn_txt = st.text_input("CTA — Botão Texto", "Agendar Agora")
            cta_btn_url = st.text_input("CTA — Botão URL",   "https://www.google.com/")

            # ── Footer ────────────────────────────────────────────────────────
            st.markdown('<div class="section-label">🔻 Footer</div>', unsafe_allow_html=True)
            footer_txt = st.text_input("Texto do footer", "© 2026 Agência Digital. Todos os direitos reservados.")

            # ── Observações livres ────────────────────────────────────────────
            st.markdown('<div class="section-label">📝 Observações</div>', unsafe_allow_html=True)
            observacoes = st.text_area(
                "Algo que não encontrou acima? Descreva aqui",
                placeholder="Ex: quero mudar a fonte, adicionar uma seção de FAQ, remover o botão X...",
                height=100,
            )

            # ── Enviar ────────────────────────────────────────────────────────
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t1_send", type="primary"):
                st.success("✅ Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
                st.balloons()

    # ════════════════════════════════════════════════════════════════════════
    # PAINEL DIREITO — IMAGEM DO TEMPLATE
    # ════════════════════════════════════════════════════════════════════════
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
