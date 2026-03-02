import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE 2 — SUBSTITUA PELA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img2.png"
TEMPLATE_NAME = "Template 2 — FitPro Academia"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {

        # Cores principais do template
        "t2_cores": [
            {"nome": "Cor principal (laranja destaque)", "valor": "#FF6B35"},
            {"nome": "Cor fundo escuro hero", "valor": "#1a1a1a"},
            {"nome": "Cor textos", "valor": "#1a1a1a"},
        ],

        # Navbar
        "t2_logos": [
            {"parte1": "Fit", "destaque": "Pro"},
        ],
        "t2_nav_links": [
            {"texto": "Sobre", "url": "#sobre"},
            {"texto": "Planos", "url": "#planos"},
            {"texto": "Treinos", "url": "#treinos"},
        ],
        "t2_nav_ctas": [
            {"texto": "Matricule-se", "url": "#contato"},
        ],

        # Hero
        "t2_hero_titulos": [
            {"parte1": "Transforme seu corpo na", "destaque": "Melhor Versão"},
        ],
        "t2_hero_subtitulos": [
            {"valor": "Treinos personalizados, equipamentos modernos e acompanhamento profissional."},
        ],
        "t2_hero_btns": [
            {"texto": "Começar Agora", "url": "#planos", "estilo": "primário"},
            {"texto": "Conheça os Planos", "url": "#planos", "estilo": "secundário"},
        ],

        # Benefícios / Diferenciais
        "t2_beneficios": [
            {"icone": "🏋️", "titulo": "Equipamentos Modernos", "descricao": "Estrutura completa para todos os níveis."},
            {"icone": "👨‍🏫", "titulo": "Personal Trainers", "descricao": "Profissionais qualificados para te acompanhar."},
            {"icone": "🔥", "titulo": "Resultados Reais", "descricao": "Metodologia focada em performance e evolução."},
        ],

        # Planos
        "t2_planos": [
            {"nome": "Plano Básico", "preco": "R$ 79/mês", "descricao": "Acesso em horário comercial"},
            {"nome": "Plano Premium", "preco": "R$ 129/mês", "descricao": "Acesso total + aulas especiais"},
        ],
    }

    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def _add_btn(key, label):
    return st.button(label, key=key)


def _del_btn(key, label="🗑"):
    return st.button(label, key=key)


