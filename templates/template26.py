import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img26.png"
TEMPLATE_NAME = "Template 26 — Dockyard Social Style (Food & Drink Market)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores Dockyard
        "t26_cores": [
            {"nome": "Principal (Amarelo Dock)", "valor": "#ffcc00"},
            {"nome": "Escura (Preto Dock)", "valor": "#111111"},
            {"nome": "Fundo (Branco Dock)", "valor": "#f4f4f4"},
        ],
        # Barra de Anúncio
        "t26_announcements": [{"valor": "ABERTO NESTE FINAL DE SEMANA • GARANTA SEU INGRESSO"}],
        # Navbar
        "t26_nav_logos": [{"valor": "DOCKYARD SOCIAL"}],
        "t26_nav_links": [
            {"texto": "O QUE ROLA", "url": "#oque-rola"},
            {"texto": "COMIDA", "url": "#comida"},
            {"texto": "BEBIDA", "url": "#bebida"},
            {"texto": "RESERVAR", "url": "#reservar"},
        ],
        # Hero Section
        "t26_hero_titulos": [{"valor": "COMIDA DE RUA.<br>BOAS VIBES.<br>PARA TODOS."}],
        "t26_hero_descs": [{"valor": "O melhor mercado de comida de rua de Glasgow, agora na sua tela."}],
        # Cards de Destaque
        "t26_card_items": [
            {"img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600", "title": "COMIDA", "subtitle": "10+ VENDEDORES"},
            {"img": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600", "title": "BEBIDA", "subtitle": "CRAFT BEER & COCKTAILS"},
            {"img": "https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?w=600", "title": "EVENTOS", "subtitle": "MÚSICA AO VIVO"},
        ],
        # Seção Sobre (Impacto)
        "t26_about_titulos": [{"valor": "MAIS QUE UM MERCADO."}],
        "t26_about_descs": [{"valor": "A Dockyard Social foi criada para oferecer um espaço seguro e inclusivo para todos. Nós apoiamos talentos locais, reduzimos o desperdício e garantimos que a única coisa quente por aqui (além da comida) seja a hospitalidade."}],
        # Seção Reserva (CTA)
        "t26_cta_titulos": [{"valor": "PRONTO PARA VIVER A EXPERIÊNCIA?"}],
        "t26_cta_descs": [{"valor": "Garanta seu ingresso agora e venha fazer parte da melhor vibe de Glasgow."}],
        "t26_cta_btns": [{"texto": "RESERVAR AGORA", "url": "https://www.google.com/"}],
        # Footer
        "t26_foot_brand_names": [{"valor": "DOCKYARD."}],
        "t26_foot_addresses": [{"valor": "952 South St, Glasgow G14 0BX"}],
        "t26_foot_emails": [{"valor": "hello@dockyardsocial.com"}],
        "t26_foot_cols": [
            {
                "titulo": "REDES SOCIAIS",
                "links": [
                    {"texto": "INSTAGRAM", "url": "#"},
                    {"texto": "FACEBOOK", "url": "#"},
                    {"texto": "TIKTOK", "url": "#"}
                ]
            }
        ],
        "t26_foot_copys": [{"valor": "© 2026 DOCKYARD SOCIAL. SEMPRE REAL, NUNCA COPIADO."}],
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
            for i, cor in enumerate(st.session_state.t26_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t26_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t26_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t26_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t26_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t26_cores) > 1 and _del_btn(f"t26_cor_del_{i}"):
                        st.session_state.t26_cores.pop(i); st.rerun()
            if _add_btn("t26_cor_add", "＋ Adicionar cor"):
                st.session_state.t26_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # AVISO (ANNOUNCEMENT)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📢 Barra de Aviso</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t26_announcements):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t26_announcements[i]["valor"] = st.text_input("Texto do Aviso", item["valor"], key=f"t26_ann_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t26_announcements) > 1 and _del_btn(f"t26_ann_del_{i}"):
                        st.session_state.t26_announcements.pop(i); st.rerun()
            if _add_btn("t26_ann_add", "＋ Adicionar aviso"):
                st.session_state.t26_announcements.append({"valor": "NOVO AVISO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t26_nav_logos):
                st.session_state.t26_nav_logos[i]["valor"] = st.text_input("Logo/Nome Mercado", item["valor"], key=f"t26_nl_{i}")
            
            st.caption("Links do Menu")
            for i, link in enumerate(st.session_state.t26_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t26_nav_links[i]["texto"] = st.text_input("Texto", link["texto"], key=f"t26_nl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t26_nav_links[i]["url"] = st.text_input("URL", link["url"], key=f"t26_nl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t26_nav_links) > 1 and _del_btn(f"t26_nl_del_{i}"):
                        st.session_state.t26_nav_links.pop(i); st.rerun()
            if _add_btn("t26_nl_add", "＋ Adicionar link"):
                st.session_state.t26_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO SECTION
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🍔 Hero Section</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t26_hero_titulos):
                st.session_state.t26_hero_titulos[i]["valor"] = st.text_area("Título Hero (use <br>)", t["valor"], key=f"t26_h_t_{i}")
            for i, d in enumerate(st.session_state.t26_hero_descs):
                st.session_state.t26_hero_descs[i]["valor"] = st.text_area("Subtítulo Hero", d["valor"], key=f"t26_h_d_{i}")

            # ══════════════════════════════════════════════════════════════════
            # CARDS DE DESTAQUE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🃏 Cards de Destaque</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t26_card_items):
                with st.expander(f"Card {i+1}: {item['title']}"):
                    st.session_state.t26_card_items[i]["title"] = st.text_input("Título", item["title"], key=f"t26_ci_t_{i}")
                    st.session_state.t26_card_items[i]["subtitle"] = st.text_input("Subtítulo", item["subtitle"], key=f"t26_ci_s_{i}")
                    st.session_state.t26_card_items[i]["img"] = st.text_input("URL Imagem", item["img"], key=f"t26_ci_i_{i}")
                    if len(st.session_state.t26_card_items) > 1 and _del_btn(f"t26_ci_del_{i}", "Remover card"):
                        st.session_state.t26_card_items.pop(i); st.rerun()
            if _add_btn("t26_ci_add", "＋ Adicionar card"):
                st.session_state.t26_card_items.append({"img": "", "title": "NOVO", "subtitle": "DESCRIÇÃO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # SOBRE (IMPACTO)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📜 Seção Sobre</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t26_about_titulos):
                st.session_state.t26_about_titulos[i]["valor"] = st.text_input("Título Sobre", t["valor"], key=f"t26_at_{i}")
            for i, d in enumerate(st.session_state.t26_about_descs):
                st.session_state.t26_about_descs[i]["valor"] = st.text_area("Descrição Sobre", d["valor"], key=f"t26_ad_{i}")

            # ══════════════════════════════════════════════════════════════════
            # RESERVA (CTA)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📅 Seção de Reserva</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t26_cta_titulos):
                st.session_state.t26_cta_titulos[i]["valor"] = st.text_input("Título CTA", t["valor"], key=f"t26_ct_t_{i}")
            for i, d in enumerate(st.session_state.t26_cta_descs):
                st.session_state.t26_cta_descs[i]["valor"] = st.text_area("Descrição CTA", d["valor"], key=f"t26_ct_d_{i}")
            
            st.caption("Botões de Reserva")
            for i, btn in enumerate(st.session_state.t26_cta_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t26_cta_btns[i]["texto"] = st.text_input("Texto Botão", btn["texto"], key=f"t26_ct_b_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t26_cta_btns[i]["url"] = st.text_input("URL Botão", btn["url"], key=f"t26_ct_b_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t26_cta_btns) > 1 and _del_btn(f"t26_ct_b_del_{i}"):
                        st.session_state.t26_cta_btns.pop(i); st.rerun()
            if _add_btn("t26_ct_b_add", "＋ Adicionar botão"):
                st.session_state.t26_cta_btns.append({"texto": "RESERVAR", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)
            for i, name in enumerate(st.session_state.t26_foot_brand_names):
                st.session_state.t26_foot_brand_names[i]["valor"] = st.text_input("Nome Marca (Footer)", name["valor"], key=f"t26_fn_{i}")
            for i, addr in enumerate(st.session_state.t26_foot_addresses):
                st.session_state.t26_foot_addresses[i]["valor"] = st.text_input("Endereço", addr["valor"], key=f"t26_fa_{i}")
            for i, email in enumerate(st.session_state.t26_foot_emails):
                st.session_state.t26_foot_emails[i]["valor"] = st.text_input("Email", email["valor"], key=f"t26_fe_{i}")
            
            st.caption("Colunas de Links (Redes Sociais)")
            for i, col in enumerate(st.session_state.t26_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t26_foot_cols[i]["titulo"] = st.text_input("Título Coluna", col["titulo"], key=f"t26_fc_t_{i}")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1: st.session_state.t26_foot_cols[i]["links"][j]["texto"] = st.text_input("Texto", link["texto"], key=f"t26_fc_l_t_{i}_{j}", label_visibility="collapsed")
                        with c2: st.session_state.t26_foot_cols[i]["links"][j]["url"] = st.text_input("URL", link["url"], key=f"t26_fc_l_u_{i}_{j}", label_visibility="collapsed")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t26_fc_l_del_{i}_{j}"):
                                st.session_state.t26_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t26_fc_l_add_{i}", "＋ Adicionar link"):
                        st.session_state.t26_foot_cols[i]["links"].append({"texto": "LINK", "url": "#"}); st.rerun()
                    
                    if len(st.session_state.t26_foot_cols) > 1 and st.button("Remover Coluna Inteira", key=f"t26_fc_del_{i}"):
                        st.session_state.t26_foot_cols.pop(i); st.rerun()
            if _add_btn("t26_fc_add", "＋ Adicionar coluna"):
                st.session_state.t26_foot_cols.append({"titulo": "NOVA", "links": [{"texto": "Link", "url": "#"}]}); st.rerun()

            for i, copy in enumerate(st.session_state.t26_foot_copys):
                st.session_state.t26_foot_copys[i]["valor"] = st.text_input("Copyright", copy["valor"], key=f"t26_fcp_{i}")

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t13_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t13_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t26_obs_{i}", height=80,
                        placeholder="Ex: Usar uma paleta mais urbana...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t13_obs) > 1 and _del_btn(f"t26_obs_del_{i}"):
                        st.session_state.t13_obs.pop(i); st.rerun()
            if _add_btn("t26_obs_add", "＋ Adicionar observação"):
                st.session_state.t13_obs.append({"valor": ""}); st.rerun()

            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t26_send", type="primary"):
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
        page_icon="🍔",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
