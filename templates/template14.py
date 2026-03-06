import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img14.png"
TEMPLATE_NAME = "Template 14 — Memphis Zoo Style (Experiência & Aventura)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── CORES ───────────────────────────────────────────────────────────
        "t14_cores": [
            {"nome": "Laranja (Botões)",      "valor": "#f37021"},
            {"nome": "Verde (Conservação)",   "valor": "#004a26"},
            {"nome": "Bege (Fundo Visita)",   "valor": "#f9f7f2"},
            {"nome": "Cor de Texto (Escuro)", "valor": "#333333"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t14_logos": [{"valor": "MEMPHIS ZOO"}],
        "t14_nav_links": [
            {"texto": "ANIMALS",      "url": "#animals"},
            {"texto": "EXHIBITS",     "url": "#exhibits"},
            {"texto": "EDUCATION",    "url": "#education"},
            {"texto": "CONSERVATION", "url": "#conservation"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t14_hero_titulos": [{"valor": "ADVENTURE AWAITS"}],
        "t14_hero_descs":   [{"valor": "Explore o mundo selvagem no coração de Memphis."}],
        "t14_hero_imgs":    [{"valor": "https://images.unsplash.com/photo-1546182990-dffeafbe841d?auto=format&fit=crop&w=1600&q=80"}],

        # ── BOTÕES RÁPIDOS ───────────────────────────────────────────────────
        "t14_quick_btns": [
            {"texto": "BUY TICKETS",      "url": "https://www.google.com/"},
            {"texto": "BECOME A MEMBER",  "url": "https://www.google.com/"},
            {"texto": "DONATE TODAY",     "url": "https://www.google.com/"},
        ],

        # ── VISITA ──────────────────────────────────────────────────────────
        "t14_visit_titulos": [{"valor": "PLANEJE SUA VISITA"}],
        "t14_visit_descs":   [{"valor": "Estamos abertos diariamente das 9h às 17h. Venha ver nossos novos filhotes!"}],
        "t14_visit_infos": [
            {"titulo": "🕒 Horários",    "desc": "Seg - Dom: 09:00 - 17:00"},
            {"titulo": "📍 Localização", "desc": "2000 Prentiss Pl, Memphis, TN"},
            {"titulo": "🗺️ Mapa do Zoo", "desc": "BAIXAR MAPA", "url": "https://www.google.com/"},
        ],

        # ── ANIMAIS ─────────────────────────────────────────────────────────
        "t14_animal_secao_titulos": [{"valor": "CONHEÇA OS RESIDENTES"}],
        "t14_animal_items": [
            {"img": "https://images.unsplash.com/photo-1517685352821-92cf88aee5a5?w=500", "nome": "Leão Africano",    "cat": "FELINOS", "btn_txt": "Saber mais",  "url": "https://www.google.com/"},
            {"img": "https://images.unsplash.com/photo-1544860707-c352cc5a92e3?w=500", "nome": "Panda Gigante",    "cat": "ÁSIA",    "btn_txt": "Saber mais",  "url": "https://www.google.com/"},
            {"img": "https://images.unsplash.com/photo-1557008075-7f2c5efa4cfd?w=500", "nome": "Girafa Reticulada","cat": "SAVANA",  "btn_txt": "Saber mais",  "url": "https://www.google.com/"},
        ],

        # ── CONSERVAÇÃO ─────────────────────────────────────────────────────
        "t14_cons_titulos": [{"valor": "SALVANDO ESPÉCIES NO MUNDO TODO"}],
        "t14_cons_descs":   [{"valor": "O Memphis Zoo é líder em pesquisa e conservação. Desde a reintrodução de sapos raros até a proteção de habitats na África, seu ingresso faz a diferença."}],
        "t14_cons_btns":    [{"texto": "VEJA NOSSO IMPACTO", "url": "https://www.google.com/"}],

        # ── EVENTOS ─────────────────────────────────────────────────────────
        "t14_event_titulos": [{"valor": "NOITE NO ZOO"}],
        "t14_event_descs":   [{"valor": "Participe de nossos eventos noturnos exclusivos para famílias. Jantares temáticos, tours guiados sob o luar e muito mais."}],
        "t14_event_imgs":    [{"valor": "https://images.unsplash.com/photo-1502675135487-e971002a6adb?w=600"}],
        "t14_event_btns":    [{"texto": "VER CALENDÁRIO DE EVENTOS", "url": "https://www.google.com/"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t14_foot_logos": [{"valor": "MEMPHIS ZOO"}],
        "t14_foot_descs": [{"valor": "Conectando pessoas aos animais através de experiências memoráveis."}],
        "t14_foot_cols": [
            {"titulo": "EXPLORE",  "links": [{"texto": "Animais", "url": "#"}, {"texto": "Experiências", "url": "#"}, {"texto": "Membros", "url": "#"}]},
            {"titulo": "SUPORTE",  "links": [{"texto": "Doar", "url": "#"}, {"texto": "Voluntários", "url": "#"}, {"texto": "Trabalhe Conosco", "url": "#"}]},
        ],
        "t14_foot_copys": [{"valor": "© 2026 Memphis Zoo. Todos os direitos reservados."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t14_obs": [{"valor": ""}],
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
            for i, cor in enumerate(st.session_state.t14_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t14_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t14_cor_n_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t14_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t14_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t14_cores) > 1 and _del_btn(f"t14_cor_del_{i}"):
                        st.session_state.t14_cores.pop(i); st.rerun()
            if _add_btn("t14_cor_add", "＋ Adicionar cor"):
                st.session_state.t14_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Header)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca")
            for i, logo in enumerate(st.session_state.t14_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t14_logos[i]["valor"] = st.text_input(
                        "Logo", logo["valor"], key=f"t14_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t14_logos) > 1 and _del_btn(f"t14_logo_del_{i}"):
                        st.session_state.t14_logos.pop(i); st.rerun()
            if _add_btn("t14_logo_add", "＋ Adicionar logo"):
                st.session_state.t14_logos.append({"valor": "MARCA"}); st.rerun()

            st.caption("Links do menu  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t14_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t14_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t14_nl_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t14_nav_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t14_nl_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t14_nav_links) > 1 and _del_btn(f"t14_nl_del_{i}"):
                        st.session_state.t14_nav_links.pop(i); st.rerun()
            if _add_btn("t14_nl_add", "＋ Adicionar link ao menu"):
                st.session_state.t14_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🦁 Hero Section</div>', unsafe_allow_html=True)

            st.caption("Título principal")
            for i, t in enumerate(st.session_state.t14_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t14_hero_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t14_h_t_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t14_hero_titulos) > 1 and _del_btn(f"t14_h_t_del_{i}"):
                        st.session_state.t14_hero_titulos.pop(i); st.rerun()
            if _add_btn("t14_h_t_add", "＋ Adicionar título"):
                st.session_state.t14_hero_titulos.append({"valor": "NOVO TÍTULO"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t14_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t14_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t14_h_d_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t14_hero_descs) > 1 and _del_btn(f"t14_h_d_del_{i}"):
                        st.session_state.t14_hero_descs.pop(i); st.rerun()
            if _add_btn("t14_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t14_hero_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Imagem de fundo  *(URL)*")
            for i, img in enumerate(st.session_state.t14_hero_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t14_hero_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t14_h_i_{i}", label_visibility="collapsed", placeholder="https://...")
                with c2:
                    if len(st.session_state.t14_hero_imgs) > 1 and _del_btn(f"t14_h_i_del_{i}"):
                        st.session_state.t14_hero_imgs.pop(i); st.rerun()
            if _add_btn("t14_h_i_add", "＋ Adicionar imagem de fundo"):
                st.session_state.t14_hero_imgs.append({"valor": "https://"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # BOTÕES RÁPIDOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">⚡ Ações Rápidas</div>', unsafe_allow_html=True)
            st.caption("Botões de destaque  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t14_quick_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t14_quick_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t14_qb_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t14_quick_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t14_qb_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t14_quick_btns) > 1 and _del_btn(f"t14_qb_del_{i}"):
                        st.session_state.t14_quick_btns.pop(i); st.rerun()
            if _add_btn("t14_qb_add", "＋ Adicionar botão rápido"):
                st.session_state.t14_quick_btns.append({"texto": "BOTÃO", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # VISITA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🕒 Planeje sua Visita</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t14_visit_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t14_visit_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t14_vt_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t14_visit_titulos) > 1 and _del_btn(f"t14_vt_del_{i}"):
                        st.session_state.t14_visit_titulos.pop(i); st.rerun()
            if _add_btn("t14_vt_add", "＋ Adicionar título"):
                st.session_state.t14_visit_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t14_visit_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t14_visit_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t14_vd_{i}", height=70, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t14_visit_descs) > 1 and _del_btn(f"t14_vd_del_{i}"):
                        st.session_state.t14_visit_descs.pop(i); st.rerun()
            if _add_btn("t14_vd_add", "＋ Adicionar descrição"):
                st.session_state.t14_visit_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Cards de informação  *(Título | Descrição | URL opcional)*")
            for i, info in enumerate(st.session_state.t14_visit_infos):
                with st.expander(f"Info {i+1}: {info['titulo']}"):
                    st.session_state.t14_visit_infos[i]["titulo"] = st.text_input(
                        "Título", info["titulo"], key=f"t14_vi_t_{i}")
                    st.session_state.t14_visit_infos[i]["desc"] = st.text_area(
                        "Descrição / Texto do botão", info["desc"], key=f"t14_vi_d_{i}", height=70)
                    if "url" in info:
                        st.session_state.t14_visit_infos[i]["url"] = st.text_input(
                            "URL do Botão  *(deixe em branco para não exibir)*", info["url"], key=f"t14_vi_u_{i}")
                    if len(st.session_state.t14_visit_infos) > 1:
                        if st.button("🗑 Remover esta info", key=f"t14_vi_del_{i}"):
                            st.session_state.t14_visit_infos.pop(i); st.rerun()
            if _add_btn("t14_vi_add", "＋ Adicionar card de info"):
                st.session_state.t14_visit_infos.append({"titulo": "NOVO", "desc": "..."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ANIMAIS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🐾 Nossos Residentes</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t14_animal_secao_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t14_animal_secao_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t14_ast_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t14_animal_secao_titulos) > 1 and _del_btn(f"t14_ast_del_{i}"):
                        st.session_state.t14_animal_secao_titulos.pop(i); st.rerun()
            if _add_btn("t14_ast_add", "＋ Adicionar título de seção"):
                st.session_state.t14_animal_secao_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Cards de animais  *(Nome | Categoria | Imagem | Botão | URL)*")
            for i, item in enumerate(st.session_state.t14_animal_items):
                with st.expander(f"Animal {i+1}: {item['nome']}"):
                    st.session_state.t14_animal_items[i]["nome"] = st.text_input(
                        "Nome do Animal", item["nome"], key=f"t14_ai_n_{i}")
                    st.session_state.t14_animal_items[i]["cat"] = st.text_input(
                        "Categoria", item["cat"], key=f"t14_ai_c_{i}")
                    st.session_state.t14_animal_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t14_ai_i_{i}")
                    st.session_state.t14_animal_items[i]["btn_txt"] = st.text_input(
                        "Texto do Botão", item["btn_txt"], key=f"t14_ai_bt_{i}")
                    st.session_state.t14_animal_items[i]["url"] = st.text_input(
                        "URL do Botão", item["url"], key=f"t14_ai_u_{i}")
                    if len(st.session_state.t14_animal_items) > 1:
                        if st.button("🗑 Remover este animal", key=f"t14_ai_del_{i}"):
                            st.session_state.t14_animal_items.pop(i); st.rerun()
            if _add_btn("t14_ai_add", "＋ Adicionar animal"):
                st.session_state.t14_animal_items.append({
                    "img": "", "nome": "NOVO ANIMAL", "cat": "CATEGORIA",
                    "btn_txt": "Saber mais", "url": "#"
                }); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # CONSERVAÇÃO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌍 Conservação & Impacto</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, t in enumerate(st.session_state.t14_cons_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t14_cons_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t14_ct_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t14_cons_titulos) > 1 and _del_btn(f"t14_ct_del_{i}"):
                        st.session_state.t14_cons_titulos.pop(i); st.rerun()
            if _add_btn("t14_ct_add", "＋ Adicionar título"):
                st.session_state.t14_cons_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t14_cons_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t14_cons_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t14_cd_{i}", height=90, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t14_cons_descs) > 1 and _del_btn(f"t14_cd_del_{i}"):
                        st.session_state.t14_cons_descs.pop(i); st.rerun()
            if _add_btn("t14_cd_add", "＋ Adicionar descrição"):
                st.session_state.t14_cons_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Botão  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t14_cons_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t14_cons_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t14_cb_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t14_cons_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t14_cb_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t14_cons_btns) > 1 and _del_btn(f"t14_cb_del_{i}"):
                        st.session_state.t14_cons_btns.pop(i); st.rerun()
            if _add_btn("t14_cb_add", "＋ Adicionar botão"):
                st.session_state.t14_cons_btns.append({"texto": "SAIBA MAIS", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # EVENTOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌙 Eventos & Educação</div>', unsafe_allow_html=True)

            st.caption("Título do evento")
            for i, t in enumerate(st.session_state.t14_event_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t14_event_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t14_et_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t14_event_titulos) > 1 and _del_btn(f"t14_et_del_{i}"):
                        st.session_state.t14_event_titulos.pop(i); st.rerun()
            if _add_btn("t14_et_add", "＋ Adicionar título"):
                st.session_state.t14_event_titulos.append({"valor": "NOVO EVENTO"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t14_event_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t14_event_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t14_ed_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t14_event_descs) > 1 and _del_btn(f"t14_ed_del_{i}"):
                        st.session_state.t14_event_descs.pop(i); st.rerun()
            if _add_btn("t14_ed_add", "＋ Adicionar descrição"):
                st.session_state.t14_event_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Imagem  *(URL)*")
            for i, img in enumerate(st.session_state.t14_event_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t14_event_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t14_ei_{i}", label_visibility="collapsed", placeholder="https://...")
                with c2:
                    if len(st.session_state.t14_event_imgs) > 1 and _del_btn(f"t14_ei_del_{i}"):
                        st.session_state.t14_event_imgs.pop(i); st.rerun()
            if _add_btn("t14_ei_add", "＋ Adicionar imagem"):
                st.session_state.t14_event_imgs.append({"valor": "https://"}); st.rerun()

            st.caption("Botão  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t14_event_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t14_event_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t14_eb_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t14_event_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t14_eb_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t14_event_btns) > 1 and _del_btn(f"t14_eb_del_{i}"):
                        st.session_state.t14_event_btns.pop(i); st.rerun()
            if _add_btn("t14_eb_add", "＋ Adicionar botão"):
                st.session_state.t14_event_btns.append({"texto": "VER MAIS", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Logo do rodapé")
            for i, logo in enumerate(st.session_state.t14_foot_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t14_foot_logos[i]["valor"] = st.text_input(
                        "Logo Footer", logo["valor"], key=f"t14_fl_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t14_foot_logos) > 1 and _del_btn(f"t14_fl_del_{i}"):
                        st.session_state.t14_foot_logos.pop(i); st.rerun()
            if _add_btn("t14_fl_add", "＋ Adicionar logo"):
                st.session_state.t14_foot_logos.append({"valor": "MARCA"}); st.rerun()

            st.caption("Descrição  *(texto abaixo do logo)*")
            for i, desc in enumerate(st.session_state.t14_foot_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t14_foot_descs[i]["valor"] = st.text_area(
                        "Descrição Footer", desc["valor"], key=f"t14_fd_{i}", height=70, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t14_foot_descs) > 1 and _del_btn(f"t14_fd_del_{i}"):
                        st.session_state.t14_foot_descs.pop(i); st.rerun()
            if _add_btn("t14_fd_add", "＋ Adicionar descrição"):
                st.session_state.t14_foot_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Colunas de links  *(Título | Links)*")
            for i, col in enumerate(st.session_state.t14_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t14_foot_cols[i]["titulo"] = st.text_input(
                        "Título da Coluna", col["titulo"], key=f"t14_fcol_ti_{i}")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1:
                            st.session_state.t14_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t14_fcol_lt_{i}_{j}", label_visibility="collapsed")
                        with c2:
                            st.session_state.t14_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t14_fcol_lu_{i}_{j}", label_visibility="collapsed")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t14_fcol_ld_{i}_{j}"):
                                st.session_state.t14_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t14_fcol_la_{i}", "＋ Adicionar link"):
                        st.session_state.t14_foot_cols[i]["links"].append({"texto": "Novo Link", "url": "#"}); st.rerun()
                    if len(st.session_state.t14_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t14_fcol_del_{i}"):
                            st.session_state.t14_foot_cols.pop(i); st.rerun()
            if _add_btn("t14_fcol_add", "＋ Adicionar coluna ao rodapé"):
                st.session_state.t14_foot_cols.append({"titulo": "NOVA COLUNA", "links": [{"texto": "Link", "url": "#"}]}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t14_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t14_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t14_fcp_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t14_foot_copys) > 1 and _del_btn(f"t14_fcp_del_{i}"):
                        st.session_state.t14_foot_copys.pop(i); st.rerun()
            if _add_btn("t14_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t14_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t14_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t14_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t14_obs_{i}", height=80,
                        placeholder="Ex: Mudar o laranja para um tom mais vibrante...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t14_obs) > 1 and _del_btn(f"t14_obs_del_{i}"):
                        st.session_state.t14_obs.pop(i); st.rerun()
            if _add_btn("t14_obs_add", "＋ Adicionar observação"):
                st.session_state.t14_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ENVIAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t14_send", type="primary"):
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
        page_icon="🦁",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