# ─────────────────────────────────────────────────────────────────────────────
# RENDER PRINCIPAL
# ─────────────────────────────────────────────────────────────────────────────
def render():
    _init()

    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        html, body, [data-testid="stAppViewContainer"] {
            font-family: 'Inter', sans-serif;
            background: #f4f6fb;
        }
        [data-testid="stHeader"],
        [data-testid="stToolbarActions"],
        [data-testid="stDecoration"],
        footer { display:none!important; }

        .section-label {
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            color: #94a3b8;
            margin: 22px 0 8px;
            padding-bottom: 6px;
            border-bottom: 1px solid #f1f5f9;
        }

        .panel-title { font-size: 18px; font-weight: 700; }
        .panel-subtitle { font-size: 13px; color: #64748b; }

        .template-img-wrapper {
            height: calc(100vh - 120px);
            overflow-y: auto;
            border-radius: 12px;
            border: 1px solid #e2e8f0;
            background: #f8faff;
        }

        .template-img-wrapper img {
            width: 100%;
            display: block;
        }
    </style>
    """, unsafe_allow_html=True)

    col_form, col_preview = st.columns([1, 2], gap="medium")

    # ─────────────────────────── FORMULÁRIO ───────────────────────────
    with col_form:

        st.markdown('<div class="panel-title">✏️ Editor de Template</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="panel-subtitle">{TEMPLATE_NAME}</div>', unsafe_allow_html=True)

        with st.container(height=720, border=False):

            # 🎨 CORES
            st.markdown('<div class="section-label">🎨 Cores</div>', unsafe_allow_html=True)

            for i, cor in enumerate(st.session_state.t2_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t2_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t2_cor_nome_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t2_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t2_cor_val_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t2_cores) > 1 and _del_btn(f"t2_cor_del_{i}"):
                        st.session_state.t2_cores.pop(i)
                        st.rerun()

            if _add_btn("t2_cor_add", "＋ Adicionar cor"):
                st.session_state.t2_cores.append({"nome": "Nova cor", "valor": "#FFFFFF"})
                st.rerun()

            # 🔝 NAVBAR
            st.markdown('<div class="section-label">🔝 Navbar</div>', unsafe_allow_html=True)

            st.caption("Logo (Parte normal | Destaque)")
            for i, logo in enumerate(st.session_state.t2_logos):
                c1, c2 = st.columns(2)
                with c1:
                    st.session_state.t2_logos[i]["parte1"] = st.text_input(
                        "Parte 1", logo["parte1"], key=f"t2_logo_p1_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t2_logos[i]["destaque"] = st.text_input(
                        "Destaque", logo["destaque"], key=f"t2_logo_dest_{i}", label_visibility="collapsed")

            st.caption("Links de navegação")
            for i, link in enumerate(st.session_state.t2_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t2_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t2_nav_txt_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t2_nav_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t2_nav_url_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t2_nav_links) > 1 and _del_btn(f"t2_nav_del_{i}"):
                        st.session_state.t2_nav_links.pop(i)
                        st.rerun()

            if _add_btn("t2_nav_add", "＋ Adicionar link"):
                st.session_state.t2_nav_links.append({"texto": "Novo", "url": "#"})
                st.rerun()

            # 🦸 HERO
            st.markdown('<div class="section-label">🦸 Hero</div>', unsafe_allow_html=True)

            for i, t in enumerate(st.session_state.t2_hero_titulos):
                c1, c2 = st.columns(2)
                with c1:
                    st.session_state.t2_hero_titulos[i]["parte1"] = st.text_input(
                        "Texto", t["parte1"], key=f"t2_ht_p1_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t2_hero_titulos[i]["destaque"] = st.text_input(
                        "Destaque", t["destaque"], key=f"t2_ht_dest_{i}", label_visibility="collapsed")

            st.caption("Subtítulo")
            for i, sub in enumerate(st.session_state.t2_hero_subtitulos):
                st.session_state.t2_hero_subtitulos[i]["valor"] = st.text_area(
                    "Sub", sub["valor"], key=f"t2_hsub_{i}", height=70, label_visibility="collapsed")

            # 💪 BENEFÍCIOS
            st.markdown('<div class="section-label">💪 Benefícios</div>', unsafe_allow_html=True)

            for i, b in enumerate(st.session_state.t2_beneficios):
                with st.expander(f"Benefício {i+1} — {b['titulo']}"):
                    st.session_state.t2_beneficios[i]["icone"] = st.text_input(
                        "Ícone", b["icone"], key=f"t2_ben_ico_{i}")
                    st.session_state.t2_beneficios[i]["titulo"] = st.text_input(
                        "Título", b["titulo"], key=f"t2_ben_tit_{i}")
                    st.session_state.t2_beneficios[i]["descricao"] = st.text_area(
                        "Descrição", b["descricao"], key=f"t2_ben_desc_{i}", height=60)
                    if len(st.session_state.t2_beneficios) > 1:
                        if st.button("🗑 Remover", key=f"t2_ben_del_{i}"):
                            st.session_state.t2_beneficios.pop(i)
                            st.rerun()

            if _add_btn("t2_ben_add", "＋ Adicionar benefício"):
                st.session_state.t2_beneficios.append(
                    {"icone": "⭐", "titulo": "Novo benefício", "descricao": "Descrição"})
                st.rerun()

            # 💳 PLANOS
            st.markdown('<div class="section-label">💳 Planos</div>', unsafe_allow_html=True)

            for i, p in enumerate(st.session_state.t2_planos):
                with st.expander(f"Plano {i+1} — {p['nome']}"):
                    st.session_state.t2_planos[i]["nome"] = st.text_input(
                        "Nome", p["nome"], key=f"t2_pl_nome_{i}")
                    st.session_state.t2_planos[i]["preco"] = st.text_input(
                        "Preço", p["preco"], key=f"t2_pl_preco_{i}")
                    st.session_state.t2_planos[i]["descricao"] = st.text_area(
                        "Descrição", p["descricao"], key=f"t2_pl_desc_{i}", height=60)

                    if len(st.session_state.t2_planos) > 1:
                        if st.button("🗑 Remover plano", key=f"t2_pl_del_{i}"):
                            st.session_state.t2_planos.pop(i)
                            st.rerun()

            if _add_btn("t2_pl_add", "＋ Adicionar plano"):
                st.session_state.t2_planos.append(
                    {"nome": "Novo Plano", "preco": "R$ 0/mês", "descricao": "Descrição"})
                st.rerun()

    # ─────────────────────────── PREVIEW ───────────────────────────
    with col_preview:
        st.markdown('<div class="img-caption">Preview visual do template</div>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}"></div>',
            unsafe_allow_html=True
        )
