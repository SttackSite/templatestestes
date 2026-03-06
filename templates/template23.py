import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img23.png"
TEMPLATE_NAME = "Template 23 — PAIX Design Style (Architecture & Interior Design)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── CORES ───────────────────────────────────────────────────────────
        "t23_cores": [
            {"nome": "Fundo (Tom de Pedra)",        "valor": "#f7f7f7"},
            {"nome": "Texto Principal (Preto)",      "valor": "#1a1a1a"},
            {"nome": "Texto Secundário (Cinza)",     "valor": "#555555"},
            {"nome": "Linhas e Bordas",              "valor": "#dddddd"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t23_nav_logos": [{"valor": "PAIX DESIGN"}],
        "t23_nav_links": [
            {"texto": "Projetos",   "url": "#projetos"},
            {"texto": "Escritório", "url": "#escritorio"},
            {"texto": "Contato",    "url": "#contato"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t23_hero_labels":  [{"valor": "Arquitetura & Design de Interiores"}],
        "t23_hero_titulos": [{"valor": "A beleza reside na <br> intenção e na calma."}],
        "t23_hero_descs":   [{"valor": "PAIX é um estúdio de design focado na criação de espaços que transcendem o tempo. Nossa abordagem é guiada pela pureza dos materiais e pela harmonia entre a luz natural e a forma construída."}],

        # ── PROJETOS ────────────────────────────────────────────────────────
        "t23_project_items": [
            {"img": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=1600", "title": "Casa Minimalista",    "location": "Sintra", "year": "2024", "category": "Residencial / Design de Mobiliário"},
            {"img": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?w=1600", "title": "Apartamento Galeria", "location": "Porto",  "year": "2023", "category": "Residencial / Design de Mobiliário"},
        ],

        # ── SOBRE (TRANSICIONAL) ─────────────────────────────────────────────
        "t23_about_titulos": [{"valor": "Atmosferas Tangíveis"}],
        "t23_about_descs":   [{"valor": "Trabalhamos em estreita colaboração com artesãos locais para garantir que cada detalhe, desde a textura da parede até o encaixe da madeira, conte uma história de autenticidade e respeito ao ambiente."}],
        "t23_about_btns":    [{"texto": "Conheça Nosso Trabalho", "url": "https://www.google.com/"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t23_foot_brand_names": [{"valor": "PAIX DESIGN STUDIO"}],
        "t23_foot_addresses":   [{"valor": "AVENIDA DA LIBERDADE, LISBOA"}],
        "t23_foot_emails":      [{"valor": "hello@paix-design.com"}],
        "t23_foot_cols": [
            {"titulo": "REDES SOCIAIS", "links": [
                {"texto": "INSTAGRAM", "url": "#"},
                {"texto": "BEHANCE",   "url": "#"},
                {"texto": "LINKEDIN",  "url": "#"},
            ]},
        ],
        "t23_foot_copys": [{"valor": "© 2026 PAIX DESIGN. TODOS OS DIREITOS RESERVADOS."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t23_obs": [{"valor": ""}],
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
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300&family=Inter:wght@200;400&display=swap');
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
            for i, cor in enumerate(st.session_state.t23_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t23_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t23_cor_n_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t23_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t23_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t23_cores) > 1 and _del_btn(f"t23_cor_del_{i}"):
                        st.session_state.t23_cores.pop(i); st.rerun()
            if _add_btn("t23_cor_add", "＋ Adicionar cor"):
                st.session_state.t23_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome do escritório  *(lado esquerdo)*")
            for i, item in enumerate(st.session_state.t23_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_nav_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t23_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t23_nav_logos) > 1 and _del_btn(f"t23_logo_del_{i}"):
                        st.session_state.t23_nav_logos.pop(i); st.rerun()
            if _add_btn("t23_logo_add", "＋ Adicionar logo"):
                st.session_state.t23_nav_logos.append({"valor": "ESTÚDIO"}); st.rerun()

            st.caption("Links do menu  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t23_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t23_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t23_nl_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t23_nav_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t23_nl_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t23_nav_links) > 1 and _del_btn(f"t23_nl_del_{i}"):
                        st.session_state.t23_nav_links.pop(i); st.rerun()
            if _add_btn("t23_nl_add", "＋ Adicionar link"):
                st.session_state.t23_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏛️ Hero Section</div>', unsafe_allow_html=True)

            st.caption("Label / Subtítulo  *(texto pequeno em cinza)*")
            for i, l in enumerate(st.session_state.t23_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_hero_labels[i]["valor"] = st.text_input(
                        "Label", l["valor"], key=f"t23_h_l_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t23_hero_labels) > 1 and _del_btn(f"t23_h_l_del_{i}"):
                        st.session_state.t23_hero_labels.pop(i); st.rerun()
            if _add_btn("t23_h_l_add", "＋ Adicionar label"):
                st.session_state.t23_hero_labels.append({"valor": "Novo Label"}); st.rerun()

            st.caption("Título principal  *(use <br> para quebrar linha)*")
            for i, t in enumerate(st.session_state.t23_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t23_h_t_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t23_hero_titulos) > 1 and _del_btn(f"t23_h_t_del_{i}"):
                        st.session_state.t23_hero_titulos.pop(i); st.rerun()
            if _add_btn("t23_h_t_add", "＋ Adicionar título"):
                st.session_state.t23_hero_titulos.append({"valor": "Novo título poético."}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t23_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t23_h_d_{i}", height=90, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t23_hero_descs) > 1 and _del_btn(f"t23_h_d_del_{i}"):
                        st.session_state.t23_hero_descs.pop(i); st.rerun()
            if _add_btn("t23_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t23_hero_descs.append({"valor": "Nova descrição do estúdio."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # PROJETOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Projetos em Destaque</div>', unsafe_allow_html=True)
            st.caption("Cards de projeto  *(Título | Localização | Ano | Categoria | Imagem)*")
            for i, item in enumerate(st.session_state.t23_project_items):
                with st.expander(f"Projeto {i+1}: {item['title']}"):
                    st.session_state.t23_project_items[i]["title"] = st.text_input(
                        "Título do Projeto", item["title"], key=f"t23_pi_t_{i}")
                    st.session_state.t23_project_items[i]["location"] = st.text_input(
                        "Localização", item["location"], key=f"t23_pi_l_{i}")
                    st.session_state.t23_project_items[i]["year"] = st.text_input(
                        "Ano", item["year"], key=f"t23_pi_y_{i}")
                    st.session_state.t23_project_items[i]["category"] = st.text_input(
                        "Categoria", item["category"], key=f"t23_pi_c_{i}")
                    st.session_state.t23_project_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t23_pi_i_{i}")
                    if len(st.session_state.t23_project_items) > 1:
                        if st.button("🗑 Remover este projeto", key=f"t23_pi_del_{i}"):
                            st.session_state.t23_project_items.pop(i); st.rerun()
            if _add_btn("t23_pi_add", "＋ Adicionar projeto"):
                st.session_state.t23_project_items.append({
                    "img": "", "title": "NOVO PROJETO", "location": "CIDADE",
                    "year": "2026", "category": "RESIDENCIAL"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # SOBRE (TRANSICIONAL)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📜 Sobre o Escritório</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, t in enumerate(st.session_state.t23_about_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_about_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t23_at_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t23_about_titulos) > 1 and _del_btn(f"t23_at_del_{i}"):
                        st.session_state.t23_about_titulos.pop(i); st.rerun()
            if _add_btn("t23_at_add", "＋ Adicionar título"):
                st.session_state.t23_about_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t23_about_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_about_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t23_ad_{i}", height=90, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t23_about_descs) > 1 and _del_btn(f"t23_ad_del_{i}"):
                        st.session_state.t23_about_descs.pop(i); st.rerun()
            if _add_btn("t23_ad_add", "＋ Adicionar descrição"):
                st.session_state.t23_about_descs.append({"valor": "Nova descrição."}); st.rerun()

            st.caption("Botões  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t23_about_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t23_about_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t23_ab_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t23_about_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t23_ab_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t23_about_btns) > 1 and _del_btn(f"t23_ab_del_{i}"):
                        st.session_state.t23_about_btns.pop(i); st.rerun()
            if _add_btn("t23_ab_add", "＋ Adicionar botão"):
                st.session_state.t23_about_btns.append({"texto": "VEJA MAIS", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé Completo</div>', unsafe_allow_html=True)

            st.caption("Nome do escritório")
            for i, name in enumerate(st.session_state.t23_foot_brand_names):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_foot_brand_names[i]["valor"] = st.text_input(
                        "Nome", name["valor"], key=f"t23_fn_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t23_foot_brand_names) > 1 and _del_btn(f"t23_fn_del_{i}"):
                        st.session_state.t23_foot_brand_names.pop(i); st.rerun()
            if _add_btn("t23_fn_add", "＋ Adicionar nome"):
                st.session_state.t23_foot_brand_names.append({"valor": "ESTÚDIO"}); st.rerun()

            st.caption("Endereço")
            for i, addr in enumerate(st.session_state.t23_foot_addresses):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_foot_addresses[i]["valor"] = st.text_input(
                        "Endereço", addr["valor"], key=f"t23_fa_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t23_foot_addresses) > 1 and _del_btn(f"t23_fa_del_{i}"):
                        st.session_state.t23_foot_addresses.pop(i); st.rerun()
            if _add_btn("t23_fa_add", "＋ Adicionar endereço"):
                st.session_state.t23_foot_addresses.append({"valor": "RUA, CIDADE"}); st.rerun()

            st.caption("Email de contato")
            for i, email in enumerate(st.session_state.t23_foot_emails):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_foot_emails[i]["valor"] = st.text_input(
                        "Email", email["valor"], key=f"t23_fe_{i}", label_visibility="collapsed", placeholder="email@estudio.com")
                with c2:
                    if len(st.session_state.t23_foot_emails) > 1 and _del_btn(f"t23_fe_del_{i}"):
                        st.session_state.t23_foot_emails.pop(i); st.rerun()
            if _add_btn("t23_fe_add", "＋ Adicionar email"):
                st.session_state.t23_foot_emails.append({"valor": "email@estudio.com"}); st.rerun()

            st.caption("Colunas de links  *(redes sociais)*")
            for i, col in enumerate(st.session_state.t23_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t23_foot_cols[i]["titulo"] = st.text_input(
                        "Título Coluna", col["titulo"], key=f"t23_fc_t_{i}")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1:
                            st.session_state.t23_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t23_fc_l_t_{i}_{j}", label_visibility="collapsed")
                        with c2:
                            st.session_state.t23_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t23_fc_l_u_{i}_{j}", label_visibility="collapsed")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t23_fc_l_del_{i}_{j}"):
                                st.session_state.t23_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t23_fc_l_add_{i}", "＋ Adicionar link"):
                        st.session_state.t23_foot_cols[i]["links"].append({"texto": "LINK", "url": "#"}); st.rerun()
                    if len(st.session_state.t23_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t23_fc_del_{i}"):
                            st.session_state.t23_foot_cols.pop(i); st.rerun()
            if _add_btn("t23_fc_add", "＋ Adicionar coluna"):
                st.session_state.t23_foot_cols.append({"titulo": "NOVA", "links": [{"texto": "Link", "url": "#"}]}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t23_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t23_fcp_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t23_foot_copys) > 1 and _del_btn(f"t23_fcp_del_{i}"):
                        st.session_state.t23_foot_copys.pop(i); st.rerun()
            if _add_btn("t23_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t23_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t23_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t23_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t23_obs_{i}", height=80,
                        placeholder="Ex: Usar uma paleta mais monocromática...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t23_obs) > 1 and _del_btn(f"t23_obs_del_{i}"):
                        st.session_state.t23_obs.pop(i); st.rerun()
            if _add_btn("t23_obs_add", "＋ Adicionar observação"):
                st.session_state.t23_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ENVIAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t23_send", type="primary"):
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
        page_icon="🏛️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
