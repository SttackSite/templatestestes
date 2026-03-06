import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img16.png"
TEMPLATE_NAME = "Template 16 — LITIGUARD Style (Legal & Strategic Advisory)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── CORES ───────────────────────────────────────────────────────────
        "t16_cores": [
            {"nome": "Azul Marinho (Principal)", "valor": "#1a2b3c"},
            {"nome": "Dourado (Destaque)",        "valor": "#c5a059"},
            {"nome": "Fundo (Branco)",            "valor": "#ffffff"},
            {"nome": "Texto (Escuro)",            "valor": "#1a2b3c"},
        ],

        # ── TOP BAR ─────────────────────────────────────────────────────────
        "t16_top_bar_links": [
            {"texto": "LITIGATION & ADVISORY SERVICES", "url": "#"},
            {"texto": "EN | FR | DE",                   "url": "#"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t16_logos": [{"valor": "LITIGUARD"}],
        "t16_nav_links": [
            {"texto": "ABOUT",    "url": "#about"},
            {"texto": "SERVICES", "url": "#services"},
            {"texto": "NETWORK",  "url": "#network"},
            {"texto": "CONTACT",  "url": "#contact"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t16_hero_titulos": [{"valor": "Protecting Your Interests"}],
        "t16_hero_descs":   [{"valor": "A global network of legal experts dedicated to complex litigation and strategic advisory."}],
        "t16_hero_imgs":    [{"valor": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?auto=format&fit=crop&w=1600&q=80"}],

        # ── ABOUT ───────────────────────────────────────────────────────────
        "t16_about_titulos": [{"valor": "Strategic Legal<br>Representation"}],
        "t16_about_descs":   [{"valor": "Litiguard provides comprehensive support in cross-border disputes. Our approach combines local expertise with a global perspective to ensure the best possible outcome for institutional and private clients."}],
        "t16_about_btns":    [{"texto": "Discover Our Vision", "url": "https://www.google.com/"}],

        # ── EXPERTISE (SERVICES) ────────────────────────────────────────────
        "t16_exp_secao_titulos": [{"valor": "Our Expertise"}],
        "t16_exp_items": [
            {"icon": "⚖️", "titulo": "Commercial Litigation",  "desc": "Resolving complex business disputes with precision and strategic foresight."},
            {"icon": "🌍", "titulo": "Cross-Border Claims",     "desc": "Navigating multiple jurisdictions to protect assets and enforce rights worldwide."},
            {"icon": "🤝", "titulo": "Arbitration",             "desc": "Expert representation in international arbitration proceedings and alternative dispute resolution."},
            {"icon": "🛡️", "titulo": "Asset Recovery",          "desc": "Tracing and recovering assets across global financial centers and tax havens."},
            {"icon": "📈", "titulo": "Investment Disputes",     "desc": "Protecting investors' rights under bilateral treaties and international law."},
            {"icon": "📜", "titulo": "Corporate Advisory",      "desc": "Proactive legal strategies to mitigate risks and ensure regulatory compliance."},
        ],

        # ── NETWORK ─────────────────────────────────────────────────────────
        "t16_net_titulos": [{"valor": "A Truly Global Presence"}],
        "t16_net_descs":   [{"valor": "Our network spans over 40 countries, providing seamless legal support whenever and wherever our clients need it most."}],
        "t16_net_cities": [
            {"nome": "LONDON"},
            {"nome": "BRUSSELS"},
            {"nome": "DUBAI"},
        ],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t16_foot_logos": [{"valor": "LITIGUARD"}],
        "t16_foot_descs": [{"valor": "International Litigation & Advisory Support Network."}],
        "t16_foot_cols": [
            {"titulo": "OFFICES", "links": [{"texto": "Brussels, Belgium", "url": "#"}, {"texto": "Geneva, Switzerland", "url": "#"}, {"texto": "London, UK", "url": "#"}]},
            {"titulo": "LEGAL",   "links": [{"texto": "Privacy Policy", "url": "#"}, {"texto": "Terms of Service", "url": "#"}, {"texto": "Cookies", "url": "#"}]},
        ],
        "t16_foot_copys": [{"valor": "© 2026 LITIGUARD. ALL RIGHTS RESERVED."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t16_obs": [{"valor": ""}],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def _add_btn(key, label="＋ Adicionar"):
    return st.button(label, key=key)

def _del_btn(key, label="🗑"):
    return st.button(label, key=key, help="Remover")


# ─────────────────────────────────────────────────────────────────────────────
# RENDER PRINCIPAL
# ─────────────────────────────────────────────────────────────────────────────
def render():
    _init()

    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        html, body, [data-testid="stAppViewContainer"] { font-family: 'Inter', sans-serif; background: #f4f6fb; }
        [data-testid="stHeader"],[data-testid="stToolbarActions"],[data-testid="stDecoration"],footer { display:none!important; }
        .section-label {
            font-size: 11px; font-weight: 700; text-transform: uppercase;
            letter-spacing: 1px; color: #94a3b8;
            margin: 22px 0 8px; padding-bottom: 6px;
            border-bottom: 1px solid #f1f5f9;
        }
        .panel-title    { font-size: 18px; font-weight: 700; color: #1a1a2e; margin-bottom: 2px; }
        .panel-subtitle { font-size: 13px; color: #64748b; margin-bottom: 14px; }
        .img-caption    { font-size: 12px; color: #94a3b8; text-align: center; padding: 6px 0 4px; }
        .template-img-wrapper {
            height: calc(100vh - 120px); overflow-y: auto;
            border-radius: 12px; border: 1px solid #e2e8f0; background: #f8faff;
        }
        .template-img-wrapper img { width: 100%; display: block; }
    </style>
    """, unsafe_allow_html=True)

    col_form, col_preview = st.columns([1, 2], gap="medium")

    with col_form:
        st.markdown('<div class="panel-title">✏️ Editor de Template</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="panel-subtitle">{TEMPLATE_NAME}</div>', unsafe_allow_html=True)

        with st.container(height=720, border=False):

            # ══════════════════════════════════════════════════════════════════
            # CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            for i, cor in enumerate(st.session_state.t16_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t16_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t16_cor_n_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t16_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t16_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t16_cores) > 1 and _del_btn(f"t16_cor_del_{i}"):
                        st.session_state.t16_cores.pop(i); st.rerun()
            if _add_btn("t16_cor_add", "＋ Adicionar cor"):
                st.session_state.t16_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # TOP BAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📜 Barra Superior (Top Bar)</div>', unsafe_allow_html=True)
            st.caption("Itens da barra  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t16_top_bar_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t16_top_bar_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t16_tb_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t16_top_bar_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t16_tb_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t16_top_bar_links) > 1 and _del_btn(f"t16_tb_del_{i}"):
                        st.session_state.t16_top_bar_links.pop(i); st.rerun()
            if _add_btn("t16_tb_add", "＋ Adicionar item"):
                st.session_state.t16_top_bar_links.append({"texto": "ITEM", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Header)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da empresa")
            for i, logo in enumerate(st.session_state.t16_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_logos[i]["valor"] = st.text_input(
                        "Logo", logo["valor"], key=f"t16_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t16_logos) > 1 and _del_btn(f"t16_logo_del_{i}"):
                        st.session_state.t16_logos.pop(i); st.rerun()
            if _add_btn("t16_logo_add", "＋ Adicionar logo"):
                st.session_state.t16_logos.append({"valor": "EMPRESA"}); st.rerun()

            st.caption("Links do menu  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t16_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t16_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t16_nl_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t16_nav_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t16_nl_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t16_nav_links) > 1 and _del_btn(f"t16_nl_del_{i}"):
                        st.session_state.t16_nav_links.pop(i); st.rerun()
            if _add_btn("t16_nl_add", "＋ Adicionar link ao menu"):
                st.session_state.t16_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏛️ Hero Section</div>', unsafe_allow_html=True)

            st.caption("Título principal")
            for i, t in enumerate(st.session_state.t16_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_hero_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t16_h_t_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t16_hero_titulos) > 1 and _del_btn(f"t16_h_t_del_{i}"):
                        st.session_state.t16_hero_titulos.pop(i); st.rerun()
            if _add_btn("t16_h_t_add", "＋ Adicionar título"):
                st.session_state.t16_hero_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t16_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t16_h_d_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t16_hero_descs) > 1 and _del_btn(f"t16_h_d_del_{i}"):
                        st.session_state.t16_hero_descs.pop(i); st.rerun()
            if _add_btn("t16_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t16_hero_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Imagem de fundo  *(URL)*")
            for i, img in enumerate(st.session_state.t16_hero_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_hero_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t16_h_i_{i}", label_visibility="collapsed", placeholder="https://...")
                with c2:
                    if len(st.session_state.t16_hero_imgs) > 1 and _del_btn(f"t16_h_i_del_{i}"):
                        st.session_state.t16_hero_imgs.pop(i); st.rerun()
            if _add_btn("t16_h_i_add", "＋ Adicionar imagem de fundo"):
                st.session_state.t16_hero_imgs.append({"valor": "https://"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ABOUT
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📖 Seção Sobre (About)</div>', unsafe_allow_html=True)

            st.caption("Título  *(use <br> para quebrar linha)*")
            for i, t in enumerate(st.session_state.t16_about_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_about_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t16_at_{i}", height=70, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t16_about_titulos) > 1 and _del_btn(f"t16_at_del_{i}"):
                        st.session_state.t16_about_titulos.pop(i); st.rerun()
            if _add_btn("t16_at_add", "＋ Adicionar título"):
                st.session_state.t16_about_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t16_about_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_about_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t16_ad_{i}", height=90, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t16_about_descs) > 1 and _del_btn(f"t16_ad_del_{i}"):
                        st.session_state.t16_about_descs.pop(i); st.rerun()
            if _add_btn("t16_ad_add", "＋ Adicionar descrição"):
                st.session_state.t16_about_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Botão  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t16_about_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t16_about_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t16_ab_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t16_about_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t16_ab_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t16_about_btns) > 1 and _del_btn(f"t16_ab_del_{i}"):
                        st.session_state.t16_about_btns.pop(i); st.rerun()
            if _add_btn("t16_ab_add", "＋ Adicionar botão"):
                st.session_state.t16_about_btns.append({"texto": "SAIBA MAIS", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # EXPERTISE (SERVICES)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">⚖️ Nossa Expertise (Serviços)</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t16_exp_secao_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_exp_secao_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t16_est_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t16_exp_secao_titulos) > 1 and _del_btn(f"t16_est_del_{i}"):
                        st.session_state.t16_exp_secao_titulos.pop(i); st.rerun()
            if _add_btn("t16_est_add", "＋ Adicionar título de seção"):
                st.session_state.t16_exp_secao_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Cards de serviço  *(Título | Descrição | Ícone)*")
            for i, item in enumerate(st.session_state.t16_exp_items):
                with st.expander(f"Serviço {i+1}: {item['titulo']}"):
                    st.session_state.t16_exp_items[i]["titulo"] = st.text_input(
                        "Título", item["titulo"], key=f"t16_ei_t_{i}")
                    st.session_state.t16_exp_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t16_ei_d_{i}", height=80)
                    st.session_state.t16_exp_items[i]["icon"] = st.text_input(
                        "Ícone / Emoji", item["icon"], key=f"t16_ei_i_{i}")
                    if len(st.session_state.t16_exp_items) > 1:
                        if st.button("🗑 Remover este serviço", key=f"t16_ei_del_{i}"):
                            st.session_state.t16_exp_items.pop(i); st.rerun()
            if _add_btn("t16_ei_add", "＋ Adicionar serviço"):
                st.session_state.t16_exp_items.append({
                    "icon": "⚖️", "titulo": "NOVO SERVIÇO", "desc": "Descrição do serviço."
                }); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NETWORK
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌍 Rede Global (Network)</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, t in enumerate(st.session_state.t16_net_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_net_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t16_nt_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t16_net_titulos) > 1 and _del_btn(f"t16_nt_del_{i}"):
                        st.session_state.t16_net_titulos.pop(i); st.rerun()
            if _add_btn("t16_nt_add", "＋ Adicionar título"):
                st.session_state.t16_net_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t16_net_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_net_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t16_nd_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t16_net_descs) > 1 and _del_btn(f"t16_nd_del_{i}"):
                        st.session_state.t16_net_descs.pop(i); st.rerun()
            if _add_btn("t16_nd_add", "＋ Adicionar descrição"):
                st.session_state.t16_net_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Cidades / Locais da rede")
            for i, city in enumerate(st.session_state.t16_net_cities):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_net_cities[i]["nome"] = st.text_input(
                        "Cidade", city["nome"], key=f"t16_nc_n_{i}", label_visibility="collapsed", placeholder="CIDADE")
                with c2:
                    if len(st.session_state.t16_net_cities) > 1 and _del_btn(f"t16_nc_del_{i}"):
                        st.session_state.t16_net_cities.pop(i); st.rerun()
            if _add_btn("t16_nc_add", "＋ Adicionar cidade"):
                st.session_state.t16_net_cities.append({"nome": "NOVA CIDADE"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé Completo</div>', unsafe_allow_html=True)

            st.caption("Logo do rodapé")
            for i, logo in enumerate(st.session_state.t16_foot_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_foot_logos[i]["valor"] = st.text_input(
                        "Logo Footer", logo["valor"], key=f"t16_fl_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t16_foot_logos) > 1 and _del_btn(f"t16_fl_del_{i}"):
                        st.session_state.t16_foot_logos.pop(i); st.rerun()
            if _add_btn("t16_fl_add", "＋ Adicionar logo"):
                st.session_state.t16_foot_logos.append({"valor": "EMPRESA"}); st.rerun()

            st.caption("Descrição da empresa  *(texto abaixo do logo)*")
            for i, desc in enumerate(st.session_state.t16_foot_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_foot_descs[i]["valor"] = st.text_area(
                        "Descrição Footer", desc["valor"], key=f"t16_fd_{i}", height=70, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t16_foot_descs) > 1 and _del_btn(f"t16_fd_del_{i}"):
                        st.session_state.t16_foot_descs.pop(i); st.rerun()
            if _add_btn("t16_fd_add", "＋ Adicionar descrição"):
                st.session_state.t16_foot_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Colunas de links  *(Título | Links)*")
            for i, col in enumerate(st.session_state.t16_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t16_foot_cols[i]["titulo"] = st.text_input(
                        "Título da Coluna", col["titulo"], key=f"t16_fcol_ti_{i}")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1:
                            st.session_state.t16_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t16_fcol_lt_{i}_{j}", label_visibility="collapsed")
                        with c2:
                            st.session_state.t16_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t16_fcol_lu_{i}_{j}", label_visibility="collapsed")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t16_fcol_ld_{i}_{j}"):
                                st.session_state.t16_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t16_fcol_la_{i}", "＋ Adicionar link"):
                        st.session_state.t16_foot_cols[i]["links"].append({"texto": "Novo Link", "url": "#"}); st.rerun()
                    if len(st.session_state.t16_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t16_fcol_del_{i}"):
                            st.session_state.t16_foot_cols.pop(i); st.rerun()
            if _add_btn("t16_fcol_add", "＋ Adicionar coluna ao rodapé"):
                st.session_state.t16_foot_cols.append({"titulo": "NOVA COLUNA", "links": [{"texto": "Link", "url": "#"}]}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t16_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t16_fcp_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t16_foot_copys) > 1 and _del_btn(f"t16_fcp_del_{i}"):
                        st.session_state.t16_foot_copys.pop(i); st.rerun()
            if _add_btn("t16_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t16_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t16_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t16_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t16_obs_{i}", height=80,
                        placeholder="Ex: Mudar a cor dourada para um tom mais bronze...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t16_obs) > 1 and _del_btn(f"t16_obs_del_{i}"):
                        st.session_state.t16_obs.pop(i); st.rerun()
            if _add_btn("t16_obs_add", "＋ Adicionar observação"):
                st.session_state.t16_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ENVIAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t16_send", type="primary"):
                st.success("✅ Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
                st.balloons()

    # ════════════════════════════════════════════════════════════════════════
    # PAINEL DIREITO — PREVIEW
    # ════════════════════════════════════════════════════════════════════════
    with col_preview:
        st.markdown(
            '<p class="img-caption">📌 Referência visual do template — role para ver o site completo</p>',
            unsafe_allow_html=True)
        st.markdown(
            f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}" alt="Preview do template" /></div>',
            unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(
        page_title=f"Editor — {TEMPLATE_NAME}",
        page_icon="⚖️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
