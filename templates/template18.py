import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img18.png"
TEMPLATE_NAME = "Template 18 — Daniel Aristizábal Style (Digital Studio)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── CORES ───────────────────────────────────────────────────────────
        "t18_cores": [
            {"nome": "Fundo (Preto)",                  "valor": "#000000"},
            {"nome": "Texto (Branco)",                  "valor": "#ffffff"},
            {"nome": "Bordas/Linhas (Cinza)",           "valor": "#222222"},
            {"nome": "Texto Secundário (Cinza Médio)",  "valor": "#666666"},
        ],

        # ── HEADER ──────────────────────────────────────────────────────────
        "t18_header_nomes": [{"valor": "Daniel Aristizábal"}],
        "t18_header_links": [
            {"texto": "Index",   "url": "#index"},
            {"texto": "Studio",  "url": "#studio"},
            {"texto": "Archive", "url": "#archive"},
            {"texto": "Shop",    "url": "#shop"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t18_hero_titulos": [{"valor": "DANIEL<br>ARISTI<br>ZÁBAL"}],
        "t18_hero_descs":   [{"valor": "Digital Art Director and Motion Designer. Merging surrealism with CGI to explore new visual languages. Based in Medellín, working globally."}],

        # ── PROJETOS ────────────────────────────────────────────────────────
        "t18_project_items": [
            {"img": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1200", "nome": "Digital Surrealism",    "year": "2024", "col_size": 2},
            {"img": "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?w=600",    "nome": "Chrome Study",          "year": "2023", "col_size": 1},
            {"img": "https://images.unsplash.com/photo-1633167606207-d840b5070fc2?w=600",  "nome": "Organic Forms",         "year": "2024", "col_size": 1},
            {"img": "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?w=600",  "nome": "Color Theory",          "year": "2023", "col_size": 1},
            {"img": "https://images.unsplash.com/photo-1558591710-4b4a1ae0f04d?w=600",    "nome": "Texture Flow",          "year": "2022", "col_size": 1},
            {"img": "https://images.unsplash.com/photo-1574169208507-84376144848b?w=600",  "nome": "CGI Sculpture",         "year": "2024", "col_size": 1},
            {"img": "https://images.unsplash.com/photo-1620641788421-7a1c342ea42e?w=1200", "nome": "Metaverse Landscapes",  "year": "2024", "col_size": 2},
        ],

        # ── STUDIO ──────────────────────────────────────────────────────────
        "t18_studio_titulos": [{"valor": "THE STUDIO"}],
        "t18_studio_descs":   [{"valor": "Nós operamos na intersecção entre o design clássico e o futurismo digital. Especializados em CGI, direção de arte e identidades visuais que desafiam a lógica."}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t18_foot_col_titles": [
            {"valor": "CONNECT"},
            {"valor": "NEW BUSINESS"},
        ],
        "t18_foot_socials": [
            {"texto": "Instagram", "url": "https://www.google.com/"},
            {"texto": "Behance",   "url": "https://www.google.com/"},
            {"texto": "LinkedIn",  "url": "https://www.google.com/"},
            {"texto": "Vimeo",     "url": "https://www.google.com/"},
        ],
        "t18_foot_emails": [{"texto": "studio@aristizabal.net", "url": "mailto:studio@aristizabal.net"}],
        "t18_foot_copys":  [{"valor": "© 2026 DANIEL ARISTIZÁBAL STUDIO — ALL RIGHTS RESERVED"}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t18_obs": [{"valor": ""}],
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
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&family=JetBrains+Mono:wght@300;400;700&display=swap');
        html, body, [data-testid="stAppViewContainer"] { font-family: 'JetBrains Mono', monospace; background: #f4f6fb; }
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
            for i, cor in enumerate(st.session_state.t18_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t18_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t18_cor_n_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t18_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t18_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t18_cores) > 1 and _del_btn(f"t18_cor_del_{i}"):
                        st.session_state.t18_cores.pop(i); st.rerun()
            if _add_btn("t18_cor_add", "＋ Adicionar cor"):
                st.session_state.t18_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HEADER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Cabeçalho (Header)</div>', unsafe_allow_html=True)

            st.caption("Nome do estúdio / artista  *(lado esquerdo)*")
            for i, item in enumerate(st.session_state.t18_header_nomes):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t18_header_nomes[i]["valor"] = st.text_input(
                        "Nome", item["valor"], key=f"t18_hn_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t18_header_nomes) > 1 and _del_btn(f"t18_hn_del_{i}"):
                        st.session_state.t18_header_nomes.pop(i); st.rerun()
            if _add_btn("t18_hn_add", "＋ Adicionar nome"):
                st.session_state.t18_header_nomes.append({"valor": "Estúdio"}); st.rerun()

            st.caption("Menu de navegação  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t18_header_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t18_header_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t18_hl_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t18_header_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t18_hl_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t18_header_links) > 1 and _del_btn(f"t18_hl_del_{i}"):
                        st.session_state.t18_header_links.pop(i); st.rerun()
            if _add_btn("t18_hl_add", "＋ Adicionar link ao menu"):
                st.session_state.t18_header_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💥 Hero Section</div>', unsafe_allow_html=True)

            st.caption("Título principal  *(use <br> para quebrar linha)*")
            for i, t in enumerate(st.session_state.t18_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t18_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t18_h_t_{i}", height=90, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t18_hero_titulos) > 1 and _del_btn(f"t18_h_t_del_{i}"):
                        st.session_state.t18_hero_titulos.pop(i); st.rerun()
            if _add_btn("t18_h_t_add", "＋ Adicionar título"):
                st.session_state.t18_hero_titulos.append({"valor": "NOVO TÍTULO"}); st.rerun()

            st.caption("Descrição  *(texto abaixo do título)*")
            for i, d in enumerate(st.session_state.t18_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t18_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t18_h_d_{i}", height=100, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t18_hero_descs) > 1 and _del_btn(f"t18_h_d_del_{i}"):
                        st.session_state.t18_hero_descs.pop(i); st.rerun()
            if _add_btn("t18_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t18_hero_descs.append({"valor": "Nova descrição do estúdio."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # PROJETOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Portfólio de Projetos</div>', unsafe_allow_html=True)
            st.caption("Cards de projeto  *(Nome | Ano | Imagem | Largura da coluna)*")
            for i, item in enumerate(st.session_state.t18_project_items):
                with st.expander(f"Projeto {i+1}: {item['nome']}"):
                    st.session_state.t18_project_items[i]["nome"] = st.text_input(
                        "Nome do Projeto", item["nome"], key=f"t18_pi_n_{i}")
                    st.session_state.t18_project_items[i]["year"] = st.text_input(
                        "Ano", item["year"], key=f"t18_pi_y_{i}")
                    st.session_state.t18_project_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t18_pi_i_{i}")
                    st.session_state.t18_project_items[i]["col_size"] = st.selectbox(
                        "Largura da Coluna  *(1 = normal | 2 = larga)*",
                        [1, 2], index=item["col_size"] - 1, key=f"t18_pi_s_{i}")
                    if len(st.session_state.t18_project_items) > 1:
                        if st.button("🗑 Remover este projeto", key=f"t18_pi_del_{i}"):
                            st.session_state.t18_project_items.pop(i); st.rerun()
            if _add_btn("t18_pi_add", "＋ Adicionar projeto"):
                st.session_state.t18_project_items.append({"img": "", "nome": "NOVO", "year": "2026", "col_size": 1}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # STUDIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏢 The Studio</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t18_studio_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t18_studio_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t18_st_t_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t18_studio_titulos) > 1 and _del_btn(f"t18_st_t_del_{i}"):
                        st.session_state.t18_studio_titulos.pop(i); st.rerun()
            if _add_btn("t18_st_t_add", "＋ Adicionar título"):
                st.session_state.t18_studio_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição do estúdio")
            for i, d in enumerate(st.session_state.t18_studio_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t18_studio_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t18_st_d_{i}", height=100, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t18_studio_descs) > 1 and _del_btn(f"t18_st_d_del_{i}"):
                        st.session_state.t18_studio_descs.pop(i); st.rerun()
            if _add_btn("t18_st_d_add", "＋ Adicionar descrição"):
                st.session_state.t18_studio_descs.append({"valor": "Nova descrição do estúdio."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé Minimalista</div>', unsafe_allow_html=True)

            st.caption("Títulos das colunas  *(Coluna 1: redes | Coluna 2: contato)*")
            for i, title in enumerate(st.session_state.t18_foot_col_titles):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t18_foot_col_titles[i]["valor"] = st.text_input(
                        f"Título Coluna {i+1}", title["valor"], key=f"t18_fct_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t18_foot_col_titles) > 1 and _del_btn(f"t18_fct_del_{i}"):
                        st.session_state.t18_foot_col_titles.pop(i); st.rerun()
            if _add_btn("t18_fct_add", "＋ Adicionar título de coluna"):
                st.session_state.t18_foot_col_titles.append({"valor": "NOVA COLUNA"}); st.rerun()

            st.caption("Redes sociais  *(Coluna 1 — Nome | URL)*")
            for i, social in enumerate(st.session_state.t18_foot_socials):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t18_foot_socials[i]["texto"] = st.text_input(
                        "Nome", social["texto"], key=f"t18_fs_t_{i}", label_visibility="collapsed", placeholder="Rede Social")
                with c2:
                    st.session_state.t18_foot_socials[i]["url"] = st.text_input(
                        "URL", social["url"], key=f"t18_fs_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t18_foot_socials) > 1 and _del_btn(f"t18_fs_del_{i}"):
                        st.session_state.t18_foot_socials.pop(i); st.rerun()
            if _add_btn("t18_fs_add", "＋ Adicionar rede social"):
                st.session_state.t18_foot_socials.append({"texto": "Social", "url": "#"}); st.rerun()

            st.caption("Contato / Email  *(Coluna 2 — Texto | mailto:)*")
            for i, email in enumerate(st.session_state.t18_foot_emails):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t18_foot_emails[i]["texto"] = st.text_input(
                        "Email", email["texto"], key=f"t18_fe_t_{i}", label_visibility="collapsed", placeholder="email@exemplo.com")
                with c2:
                    st.session_state.t18_foot_emails[i]["url"] = st.text_input(
                        "Link mailto", email["url"], key=f"t18_fe_u_{i}", label_visibility="collapsed", placeholder="mailto:email@exemplo.com")
                with c3:
                    if len(st.session_state.t18_foot_emails) > 1 and _del_btn(f"t18_fe_del_{i}"):
                        st.session_state.t18_foot_emails.pop(i); st.rerun()
            if _add_btn("t18_fe_add", "＋ Adicionar contato"):
                st.session_state.t18_foot_emails.append({"texto": "email@site.com", "url": "mailto:email@site.com"}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t18_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t18_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t18_fcp_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t18_foot_copys) > 1 and _del_btn(f"t18_fcp_del_{i}"):
                        st.session_state.t18_foot_copys.pop(i); st.rerun()
            if _add_btn("t18_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t18_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t18_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t18_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t18_obs_{i}", height=80,
                        placeholder="Ex: Usar mais efeitos de distorção CGI...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t18_obs) > 1 and _del_btn(f"t18_obs_del_{i}"):
                        st.session_state.t18_obs.pop(i); st.rerun()
            if _add_btn("t18_obs_add", "＋ Adicionar observação"):
                st.session_state.t18_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ENVIAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t18_send", type="primary"):
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
        page_icon="🎨",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
