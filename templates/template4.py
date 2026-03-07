import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img4.png"
TEMPLATE_NAME = "Template 4 — Inovação Absoluta (Champion)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── CORES ───────────────────────────────────────────────────────────
        "t4_cores": [
            {"nome": "Cor Neon Principal (Glow)", "valor": "#00FF88"},
            {"nome": "Cor Secundária (Cyan)",     "valor": "#00D9FF"},
            {"nome": "Cor de Destaque (Magenta)", "valor": "#FF00FF"},
            {"nome": "Cor de Fundo (Deep Black)", "valor": "#000000"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t4_logos": [{"valor": "CHAMPION"}],
        "t4_nav_links": [
            {"texto": "Recursos",  "url": "#recursos"},
            {"texto": "Portfólio", "url": "#portfolio"},
            {"texto": "Sobre",     "url": "#sobre"},
            {"texto": "Contato",   "url": "#contato"},
        ],
        "t4_nav_ctas": [{"texto": "Começar", "url": "https://www.google.com/"}],

        # ── HERO ────────────────────────────────────────────────────────────
        "t4_hero_titulos":    [{"valor": "INOVAÇÃO ABSOLUTA"}],
        "t4_hero_subtitulos": [{"valor": "Design que transcende limites"}],
        "t4_hero_btns": [
            {"texto": "Explorar Agora", "url": "https://www.google.com/", "estilo": "primário"},
            {"texto": "Saiba Mais",     "url": "https://www.google.com/", "estilo": "secundário"},
        ],

        # ── RECURSOS (FEATURES) ─────────────────────────────────────────────
        "t4_feat_cards": [
            {"icone": "⚡", "titulo": "Velocidade",  "descricao": "Performance extrema com carregamento instantâneo em qualquer dispositivo."},
            {"icone": "🎨", "titulo": "Design",      "descricao": "Interface visual revolucionária com animações que impressionam."},
            {"icone": "🔧", "titulo": "Flexível",    "descricao": "Totalmente customizável para qualquer tipo de negócio ou projeto."},
            {"icone": "📱", "titulo": "Responsivo",  "descricao": "Funciona perfeitamente em todos os dispositivos e tamanhos de tela."},
            {"icone": "🚀", "titulo": "Conversão",   "descricao": "Design estratégico focado em maximizar taxas de conversão."},
            {"icone": "✨", "titulo": "Premium",     "descricao": "Experiência de luxo em cada interação e detalhe visual."},
        ],

        # ── SHOWCASE (NÚMEROS) ───────────────────────────────────────────────
        "t4_show_titulos": [{"valor": "NÚMEROS QUE FALAM"}],
        "t4_show_cards": [
            {"numero": "500%",  "label": "Mais Engajamento"},
            {"numero": "100K+", "label": "Usuários Ativos"},
            {"numero": "99.9%", "label": "Uptime"},
            {"numero": "24/7",  "label": "Suporte Premium"},
        ],

        # ── CTA FINAL ───────────────────────────────────────────────────────
        "t4_ctaf_titulos": [{"valor": "Pronto para Revolucionar?"}],
        "t4_ctaf_descs":   [{"valor": "Junte-se aos líderes que já transformaram seus negócios com design de campeão."}],
        "t4_ctaf_btns":    [{"texto": "Começar Sua Revolução", "url": "https://www.google.com/"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t4_footer_infos":  [{"valor": "Email: hello@champion.com | Telefone: +55 (99) 99999-9999"}],
        "t4_footer_addrs":  [{"valor": "Endereço: Av. Inovação, 1000 - São Paulo, SP"}],
        "t4_footer_copys":  [{"valor": "© 2025 Champion Design. Todos os direitos reservados. Design que vence campeonatos."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t4_obs": [{"valor": ""}],
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
            st.markdown('<div class="section-label">🎨 Cores Neon & Fundo</div>', unsafe_allow_html=True)
            for i, cor in enumerate(st.session_state.t4_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t4_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t4_cor_nome_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t4_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t4_cor_val_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t4_cores) > 1 and _del_btn(f"t4_cor_del_{i}"):
                        st.session_state.t4_cores.pop(i); st.rerun()
            if _add_btn("t4_cor_add", "＋ Adicionar cor"):
                st.session_state.t4_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo  *(fonte Space Mono com glow neon)*")
            for i, item in enumerate(st.session_state.t4_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t4_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t4_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t4_logos) > 1 and _del_btn(f"t4_logo_del_{i}"):
                        st.session_state.t4_logos.pop(i); st.rerun()
            if _add_btn("t4_logo_add", "＋ Adicionar logo"):
                st.session_state.t4_logos.append({"valor": "MARCA"}); st.rerun()

            st.caption("Links do menu  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t4_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t4_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t4_nl_txt_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t4_nav_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t4_nl_url_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t4_nav_links) > 1 and _del_btn(f"t4_nl_del_{i}"):
                        st.session_state.t4_nav_links.pop(i); st.rerun()
            if _add_btn("t4_nl_add", "＋ Adicionar link"):
                st.session_state.t4_nav_links.append({"texto": "Link", "url": "#"}); st.rerun()

            st.caption("Botão CTA da navbar  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t4_nav_ctas):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t4_nav_ctas[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t4_ncta_txt_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t4_nav_ctas[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t4_ncta_url_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t4_nav_ctas) > 1 and _del_btn(f"t4_ncta_del_{i}"):
                        st.session_state.t4_nav_ctas.pop(i); st.rerun()
            if _add_btn("t4_ncta_add", "＋ Adicionar CTA navbar"):
                st.session_state.t4_nav_ctas.append({"texto": "CTA", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">⚡ Hero (Principal)</div>', unsafe_allow_html=True)

            st.caption("Título  *(Space Mono grande com glow neon)*")
            for i, t in enumerate(st.session_state.t4_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t4_hero_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t4_ht_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t4_hero_titulos) > 1 and _del_btn(f"t4_ht_del_{i}"):
                        st.session_state.t4_hero_titulos.pop(i); st.rerun()
            if _add_btn("t4_ht_add", "＋ Adicionar título"):
                st.session_state.t4_hero_titulos.append({"valor": "NOVO TÍTULO"}); st.rerun()

            st.caption("Subtítulo  *(texto cyan menor)*")
            for i, s in enumerate(st.session_state.t4_hero_subtitulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t4_hero_subtitulos[i]["valor"] = st.text_input(
                        "Subtítulo", s["valor"], key=f"t4_hs_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t4_hero_subtitulos) > 1 and _del_btn(f"t4_hs_del_{i}"):
                        st.session_state.t4_hero_subtitulos.pop(i); st.rerun()
            if _add_btn("t4_hs_add", "＋ Adicionar subtítulo"):
                st.session_state.t4_hero_subtitulos.append({"valor": "Novo subtítulo"}); st.rerun()

            st.caption("Botões  *(Texto | URL | Estilo)*")
            for i, btn in enumerate(st.session_state.t4_hero_btns):
                c1, c2, c3, c4 = st.columns([3, 3, 3, 1])
                with c1:
                    st.session_state.t4_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t4_hbtn_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t4_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t4_hbtn_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    st.session_state.t4_hero_btns[i]["estilo"] = st.selectbox(
                        "Estilo", ["primário", "secundário"],
                        index=0 if btn["estilo"] == "primário" else 1,
                        key=f"t4_hbtn_e_{i}", label_visibility="collapsed")
                with c4:
                    if len(st.session_state.t4_hero_btns) > 1 and _del_btn(f"t4_hbtn_del_{i}"):
                        st.session_state.t4_hero_btns.pop(i); st.rerun()
            if _add_btn("t4_hbtn_add", "＋ Adicionar botão hero"):
                st.session_state.t4_hero_btns.append({"texto": "Botão", "url": "#", "estilo": "primário"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # RECURSOS (FEATURES)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💎 Recursos Revolucionários</div>', unsafe_allow_html=True)
            st.caption("Cards de recurso  *(Emoji | Título | Descrição)*")
            for i, card in enumerate(st.session_state.t4_feat_cards):
                with st.expander(f"Recurso {i+1}: {card['titulo']}"):
                    st.session_state.t4_feat_cards[i]["icone"] = st.text_input(
                        "Ícone/Emoji", card["icone"], key=f"t4_fc_i_{i}")
                    st.session_state.t4_feat_cards[i]["titulo"] = st.text_input(
                        "Título", card["titulo"], key=f"t4_fc_t_{i}")
                    st.session_state.t4_feat_cards[i]["descricao"] = st.text_area(
                        "Descrição", card["descricao"], key=f"t4_fc_d_{i}", height=80)
                    if len(st.session_state.t4_feat_cards) > 1:
                        if st.button("🗑 Remover este recurso", key=f"t4_fc_del_{i}"):
                            st.session_state.t4_feat_cards.pop(i); st.rerun()
            if _add_btn("t4_fc_add", "＋ Adicionar recurso"):
                st.session_state.t4_feat_cards.append({"icone": "✨", "titulo": "Novo Recurso", "descricao": "Descrição aqui"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # SHOWCASE (NÚMEROS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Números que Impressionam</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t4_show_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t4_show_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t4_st_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t4_show_titulos) > 1 and _del_btn(f"t4_st_del_{i}"):
                        st.session_state.t4_show_titulos.pop(i); st.rerun()
            if _add_btn("t4_st_add", "＋ Adicionar título"):
                st.session_state.t4_show_titulos.append({"valor": "NÚMEROS"}); st.rerun()

            st.caption("Cards de números  *(Valor | Rótulo)*")
            for i, card in enumerate(st.session_state.t4_show_cards):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t4_show_cards[i]["numero"] = st.text_input(
                        "Valor", card["numero"], key=f"t4_sc_n_{i}", label_visibility="collapsed", placeholder="Valor")
                with c2:
                    st.session_state.t4_show_cards[i]["label"] = st.text_input(
                        "Rótulo", card["label"], key=f"t4_sc_l_{i}", label_visibility="collapsed", placeholder="Rótulo")
                with c3:
                    if len(st.session_state.t4_show_cards) > 1 and _del_btn(f"t4_sc_del_{i}"):
                        st.session_state.t4_show_cards.pop(i); st.rerun()
            if _add_btn("t4_sc_add", "＋ Adicionar número"):
                st.session_state.t4_show_cards.append({"numero": "0", "label": "Novo Dado"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # CTA FINAL
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🚀 Chamada para Ação Final</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, t in enumerate(st.session_state.t4_ctaf_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t4_ctaf_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t4_ctaft_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t4_ctaf_titulos) > 1 and _del_btn(f"t4_ctaft_del_{i}"):
                        st.session_state.t4_ctaf_titulos.pop(i); st.rerun()
            if _add_btn("t4_ctaft_add", "＋ Adicionar título"):
                st.session_state.t4_ctaf_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t4_ctaf_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t4_ctaf_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t4_ctafd_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t4_ctaf_descs) > 1 and _del_btn(f"t4_ctafd_del_{i}"):
                        st.session_state.t4_ctaf_descs.pop(i); st.rerun()
            if _add_btn("t4_ctafd_add", "＋ Adicionar descrição"):
                st.session_state.t4_ctaf_descs.append({"valor": "Nova Descrição"}); st.rerun()

            st.caption("Botão  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t4_ctaf_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t4_ctaf_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t4_ctafb_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t4_ctaf_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t4_ctafb_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t4_ctaf_btns) > 1 and _del_btn(f"t4_ctafb_del_{i}"):
                        st.session_state.t4_ctaf_btns.pop(i); st.rerun()
            if _add_btn("t4_ctafb_add", "＋ Adicionar botão"):
                st.session_state.t4_ctaf_btns.append({"texto": "Botão", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé Futurista</div>', unsafe_allow_html=True)

            st.caption("Infos de contato  *(email, telefone etc.)*")
            for i, info in enumerate(st.session_state.t4_footer_infos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t4_footer_infos[i]["valor"] = st.text_input(
                        "Infos", info["valor"], key=f"t4_finfo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t4_footer_infos) > 1 and _del_btn(f"t4_finfo_del_{i}"):
                        st.session_state.t4_footer_infos.pop(i); st.rerun()
            if _add_btn("t4_finfo_add", "＋ Adicionar linha de contato"):
                st.session_state.t4_footer_infos.append({"valor": "Nova info"}); st.rerun()

            st.caption("Endereço")
            for i, addr in enumerate(st.session_state.t4_footer_addrs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t4_footer_addrs[i]["valor"] = st.text_input(
                        "Endereço", addr["valor"], key=f"t4_faddr_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t4_footer_addrs) > 1 and _del_btn(f"t4_faddr_del_{i}"):
                        st.session_state.t4_footer_addrs.pop(i); st.rerun()
            if _add_btn("t4_faddr_add", "＋ Adicionar endereço"):
                st.session_state.t4_footer_addrs.append({"valor": "Novo endereço"}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t4_footer_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t4_footer_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t4_fcopy_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t4_footer_copys) > 1 and _del_btn(f"t4_fcopy_del_{i}"):
                        st.session_state.t4_footer_copys.pop(i); st.rerun()
            if _add_btn("t4_fcopy_add", "＋ Adicionar linha"):
                st.session_state.t4_footer_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t4_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t4_obs[i]["valor"] = st.text_area(
                        "Obs", item["valor"], key=f"t4_obs_{i}", height=80,
                        placeholder="Ex: quero mudar a fonte, adicionar FAQ, remover botão X...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t4_obs) > 1 and _del_btn(f"t4_obs_del_{i}"):
                        st.session_state.t4_obs.pop(i); st.rerun()
            if _add_btn("t4_obs_add", "＋ Adicionar observação"):
                st.session_state.t4_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ENVIAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t4_send", type="primary"):
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
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
