import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img9.png"
TEMPLATE_NAME = "Template 9 — WIS (Learntech & Consultoria)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores WIS
        "t9_cores": [
            {"nome": "Cor Principal (Azul)",    "valor": "#0055ff"},
            {"nome": "Cor de Destaque (Laranja)", "valor": "#ff6600"},
            {"nome": "Cor Escura (Dark)",       "valor": "#1e1e1e"},
            {"nome": "Cor de Fundo (Light)",    "valor": "#f8faff"},
        ],
        # Navbar
        "t9_logos": [{"valor": "WIS<span class=\"wis-dot\">.</span>"}],
        "t9_nav_links": [
            {"texto": "SOLUÇÕES",   "url": "#solucoes"},
            {"texto": "QUEM SOMOS", "url": "#manifesto"},
            {"texto": "BLOG",       "url": "https://www.google.com/"},
            {"texto": "CONTATO",    "url": "#footer"},
        ],
        # Hero
        "t9_hero_badges": [{"valor": "Learntech & Consultoria"}],
        "t9_hero_titulos": [{"valor": "Prepare sua empresa para o <span style=\"color: var(--wis-blue)\">próximo nível</span> da aprendizagem."}],
        "t9_hero_descs": [{"valor": "Desenvolvemos soluções de aprendizagem corporativa personalizadas com foco em <b>Cultura e Performance</b>."}],
        "t9_hero_btns": [{"texto": "FALE COM ESPECIALISTAS", "url": "#solucoes"}],
        # Soluções (Grid)
        "t9_sol_labels": [{"valor": "NOSSAS SOLUÇÕES"}],
        "t9_sol_titulos": [{"valor": "Como podemos ajudar seu negócio?"}],
        "t9_sol_cards": [
            {"icon": "🚀", "titulo": "Learning Campaigns",    "desc": "Campanhas de aprendizagem engajadoras para mudanças de cultura e novos processos.", "url": "https://www.google.com/"},
            {"icon": "🤝", "titulo": "Design de Comunidades", "desc": "Criamos ecossistemas internos onde o conhecimento flui de forma orgânica e contínua.", "url": "https://www.google.com/"},
            {"icon": "📈", "titulo": "Upskilling & Reskilling","desc": "Programas intensivos de desenvolvimento de novas competências para o futuro.", "url": "https://www.google.com/"},
        ],
        # Números (Prova Social)
        "t9_stats": [
            {"valor": "+12",   "label": "Anos de Mercado"},
            {"valor": "+900",  "label": "Projetos Entregues"},
            {"valor": "+100k", "label": "Pessoas Impactadas"},
            {"valor": "+50",   "label": "Grandes Empresas"},
        ],
        # Manifesto / Diferencial
        "t9_man_badges": [{"valor": "Nossa Metodologia"}],
        "t9_man_titulos": [{"valor": "Aprendizagem aplicada que gera resultado real."}],
        "t9_man_descs": [{"valor": "Não acreditamos em treinamentos passivos. Nossa abordagem foca na <b>prática</b>, utilizando tecnologia e inovação para resolver desafios reais de liderança, cultura e vendas."}],
        "t9_man_imgs": [{"valor": "https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=800"}],
        "t9_man_btns": [{"texto": "CONHEÇA NOSSA HISTÓRIA", "url": "https://www.google.com/"}],
        # Footer
        "t9_foot_titulos": [{"valor": "WIS<span class=\"wis-dot\">.</span>"}],
        "t9_foot_locais":  [{"valor": "São Paulo | Vitória | Florianópolis"}],
        "t9_foot_contatos": [{"valor": "contato@wis.digital<br>(11) 5555-5555"}],
        "t9_foot_sociais": [
            {"nome": "Linkedin",  "url": "https://www.google.com/"},
            {"nome": "Instagram", "url": "https://www.google.com/"},
            {"nome": "Spotify",   "url": "https://www.google.com/"},
        ],
        # Observações
        "t9_obs": [{"valor": ""}],
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
            st.markdown('<div class="section-label">🎨 Identidade WIS</div>', unsafe_allow_html=True)
            for i, cor in enumerate(st.session_state.t9_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t9_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t9_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t9_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t9_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t9_cores) > 1 and _del_btn(f"t9_cor_del_{i}"):
                        st.session_state.t9_cores.pop(i); st.rerun()
            if _add_btn("t9_cor_add", "＋ Adicionar cor"):
                st.session_state.t9_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)
            st.caption("Logo WIS")
            for i, logo in enumerate(st.session_state.t9_logos):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t9_logos[i]["valor"] = st.text_input("Logo", logo["valor"], key=f"t9_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t9_logos) > 1 and _del_btn(f"t9_logo_del_{i}"):
                        st.session_state.t9_logos.pop(i); st.rerun()
            if _add_btn("t9_logo_add", "＋ Adicionar logo"):
                st.session_state.t9_logos.append({"valor": "NOVA LOGO"}); st.rerun()
            
            st.caption("Links do Menu *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t9_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t9_nav_links[i]["texto"] = st.text_input("Texto", link["texto"], key=f"t9_nl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t9_nav_links[i]["url"] = st.text_input("URL", link["url"], key=f"t9_nl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t9_nav_links) > 1 and _del_btn(f"t9_nl_del_{i}"):
                        st.session_state.t9_nav_links.pop(i); st.rerun()
            if _add_btn("t9_nl_add", "＋ Adicionar link"):
                st.session_state.t9_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🚀 Hero (Learntech)</div>', unsafe_allow_html=True)
            for i, badge in enumerate(st.session_state.t9_hero_badges):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t9_hero_badges[i]["valor"] = st.text_input("Badge", badge["valor"], key=f"t9_h_b_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t9_hero_badges) > 1 and _del_btn(f"t9_h_b_del_{i}"):
                        st.session_state.t9_hero_badges.pop(i); st.rerun()
            if _add_btn("t9_h_b_add", "＋ Adicionar badge hero"):
                st.session_state.t9_hero_badges.append({"valor": "NOVA BADGE"}); st.rerun()

            for i, t in enumerate(st.session_state.t9_hero_titulos):
                st.session_state.t9_hero_titulos[i]["valor"] = st.text_area("Título (use <span>)", t["valor"], key=f"t9_h_t_{i}")
            for i, d in enumerate(st.session_state.t9_hero_descs):
                st.session_state.t9_hero_descs[i]["valor"] = st.text_area("Descrição", d["valor"], key=f"t9_h_d_{i}")
            
            st.caption("Botões do Hero *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t9_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t9_hero_btns[i]["texto"] = st.text_input("Texto", btn["texto"], key=f"t9_hb_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t9_hero_btns[i]["url"] = st.text_input("URL", btn["url"], key=f"t9_hb_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t9_hero_btns) > 1 and _del_btn(f"t9_hb_del_{i}"):
                        st.session_state.t9_hero_btns.pop(i); st.rerun()
            if _add_btn("t9_hb_add", "＋ Adicionar botão hero"):
                st.session_state.t9_hero_btns.append({"texto": "FALE COM ESPECIALISTAS", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # SOLUÇÕES (GRID)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🤝 Soluções Corporativas</div>', unsafe_allow_html=True)
            for i, l in enumerate(st.session_state.t9_sol_labels):
                st.session_state.t9_sol_labels[i]["valor"] = st.text_input("Rótulo Seção", l["valor"], key=f"t9_sl_{i}")
            for i, t in enumerate(st.session_state.t9_sol_titulos):
                st.session_state.t9_sol_titulos[i]["valor"] = st.text_input("Título Seção", t["valor"], key=f"t9_st_{i}")
            
            for i, card in enumerate(st.session_state.t9_sol_cards):
                with st.expander(f"Solução {i+1}: {card['titulo']}"):
                    st.session_state.t9_sol_cards[i]["icon"] = st.text_input("Ícone/Emoji", card["icon"], key=f"t9_sc_i_{i}")
                    st.session_state.t9_sol_cards[i]["titulo"] = st.text_input("Título", card["titulo"], key=f"t9_sc_t_{i}")
                    st.session_state.t9_sol_cards[i]["desc"] = st.text_area("Descrição", card["desc"], key=f"t9_sc_d_{i}")
                    st.session_state.t9_sol_cards[i]["url"] = st.text_input("URL Saiba Mais", card["url"], key=f"t9_sc_u_{i}")
                    if len(st.session_state.t9_sol_cards) > 1 and _del_btn(f"t9_sc_del_{i}", "Remover solução"):
                        st.session_state.t9_sol_cards.pop(i); st.rerun()
            if _add_btn("t9_sc_add", "＋ Adicionar solução"):
                st.session_state.t9_sol_cards.append({"icon": "💡", "titulo": "Nova Solução", "desc": "...", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NÚMEROS (STATS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Prova Social (Números)</div>', unsafe_allow_html=True)
            for i, stat in enumerate(st.session_state.t9_stats):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t9_stats[i]["valor"] = st.text_input("Valor", stat["valor"], key=f"t9_st_v_{i}", label_visibility="collapsed")
                with c2: st.session_state.t9_stats[i]["label"] = st.text_input("Rótulo", stat["label"], key=f"t9_st_l_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t9_stats) > 1 and _del_btn(f"t9_st_del_{i}"):
                        st.session_state.t9_stats.pop(i); st.rerun()
            if _add_btn("t9_st_add", "＋ Adicionar estatística"):
                st.session_state.t9_stats.append({"valor": "0", "label": "NOVO DADO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # MANIFESTO / METODOLOGIA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📖 Manifesto & Metodologia</div>', unsafe_allow_html=True)
            for i, b in enumerate(st.session_state.t9_man_badges):
                st.session_state.t9_man_badges[i]["valor"] = st.text_input("Badge Metodologia", b["valor"], key=f"t9_mb_{i}")
            for i, t in enumerate(st.session_state.t9_man_titulos):
                st.session_state.t9_man_titulos[i]["valor"] = st.text_input("Título Metodologia", t["valor"], key=f"t9_mt_{i}")
            for i, d in enumerate(st.session_state.t9_man_descs):
                st.session_state.t9_man_descs[i]["valor"] = st.text_area("Descrição Metodologia", d["valor"], key=f"t9_md_{i}")
            for i, img in enumerate(st.session_state.t9_man_imgs):
                st.session_state.t9_man_imgs[i]["valor"] = st.text_input("URL Imagem", img["valor"], key=f"t9_mi_{i}")
            
            st.caption("Botões do Manifesto *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t9_man_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t9_man_btns[i]["texto"] = st.text_input("Texto", btn["texto"], key=f"t9_mbtn_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t9_man_btns[i]["url"] = st.text_input("URL", btn["url"], key=f"t9_mbtn_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t9_man_btns) > 1 and _del_btn(f"t9_mbtn_del_{i}"):
                        st.session_state.t9_man_btns.pop(i); st.rerun()
            if _add_btn("t9_mbtn_add", "＋ Adicionar botão manifesto"):
                st.session_state.t9_man_btns.append({"texto": "SAIBA MAIS", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé & Contato</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t9_foot_titulos):
                st.session_state.t9_foot_titulos[i]["valor"] = st.text_input("Logo Footer", t["valor"], key=f"t9_ft_{i}")
            for i, l in enumerate(st.session_state.t9_foot_locais):
                st.session_state.t9_foot_locais[i]["valor"] = st.text_input("Locais", l["valor"], key=f"t9_fl_{i}")
            for i, c in enumerate(st.session_state.t9_foot_contatos):
                st.session_state.t9_foot_contatos[i]["valor"] = st.text_area("Dados Contato", c["valor"], key=f"t9_fc_{i}")
            
            st.caption("Redes Sociais *(Nome | URL)*")
            for i, soc in enumerate(st.session_state.t9_foot_sociais):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t9_foot_sociais[i]["nome"] = st.text_input("Rede", soc["nome"], key=f"t9_fs_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t9_foot_sociais[i]["url"] = st.text_input("URL", soc["url"], key=f"t9_fs_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t9_foot_sociais) > 1 and _del_btn(f"t9_fs_del_{i}"):
                        st.session_state.t9_foot_sociais.pop(i); st.rerun()
            if _add_btn("t9_fs_add", "＋ Adicionar rede social"):
                st.session_state.t9_foot_sociais.append({"nome": "Rede", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t9_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t9_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t9_obs_{i}", height=80,
                        placeholder="Ex: Mudar as fotos para o estilo corporativo...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t9_obs) > 1 and _del_btn(f"t9_obs_del_{i}"):
                        st.session_state.t9_obs.pop(i); st.rerun()
            if _add_btn("t9_obs_add", "＋ Adicionar observação"):
                st.session_state.t9_obs.append({"valor": ""}); st.rerun()

            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t9_send", type="primary"):
                st.success("✅ Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
                st.balloons()

    # ════════════════════════════════════════════════════════════════════════
    # PAINEL DIREITO — PREVIEW
    # ════════════════════════════════════════════════════════════════════════
    with col_preview:
        st.markdown('<p class="img-caption">📌 Referência visual do template — role para ver o site completo</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}" alt="Preview do template" /></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(
        page_title=f"Editor — {TEMPLATE_NAME}",
        page_icon="✏️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
