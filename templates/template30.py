import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img30.png"
TEMPLATE_NAME = "Template 30 — FORZY Pro Style (Performance & Design)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── CORES ───────────────────────────────────────────────────────────
        "t30_cores": [
            {"nome": "Preto (fz-black)",         "valor": "#000000"},
            {"nome": "Branco (fz-white)",         "valor": "#ffffff"},
            {"nome": "Cinza 100 (fz-gray-100)",   "valor": "#f5f5f7"},
            {"nome": "Cinza 200 (fz-gray-200)",   "valor": "#e8e8ed"},
            {"nome": "Texto Secundário",           "valor": "#86868b"},
            {"nome": "Destaque (fz-accent)",       "valor": "#0066cc"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t30_nav_logos": [{"texto": "FORZY"}],
        "t30_nav_links": [
            {"texto": "SOLUÇÕES",   "url": "#servicos", "active": False},
            {"texto": "ECOSSISTEMA","url": "#servicos", "active": False},
            {"texto": "RESULTADOS", "url": "#impacto",  "active": False},
            {"texto": "CONTATO",    "url": "#footer",   "active": True},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t30_hero_labels":  [{"valor": "Performance & Design Agnostic"}],
        "t30_hero_titulos": [{"valor": "Design que vende.<br>Tecnologia que escala."}],
        "t30_hero_descs":   [{"valor": "A Forzy é uma consultoria estratégica focada em criar produtos digitais que dominam mercados. Não fazemos apenas sites; construímos ativos de alta performance."}],
        "t30_hero_btns":    [{"texto": "VAMOS CONSTRUIR ALGO NOVO?", "url": "#servicos"}],

        # ── SHOWCASE IMAGE ───────────────────────────────────────────────────
        "t30_showcase_imgs": [{"url": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=1600"}],

        # ── SERVIÇOS ────────────────────────────────────────────────────────
        "t30_serv_labels": [{"valor": "O que fazemos"}],
        "t30_serv_items": [
            {"num": "01", "title": "Identidade Visual & Branding",    "desc": "Construímos marcas que são impossíveis de ignorar, unindo psicologia e estética.",                                         "url": "https://www.google.com/"},
            {"num": "02", "title": "Desenvolvimento Web & Mobile",    "desc": "Sistemas robustos com as tecnologias mais rápidas do mundo para garantir 99.9% de uptime.",                               "url": "https://www.google.com/"},
            {"num": "03", "title": "Growth Marketing",                "desc": "Estratégias de aquisição baseadas em dados para escalar o seu faturamento de forma previsível.",                          "url": "https://www.google.com/"},
        ],

        # ── IMPACTO ─────────────────────────────────────────────────────────
        "t30_impact_texts": [{"valor": "\"A simplicidade é o último grau de sofisticação. Na Forzy, eliminamos o ruído para que sua mensagem brilhe.\""}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t30_foot_titles": [{"valor": "Pronto para elevar o padrão do seu negócio?"}],
        "t30_foot_brands": [{"nome": "FORZY", "desc": "Transformando ideias em interfaces de alto impacto desde 2018."}],
        "t30_foot_cols": [
            {
                "titulo": "CONTATO",
                "links": [
                    {"texto": "hello@forzy.com.br", "url": "mailto:hello@forzy.com.br"},
                    {"texto": "+55 11 99999-9999",  "url": "https://www.google.com/"},
                ]
            },
            {
                "titulo": "FOLLOW",
                "links": [
                    {"texto": "Instagram", "url": "https://www.google.com/"},
                    {"texto": "LinkedIn",  "url": "https://www.google.com/"},
                    {"texto": "Behance",   "url": "https://www.google.com/"},
                ]
            }
        ],
        "t30_foot_copys": [{"valor": "© 2026 FORZY INTERFACE DESIGN. ALL RIGHTS RESERVED."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t30_obs": [{"valor": ""}],
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
            for i, cor in enumerate(st.session_state.t30_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t30_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t30_cor_n_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t30_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t30_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t30_cores) > 1 and _del_btn(f"t30_cor_del_{i}"):
                        st.session_state.t30_cores.pop(i); st.rerun()
            if _add_btn("t30_cor_add", "＋ Adicionar cor"):
                st.session_state.t30_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Nome da marca  *(aparece no canto esquerdo)*")
            for i, item in enumerate(st.session_state.t30_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_nav_logos[i]["texto"] = st.text_input(
                        "Nome", item["texto"], key=f"t30_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t30_nav_logos) > 1 and _del_btn(f"t30_logo_del_{i}"):
                        st.session_state.t30_nav_logos.pop(i); st.rerun()
            if _add_btn("t30_logo_add", "＋ Adicionar logo"):
                st.session_state.t30_nav_logos.append({"texto": "MARCA"}); st.rerun()

            st.caption("Links do menu  *(Texto | URL | Ativo?)*")
            for i, link in enumerate(st.session_state.t30_nav_links):
                c1, c2, c3, c4 = st.columns([3, 3, 2, 1])
                with c1:
                    st.session_state.t30_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t30_navl_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t30_nav_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t30_navl_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    st.session_state.t30_nav_links[i]["active"] = st.checkbox(
                        "Ativo", link.get("active", False), key=f"t30_navl_a_{i}")
                with c4:
                    if len(st.session_state.t30_nav_links) > 1 and _del_btn(f"t30_navl_del_{i}"):
                        st.session_state.t30_nav_links.pop(i); st.rerun()
            if _add_btn("t30_navl_add", "＋ Adicionar link"):
                st.session_state.t30_nav_links.append({"texto": "LINK", "url": "#", "active": False}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🚀 Hero Section</div>', unsafe_allow_html=True)

            st.caption("Label  *(texto pequeno em cinza acima do título)*")
            for i, l in enumerate(st.session_state.t30_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_hero_labels[i]["valor"] = st.text_input(
                        "Label", l["valor"], key=f"t30_h_l_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t30_hero_labels) > 1 and _del_btn(f"t30_h_l_del_{i}"):
                        st.session_state.t30_hero_labels.pop(i); st.rerun()
            if _add_btn("t30_h_l_add", "＋ Adicionar label"):
                st.session_state.t30_hero_labels.append({"valor": "Novo label"}); st.rerun()

            st.caption("Título principal  *(suporta <br> para quebra de linha)*")
            for i, t in enumerate(st.session_state.t30_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t30_h_t_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t30_hero_titulos) > 1 and _del_btn(f"t30_h_t_del_{i}"):
                        st.session_state.t30_hero_titulos.pop(i); st.rerun()
            if _add_btn("t30_h_t_add", "＋ Adicionar título"):
                st.session_state.t30_hero_titulos.append({"valor": "Novo título."}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t30_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t30_h_d_{i}", height=90, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t30_hero_descs) > 1 and _del_btn(f"t30_h_d_del_{i}"):
                        st.session_state.t30_hero_descs.pop(i); st.rerun()
            if _add_btn("t30_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t30_hero_descs.append({"valor": "Nova descrição."}); st.rerun()

            st.caption("Botões  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t30_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t30_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t30_hb_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t30_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t30_hb_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t30_hero_btns) > 1 and _del_btn(f"t30_hb_del_{i}"):
                        st.session_state.t30_hero_btns.pop(i); st.rerun()
            if _add_btn("t30_hb_add", "＋ Adicionar botão"):
                st.session_state.t30_hero_btns.append({"texto": "COMEÇAR", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # SHOWCASE IMAGE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Imagem Showcase</div>', unsafe_allow_html=True)
            st.caption("URL da imagem larga em tons de cinza")
            for i, img in enumerate(st.session_state.t30_showcase_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_showcase_imgs[i]["url"] = st.text_input(
                        "URL", img["url"], key=f"t30_show_u_{i}", label_visibility="collapsed", placeholder="https://...")
                with c2:
                    if len(st.session_state.t30_showcase_imgs) > 1 and _del_btn(f"t30_show_del_{i}"):
                        st.session_state.t30_showcase_imgs.pop(i); st.rerun()
            if _add_btn("t30_show_add", "＋ Adicionar imagem"):
                st.session_state.t30_showcase_imgs.append({"url": "https://"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # SERVIÇOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🛠️ Serviços</div>', unsafe_allow_html=True)

            st.caption("Label da seção  *(texto pequeno cinza acima dos cards)*")
            for i, l in enumerate(st.session_state.t30_serv_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_serv_labels[i]["valor"] = st.text_input(
                        "Label", l["valor"], key=f"t30_sl_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t30_serv_labels) > 1 and _del_btn(f"t30_sl_del_{i}"):
                        st.session_state.t30_serv_labels.pop(i); st.rerun()
            if _add_btn("t30_sl_add", "＋ Adicionar label"):
                st.session_state.t30_serv_labels.append({"valor": "O que fazemos"}); st.rerun()

            st.caption("Cards de serviço  *(Nº | Título | Descrição | URL)*")
            for i, item in enumerate(st.session_state.t30_serv_items):
                with st.expander(f"Serviço {i+1}: {item['title']}"):
                    st.session_state.t30_serv_items[i]["num"] = st.text_input(
                        "Número", item["num"], key=f"t30_serv_n_{i}")
                    st.session_state.t30_serv_items[i]["title"] = st.text_input(
                        "Título", item["title"], key=f"t30_serv_t_{i}")
                    st.session_state.t30_serv_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t30_serv_d_{i}", height=80)
                    st.session_state.t30_serv_items[i]["url"] = st.text_input(
                        "URL Destino", item["url"], key=f"t30_serv_u_{i}")
                    if len(st.session_state.t30_serv_items) > 1:
                        if st.button("🗑 Remover este serviço", key=f"t30_serv_del_{i}"):
                            st.session_state.t30_serv_items.pop(i); st.rerun()
            if _add_btn("t30_serv_add_item", "＋ Adicionar serviço"):
                st.session_state.t30_serv_items.append({"num": "04", "title": "NOVO", "desc": "DESC", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # IMPACTO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">✨ Texto de Impacto</div>', unsafe_allow_html=True)
            st.caption("Citação ou frase de impacto em destaque")
            for i, t in enumerate(st.session_state.t30_impact_texts):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_impact_texts[i]["valor"] = st.text_area(
                        "Citação", t["valor"], key=f"t30_it_{i}", height=90, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t30_impact_texts) > 1 and _del_btn(f"t30_it_del_{i}"):
                        st.session_state.t30_impact_texts.pop(i); st.rerun()
            if _add_btn("t30_it_add", "＋ Adicionar citação"):
                st.session_state.t30_impact_texts.append({"valor": "\"Nova citação.\""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Título grande do rodapé")
            for i, t in enumerate(st.session_state.t30_foot_titles):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_foot_titles[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t30_ft_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t30_foot_titles) > 1 and _del_btn(f"t30_ft_del_{i}"):
                        st.session_state.t30_foot_titles.pop(i); st.rerun()
            if _add_btn("t30_ft_add", "＋ Adicionar título"):
                st.session_state.t30_foot_titles.append({"valor": "Pronto?"}); st.rerun()

            st.caption("Marca & Descrição")
            for i, b in enumerate(st.session_state.t30_foot_brands):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_foot_brands[i]["nome"] = st.text_input(
                        "Nome Marca", b["nome"], key=f"t30_fb_n_{i}", label_visibility="collapsed")
                    st.session_state.t30_foot_brands[i]["desc"] = st.text_area(
                        "Descrição", b["desc"], key=f"t30_fb_d_{i}", height=70, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t30_foot_brands) > 1 and _del_btn(f"t30_fb_del_{i}"):
                        st.session_state.t30_foot_brands.pop(i); st.rerun()
            if _add_btn("t30_fb_add", "＋ Adicionar marca"):
                st.session_state.t30_foot_brands.append({"nome": "MARCA", "desc": "Descrição."}); st.rerun()

            st.caption("Colunas de links  *(Título | Links)*")
            for i, col in enumerate(st.session_state.t30_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t30_foot_cols[i]["titulo"] = st.text_input(
                        "Título Coluna", col["titulo"], key=f"t30_fc_t_{i}")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1:
                            st.session_state.t30_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t30_fcl_t_{i}_{j}", label_visibility="collapsed")
                        with c2:
                            st.session_state.t30_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t30_fcl_u_{i}_{j}", label_visibility="collapsed")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t30_fcl_del_{i}_{j}"):
                                st.session_state.t30_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t30_fcl_add_{i}", "＋ Adicionar link"):
                        st.session_state.t30_foot_cols[i]["links"].append({"texto": "LINK", "url": "#"}); st.rerun()
                    if len(st.session_state.t30_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t30_fc_del_{i}"):
                            st.session_state.t30_foot_cols.pop(i); st.rerun()
            if _add_btn("t30_fc_add", "＋ Adicionar coluna"):
                st.session_state.t30_foot_cols.append({"titulo": "NOVA", "links": [{"texto": "LINK", "url": "#"}]}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t30_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t30_fcp_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t30_foot_copys) > 1 and _del_btn(f"t30_fcp_del_{i}"):
                        st.session_state.t30_foot_copys.pop(i); st.rerun()
            if _add_btn("t30_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t30_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t30_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t30_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t30_obs_{i}", height=80,
                        placeholder="Ex: Manter estética minimalista...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t30_obs) > 1 and _del_btn(f"t30_obs_del_{i}"):
                        st.session_state.t30_obs.pop(i); st.rerun()
            if _add_btn("t30_obs_add", "＋ Adicionar observação"):
                st.session_state.t30_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ENVIAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t30_send", type="primary"):
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
        page_icon="🔥",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
