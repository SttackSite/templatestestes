import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img20.png"
TEMPLATE_NAME = "Template 20 — Moooi Style (Luxury Furniture & Lifestyle)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── CORES ───────────────────────────────────────────────────────────
        "t20_cores": [
            {"nome": "Fundo Principal (Branco)",    "valor": "#ffffff"},
            {"nome": "Texto Principal (Preto)",      "valor": "#000000"},
            {"nome": "Fundo Rodapé (Cinza Claro)",   "valor": "#fafafa"},
            {"nome": "Bordas e Linhas",              "valor": "#eeeeee"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t20_nav_logos": [{"valor": "Moooi"}],
        "t20_nav_links": [
            {"texto": "Coleção",       "url": "#colecao"},
            {"texto": "Estilo de Vida","url": "#estilo"},
            {"texto": "Histórias",     "url": "#historias"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t20_hero_labels":  [{"valor": "LANÇAMENTO DE COLEÇÃO"}],
        "t20_hero_titulos": [{"valor": "A Life Extraordinary"}],
        "t20_hero_btns":    [{"texto": "DESCUBRA O NOVO", "url": "https://www.google.com/"}],
        "t20_hero_imgs":    [{"valor": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=1600&q=80"}],

        # ── INTRODUÇÃO ──────────────────────────────────────────────────────
        "t20_intro_titulos": [{"valor": "Inspirando o Mundo desde 2001"}],
        "t20_intro_descs":   [{"valor": "A Moooi sempre foi sinônimo de um estilo de vida que é ao mesmo tempo lúdico e refinado. Nossas criações desafiam a gravidade, a luz e a imaginação, transformando espaços cotidianos em experiências extraordinárias."}],

        # ── PRODUTOS ────────────────────────────────────────────────────────
        "t20_product_items": [
            {"img": "https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=800", "nome": "Luminária Heracleum", "desc": "DESIGN POR MARCEL WANDERS", "btn_texto": "Ver Detalhes", "url": "#", "margin_top": "0px"},
            {"img": "https://images.unsplash.com/photo-1567016432779-094069958ea5?w=800",  "nome": "Sofá Cloud",          "desc": "SENTANDO NAS NUVENS",       "btn_texto": "Ver Detalhes", "url": "#", "margin_top": "80px"},
        ],

        # ── BANNER HISTÓRIAS ─────────────────────────────────────────────────
        "t20_story_imgs":    [{"valor": "https://images.unsplash.com/photo-1534349762230-e0cadf78f5db?w=1600"}],
        "t20_story_titulos": [{"valor": "Paredes que Contam Histórias"}],
        "t20_story_descs":   [{"valor": "Explore nossa coleção exclusiva de papéis de parede inspirados em animais extintos e mundos fantásticos."}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t20_foot_brand_names": [{"valor": "Moooi"}],
        "t20_foot_brand_descs": [{"valor": "A Life Extraordinary.<br>Subscreva para receber inspiração semanal."}],
        "t20_foot_cols": [
            {"titulo": "PRODUTOS",  "links": [{"texto": "Iluminação", "url": "#"}, {"texto": "Móveis", "url": "#"}, {"texto": "Acessórios", "url": "#"}, {"texto": "Tapetes", "url": "#"}]},
            {"titulo": "SERVIÇOS",  "links": [{"texto": "Localizador de Lojas", "url": "#"}, {"texto": "Atendimento", "url": "#"}, {"texto": "Downloads 3D", "url": "#"}]},
            {"titulo": "SOCIAL",    "links": [{"texto": "Instagram", "url": "#"}, {"texto": "Pinterest", "url": "#"}, {"texto": "LinkedIn", "url": "#"}]},
        ],
        "t20_foot_copys": [{"valor": "© 2026 MOOOI B.V. TODOS OS DIREITOS RESERVADOS."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t20_obs": [{"valor": ""}],
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
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500&family=Inter:wght@300;400;600&display=swap');
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
            for i, cor in enumerate(st.session_state.t20_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t20_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t20_cor_n_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t20_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t20_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t20_cores) > 1 and _del_btn(f"t20_cor_del_{i}"):
                        st.session_state.t20_cores.pop(i); st.rerun()
            if _add_btn("t20_cor_add", "＋ Adicionar cor"):
                st.session_state.t20_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca  *(centro)*")
            for i, item in enumerate(st.session_state.t20_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_nav_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t20_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t20_nav_logos) > 1 and _del_btn(f"t20_logo_del_{i}"):
                        st.session_state.t20_nav_logos.pop(i); st.rerun()
            if _add_btn("t20_logo_add", "＋ Adicionar logo"):
                st.session_state.t20_nav_logos.append({"valor": "Marca"}); st.rerun()

            st.caption("Links do menu  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t20_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t20_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t20_nl_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t20_nav_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t20_nl_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t20_nav_links) > 1 and _del_btn(f"t20_nl_del_{i}"):
                        st.session_state.t20_nav_links.pop(i); st.rerun()
            if _add_btn("t20_nl_add", "＋ Adicionar link"):
                st.session_state.t20_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">✨ Hero Section</div>', unsafe_allow_html=True)

            st.caption("Label superior  *(texto pequeno acima do título)*")
            for i, l in enumerate(st.session_state.t20_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_hero_labels[i]["valor"] = st.text_input(
                        "Label", l["valor"], key=f"t20_h_l_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t20_hero_labels) > 1 and _del_btn(f"t20_h_l_del_{i}"):
                        st.session_state.t20_hero_labels.pop(i); st.rerun()
            if _add_btn("t20_h_l_add", "＋ Adicionar label"):
                st.session_state.t20_hero_labels.append({"valor": "Novo Label"}); st.rerun()

            st.caption("Título principal")
            for i, t in enumerate(st.session_state.t20_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_hero_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t20_h_t_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t20_hero_titulos) > 1 and _del_btn(f"t20_h_t_del_{i}"):
                        st.session_state.t20_hero_titulos.pop(i); st.rerun()
            if _add_btn("t20_h_t_add", "＋ Adicionar título"):
                st.session_state.t20_hero_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Imagem de fundo  *(URL)*")
            for i, img in enumerate(st.session_state.t20_hero_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_hero_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t20_h_i_{i}", label_visibility="collapsed", placeholder="https://...")
                with c2:
                    if len(st.session_state.t20_hero_imgs) > 1 and _del_btn(f"t20_h_i_del_{i}"):
                        st.session_state.t20_hero_imgs.pop(i); st.rerun()
            if _add_btn("t20_h_i_add", "＋ Adicionar imagem"):
                st.session_state.t20_hero_imgs.append({"valor": "https://"}); st.rerun()

            st.caption("Botão  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t20_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t20_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t20_hb_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t20_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t20_hb_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t20_hero_btns) > 1 and _del_btn(f"t20_hb_del_{i}"):
                        st.session_state.t20_hero_btns.pop(i); st.rerun()
            if _add_btn("t20_hb_add", "＋ Adicionar botão"):
                st.session_state.t20_hero_btns.append({"texto": "DESCUBRA", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # INTRODUÇÃO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📖 Introdução da Marca</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, t in enumerate(st.session_state.t20_intro_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_intro_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t20_it_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t20_intro_titulos) > 1 and _del_btn(f"t20_it_del_{i}"):
                        st.session_state.t20_intro_titulos.pop(i); st.rerun()
            if _add_btn("t20_it_add", "＋ Adicionar título"):
                st.session_state.t20_intro_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição da marca")
            for i, d in enumerate(st.session_state.t20_intro_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_intro_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t20_id_{i}", height=100, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t20_intro_descs) > 1 and _del_btn(f"t20_id_del_{i}"):
                        st.session_state.t20_intro_descs.pop(i); st.rerun()
            if _add_btn("t20_id_add", "＋ Adicionar descrição"):
                st.session_state.t20_intro_descs.append({"valor": "Nova descrição."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # PRODUTOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🪑 Coleção de Produtos</div>', unsafe_allow_html=True)
            st.caption("Cards de produto  *(Nome | Designer | Imagem | Botão)*")
            for i, item in enumerate(st.session_state.t20_product_items):
                with st.expander(f"Produto {i+1}: {item['nome']}"):
                    st.session_state.t20_product_items[i]["nome"] = st.text_input(
                        "Nome do Produto", item["nome"], key=f"t20_pi_n_{i}")
                    st.session_state.t20_product_items[i]["desc"] = st.text_input(
                        "Designer / Descrição", item["desc"], key=f"t20_pi_d_{i}")
                    st.session_state.t20_product_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t20_pi_i_{i}")
                    st.session_state.t20_product_items[i]["btn_texto"] = st.text_input(
                        "Texto do Botão", item["btn_texto"], key=f"t20_pi_bt_{i}")
                    st.session_state.t20_product_items[i]["url"] = st.text_input(
                        "URL do Link", item["url"], key=f"t20_pi_u_{i}")
                    st.session_state.t20_product_items[i]["margin_top"] = st.text_input(
                        "Margem Superior  *(ex: 80px)*", item["margin_top"], key=f"t20_pi_m_{i}")
                    if len(st.session_state.t20_product_items) > 1:
                        if st.button("🗑 Remover este produto", key=f"t20_pi_del_{i}"):
                            st.session_state.t20_product_items.pop(i); st.rerun()
            if _add_btn("t20_pi_add", "＋ Adicionar produto"):
                st.session_state.t20_product_items.append({
                    "img": "", "nome": "Novo Produto", "desc": "DESIGNER",
                    "btn_texto": "Ver Detalhes", "url": "#", "margin_top": "0px"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # BANNER HISTÓRIAS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Banner Histórias</div>', unsafe_allow_html=True)

            st.caption("Imagem do banner  *(URL)*")
            for i, img in enumerate(st.session_state.t20_story_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_story_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t20_si_{i}", label_visibility="collapsed", placeholder="https://...")
                with c2:
                    if len(st.session_state.t20_story_imgs) > 1 and _del_btn(f"t20_si_del_{i}"):
                        st.session_state.t20_story_imgs.pop(i); st.rerun()
            if _add_btn("t20_si_add", "＋ Adicionar imagem"):
                st.session_state.t20_story_imgs.append({"valor": "https://"}); st.rerun()

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t20_story_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_story_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t20_st_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t20_story_titulos) > 1 and _del_btn(f"t20_st_del_{i}"):
                        st.session_state.t20_story_titulos.pop(i); st.rerun()
            if _add_btn("t20_st_add", "＋ Adicionar título"):
                st.session_state.t20_story_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t20_story_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_story_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t20_sd_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t20_story_descs) > 1 and _del_btn(f"t20_sd_del_{i}"):
                        st.session_state.t20_story_descs.pop(i); st.rerun()
            if _add_btn("t20_sd_add", "＋ Adicionar descrição"):
                st.session_state.t20_story_descs.append({"valor": "Nova descrição."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé Completo</div>', unsafe_allow_html=True)

            st.caption("Nome da marca  *(serif grande)*")
            for i, name in enumerate(st.session_state.t20_foot_brand_names):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_foot_brand_names[i]["valor"] = st.text_input(
                        "Nome", name["valor"], key=f"t20_fn_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t20_foot_brand_names) > 1 and _del_btn(f"t20_fn_del_{i}"):
                        st.session_state.t20_foot_brand_names.pop(i); st.rerun()
            if _add_btn("t20_fn_add", "＋ Adicionar nome"):
                st.session_state.t20_foot_brand_names.append({"valor": "Marca"}); st.rerun()

            st.caption("Descrição da marca  *(use <br> para quebrar linha)*")
            for i, desc in enumerate(st.session_state.t20_foot_brand_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_foot_brand_descs[i]["valor"] = st.text_area(
                        "Descrição", desc["valor"], key=f"t20_fd_{i}", height=70, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t20_foot_brand_descs) > 1 and _del_btn(f"t20_fd_del_{i}"):
                        st.session_state.t20_foot_brand_descs.pop(i); st.rerun()
            if _add_btn("t20_fd_add", "＋ Adicionar descrição"):
                st.session_state.t20_foot_brand_descs.append({"valor": "Nova descrição."}); st.rerun()

            st.caption("Colunas de links")
            for i, col in enumerate(st.session_state.t20_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t20_foot_cols[i]["titulo"] = st.text_input(
                        "Título Coluna", col["titulo"], key=f"t20_fc_t_{i}")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1:
                            st.session_state.t20_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t20_fc_l_t_{i}_{j}", label_visibility="collapsed")
                        with c2:
                            st.session_state.t20_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t20_fc_l_u_{i}_{j}", label_visibility="collapsed")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t20_fc_l_del_{i}_{j}"):
                                st.session_state.t20_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t20_fc_l_add_{i}", "＋ Adicionar link"):
                        st.session_state.t20_foot_cols[i]["links"].append({"texto": "LINK", "url": "#"}); st.rerun()
                    if len(st.session_state.t20_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t20_fc_del_{i}"):
                            st.session_state.t20_foot_cols.pop(i); st.rerun()
            if _add_btn("t20_fc_add", "＋ Adicionar coluna"):
                st.session_state.t20_foot_cols.append({"titulo": "NOVA", "links": [{"texto": "Link", "url": "#"}]}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t20_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t20_fcp_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t20_foot_copys) > 1 and _del_btn(f"t20_fcp_del_{i}"):
                        st.session_state.t20_foot_copys.pop(i); st.rerun()
            if _add_btn("t20_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t20_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t20_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t20_obs_{i}", height=80,
                        placeholder="Ex: Tornar o layout mais minimalista...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t20_obs) > 1 and _del_btn(f"t20_obs_del_{i}"):
                        st.session_state.t20_obs.pop(i); st.rerun()
            if _add_btn("t20_obs_add", "＋ Adicionar observação"):
                st.session_state.t20_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ENVIAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t20_send", type="primary"):
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
        page_icon="✨",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
