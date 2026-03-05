import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img11.png"
TEMPLATE_NAME = "Template 11 — Pura Vida Brackets (E-commerce & Estilo de Vida)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── CORES ───────────────────────────────────────────────────────────
        "t11_cores": [
            {"nome": "Cor de Anúncio (Rosa)",      "valor": "#ffb6c1"},
            {"nome": "Cor de Preço (Rosa Quente)",  "valor": "#ff69b4"},
            {"nome": "Cor de Texto (Escuro)",       "valor": "#333333"},
            {"nome": "Cor de Fundo (Light)",        "valor": "#f9f9f9"},
        ],

        # ── BARRA DE ANÚNCIO ─────────────────────────────────────────────────
        "t11_announcements": [{"valor": "FRETE GRÁTIS EM PEDIDOS ACIMA DE R$ 150! 🌴"}],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t11_logos": [{"valor": "Pura Vida"}],
        "t11_nav_links": [
            {"texto": "Pulseiras", "url": "#bracelets"},
            {"texto": "Joias",     "url": "#jewelry"},
            {"texto": "Coleções",  "url": "#collections"},
            {"texto": "Sale",      "url": "#sale"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t11_hero_imgs":    [{"valor": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1500&q=80"}],
        "t11_hero_titulos": [{"valor": "VIVA O MOMENTO"}],
        "t11_hero_descs":   [{"valor": "Nossas peças são feitas à mão por artesãos ao redor do mundo, espalhando a energia \"Pura Vida\"."}],

        # ── PRODUTOS ────────────────────────────────────────────────────────
        "t11_prod_secao_titulos": [{"valor": "Novidades"}],
        "t11_prod_items": [
            {"nome": "Pack Shoreline", "preco": "45,00", "img": "https://images.unsplash.com/photo-1611591437281-460bfbe1220a?auto=format&fit=crop&w=400&q=80", "btn_txt": "Adicionar", "url": "https://www.google.com/"},
            {"nome": "Ocean Blue",     "preco": "32,00", "img": "https://images.unsplash.com/photo-1573408301185-9146fe634ad0?auto=format&fit=crop&w=400&q=80", "btn_txt": "Adicionar", "url": "https://www.google.com/"},
            {"nome": "Sunset Vibes",   "preco": "38,00", "img": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?auto=format&fit=crop&w=400&q=80", "btn_txt": "Adicionar", "url": "https://www.google.com/"},
            {"nome": "Sand & Salt",    "preco": "29,00", "img": "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?auto=format&fit=crop&w=400&q=80", "btn_txt": "Adicionar", "url": "https://www.google.com/"},
        ],

        # ── IMPACTO SOCIAL ───────────────────────────────────────────────────
        "t11_imp_imgs":    [{"valor": "https://images.unsplash.com/photo-1484820540004-14229fe36ca4?auto=format&fit=crop&w=800&q=80"}],
        "t11_imp_titulos": [{"valor": "Retribuindo ao Planeta"}],
        "t11_imp_descs":   [{"valor": "Cada compra ajuda a apoiar causas ambientais e artesãos locais. Já doamos mais de R$ 4 milhões para instituições de caridade através de vocês."}],
        "t11_imp_btns":    [{"texto": "Saiba Mais", "url": "https://www.google.com/"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t11_foot_logos":   [{"valor": "Pura Vida"}],
        "t11_foot_copys":   [{"valor": "© 2026 Pura Vida Brackets. Siga-nos no Instagram @puravida"}],
        "t11_foot_sociais": [{"texto": "@puravida", "url": "https://www.google.com/"}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t11_obs": [{"valor": ""}],
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
            for i, cor in enumerate(st.session_state.t11_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t11_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t11_cor_n_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t11_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t11_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t11_cores) > 1 and _del_btn(f"t11_cor_del_{i}"):
                        st.session_state.t11_cores.pop(i); st.rerun()
            if _add_btn("t11_cor_add", "＋ Adicionar cor"):
                st.session_state.t11_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # BARRA DE ANÚNCIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📢 Barra de Anúncio</div>', unsafe_allow_html=True)
            st.caption("Texto exibido na faixa rosa do topo")
            for i, ann in enumerate(st.session_state.t11_announcements):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_announcements[i]["valor"] = st.text_input(
                        "Anúncio", ann["valor"], key=f"t11_ann_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t11_announcements) > 1 and _del_btn(f"t11_ann_del_{i}"):
                        st.session_state.t11_announcements.pop(i); st.rerun()
            if _add_btn("t11_ann_add", "＋ Adicionar anúncio"):
                st.session_state.t11_announcements.append({"valor": "NOVO ANÚNCIO 🌴"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Logo e Navegação</div>', unsafe_allow_html=True)

            st.caption("Nome da marca  *(exibido em fonte cursiva)*")
            for i, logo in enumerate(st.session_state.t11_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_logos[i]["valor"] = st.text_input(
                        "Marca", logo["valor"], key=f"t11_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t11_logos) > 1 and _del_btn(f"t11_logo_del_{i}"):
                        st.session_state.t11_logos.pop(i); st.rerun()
            if _add_btn("t11_logo_add", "＋ Adicionar logo"):
                st.session_state.t11_logos.append({"valor": "Nova Marca"}); st.rerun()

            st.caption("Links do menu  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t11_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t11_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t11_nl_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t11_nav_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t11_nl_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t11_nav_links) > 1 and _del_btn(f"t11_nl_del_{i}"):
                        st.session_state.t11_nav_links.pop(i); st.rerun()
            if _add_btn("t11_nl_add", "＋ Adicionar link ao menu"):
                st.session_state.t11_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌴 Hero Banner</div>', unsafe_allow_html=True)

            st.caption("Imagem de fundo  *(URL da foto)*")
            for i, img in enumerate(st.session_state.t11_hero_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_hero_imgs[i]["valor"] = st.text_input(
                        "Imagem Hero", img["valor"], key=f"t11_h_i_{i}", label_visibility="collapsed",
                        placeholder="https://...")
                with c2:
                    if len(st.session_state.t11_hero_imgs) > 1 and _del_btn(f"t11_h_i_del_{i}"):
                        st.session_state.t11_hero_imgs.pop(i); st.rerun()
            if _add_btn("t11_h_i_add", "＋ Adicionar imagem hero"):
                st.session_state.t11_hero_imgs.append({"valor": "https://"}); st.rerun()

            st.caption("Título principal")
            for i, t in enumerate(st.session_state.t11_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_hero_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t11_h_t_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t11_hero_titulos) > 1 and _del_btn(f"t11_h_t_del_{i}"):
                        st.session_state.t11_hero_titulos.pop(i); st.rerun()
            if _add_btn("t11_h_t_add", "＋ Adicionar título"):
                st.session_state.t11_hero_titulos.append({"valor": "NOVO TÍTULO"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t11_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t11_h_d_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t11_hero_descs) > 1 and _del_btn(f"t11_h_d_del_{i}"):
                        st.session_state.t11_hero_descs.pop(i); st.rerun()
            if _add_btn("t11_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t11_hero_descs.append({"valor": "Nova descrição"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # PRODUTOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🛍️ Vitrine de Produtos</div>', unsafe_allow_html=True)

            st.caption("Título da vitrine")
            for i, t in enumerate(st.session_state.t11_prod_secao_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_prod_secao_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t11_pst_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t11_prod_secao_titulos) > 1 and _del_btn(f"t11_pst_del_{i}"):
                        st.session_state.t11_prod_secao_titulos.pop(i); st.rerun()
            if _add_btn("t11_pst_add", "＋ Adicionar título de vitrine"):
                st.session_state.t11_prod_secao_titulos.append({"valor": "Nova Seção"}); st.rerun()

            st.caption("Cards de produto  *(Nome | Preço | Imagem | Botão | URL)*")
            for i, item in enumerate(st.session_state.t11_prod_items):
                with st.expander(f"Produto {i+1}: {item['nome']}"):
                    st.session_state.t11_prod_items[i]["nome"] = st.text_input(
                        "Nome do Produto", item["nome"], key=f"t11_pi_n_{i}")
                    st.session_state.t11_prod_items[i]["preco"] = st.text_input(
                        "Preço  (ex: 45,00)", item["preco"], key=f"t11_pi_p_{i}")
                    st.session_state.t11_prod_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t11_pi_i_{i}")
                    st.session_state.t11_prod_items[i]["btn_txt"] = st.text_input(
                        "Texto do Botão", item["btn_txt"], key=f"t11_pi_bt_{i}")
                    st.session_state.t11_prod_items[i]["url"] = st.text_input(
                        "URL do Botão", item["url"], key=f"t11_pi_u_{i}")
                    if len(st.session_state.t11_prod_items) > 1:
                        if st.button("🗑 Remover este produto", key=f"t11_pi_del_{i}"):
                            st.session_state.t11_prod_items.pop(i); st.rerun()
            if _add_btn("t11_pi_add", "＋ Adicionar produto"):
                st.session_state.t11_prod_items.append({
                    "nome": "Novo Produto", "preco": "0,00",
                    "img": "", "btn_txt": "Adicionar", "url": "#"
                }); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # IMPACTO SOCIAL
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌍 Impacto Social</div>', unsafe_allow_html=True)

            st.caption("Imagem  *(URL da foto ao lado do texto)*")
            for i, img in enumerate(st.session_state.t11_imp_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_imp_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t11_is_i_{i}", label_visibility="collapsed",
                        placeholder="https://...")
                with c2:
                    if len(st.session_state.t11_imp_imgs) > 1 and _del_btn(f"t11_is_i_del_{i}"):
                        st.session_state.t11_imp_imgs.pop(i); st.rerun()
            if _add_btn("t11_is_i_add", "＋ Adicionar imagem"):
                st.session_state.t11_imp_imgs.append({"valor": "https://"}); st.rerun()

            st.caption("Título")
            for i, t in enumerate(st.session_state.t11_imp_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_imp_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t11_is_t_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t11_imp_titulos) > 1 and _del_btn(f"t11_is_t_del_{i}"):
                        st.session_state.t11_imp_titulos.pop(i); st.rerun()
            if _add_btn("t11_is_t_add", "＋ Adicionar título"):
                st.session_state.t11_imp_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t11_imp_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_imp_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t11_is_d_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t11_imp_descs) > 1 and _del_btn(f"t11_is_d_del_{i}"):
                        st.session_state.t11_imp_descs.pop(i); st.rerun()
            if _add_btn("t11_is_d_add", "＋ Adicionar descrição"):
                st.session_state.t11_imp_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Botão  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t11_imp_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t11_imp_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t11_isb_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t11_imp_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t11_isb_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t11_imp_btns) > 1 and _del_btn(f"t11_isb_del_{i}"):
                        st.session_state.t11_imp_btns.pop(i); st.rerun()
            if _add_btn("t11_isb_add", "＋ Adicionar botão"):
                st.session_state.t11_imp_btns.append({"texto": "Saiba Mais", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Logo do rodapé  *(exibido em fonte cursiva)*")
            for i, logo in enumerate(st.session_state.t11_foot_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_foot_logos[i]["valor"] = st.text_input(
                        "Logo Footer", logo["valor"], key=f"t11_fl_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t11_foot_logos) > 1 and _del_btn(f"t11_fl_del_{i}"):
                        st.session_state.t11_foot_logos.pop(i); st.rerun()
            if _add_btn("t11_fl_add", "＋ Adicionar logo ao rodapé"):
                st.session_state.t11_foot_logos.append({"valor": "Nova Marca"}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t11_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t11_fcp_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t11_foot_copys) > 1 and _del_btn(f"t11_fcp_del_{i}"):
                        st.session_state.t11_foot_copys.pop(i); st.rerun()
            if _add_btn("t11_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t11_foot_copys.append({"valor": "© 2026"}); st.rerun()

            st.caption("Redes sociais  *(Texto | URL)*")
            for i, soc in enumerate(st.session_state.t11_foot_sociais):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t11_foot_sociais[i]["texto"] = st.text_input(
                        "Rede", soc["texto"], key=f"t11_fs_t_{i}", label_visibility="collapsed", placeholder="@perfil")
                with c2:
                    st.session_state.t11_foot_sociais[i]["url"] = st.text_input(
                        "URL", soc["url"], key=f"t11_fs_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t11_foot_sociais) > 1 and _del_btn(f"t11_fs_del_{i}"):
                        st.session_state.t11_foot_sociais.pop(i); st.rerun()
            if _add_btn("t11_fs_add", "＋ Adicionar rede social"):
                st.session_state.t11_foot_sociais.append({"texto": "@perfil", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t11_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t11_obs_{i}", height=80,
                        placeholder="Ex: Alterar a fonte cursiva para uma mais moderna...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t11_obs) > 1 and _del_btn(f"t11_obs_del_{i}"):
                        st.session_state.t11_obs.pop(i); st.rerun()
            if _add_btn("t11_obs_add", "＋ Adicionar observação"):
                st.session_state.t11_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ENVIAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t11_send", type="primary"):
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
        page_icon="✏️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
