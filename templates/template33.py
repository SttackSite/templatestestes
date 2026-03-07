import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img33.png"
TEMPLATE_NAME = "Template 33 — Saulo Simon Style (Creative Developer)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── CORES ───────────────────────────────────────────────────────────
        "t33_cores": [
            {"nome": "Fundo (ss-bg)",   "valor": "#ffae00"},
            {"nome": "Preto (ss-black)","valor": "#222222"},
            {"nome": "Branco (ss-white)","valor": "#ffffff"},
            {"nome": "Card (ss-card)",  "valor": "#ffc445"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t33_nav_logos": [{"texto": "ss"}],
        "t33_nav_links": [
            {"texto": "Projetos",    "url": "#projetos"},
            {"texto": "Experiências","url": "#sobre"},
            {"texto": "Sobre",       "url": "#sobre"},
        ],
        "t33_nav_ctas": [{"texto": "Dê o Play", "url": "#footer"}],

        # ── HERO ────────────────────────────────────────────────────────────
        "t33_hero_titulos":    [{"valor": "SAULO<br>SIMON"}],
        "t33_hero_subtitulos": [{"valor": "DESENVOLVEDOR CREATIVO & MESTRE DO WEBGL"}],
        "t33_hero_btns":       [{"texto": "DIRIGIR PELO SITE", "url": "#projetos"}],
        "t33_hero_simulacoes": [{"img_url": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=1200", "texto": "SIMULAÇÃO INTERATIVA 3D"}],

        # ── PROJETOS ────────────────────────────────────────────────────────
        "t33_proj_headers": [{"valor": "TRABALHOS EM DESTAQUE"}],
        "t33_proj_items": [
            {"tag": "THREE.JS JOURNEY",  "titulo": "O curso definitivo de Three.js",    "desc": "Aprenda a criar mundos 3D incríveis para a web partindo do zero absoluto.",                                        "img_bg": "#222", "btn_texto": "VER CURSO",    "btn_url": "https://www.google.com/"},
            {"tag": "WEBGL EXPERIENCE",  "titulo": "Oris: O Relógio Interativo",         "desc": "Uma experiência imersiva para explorar cada detalhe da mecânica de luxo em tempo real.",                          "img_bg": "#fff", "btn_texto": "VER PROJETO", "btn_url": "https://www.google.com/"},
        ],

        # ── SOBRE ───────────────────────────────────────────────────────────
        "t33_sobre_imgs":    [{"bg_color": "#222", "border_color": "white"}],
        "t33_sobre_titulos": [{"valor": "QUEM É O SAULO?"}],
        "t33_sobre_textos": [
            {"valor": "Sou um desenvolvedor freelancer francês apaixonado por criar experiências digitais que desafiam os limites do navegador. Especialista em WebGL, Three.js e animações de alta performance."},
            {"valor": "Trabalho com agências e marcas globais para transformar conceitos abstratos em mundos interativos onde o usuário é o protagonista."},
        ],
        "t33_sobre_btns": [{"texto": "MEU SETUP DE TRABALHO", "url": "https://www.google.com/"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t33_foot_titulos": [{"valor": "VAMOS JOGAR?"}],
        "t33_foot_links": [
            {"texto": "TWITTER",  "url": "https://www.google.com/"},
            {"texto": "GITHUB",   "url": "https://www.google.com/"},
            {"texto": "LINKEDIN", "url": "https://www.google.com/"},
            {"texto": "E-MAIL",   "url": "mailto:saulo@simon.dev"},
        ],
        "t33_foot_copys": [{"valor": "© 2026 SAULO SIMON — DESENVOLVIDO COM CÓDIGO E PAIXÃO."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t33_obs": [{"valor": ""}],
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
            for i, cor in enumerate(st.session_state.t33_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t33_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t33_cor_n_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t33_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t33_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t33_cores) > 1 and _del_btn(f"t33_cor_del_{i}"):
                        st.session_state.t33_cores.pop(i); st.rerun()
            if _add_btn("t33_cor_add", "＋ Adicionar cor"):
                st.session_state.t33_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo  *(iniciais em caixa bordada)*")
            for i, item in enumerate(st.session_state.t33_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_nav_logos[i]["texto"] = st.text_input(
                        "Iniciais", item["texto"], key=f"t33_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t33_nav_logos) > 1 and _del_btn(f"t33_logo_del_{i}"):
                        st.session_state.t33_nav_logos.pop(i); st.rerun()
            if _add_btn("t33_logo_add", "＋ Adicionar logo"):
                st.session_state.t33_nav_logos.append({"texto": "XX"}); st.rerun()

            st.caption("Links do menu  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t33_nav_links):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1:
                    st.session_state.t33_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t33_navl_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t33_nav_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t33_navl_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t33_nav_links) > 1 and _del_btn(f"t33_navl_del_{i}"):
                        st.session_state.t33_nav_links.pop(i); st.rerun()
            if _add_btn("t33_navl_add", "＋ Adicionar link"):
                st.session_state.t33_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            st.caption("Link destaque  *(estilo play, texto branco com sombra)*")
            for i, cta in enumerate(st.session_state.t33_nav_ctas):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1:
                    st.session_state.t33_nav_ctas[i]["texto"] = st.text_input(
                        "Texto", cta["texto"], key=f"t33_ncta_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t33_nav_ctas[i]["url"] = st.text_input(
                        "URL", cta["url"], key=f"t33_ncta_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t33_nav_ctas) > 1 and _del_btn(f"t33_ncta_del_{i}"):
                        st.session_state.t33_nav_ctas.pop(i); st.rerun()
            if _add_btn("t33_ncta_add", "＋ Adicionar CTA"):
                st.session_state.t33_nav_ctas.append({"texto": "PLAY", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎮 Hero Section</div>', unsafe_allow_html=True)

            st.caption("Título  *(fonte Bungee grande, suporta <br>)*")
            for i, t in enumerate(st.session_state.t33_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t33_h_t_{i}", height=70, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t33_hero_titulos) > 1 and _del_btn(f"t33_h_t_del_{i}"):
                        st.session_state.t33_hero_titulos.pop(i); st.rerun()
            if _add_btn("t33_h_t_add", "＋ Adicionar título"):
                st.session_state.t33_hero_titulos.append({"valor": "NOVO TÍTULO"}); st.rerun()

            st.caption("Subtítulo  *(fonte Bungee menor, texto preto)*")
            for i, stt in enumerate(st.session_state.t33_hero_subtitulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_hero_subtitulos[i]["valor"] = st.text_input(
                        "Subtítulo", stt["valor"], key=f"t33_h_st_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t33_hero_subtitulos) > 1 and _del_btn(f"t33_h_st_del_{i}"):
                        st.session_state.t33_hero_subtitulos.pop(i); st.rerun()
            if _add_btn("t33_h_st_add", "＋ Adicionar subtítulo"):
                st.session_state.t33_hero_subtitulos.append({"valor": "NOVO SUBTÍTULO"}); st.rerun()

            st.caption("Botão central  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t33_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t33_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t33_hb_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t33_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t33_hb_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t33_hero_btns) > 1 and _del_btn(f"t33_hb_del_{i}"):
                        st.session_state.t33_hero_btns.pop(i); st.rerun()
            if _add_btn("t33_hb_add", "＋ Adicionar botão"):
                st.session_state.t33_hero_btns.append({"texto": "COMEÇAR", "url": "#"}); st.rerun()

            st.caption("Simulação 3D  *(URL imagem de fundo | Texto overlay)*")
            for i, sim in enumerate(st.session_state.t33_hero_simulacoes):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_hero_simulacoes[i]["img_url"] = st.text_input(
                        "URL Imagem", sim["img_url"], key=f"t33_h_s_i_{i}", label_visibility="collapsed", placeholder="https://...")
                    st.session_state.t33_hero_simulacoes[i]["texto"] = st.text_input(
                        "Texto Overlay", sim["texto"], key=f"t33_h_s_t_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t33_hero_simulacoes) > 1 and _del_btn(f"t33_h_s_del_{i}"):
                        st.session_state.t33_hero_simulacoes.pop(i); st.rerun()
            if _add_btn("t33_h_s_add", "＋ Adicionar simulação"):
                st.session_state.t33_hero_simulacoes.append({"img_url": "https://", "texto": "SIMULAÇÃO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # PROJETOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🚀 Trabalhos em Destaque</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, ph in enumerate(st.session_state.t33_proj_headers):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_proj_headers[i]["valor"] = st.text_input(
                        "Título", ph["valor"], key=f"t33_p_h_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t33_proj_headers) > 1 and _del_btn(f"t33_p_h_del_{i}"):
                        st.session_state.t33_proj_headers.pop(i); st.rerun()
            if _add_btn("t33_p_h_add", "＋ Adicionar título"):
                st.session_state.t33_proj_headers.append({"valor": "PROJETOS"}); st.rerun()

            st.caption("Cards de projeto  *(Tag | Título | Desc | Cor fundo | Botão)*")
            for i, item in enumerate(st.session_state.t33_proj_items):
                with st.expander(f"Projeto {i+1}: {item['titulo']}"):
                    st.session_state.t33_proj_items[i]["tag"] = st.text_input(
                        "Tag", item["tag"], key=f"t33_pi_tag_{i}")
                    st.session_state.t33_proj_items[i]["titulo"] = st.text_input(
                        "Título", item["titulo"], key=f"t33_pi_t_{i}")
                    st.session_state.t33_proj_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t33_pi_d_{i}", height=80)
                    st.session_state.t33_proj_items[i]["img_bg"] = st.text_input(
                        "Cor Fundo Placeholder (Hex)", item["img_bg"], key=f"t33_pi_bg_{i}")
                    st.session_state.t33_proj_items[i]["btn_texto"] = st.text_input(
                        "Texto Botão", item["btn_texto"], key=f"t33_pi_bt_{i}")
                    st.session_state.t33_proj_items[i]["btn_url"] = st.text_input(
                        "URL Botão", item["btn_url"], key=f"t33_pi_bu_{i}")
                    if len(st.session_state.t33_proj_items) > 1:
                        if st.button("🗑 Remover este projeto", key=f"t33_pi_del_{i}"):
                            st.session_state.t33_proj_items.pop(i); st.rerun()
            if _add_btn("t33_pi_add", "＋ Adicionar projeto"):
                st.session_state.t33_proj_items.append({
                    "tag": "NOVA TAG", "titulo": "NOVO PROJETO", "desc": "DESC",
                    "img_bg": "#222", "btn_texto": "VER MAIS", "btn_url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # SOBRE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👤 Sobre o Profissional</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, stit in enumerate(st.session_state.t33_sobre_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_sobre_titulos[i]["valor"] = st.text_input(
                        "Título", stit["valor"], key=f"t33_s_t_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t33_sobre_titulos) > 1 and _del_btn(f"t33_s_t_del_{i}"):
                        st.session_state.t33_sobre_titulos.pop(i); st.rerun()
            if _add_btn("t33_s_t_add", "＋ Adicionar título"):
                st.session_state.t33_sobre_titulos.append({"valor": "QUEM SOU?"}); st.rerun()

            st.caption("Parágrafos de bio")
            for i, stxt in enumerate(st.session_state.t33_sobre_textos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_sobre_textos[i]["valor"] = st.text_area(
                        "Texto", stxt["valor"], key=f"t33_s_tx_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t33_sobre_textos) > 1 and _del_btn(f"t33_s_tx_del_{i}"):
                        st.session_state.t33_sobre_textos.pop(i); st.rerun()
            if _add_btn("t33_s_tx_add", "＋ Adicionar parágrafo"):
                st.session_state.t33_sobre_textos.append({"valor": "Novo parágrafo..."}); st.rerun()

            st.caption("Botão  *(Texto | URL)*")
            for i, sbtn in enumerate(st.session_state.t33_sobre_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t33_sobre_btns[i]["texto"] = st.text_input(
                        "Texto", sbtn["texto"], key=f"t33_sb_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t33_sobre_btns[i]["url"] = st.text_input(
                        "URL", sbtn["url"], key=f"t33_sb_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t33_sobre_btns) > 1 and _del_btn(f"t33_sb_del_{i}"):
                        st.session_state.t33_sobre_btns.pop(i); st.rerun()
            if _add_btn("t33_sb_add", "＋ Adicionar botão"):
                st.session_state.t33_sobre_btns.append({"texto": "VER MAIS", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏁 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Título grande do rodapé")
            for i, ft in enumerate(st.session_state.t33_foot_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_foot_titulos[i]["valor"] = st.text_input(
                        "Título", ft["valor"], key=f"t33_f_t_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t33_foot_titulos) > 1 and _del_btn(f"t33_f_t_del_{i}"):
                        st.session_state.t33_foot_titulos.pop(i); st.rerun()
            if _add_btn("t33_f_t_add", "＋ Adicionar título"):
                st.session_state.t33_foot_titulos.append({"valor": "VAMOS?"}); st.rerun()

            st.caption("Links sociais  *(Rede | URL / mailto)*")
            for i, flink in enumerate(st.session_state.t33_foot_links):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1:
                    st.session_state.t33_foot_links[i]["texto"] = st.text_input(
                        "Rede", flink["texto"], key=f"t33_fl_t_{i}", label_visibility="collapsed", placeholder="Rede")
                with c2:
                    st.session_state.t33_foot_links[i]["url"] = st.text_input(
                        "URL/Email", flink["url"], key=f"t33_fl_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t33_foot_links) > 1 and _del_btn(f"t33_fl_del_{i}"):
                        st.session_state.t33_foot_links.pop(i); st.rerun()
            if _add_btn("t33_fl_add", "＋ Adicionar rede social"):
                st.session_state.t33_foot_links.append({"texto": "REDE", "url": "#"}); st.rerun()

            st.caption("Copyright")
            for i, fcp in enumerate(st.session_state.t33_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", fcp["valor"], key=f"t33_fcp_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t33_foot_copys) > 1 and _del_btn(f"t33_fcp_del_{i}"):
                        st.session_state.t33_foot_copys.pop(i); st.rerun()
            if _add_btn("t33_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t33_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t33_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t33_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t33_obs_{i}", height=80,
                        placeholder="Ex: Manter estética gamer e amarelo vibrante...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t33_obs) > 1 and _del_btn(f"t33_obs_del_{i}"):
                        st.session_state.t33_obs.pop(i); st.rerun()
            if _add_btn("t33_obs_add", "＋ Adicionar observação"):
                st.session_state.t33_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ENVIAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t33_send", type="primary"):
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
        page_icon="🎮",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
