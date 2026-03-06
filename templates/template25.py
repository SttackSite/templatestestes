import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img25.png"
TEMPLATE_NAME = "Template 25 — Plunder & Poach Style (Strategy & Design Agency)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── CORES ───────────────────────────────────────────────────────────
        "t25_cores": [
            {"nome": "Fundo (Papel/Creme)",      "valor": "#f4f1ea"},
            {"nome": "Texto Principal (Preto)",   "valor": "#1a1a1a"},
            {"nome": "Destaque (Escuro)",          "valor": "#333333"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t25_nav_logos": [{"valor": "Plunder & Poach"}],
        "t25_nav_links": [
            {"texto": "Trabalhos", "url": "#trabalhos"},
            {"texto": "Estúdio",   "url": "#estudio"},
            {"texto": "Contato",   "url": "#contato"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t25_hero_labels":  [{"valor": "Estratégia · Design · Rebeldia"}],
        "t25_hero_titulos": [{"valor": "FINALIZAMOS<br>O COMUM."}],
        "t25_hero_descs":   [{"valor": "Somos uma agência de criação para marcas que não têm medo de quebrar as regras. Transformamos negócios em lendas através de um design audacioso e narrativas implacáveis."}],

        # ── SHOWCASE (GRID) ──────────────────────────────────────────────────
        "t25_project_items": [
            {"img": "https://images.unsplash.com/photo-1527067829737-402993088e6b?w=800", "title": "Ouro Negro",     "category": "IDENTIDADE VISUAL / CAFÉ",  "desc": "Uma marca construída sobre a herança e o sabor intenso."},
            {"img": "https://images.unsplash.com/photo-1560067174-c5a3a8f37060?w=800",    "title": "Alcateia Alpha", "category": "DIREÇÃO DE ARTE / MODA",      "desc": "O instinto selvagem traduzido em alfaiataria premium."},
            {"img": "https://images.unsplash.com/photo-1559136555-9303baea8ebd?w=800",    "title": "Bússola Norte",  "category": "ESTRATÉGIA DIGITAL / 2024",   "desc": "Guiando marcas em mares nunca navegados."},
            {"img": "https://images.unsplash.com/photo-1520004434532-668416a08753?w=800", "title": "Armazém V",      "category": "BRANDING / ARQUITETURA",      "desc": "Espaços que respiram história e design industrial."},
        ],

        # ── MANIFESTO ───────────────────────────────────────────────────────
        "t25_manifest_titulos": [{"valor": "VOCÊ É A PRESA OU O PREDADOR?"}],
        "t25_manifest_descs":   [{"valor": "\"No mercado moderno, a neutralidade é o caminho mais rápido para a extinção. Nós ajudamos você a afiar as garras e dominar seu território.\""}],
        "t25_manifest_labels":  [{"valor": "Pronto para o ataque?"}],
        "t25_manifest_btns":    [{"texto": "Inicie sua Jornada", "url": "https://www.google.com/"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t25_foot_brand_names": [{"valor": "Plunder & Poach."}],
        "t25_foot_brand_descs": [{"valor": "Capturando a essência do extraordinário."}],
        "t25_foot_emails":      [{"valor": "studio@plunderpoach.com"}],
        "t25_foot_locations":   [{"valor": "Londres / Global"}],
        "t25_foot_copys":       [{"valor": "© 2026 PLUNDER & POACH — TODOS OS DIREITOS RESERVADOS."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t25_obs": [{"valor": ""}],
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
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
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
            for i, cor in enumerate(st.session_state.t25_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t25_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t25_cor_n_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t25_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t25_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t25_cores) > 1 and _del_btn(f"t25_cor_del_{i}"):
                        st.session_state.t25_cores.pop(i); st.rerun()
            if _add_btn("t25_cor_add", "＋ Adicionar cor"):
                st.session_state.t25_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da agência  *(lado esquerdo)*")
            for i, item in enumerate(st.session_state.t25_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t25_nav_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t25_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t25_nav_logos) > 1 and _del_btn(f"t25_logo_del_{i}"):
                        st.session_state.t25_nav_logos.pop(i); st.rerun()
            if _add_btn("t25_logo_add", "＋ Adicionar logo"):
                st.session_state.t25_nav_logos.append({"valor": "AGÊNCIA"}); st.rerun()

            st.caption("Links do menu  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t25_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t25_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t25_nl_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t25_nav_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t25_nl_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t25_nav_links) > 1 and _del_btn(f"t25_nl_del_{i}"):
                        st.session_state.t25_nav_links.pop(i); st.rerun()
            if _add_btn("t25_nl_add", "＋ Adicionar link"):
                st.session_state.t25_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">⚓ Hero Section</div>', unsafe_allow_html=True)

            st.caption("Label  *(texto pequeno acima do título)*")
            for i, l in enumerate(st.session_state.t25_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t25_hero_labels[i]["valor"] = st.text_input(
                        "Label", l["valor"], key=f"t25_h_l_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t25_hero_labels) > 1 and _del_btn(f"t25_h_l_del_{i}"):
                        st.session_state.t25_hero_labels.pop(i); st.rerun()
            if _add_btn("t25_h_l_add", "＋ Adicionar label"):
                st.session_state.t25_hero_labels.append({"valor": "Novo Label"}); st.rerun()

            st.caption("Título principal  *(use <br> para quebrar linha)*")
            for i, t in enumerate(st.session_state.t25_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t25_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t25_h_t_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t25_hero_titulos) > 1 and _del_btn(f"t25_h_t_del_{i}"):
                        st.session_state.t25_hero_titulos.pop(i); st.rerun()
            if _add_btn("t25_h_t_add", "＋ Adicionar título"):
                st.session_state.t25_hero_titulos.append({"valor": "NOVO TÍTULO."}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t25_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t25_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t25_h_d_{i}", height=90, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t25_hero_descs) > 1 and _del_btn(f"t25_h_d_del_{i}"):
                        st.session_state.t25_hero_descs.pop(i); st.rerun()
            if _add_btn("t25_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t25_hero_descs.append({"valor": "Nova descrição da agência."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # SHOWCASE (GRID)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Showcase de Projetos</div>', unsafe_allow_html=True)
            st.caption("Cards de projeto  *(Título | Categoria | Descrição | Imagem)*")
            for i, item in enumerate(st.session_state.t25_project_items):
                with st.expander(f"Projeto {i+1}: {item['title']}"):
                    st.session_state.t25_project_items[i]["title"] = st.text_input(
                        "Título do Projeto", item["title"], key=f"t25_pi_t_{i}")
                    st.session_state.t25_project_items[i]["category"] = st.text_input(
                        "Categoria", item["category"], key=f"t25_pi_c_{i}")
                    st.session_state.t25_project_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t25_pi_d_{i}", height=70)
                    st.session_state.t25_project_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t25_pi_i_{i}")
                    if len(st.session_state.t25_project_items) > 1:
                        if st.button("🗑 Remover este projeto", key=f"t25_pi_del_{i}"):
                            st.session_state.t25_project_items.pop(i); st.rerun()
            if _add_btn("t25_pi_add", "＋ Adicionar projeto"):
                st.session_state.t25_project_items.append({
                    "img": "", "title": "NOVO PROJETO",
                    "category": "BRANDING", "desc": "DESCRIÇÃO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # MANIFESTO (SEÇÃO ESCURA)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📜 Manifesto (Seção Escura)</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, t in enumerate(st.session_state.t25_manifest_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t25_manifest_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t25_mt_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t25_manifest_titulos) > 1 and _del_btn(f"t25_mt_del_{i}"):
                        st.session_state.t25_manifest_titulos.pop(i); st.rerun()
            if _add_btn("t25_mt_add", "＋ Adicionar título"):
                st.session_state.t25_manifest_titulos.append({"valor": "NOVO TÍTULO"}); st.rerun()

            st.caption("Descrição / Citação")
            for i, d in enumerate(st.session_state.t25_manifest_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t25_manifest_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t25_md_{i}", height=90, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t25_manifest_descs) > 1 and _del_btn(f"t25_md_del_{i}"):
                        st.session_state.t25_manifest_descs.pop(i); st.rerun()
            if _add_btn("t25_md_add", "＋ Adicionar descrição"):
                st.session_state.t25_manifest_descs.append({"valor": "\"Nova citação poderosa.\""}); st.rerun()

            st.caption("Label CTA  *(texto acima do botão)*")
            for i, l in enumerate(st.session_state.t25_manifest_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t25_manifest_labels[i]["valor"] = st.text_input(
                        "Label", l["valor"], key=f"t25_ml_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t25_manifest_labels) > 1 and _del_btn(f"t25_ml_del_{i}"):
                        st.session_state.t25_manifest_labels.pop(i); st.rerun()
            if _add_btn("t25_ml_add", "＋ Adicionar label"):
                st.session_state.t25_manifest_labels.append({"valor": "Novo Label"}); st.rerun()

            st.caption("Botões de ação  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t25_manifest_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t25_manifest_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t25_mb_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t25_manifest_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t25_mb_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t25_manifest_btns) > 1 and _del_btn(f"t25_mb_del_{i}"):
                        st.session_state.t25_manifest_btns.pop(i); st.rerun()
            if _add_btn("t25_mb_add", "＋ Adicionar botão"):
                st.session_state.t25_manifest_btns.append({"texto": "CONTATO", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Nome da marca")
            for i, name in enumerate(st.session_state.t25_foot_brand_names):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t25_foot_brand_names[i]["valor"] = st.text_input(
                        "Nome", name["valor"], key=f"t25_fn_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t25_foot_brand_names) > 1 and _del_btn(f"t25_fn_del_{i}"):
                        st.session_state.t25_foot_brand_names.pop(i); st.rerun()
            if _add_btn("t25_fn_add", "＋ Adicionar nome"):
                st.session_state.t25_foot_brand_names.append({"valor": "AGÊNCIA"}); st.rerun()

            st.caption("Descrição da marca")
            for i, desc in enumerate(st.session_state.t25_foot_brand_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t25_foot_brand_descs[i]["valor"] = st.text_input(
                        "Descrição", desc["valor"], key=f"t25_fd_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t25_foot_brand_descs) > 1 and _del_btn(f"t25_fd_del_{i}"):
                        st.session_state.t25_foot_brand_descs.pop(i); st.rerun()
            if _add_btn("t25_fd_add", "＋ Adicionar descrição"):
                st.session_state.t25_foot_brand_descs.append({"valor": "Nova descrição."}); st.rerun()

            st.caption("Email de contato")
            for i, email in enumerate(st.session_state.t25_foot_emails):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t25_foot_emails[i]["valor"] = st.text_input(
                        "Email", email["valor"], key=f"t25_fe_{i}", label_visibility="collapsed", placeholder="email@agencia.com")
                with c2:
                    if len(st.session_state.t25_foot_emails) > 1 and _del_btn(f"t25_fe_del_{i}"):
                        st.session_state.t25_foot_emails.pop(i); st.rerun()
            if _add_btn("t25_fe_add", "＋ Adicionar email"):
                st.session_state.t25_foot_emails.append({"valor": "email@agencia.com"}); st.rerun()

            st.caption("Localização")
            for i, loc in enumerate(st.session_state.t25_foot_locations):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t25_foot_locations[i]["valor"] = st.text_input(
                        "Localização", loc["valor"], key=f"t25_fl_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t25_foot_locations) > 1 and _del_btn(f"t25_fl_del_{i}"):
                        st.session_state.t25_foot_locations.pop(i); st.rerun()
            if _add_btn("t25_fl_add", "＋ Adicionar localização"):
                st.session_state.t25_foot_locations.append({"valor": "Cidade / Global"}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t25_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t25_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t25_fcp_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t25_foot_copys) > 1 and _del_btn(f"t25_fcp_del_{i}"):
                        st.session_state.t25_foot_copys.pop(i); st.rerun()
            if _add_btn("t25_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t25_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t25_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t25_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t25_obs_{i}", height=80,
                        placeholder="Ex: Usar uma tipografia ainda mais pesada...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t25_obs) > 1 and _del_btn(f"t25_obs_del_{i}"):
                        st.session_state.t25_obs.pop(i); st.rerun()
            if _add_btn("t25_obs_add", "＋ Adicionar observação"):
                st.session_state.t25_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ENVIAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t25_send", type="primary"):
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
        page_icon="⚓",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
