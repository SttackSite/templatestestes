import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img29.png"
TEMPLATE_NAME = "Template 29 — Website Sustentável Style (Eco-Design & Tech)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores Eco
        "t29_cores": [
            {"nome": "Verde Eco (Principal)", "valor": "#2d5a27"},
            {"nome": "Fundo Eco (Light)", "valor": "#f0f4ef"},
            {"nome": "Destaque Eco (Accent)", "valor": "#8eb486"},
            {"nome": "Escuro Eco (Dark)", "valor": "#1a2e19"},
            {"nome": "Texto Gray", "valor": "#4a4a4a"},
        ],
        # Navbar
        "t29_nav_logos": [{"emoji": "🌿", "texto": "Website Sustentável"}],
        "t29_nav_links": [
            {"texto": "Manifesto", "url": "#diferenciais"},
            {"texto": "Certificação", "url": "#impacto"},
            {"texto": "Tecnologia", "url": "#diferenciais"},
            {"texto": "CONTATO", "url": "#footer", "active": True},
        ],
        # Hero Section
        "t29_hero_badges": [{"valor": "Otimizado para baixo consumo"}],
        "t29_hero_titulos": [{"valor": "Seu site pode ser mais <span class='eco-italic'>rápido</span> e menos <span class='eco-italic'>poluente.</span>"}],
        "t29_hero_descs": [{"valor": "Desenvolvemos tecnologias web focadas em performance extrema e responsabilidade ambiental. O futuro da internet é <b>sustentável</b>."}],
        "t29_hero_btns": [{"texto": "CERTIFIQUE SEU WEBSITE", "url": "#diferenciais"}],
        # Diferenciais (Cards)
        "t29_diff_titulos": [{"valor": "Por que ser sustentável?"}],
        "t29_diff_items": [
            {"icon": "🍃", "title": "Baixa Emissão", "desc": "Reduzimos o tamanho dos arquivos e a requisição de servidores, diminuindo a pegada de carbono de cada acesso.", "btn_texto": "SAIBA MAIS", "btn_url": "https://www.google.com/"},
            {"icon": "🔍", "title": "SEO Consciente", "desc": "Sites mais leves carregam instantaneamente, o que o Google ama. Sustentabilidade é a melhor estratégia de ranking.", "btn_texto": "SAIBA MAIS", "btn_url": "https://www.google.com/"},
            {"icon": "🔋", "title": "Green Hosting", "desc": "Hospedagem em servidores alimentados por fontes de energia 100% renováveis e limpas.", "btn_texto": "SAIBA MAIS", "btn_url": "https://www.google.com/"},
        ],
        # Impacto (Stats)
        "t29_stat_items": [
            {"valor": "-40%", "label": "NA EMISSÃO DE CO2", "cor": "#8eb486"},
            {"valor": "2.5x", "label": "MAIS VELOCIDADE", "cor": "#8eb486"},
            {"valor": "100%", "label": "ENERGIA LIMPA", "cor": "#8eb486"},
        ],
        # CTA Final
        "t29_cta_titulos": [{"valor": "Pronto para o próximo passo?"}],
        "t29_cta_descs": [{"valor": "Seja parte da mudança positiva no ecossistema digital."}],
        "t29_cta_btns": [{"texto": "SOLICITAR ORÇAMENTO VERDE", "url": "https://www.google.com/"}],
        # Footer
        "t29_foot_copys": [{"valor": "© 2026 Website Sustentável. Tecnologia com Propósito."}],
        "t29_foot_links": [
            {"texto": "Política de Privacidade", "url": "https://www.google.com/"},
            {"texto": "Eco-Design Guide", "url": "https://www.google.com/"},
        ],
        # Observações
        "t13_obs": [{"valor": ""}], # Mantendo a chave para consistência
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
            for i, cor in enumerate(st.session_state.t29_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t29_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t29_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t29_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t29_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t29_cores) > 1 and _del_btn(f"t29_cor_del_{i}"):
                        st.session_state.t29_cores.pop(i); st.rerun()
            if _add_btn("t29_cor_add", "＋ Adicionar cor"):
                st.session_state.t29_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t29_nav_logos):
                c1, c2 = st.columns([2, 8])
                with c1: st.session_state.t29_nav_logos[i]["emoji"] = st.text_input("Emoji", item["emoji"], key=f"t29_nl_e_{i}")
                with c2: st.session_state.t29_nav_logos[i]["texto"] = st.text_input("Nome Marca", item["texto"], key=f"t29_nl_t_{i}")
            
            st.caption("Links do Menu")
            for i, link in enumerate(st.session_state.t29_nav_links):
                c1, c2, c3, c4 = st.columns([3, 3, 2, 1])
                with c1: st.session_state.t29_nav_links[i]["texto"] = st.text_input("Texto", link["texto"], key=f"t29_navl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t29_nav_links[i]["url"] = st.text_input("URL", link["url"], key=f"t29_navl_u_{i}", label_visibility="collapsed")
                with c3: st.session_state.t29_nav_links[i]["active"] = st.checkbox("Ativo", link.get("active", False), key=f"t29_navl_a_{i}")
                with c4:
                    if len(st.session_state.t29_nav_links) > 1 and _del_btn(f"t29_navl_del_{i}"):
                        st.session_state.t29_nav_links.pop(i); st.rerun()
            if _add_btn("t29_navl_add", "＋ Adicionar link"):
                st.session_state.t29_nav_links.append({"texto": "LINK", "url": "#", "active": False}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO SECTION
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌿 Hero Section</div>', unsafe_allow_html=True)
            for i, b in enumerate(st.session_state.t29_hero_badges):
                st.session_state.t29_hero_badges[i]["valor"] = st.text_input("Badge Hero", b["valor"], key=f"t29_h_b_{i}")
            for i, t in enumerate(st.session_state.t29_hero_titulos):
                st.session_state.t29_hero_titulos[i]["valor"] = st.text_area("Título Hero (HTML)", t["valor"], key=f"t29_h_t_{i}")
            for i, d in enumerate(st.session_state.t29_hero_descs):
                st.session_state.t29_hero_descs[i]["valor"] = st.text_area("Descrição Hero (HTML)", d["valor"], key=f"t29_h_d_{i}")
            
            st.caption("Botões Hero")
            for i, btn in enumerate(st.session_state.t29_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t29_hero_btns[i]["texto"] = st.text_input("Texto", btn["texto"], key=f"t29_hb_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t29_hero_btns[i]["url"] = st.text_input("URL", btn["url"], key=f"t29_hb_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t29_hero_btns) > 1 and _del_btn(f"t29_hb_del_{i}"):
                        st.session_state.t29_hero_btns.pop(i); st.rerun()
            if _add_btn("t29_hb_add", "＋ Adicionar botão"):
                st.session_state.t29_hero_btns.append({"texto": "COMEÇAR", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # DIFERENCIAIS (CARDS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🍃 Diferenciais (Cards)</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t29_diff_titulos):
                st.session_state.t29_diff_titulos[i]["valor"] = st.text_input("Título Seção", t["valor"], key=f"t29_dt_{i}")
            
            for i, item in enumerate(st.session_state.t29_diff_items):
                with st.expander(f"Diferencial {i+1}: {item['title']}"):
                    st.session_state.t29_diff_items[i]["icon"] = st.text_input("Ícone/Emoji", item["icon"], key=f"t29_di_i_{i}")
                    st.session_state.t29_diff_items[i]["title"] = st.text_input("Título", item["title"], key=f"t29_di_t_{i}")
                    st.session_state.t29_diff_items[i]["desc"] = st.text_area("Descrição", item["desc"], key=f"t29_di_d_{i}")
                    st.session_state.t29_diff_items[i]["btn_texto"] = st.text_input("Texto Botão", item["btn_texto"], key=f"t29_di_bt_{i}")
                    st.session_state.t29_diff_items[i]["btn_url"] = st.text_input("URL Botão", item["btn_url"], key=f"t29_di_bu_{i}")
                    if len(st.session_state.t29_diff_items) > 1 and _del_btn(f"t29_di_del_{i}", "Remover item"):
                        st.session_state.t29_diff_items.pop(i); st.rerun()
            if _add_btn("t29_di_add", "＋ Adicionar diferencial"):
                st.session_state.t29_diff_items.append({"icon": "⭐", "title": "NOVO", "desc": "DESC", "btn_texto": "SAIBA MAIS", "btn_url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # IMPACTO (STATS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Impacto (Estatísticas)</div>', unsafe_allow_html=True)
            for i, stat in enumerate(st.session_state.t29_stat_items):
                c1, c2, c3, c4 = st.columns([3, 4, 2, 1])
                with c1: st.session_state.t29_stat_items[i]["valor"] = st.text_input("Valor", stat["valor"], key=f"t29_st_v_{i}", label_visibility="collapsed")
                with c2: st.session_state.t29_stat_items[i]["label"] = st.text_input("Rótulo", stat["label"], key=f"t29_st_l_{i}", label_visibility="collapsed")
                with c3: st.session_state.t29_stat_items[i]["cor"] = st.color_picker("Cor", stat["cor"], key=f"t29_st_c_{i}", label_visibility="collapsed")
                with c4:
                    if len(st.session_state.t29_stat_items) > 1 and _del_btn(f"t29_st_del_{i}"):
                        st.session_state.t29_stat_items.pop(i); st.rerun()
            if _add_btn("t29_st_add", "＋ Adicionar número"):
                st.session_state.t29_stat_items.append({"valor": "0", "label": "LABEL", "cor": "#8eb486"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # CTA FINAL
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📢 Chamada Final (CTA)</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t29_cta_titulos):
                st.session_state.t29_cta_titulos[i]["valor"] = st.text_input("Título CTA", t["valor"], key=f"t29_ct_t_{i}")
            for i, d in enumerate(st.session_state.t29_cta_descs):
                st.session_state.t29_cta_descs[i]["valor"] = st.text_input("Descrição CTA", d["valor"], key=f"t29_ct_d_{i}")
            
            st.caption("Botões CTA")
            for i, btn in enumerate(st.session_state.t29_cta_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t29_cta_btns[i]["texto"] = st.text_input("Texto", btn["texto"], key=f"t29_ctb_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t29_cta_btns[i]["url"] = st.text_input("URL", btn["url"], key=f"t29_ctb_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t29_cta_btns) > 1 and _del_btn(f"t29_ctb_del_{i}"):
                        st.session_state.t29_cta_btns.pop(i); st.rerun()
            if _add_btn("t29_ctb_add", "＋ Adicionar botão"):
                st.session_state.t29_cta_btns.append({"texto": "COMEÇAR", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)
            for i, copy in enumerate(st.session_state.t29_foot_copys):
                st.session_state.t29_foot_copys[i]["valor"] = st.text_input("Copyright", copy["valor"], key=f"t29_fcp_{i}")
            
            st.caption("Links do Rodapé")
            for i, link in enumerate(st.session_state.t29_foot_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t29_foot_links[i]["texto"] = st.text_input("Texto", link["texto"], key=f"t29_footl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t29_foot_links[i]["url"] = st.text_input("URL", link["url"], key=f"t29_footl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t29_foot_links) > 1 and _del_btn(f"t29_footl_del_{i}"):
                        st.session_state.t29_foot_links.pop(i); st.rerun()
            if _add_btn("t29_footl_add", "＋ Adicionar link"):
                st.session_state.t29_foot_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t13_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t13_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t29_obs_{i}", height=80,
                        placeholder="Ex: Usar tons pastéis ainda mais suaves...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t13_obs) > 1 and _del_btn(f"t29_obs_del_{i}"):
                        st.session_state.t13_obs.pop(i); st.rerun()
            if _add_btn("t29_obs_add", "＋ Adicionar observação"):
                st.session_state.t13_obs.append({"valor": ""}); st.rerun()

            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t29_send", type="primary"):
                st.success("✅ Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
                st.balloons()

    # ════════════════════════════════════════════════════════════════════════
    # PAINEL DIREITO — PREVIEW (LIMPO)
    # ════════════════════════════════════════════════════════════════════════
    with col_preview:
        st.markdown('<p class="img-caption">📌 Referência visual do template — role para ver o site completo</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}" alt="Preview do template" /></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(
        page_title=f"Editor — {TEMPLATE_NAME}",
        page_icon="🌿",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
