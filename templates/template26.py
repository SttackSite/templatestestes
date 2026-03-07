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
        # ── CORES ───────────────────────────────────────────────────────────
        "t26_cores": [
            {"nome": "Principal (Amarelo Dock)", "valor": "#ffcc00"},
            {"nome": "Escura (Preto Dock)",      "valor": "#111111"},
            {"nome": "Fundo (Branco Dock)",       "valor": "#f4f4f4"},
        ],

        # ── AVISO (ANNOUNCEMENT) ─────────────────────────────────────────────
        "t26_announcements": [{"valor": "ABERTO NESTE FINAL DE SEMANA • GARANTA SEU INGRESSO"}],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t26_nav_logos": [{"valor": "DOCKYARD SOCIAL"}],
        "t26_nav_links": [
            {"texto": "O QUE ROLA", "url": "#oque-rola"},
            {"texto": "COMIDA",     "url": "#comida"},
            {"texto": "BEBIDA",     "url": "#bebida"},
            {"texto": "RESERVAR",   "url": "#reservar"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t26_hero_titulos": [{"valor": "COMIDA DE RUA.<br>BOAS VIBES.<br>PARA TODOS."}],
        "t26_hero_descs":   [{"valor": "O melhor mercado de comida de rua de Glasgow, agora na sua tela."}],

        # ── CARDS DE DESTAQUE ────────────────────────────────────────────────
        "t26_card_items": [
            {"img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600", "title": "COMIDA",  "subtitle": "10+ VENDEDORES"},
            {"img": "https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600", "title": "BEBIDA",  "subtitle": "CRAFT BEER & COCKTAILS"},
            {"img": "https://images.unsplash.com/photo-1501281668745-f7f57925c3b4?w=600", "title": "EVENTOS", "subtitle": "MÚSICA AO VIVO"},
        ],

        # ── SOBRE ───────────────────────────────────────────────────────────
        "t26_about_titulos": [{"valor": "MAIS QUE UM MERCADO."}],
        "t26_about_descs":   [{"valor": "A Dockyard Social foi criada para oferecer um espaço seguro e inclusivo para todos. Nós apoiamos talentos locais, reduzimos o desperdício e garantimos que a única coisa quente por aqui (além da comida) seja a hospitalidade."}],

        # ── CTA (RESERVA) ────────────────────────────────────────────────────
        "t26_cta_titulos": [{"valor": "PRONTO PARA VIVER A EXPERIÊNCIA?"}],
        "t26_cta_descs":   [{"valor": "Garanta seu ingresso agora e venha fazer parte da melhor vibe de Glasgow."}],
        "t26_cta_btns":    [{"texto": "RESERVAR AGORA", "url": "https://www.google.com/"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t26_foot_brand_names": [{"valor": "DOCKYARD."}],
        "t26_foot_addresses":   [{"valor": "952 South St, Glasgow G14 0BX"}],
        "t26_foot_emails":      [{"valor": "hello@dockyardsocial.com"}],
        "t26_foot_cols": [
            {"titulo": "REDES SOCIAIS", "links": [
                {"texto": "INSTAGRAM", "url": "#"},
                {"texto": "FACEBOOK",  "url": "#"},
                {"texto": "TIKTOK",    "url": "#"},
            ]},
        ],
        "t26_foot_copys": [{"valor": "© 2026 DOCKYARD SOCIAL. SEMPRE REAL, NUNCA COPIADO."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t26_obs": [{"valor": ""}],
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
                with c1:
                    st.session_state.t26_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t26_cor_n_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t26_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t26_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t26_cores) > 1 and _del_btn(f"t26_cor_del_{i}"):
                        st.session_state.t26_cores.pop(i); st.rerun()
            if _add_btn("t26_cor_add", "＋ Adicionar cor"):
                st.session_state.t26_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # AVISO (ANNOUNCEMENT)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📢 Barra de Aviso</div>', unsafe_allow_html=True)
            st.caption("Texto da faixa preta no topo da página")
            for i, item in enumerate(st.session_state.t26_announcements):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_announcements[i]["valor"] = st.text_input(
                        "Aviso", item["valor"], key=f"t26_ann_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t26_announcements) > 1 and _del_btn(f"t26_ann_del_{i}"):
                        st.session_state.t26_announcements.pop(i); st.rerun()
            if _add_btn("t26_ann_add", "＋ Adicionar aviso"):
                st.session_state.t26_announcements.append({"valor": "NOVO AVISO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome do mercado  *(lado esquerdo)*")
            for i, item in enumerate(st.session_state.t26_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_nav_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t26_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t26_nav_logos) > 1 and _del_btn(f"t26_logo_del_{i}"):
                        st.session_state.t26_nav_logos.pop(i); st.rerun()
            if _add_btn("t26_logo_add", "＋ Adicionar logo"):
                st.session_state.t26_nav_logos.append({"valor": "MERCADO"}); st.rerun()

            st.caption("Links do menu  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t26_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t26_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t26_nl_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t26_nav_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t26_nl_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t26_nav_links) > 1 and _del_btn(f"t26_nl_del_{i}"):
                        st.session_state.t26_nav_links.pop(i); st.rerun()
            if _add_btn("t26_nl_add", "＋ Adicionar link"):
                st.session_state.t26_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🍔 Hero Section</div>', unsafe_allow_html=True)

            st.caption("Título principal  *(use <br> para quebrar linha)*")
            for i, t in enumerate(st.session_state.t26_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t26_h_t_{i}", height=90, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t26_hero_titulos) > 1 and _del_btn(f"t26_h_t_del_{i}"):
                        st.session_state.t26_hero_titulos.pop(i); st.rerun()
            if _add_btn("t26_h_t_add", "＋ Adicionar título"):
                st.session_state.t26_hero_titulos.append({"valor": "NOVO TÍTULO."}); st.rerun()

            st.caption("Subtítulo")
            for i, d in enumerate(st.session_state.t26_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_hero_descs[i]["valor"] = st.text_area(
                        "Subtítulo", d["valor"], key=f"t26_h_d_{i}", height=70, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t26_hero_descs) > 1 and _del_btn(f"t26_h_d_del_{i}"):
                        st.session_state.t26_hero_descs.pop(i); st.rerun()
            if _add_btn("t26_h_d_add", "＋ Adicionar subtítulo"):
                st.session_state.t26_hero_descs.append({"valor": "Novo subtítulo."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # CARDS DE DESTAQUE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🃏 Cards de Destaque</div>', unsafe_allow_html=True)
            st.caption("Cards principais  *(Título | Subtítulo | Imagem)*")
            for i, item in enumerate(st.session_state.t26_card_items):
                with st.expander(f"Card {i+1}: {item['title']}"):
                    st.session_state.t26_card_items[i]["title"] = st.text_input(
                        "Título", item["title"], key=f"t26_ci_t_{i}")
                    st.session_state.t26_card_items[i]["subtitle"] = st.text_input(
                        "Subtítulo", item["subtitle"], key=f"t26_ci_s_{i}")
                    st.session_state.t26_card_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t26_ci_i_{i}")
                    if len(st.session_state.t26_card_items) > 1:
                        if st.button("🗑 Remover este card", key=f"t26_ci_del_{i}"):
                            st.session_state.t26_card_items.pop(i); st.rerun()
            if _add_btn("t26_ci_add", "＋ Adicionar card"):
                st.session_state.t26_card_items.append({
                    "img": "", "title": "NOVO", "subtitle": "DESCRIÇÃO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # SOBRE (IMPACTO)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📜 Seção Sobre</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, t in enumerate(st.session_state.t26_about_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_about_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t26_at_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t26_about_titulos) > 1 and _del_btn(f"t26_at_del_{i}"):
                        st.session_state.t26_about_titulos.pop(i); st.rerun()
            if _add_btn("t26_at_add", "＋ Adicionar título"):
                st.session_state.t26_about_titulos.append({"valor": "NOVO TÍTULO."}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t26_about_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_about_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t26_ad_{i}", height=100, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t26_about_descs) > 1 and _del_btn(f"t26_ad_del_{i}"):
                        st.session_state.t26_about_descs.pop(i); st.rerun()
            if _add_btn("t26_ad_add", "＋ Adicionar descrição"):
                st.session_state.t26_about_descs.append({"valor": "Nova descrição."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # CTA (RESERVA)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📅 Seção de Reserva</div>', unsafe_allow_html=True)

            st.caption("Título CTA")
            for i, t in enumerate(st.session_state.t26_cta_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_cta_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t26_ct_t_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t26_cta_titulos) > 1 and _del_btn(f"t26_ct_t_del_{i}"):
                        st.session_state.t26_cta_titulos.pop(i); st.rerun()
            if _add_btn("t26_ct_t_add", "＋ Adicionar título"):
                st.session_state.t26_cta_titulos.append({"valor": "NOVO TÍTULO?"}); st.rerun()

            st.caption("Descrição CTA")
            for i, d in enumerate(st.session_state.t26_cta_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_cta_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t26_ct_d_{i}", height=70, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t26_cta_descs) > 1 and _del_btn(f"t26_ct_d_del_{i}"):
                        st.session_state.t26_cta_descs.pop(i); st.rerun()
            if _add_btn("t26_ct_d_add", "＋ Adicionar descrição"):
                st.session_state.t26_cta_descs.append({"valor": "Nova descrição."}); st.rerun()

            st.caption("Botões de reserva  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t26_cta_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t26_cta_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t26_ct_b_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t26_cta_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t26_ct_b_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t26_cta_btns) > 1 and _del_btn(f"t26_ct_b_del_{i}"):
                        st.session_state.t26_cta_btns.pop(i); st.rerun()
            if _add_btn("t26_ct_b_add", "＋ Adicionar botão"):
                st.session_state.t26_cta_btns.append({"texto": "RESERVAR", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Nome da marca")
            for i, name in enumerate(st.session_state.t26_foot_brand_names):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_foot_brand_names[i]["valor"] = st.text_input(
                        "Nome", name["valor"], key=f"t26_fn_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t26_foot_brand_names) > 1 and _del_btn(f"t26_fn_del_{i}"):
                        st.session_state.t26_foot_brand_names.pop(i); st.rerun()
            if _add_btn("t26_fn_add", "＋ Adicionar nome"):
                st.session_state.t26_foot_brand_names.append({"valor": "MERCADO."}); st.rerun()

            st.caption("Endereço")
            for i, addr in enumerate(st.session_state.t26_foot_addresses):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_foot_addresses[i]["valor"] = st.text_input(
                        "Endereço", addr["valor"], key=f"t26_fa_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t26_foot_addresses) > 1 and _del_btn(f"t26_fa_del_{i}"):
                        st.session_state.t26_foot_addresses.pop(i); st.rerun()
            if _add_btn("t26_fa_add", "＋ Adicionar endereço"):
                st.session_state.t26_foot_addresses.append({"valor": "Rua, Cidade"}); st.rerun()

            st.caption("Email de contato")
            for i, email in enumerate(st.session_state.t26_foot_emails):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_foot_emails[i]["valor"] = st.text_input(
                        "Email", email["valor"], key=f"t26_fe_{i}", label_visibility="collapsed", placeholder="email@mercado.com")
                with c2:
                    if len(st.session_state.t26_foot_emails) > 1 and _del_btn(f"t26_fe_del_{i}"):
                        st.session_state.t26_foot_emails.pop(i); st.rerun()
            if _add_btn("t26_fe_add", "＋ Adicionar email"):
                st.session_state.t26_foot_emails.append({"valor": "email@mercado.com"}); st.rerun()

            st.caption("Colunas de links  *(redes sociais)*")
            for i, col in enumerate(st.session_state.t26_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t26_foot_cols[i]["titulo"] = st.text_input(
                        "Título Coluna", col["titulo"], key=f"t26_fc_t_{i}")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1:
                            st.session_state.t26_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t26_fc_l_t_{i}_{j}", label_visibility="collapsed")
                        with c2:
                            st.session_state.t26_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t26_fc_l_u_{i}_{j}", label_visibility="collapsed")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t26_fc_l_del_{i}_{j}"):
                                st.session_state.t26_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t26_fc_l_add_{i}", "＋ Adicionar link"):
                        st.session_state.t26_foot_cols[i]["links"].append({"texto": "LINK", "url": "#"}); st.rerun()
                    if len(st.session_state.t26_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t26_fc_del_{i}"):
                            st.session_state.t26_foot_cols.pop(i); st.rerun()
            if _add_btn("t26_fc_add", "＋ Adicionar coluna"):
                st.session_state.t26_foot_cols.append({"titulo": "NOVA", "links": [{"texto": "Link", "url": "#"}]}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t26_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t26_fcp_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t26_foot_copys) > 1 and _del_btn(f"t26_fcp_del_{i}"):
                        st.session_state.t26_foot_copys.pop(i); st.rerun()
            if _add_btn("t26_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t26_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t26_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t26_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t26_obs_{i}", height=80,
                        placeholder="Ex: Usar uma paleta mais urbana...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t26_obs) > 1 and _del_btn(f"t26_obs_del_{i}"):
                        st.session_state.t26_obs.pop(i); st.rerun()
            if _add_btn("t26_obs_add", "＋ Adicionar observação"):
                st.session_state.t26_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ENVIAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t26_send", type="primary"):
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
        page_icon="🍔",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
