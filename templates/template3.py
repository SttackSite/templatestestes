import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img3.png"
TEMPLATE_NAME = "Template 3 — Experiência Absurda (Premium)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores
        "t3_cores": [
            {"nome": "Cor de destaque (botões, logo)", "valor": "#FF006E"},
            {"nome": "Cor secundária (links, bordas)",  "valor": "#00D9FF"},
            {"nome": "Cor de fundo (gradiente 1)",      "valor": "#0f0f1e"},
            {"nome": "Cor de fundo (gradiente 2)",      "valor": "#1a1a2e"},
        ],
        # Navbar
        "t3_logos": [{"valor": "PREMIUM"}],
        "t3_nav_links": [
            {"texto": "Recursos", "url": "#recursos"},
            {"texto": "Galeria",  "url": "#galeria"},
            {"texto": "Sobre",    "url": "#sobre"},
            {"texto": "Contato",  "url": "#contato"},
        ],
        "t3_nav_ctas": [
            {"texto": "Começar Agora", "url": "https://www.google.com/"},
        ],
        # Hero
        "t3_hero_titulos": [
            {"valor": "Experiência Absurda"},
        ],
        "t3_hero_subtitulos": [
            {"valor": "Design que transforma, cores que inspiram"},
        ],
        "t3_hero_btns": [
            {"texto": "Explorar Agora", "url": "https://www.google.com/", "estilo": "primário"},
            {"texto": "Saiba Mais",      "url": "https://www.google.com/", "estilo": "secundário"},
        ],
        # Recursos (Features)
        "t3_feat_titulos": [{"valor": "Recursos Incríveis"}],
        "t3_feat_descs":   [{"valor": "Tudo que você precisa para impressionar seus clientes"}],
        "t3_feat_cards": [
            {"icone": "⚡", "titulo": "Ultra Rápido",            "descricao": "Performance otimizada para a melhor experiência do usuário em qualquer dispositivo."},
            {"icone": "🎨", "titulo": "Design Moderno",          "descricao": "Interface visual impressionante com animações suaves e cores dinâmicas."},
            {"icone": "🔧", "titulo": "Totalmente Customizável", "descricao": "Adapte cores, textos e conteúdo facilmente para seu negócio específico."},
            {"icone": "📱", "titulo": "Responsivo",              "descricao": "Funciona perfeitamente em desktop, tablet e mobile com experiência fluida."},
            {"icone": "🚀", "titulo": "Conversão Máxima",        "descricao": "Design estratégico focado em converter visitantes em clientes."},
            {"icone": "✨", "titulo": "Experiência Premium",      "descricao": "Cada detalhe foi pensado para criar uma experiência memorável."},
        ],
        # Números (Showcase)
        "t3_show_titulos": [{"valor": "Números que Falam"}],
        "t3_show_descs":   [{"valor": "Resultados comprovados de padrões premium"}],
        "t3_show_cards": [
            {"numero": "300%", "label": "Mais Conversões"},
            {"numero": "50K+", "label": "Clientes Felizes"},
            {"numero": "99%",  "label": "Satisfação"},
            {"numero": "24/7", "label": "Suporte"},
        ],
        # CTA Final
        "t3_ctaf_titulos": [{"valor": "Pronto para Transformar?"}],
        "t3_ctaf_descs":   [{"valor": "Junte-se a milhares de empresas que já estão usando padrões premium para crescer exponencialmente."}],
        "t3_ctaf_btns":    [{"texto": "Começar Sua Jornada", "url": "https://www.google.com/"}],
        # Footer
        "t3_footer_infos": [{"valor": "Email: contato@premium.com.br | Telefone: (99) 99999-9999"}],
        "t3_footer_addrs": [{"valor": "Endereço: Av. Principal, 1000 - São Paulo, SP"}],
        "t3_footer_copys": [{"valor": "© 2025 Premium padrões. Todos os direitos reservados. Transformando negócios com design excepcional."}],
        # Observações
        "t3_obs": [{"valor": ""}],
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
            st.markdown('<div class="section-label">🎨 Cores</div>', unsafe_allow_html=True)
            for i, cor in enumerate(st.session_state.t3_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t3_cores[i]["nome"] = st.text_input(
                        "Nome da cor", cor["nome"], key=f"t3_cor_nome_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t3_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t3_cor_val_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t3_cores) > 1 and _del_btn(f"t3_cor_del_{i}"):
                        st.session_state.t3_cores.pop(i); st.rerun()
            if _add_btn("t3_cor_add", "＋ Adicionar cor"):
                st.session_state.t3_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca")
            for i, item in enumerate(st.session_state.t3_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t3_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t3_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t3_logos) > 1 and _del_btn(f"t3_logo_del_{i}"):
                        st.session_state.t3_logos.pop(i); st.rerun()
            if _add_btn("t3_logo_add", "＋ Adicionar logo"):
                st.session_state.t3_logos.append({"valor": "NOVA MARCA"}); st.rerun()

            st.caption("Links do menu *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t3_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t3_nav_links[i]["texto"] = st.text_input("Txt", link["texto"], key=f"t3_nl_txt_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t3_nav_links[i]["url"] = st.text_input("URL", link["url"], key=f"t3_nl_url_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t3_nav_links) > 1 and _del_btn(f"t3_nl_del_{i}"):
                        st.session_state.t3_nav_links.pop(i); st.rerun()
            if _add_btn("t3_nl_add", "＋ Adicionar link"):
                st.session_state.t3_nav_links.append({"texto": "Link", "url": "#"}); st.rerun()

            st.caption("Botão CTA da Navbar *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t3_nav_ctas):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t3_nav_ctas[i]["texto"] = st.text_input("Txt", btn["texto"], key=f"t3_ncta_txt_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t3_nav_ctas[i]["url"] = st.text_input("URL", btn["url"], key=f"t3_ncta_url_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t3_nav_ctas) > 1 and _del_btn(f"t3_ncta_del_{i}"):
                        st.session_state.t3_nav_ctas.pop(i); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🚀 Hero (Principal)</div>', unsafe_allow_html=True)

            st.caption("Títulos do Hero")
            for i, t in enumerate(st.session_state.t3_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t3_hero_titulos[i]["valor"] = st.text_input("Título", t["valor"], key=f"t3_ht_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t3_hero_titulos) > 1 and _del_btn(f"t3_ht_del_{i}"):
                        st.session_state.t3_hero_titulos.pop(i); st.rerun()

            st.caption("Subtítulos do Hero")
            for i, s in enumerate(st.session_state.t3_hero_subtitulos):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t3_hero_subtitulos[i]["valor"] = st.text_area("Sub", s["valor"], key=f"t3_hs_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t3_hero_subtitulos) > 1 and _del_btn(f"t3_hs_del_{i}"):
                        st.session_state.t3_hero_subtitulos.pop(i); st.rerun()

            st.caption("Botões do Hero *(Texto | URL | Estilo)*")
            for i, btn in enumerate(st.session_state.t3_hero_btns):
                c1, c2, c3, c4 = st.columns([3, 3, 3, 1])
                with c1: st.session_state.t3_hero_btns[i]["texto"] = st.text_input("Txt", btn["texto"], key=f"t3_hbtn_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t3_hero_btns[i]["url"] = st.text_input("URL", btn["url"], key=f"t3_hbtn_u_{i}", label_visibility="collapsed")
                with c3: st.session_state.t3_hero_btns[i]["estilo"] = st.selectbox("Estilo", ["primário", "secundário"], index=0 if btn["estilo"]=="primário" else 1, key=f"t3_hbtn_e_{i}", label_visibility="collapsed")
                with c4:
                    if len(st.session_state.t3_hero_btns) > 1 and _del_btn(f"t3_hbtn_del_{i}"):
                        st.session_state.t3_hero_btns.pop(i); st.rerun()
            if _add_btn("t3_hbtn_add", "＋ Adicionar botão hero"):
                st.session_state.t3_hero_btns.append({"texto": "Botão", "url": "#", "estilo": "primário"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # RECURSOS (FEATURES)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">✨ Recursos</div>', unsafe_allow_html=True)
            st.caption("Título e Descrição da Seção")
            for i, t in enumerate(st.session_state.t3_feat_titulos):
                st.session_state.t3_feat_titulos[i]["valor"] = st.text_input("Título Seção", t["valor"], key=f"t3_ft_{i}", label_visibility="collapsed")
            for i, d in enumerate(st.session_state.t3_feat_descs):
                st.session_state.t3_feat_descs[i]["valor"] = st.text_input("Desc Seção", d["valor"], key=f"t3_fd_{i}", label_visibility="collapsed")

            st.caption("Cards de Recursos")
            for i, card in enumerate(st.session_state.t3_feat_cards):
                with st.expander(f"Recurso {i+1}: {card['titulo']}"):
                    st.session_state.t3_feat_cards[i]["icone"] = st.text_input("Ícone/Emoji", card["icone"], key=f"t3_fc_i_{i}")
                    st.session_state.t3_feat_cards[i]["titulo"] = st.text_input("Título", card["titulo"], key=f"t3_fc_t_{i}")
                    st.session_state.t3_feat_cards[i]["descricao"] = st.text_area("Descrição", card["descricao"], key=f"t3_fc_d_{i}")
                    if len(st.session_state.t3_feat_cards) > 1 and _del_btn(f"t3_fc_del_{i}", "Excluir recurso"):
                        st.session_state.t3_feat_cards.pop(i); st.rerun()
            if _add_btn("t3_fc_add", "＋ Adicionar recurso"):
                st.session_state.t3_feat_cards.append({"icone": "✨", "titulo": "Novo Recurso", "descricao": "Descrição aqui"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NÚMEROS (SHOWCASE)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Números (Showcase)</div>', unsafe_allow_html=True)
            for i, card in enumerate(st.session_state.t3_show_cards):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t3_show_cards[i]["numero"] = st.text_input("Valor", card["numero"], key=f"t3_sc_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t3_show_cards[i]["label"] = st.text_input("Rótulo", card["label"], key=f"t3_sc_l_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t3_show_cards) > 1 and _del_btn(f"t3_sc_del_{i}"):
                        st.session_state.t3_show_cards.pop(i); st.rerun()
            if _add_btn("t3_sc_add", "＋ Adicionar número"):
                st.session_state.t3_show_cards.append({"numero": "0", "label": "Novo Dado"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # CTA FINAL
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📢 Chamada Final</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t3_ctaf_titulos):
                st.session_state.t3_ctaf_titulos[i]["valor"] = st.text_input("Título CTA", t["valor"], key=f"t3_ctaft_{i}", label_visibility="collapsed")
            for i, d in enumerate(st.session_state.t3_ctaf_descs):
                st.session_state.t3_ctaf_descs[i]["valor"] = st.text_area("Desc CTA", d["valor"], key=f"t3_ctafd_{i}", label_visibility="collapsed")
            for i, btn in enumerate(st.session_state.t3_ctaf_btns):
                c1, c2 = st.columns([5, 5])
                with c1: st.session_state.t3_ctaf_btns[i]["texto"] = st.text_input("Txt Botão", btn["texto"], key=f"t3_ctafb_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t3_ctaf_btns[i]["url"] = st.text_input("URL Botão", btn["url"], key=f"t3_ctafb_u_{i}", label_visibility="collapsed")

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)
            for i, info in enumerate(st.session_state.t3_footer_infos):
                st.session_state.t3_footer_infos[i]["valor"] = st.text_input("Infos", info["valor"], key=f"t3_finfo_{i}", label_visibility="collapsed")
            for i, addr in enumerate(st.session_state.t3_footer_addrs):
                st.session_state.t3_footer_addrs[i]["valor"] = st.text_input("Endereço", addr["valor"], key=f"t3_faddr_{i}", label_visibility="collapsed")
            for i, copy in enumerate(st.session_state.t3_footer_copys):
                st.session_state.t3_footer_copys[i]["valor"] = st.text_input("Copyright", copy["valor"], key=f"t3_fcopy_{i}", label_visibility="collapsed")

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t3_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t3_obs[i]["valor"] = st.text_area(
                        "Obs", item["valor"], key=f"t3_obs_{i}", height=80,
                        placeholder="Ex: quero mudar a fonte, adicionar FAQ, remover botão X...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t3_obs) > 1 and _del_btn(f"t3_obs_del_{i}"):
                        st.session_state.t3_obs.pop(i); st.rerun()
            if _add_btn("t3_obs_add", "＋ Adicionar observação"):
                st.session_state.t3_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FINALIZAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t3_send", type="primary"):
                st.success("✅ Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
                st.balloons()

    # ════════════════════════════════════════════════════════════════════════
    # PAINEL DIREITO — IMAGEM DO TEMPLATE
    # ════════════════════════════════════════════════════════════════════════
    with col_preview:
        st.markdown(
            '<p class="img-caption">📌 Referência visual do template — role para ver o site completo</p>',
            unsafe_allow_html=True)
        st.markdown(
            f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}" alt="Preview do template" /></div>',
            unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# EXECUÇÃO DIRETA
# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    st.set_page_config(
        page_title=f"Editor — {TEMPLATE_NAME}",
        page_icon="✏️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
