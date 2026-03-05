import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img10.png"
TEMPLATE_NAME = "Template 10 — GetResponse Style (Marketing & Automação)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── CORES ───────────────────────────────────────────────────────────
        "t10_cores": [
            {"nome": "Cor Principal (Azul)",     "valor": "#0066FF"},
            {"nome": "Cor de Destaque (Amarelo)", "valor": "#FFD60A"},
            {"nome": "Cor Escura (Texto)",        "valor": "#1a1a1a"},
            {"nome": "Cor de Fundo (Branco)",     "valor": "#ffffff"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t10_logos": [{"valor": "GetResponse"}],
        "t10_nav_links": [
            {"texto": "Produto",  "url": "#produto"},
            {"texto": "Recursos", "url": "#recursos"},
            {"texto": "Preços",   "url": "#precos"},
            {"texto": "Sobre",    "url": "#sobre"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t10_hero_labels":  [{"valor": "Email Marketing & Automação"}],
        "t10_hero_titulos": [{"valor": "Não é você, é o algoritmo"}],
        "t10_hero_descs":   [{"valor": "Plataforma de email marketing, automação e landing pages com IA integrada. Crie, teste e venda mais rápido."}],
        "t10_hero_visuals": [{"valor": "📧"}],
        "t10_hero_btns": [
            {"texto": "Comece Grátis", "url": "https://www.google.com/", "tipo": "Primário"},
            {"texto": "Saiba Mais",    "url": "https://www.google.com/", "tipo": "Secundário"},
        ],

        # ── ESTATÍSTICAS ────────────────────────────────────────────────────
        "t10_stats": [
            {"valor": "99%",   "label": "Taxa de Entregabilidade para 160+ países"},
            {"valor": "+150",  "label": "Integrações Disponíveis"},
            {"valor": "350K+", "label": "Clientes ao Redor do Mundo"},
            {"valor": "24/7",  "label": "Suporte de Sucesso do Cliente"},
        ],

        # ── FEATURES ────────────────────────────────────────────────────────
        "t10_feat_titulos": [{"valor": "Ferramentas Poderosas para Seu Negócio"}],
        "t10_feat_cards": [
            {"icon": "📧", "titulo": "Email Marketing", "desc": "Envie newsletters ilimitadas com IA que cria linhas de assunto e personaliza conteúdo para seu público."},
            {"icon": "🤖", "titulo": "Automação com IA", "desc": "Crie jornadas automáticas que identificam o melhor momento para contatar seus clientes."},
            {"icon": "🌐", "titulo": "Landing Pages",   "desc": "Publique landing pages ilimitadas com IA que escreve o texto e escolhe o layout ideal."},
        ],

        # ── DEPOIMENTO ──────────────────────────────────────────────────────
        "t10_test_texts":   [{"valor": "\"Geramos US$ 43.000 em vendas com apenas 10 e-mails usando a GetResponse. A automação e a IA mudaram nosso negócio.\""}],
        "t10_test_authors": [{"valor": "João Silva - CEO da Tech Company"}],

        # ── CTA ─────────────────────────────────────────────────────────────
        "t10_cta_titulos":      [{"valor": "Junte-se a 350.000+ Empresas"}],
        "t10_cta_placeholders": [{"valor": "Seu endereço de e-mail"}],
        "t10_cta_btns":         [{"texto": "Começar Grátis", "url": "https://www.google.com/"}],
        "t10_cta_notes":        [{"valor": "Teste gratuito de 14 dias | Não precisa de cartão | Cancele a qualquer momento"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t10_foot_cols": [
            {"titulo": "Produto",  "links": [{"texto": "Email Marketing", "url": "https://www.google.com/"}, {"texto": "Automação", "url": "https://www.google.com/"}, {"texto": "Landing Pages", "url": "https://www.google.com/"}, {"texto": "Formulários", "url": "https://www.google.com/"}]},
            {"titulo": "Recursos", "links": [{"texto": "Blog", "url": "https://www.google.com/"}, {"texto": "Webinars", "url": "https://www.google.com/"}, {"texto": "Templates", "url": "https://www.google.com/"}, {"texto": "Integrações", "url": "https://www.google.com/"}]},
            {"titulo": "Empresa",  "links": [{"texto": "Sobre Nós", "url": "https://www.google.com/"}, {"texto": "Carreiras", "url": "https://www.google.com/"}, {"texto": "Imprensa", "url": "https://www.google.com/"}, {"texto": "Contato", "url": "https://www.google.com/"}]},
            {"titulo": "Legal",    "links": [{"texto": "Privacidade", "url": "https://www.google.com/"}, {"texto": "Termos", "url": "https://www.google.com/"}, {"texto": "Cookies", "url": "https://www.google.com/"}, {"texto": "Suporte", "url": "https://www.google.com/"}]},
        ],
        "t10_foot_copys": [{"valor": "© 2026 GetResponse. Todos os direitos reservados."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t10_obs": [{"valor": ""}],
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
            for i, cor in enumerate(st.session_state.t10_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t10_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t10_cor_n_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t10_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t10_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t10_cores) > 1 and _del_btn(f"t10_cor_del_{i}"):
                        st.session_state.t10_cores.pop(i); st.rerun()
            if _add_btn("t10_cor_add", "＋ Adicionar cor"):
                st.session_state.t10_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca")
            for i, logo in enumerate(st.session_state.t10_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_logos[i]["valor"] = st.text_input(
                        "Logo", logo["valor"], key=f"t10_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t10_logos) > 1 and _del_btn(f"t10_logo_del_{i}"):
                        st.session_state.t10_logos.pop(i); st.rerun()
            if _add_btn("t10_logo_add", "＋ Adicionar logo"):
                st.session_state.t10_logos.append({"valor": "NOVA LOGO"}); st.rerun()

            st.caption("Links do menu  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t10_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t10_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t10_nl_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t10_nav_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t10_nl_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t10_nav_links) > 1 and _del_btn(f"t10_nl_del_{i}"):
                        st.session_state.t10_nav_links.pop(i); st.rerun()
            if _add_btn("t10_nl_add", "＋ Adicionar link ao menu"):
                st.session_state.t10_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📧 Hero (Marketing)</div>', unsafe_allow_html=True)

            st.caption("Label  *(texto pequeno acima do título)*")
            for i, label in enumerate(st.session_state.t10_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_hero_labels[i]["valor"] = st.text_input(
                        "Label", label["valor"], key=f"t10_h_l_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t10_hero_labels) > 1 and _del_btn(f"t10_h_l_del_{i}"):
                        st.session_state.t10_hero_labels.pop(i); st.rerun()
            if _add_btn("t10_h_l_add", "＋ Adicionar label"):
                st.session_state.t10_hero_labels.append({"valor": "Novo Label"}); st.rerun()

            st.caption("Título principal")
            for i, t in enumerate(st.session_state.t10_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t10_h_t_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t10_hero_titulos) > 1 and _del_btn(f"t10_h_t_del_{i}"):
                        st.session_state.t10_hero_titulos.pop(i); st.rerun()
            if _add_btn("t10_h_t_add", "＋ Adicionar título"):
                st.session_state.t10_hero_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t10_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t10_h_d_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t10_hero_descs) > 1 and _del_btn(f"t10_h_d_del_{i}"):
                        st.session_state.t10_hero_descs.pop(i); st.rerun()
            if _add_btn("t10_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t10_hero_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Emoji visual  *(círculo decorativo à direita do hero)*")
            for i, v in enumerate(st.session_state.t10_hero_visuals):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_hero_visuals[i]["valor"] = st.text_input(
                        "Emoji Visual", v["valor"], key=f"t10_h_v_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t10_hero_visuals) > 1 and _del_btn(f"t10_h_v_del_{i}"):
                        st.session_state.t10_hero_visuals.pop(i); st.rerun()
            if _add_btn("t10_h_v_add", "＋ Adicionar emoji visual"):
                st.session_state.t10_hero_visuals.append({"valor": "🚀"}); st.rerun()

            st.caption("Botões do Hero  *(Texto | URL | Tipo)*")
            for i, btn in enumerate(st.session_state.t10_hero_btns):
                with st.expander(f"Botão {i+1}: {btn['texto']}"):
                    st.session_state.t10_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t10_hb_t_{i}")
                    st.session_state.t10_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t10_hb_u_{i}")
                    st.session_state.t10_hero_btns[i]["tipo"] = st.selectbox(
                        "Tipo", ["Primário", "Secundário"],
                        index=0 if btn["tipo"] == "Primário" else 1,
                        key=f"t10_hb_tp_{i}")
                    if len(st.session_state.t10_hero_btns) > 1:
                        if st.button("🗑 Remover este botão", key=f"t10_hb_del_{i}"):
                            st.session_state.t10_hero_btns.pop(i); st.rerun()
            if _add_btn("t10_hb_add", "＋ Adicionar botão ao hero"):
                st.session_state.t10_hero_btns.append({"texto": "NOVO BOTÃO", "url": "#", "tipo": "Primário"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ESTATÍSTICAS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Estatísticas Globais</div>', unsafe_allow_html=True)
            st.caption("Valor | Descrição")
            for i, stat in enumerate(st.session_state.t10_stats):
                c1, c2, c3 = st.columns([3, 5, 1])
                with c1:
                    st.session_state.t10_stats[i]["valor"] = st.text_input(
                        "Valor", stat["valor"], key=f"t10_st_v_{i}", label_visibility="collapsed", placeholder="Ex: 99%")
                with c2:
                    st.session_state.t10_stats[i]["label"] = st.text_input(
                        "Rótulo", stat["label"], key=f"t10_st_l_{i}", label_visibility="collapsed", placeholder="Descrição")
                with c3:
                    if len(st.session_state.t10_stats) > 1 and _del_btn(f"t10_st_del_{i}"):
                        st.session_state.t10_stats.pop(i); st.rerun()
            if _add_btn("t10_st_add", "＋ Adicionar estatística"):
                st.session_state.t10_stats.append({"valor": "0", "label": "Novo Dado"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FEATURES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🛠️ Ferramentas Poderosas</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t10_feat_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_feat_titulos[i]["valor"] = st.text_input(
                        "Título Seção", t["valor"], key=f"t10_featt_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t10_feat_titulos) > 1 and _del_btn(f"t10_featt_del_{i}"):
                        st.session_state.t10_feat_titulos.pop(i); st.rerun()
            if _add_btn("t10_featt_add", "＋ Adicionar título de seção"):
                st.session_state.t10_feat_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Cards de funcionalidade  *(Emoji | Título | Descrição)*")
            for i, card in enumerate(st.session_state.t10_feat_cards):
                with st.expander(f"Feature {i+1}: {card['titulo']}"):
                    st.session_state.t10_feat_cards[i]["icon"] = st.text_input(
                        "Emoji Ícone", card["icon"], key=f"t10_fcard_i_{i}")
                    st.session_state.t10_feat_cards[i]["titulo"] = st.text_input(
                        "Título", card["titulo"], key=f"t10_fcard_t_{i}")
                    st.session_state.t10_feat_cards[i]["desc"] = st.text_area(
                        "Descrição", card["desc"], key=f"t10_fcard_d_{i}", height=80)
                    if len(st.session_state.t10_feat_cards) > 1:
                        if st.button("🗑 Remover esta feature", key=f"t10_fcard_del_{i}"):
                            st.session_state.t10_feat_cards.pop(i); st.rerun()
            if _add_btn("t10_fcard_add", "＋ Adicionar funcionalidade"):
                st.session_state.t10_feat_cards.append({"icon": "🚀", "titulo": "Nova Feature", "desc": "Descrição da feature."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # DEPOIMENTO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💬 Prova Social (Depoimento)</div>', unsafe_allow_html=True)

            st.caption("Texto do depoimento")
            for i, text in enumerate(st.session_state.t10_test_texts):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_test_texts[i]["valor"] = st.text_area(
                        "Depoimento", text["valor"], key=f"t10_tt_{i}", height=90, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t10_test_texts) > 1 and _del_btn(f"t10_tt_del_{i}"):
                        st.session_state.t10_test_texts.pop(i); st.rerun()
            if _add_btn("t10_tt_add", "＋ Adicionar depoimento"):
                st.session_state.t10_test_texts.append({"valor": "\"Novo depoimento.\""}); st.rerun()

            st.caption("Autor e cargo")
            for i, author in enumerate(st.session_state.t10_test_authors):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_test_authors[i]["valor"] = st.text_input(
                        "Autor", author["valor"], key=f"t10_ta_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t10_test_authors) > 1 and _del_btn(f"t10_ta_del_{i}"):
                        st.session_state.t10_test_authors.pop(i); st.rerun()
            if _add_btn("t10_ta_add", "＋ Adicionar autor"):
                st.session_state.t10_test_authors.append({"valor": "Nome - Cargo"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # CTA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📢 Chamada para Ação (CTA)</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, t in enumerate(st.session_state.t10_cta_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_cta_titulos[i]["valor"] = st.text_input(
                        "Título CTA", t["valor"], key=f"t10_ctat_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t10_cta_titulos) > 1 and _del_btn(f"t10_ctat_del_{i}"):
                        st.session_state.t10_cta_titulos.pop(i); st.rerun()
            if _add_btn("t10_ctat_add", "＋ Adicionar título CTA"):
                st.session_state.t10_cta_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Placeholder do campo de email")
            for i, p in enumerate(st.session_state.t10_cta_placeholders):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_cta_placeholders[i]["valor"] = st.text_input(
                        "Placeholder", p["valor"], key=f"t10_ctap_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t10_cta_placeholders) > 1 and _del_btn(f"t10_ctap_del_{i}"):
                        st.session_state.t10_cta_placeholders.pop(i); st.rerun()
            if _add_btn("t10_ctap_add", "＋ Adicionar placeholder"):
                st.session_state.t10_cta_placeholders.append({"valor": "Seu e-mail"}); st.rerun()

            st.caption("Botão  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t10_cta_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t10_cta_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t10_ctab_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t10_cta_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t10_ctab_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t10_cta_btns) > 1 and _del_btn(f"t10_ctab_del_{i}"):
                        st.session_state.t10_cta_btns.pop(i); st.rerun()
            if _add_btn("t10_ctab_add", "＋ Adicionar botão CTA"):
                st.session_state.t10_cta_btns.append({"texto": "Novo Botão", "url": "#"}); st.rerun()

            st.caption("Nota de rodapé  *(ex: termos do teste grátis)*")
            for i, n in enumerate(st.session_state.t10_cta_notes):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_cta_notes[i]["valor"] = st.text_input(
                        "Nota", n["valor"], key=f"t10_ctan_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t10_cta_notes) > 1 and _del_btn(f"t10_ctan_del_{i}"):
                        st.session_state.t10_cta_notes.pop(i); st.rerun()
            if _add_btn("t10_ctan_add", "＋ Adicionar nota"):
                st.session_state.t10_cta_notes.append({"valor": "Nova nota"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé Dinâmico</div>', unsafe_allow_html=True)

            st.caption("Colunas do rodapé  *(Título | Links)*")
            for i, col in enumerate(st.session_state.t10_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t10_foot_cols[i]["titulo"] = st.text_input(
                        "Título da Coluna", col["titulo"], key=f"t10_fcol_ti_{i}")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1:
                            st.session_state.t10_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t10_fcol_lt_{i}_{j}", label_visibility="collapsed")
                        with c2:
                            st.session_state.t10_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t10_fcol_lu_{i}_{j}", label_visibility="collapsed")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t10_fcol_ld_{i}_{j}"):
                                st.session_state.t10_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t10_fcol_la_{i}", "＋ Adicionar link"):
                        st.session_state.t10_foot_cols[i]["links"].append({"texto": "Novo Link", "url": "#"}); st.rerun()
                    if len(st.session_state.t10_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t10_fcol_del_{i}"):
                            st.session_state.t10_foot_cols.pop(i); st.rerun()
            if _add_btn("t10_foot_col_add", "＋ Adicionar coluna ao rodapé"):
                st.session_state.t10_foot_cols.append({"titulo": "Nova Coluna", "links": [{"texto": "Link", "url": "#"}]}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t10_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t10_fcp_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t10_foot_copys) > 1 and _del_btn(f"t10_fcp_del_{i}"):
                        st.session_state.t10_foot_copys.pop(i); st.rerun()
            if _add_btn("t10_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t10_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t10_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t10_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t10_obs_{i}", height=80,
                        placeholder="Ex: Alterar o emoji do visual para um foguete...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t10_obs) > 1 and _del_btn(f"t10_obs_del_{i}"):
                        st.session_state.t10_obs.pop(i); st.rerun()
            if _add_btn("t10_obs_add", "＋ Adicionar observação"):
                st.session_state.t10_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ENVIAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t10_send", type="primary"):
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
