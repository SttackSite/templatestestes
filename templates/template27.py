import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img27.png"
TEMPLATE_NAME = "Template 27 — LittleTracks Style (Kids & Family App)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── CORES ───────────────────────────────────────────────────────────
        "t27_cores": [
            {"nome": "Roxo Principal",  "valor": "#9d8df1"},
            {"nome": "Azul Suave",      "valor": "#a0d2eb"},
            {"nome": "Rosa",            "valor": "#ffafcc"},
            {"nome": "Amarelo",         "valor": "#ffee93"},
            {"nome": "Fundo Principal", "valor": "#fdfcf0"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t27_nav_logos": [{"valor": "🐾 littletracks"}],
        "t27_nav_links": [
            {"texto": "O App",           "url": "#hero"},
            {"texto": "Funcionalidades", "url": "#funcionalidades"},
            {"texto": "Preços",          "url": "#precos"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t27_hero_titulos": [{"valor": "Guardar memórias <br><span style='color: #9d8df1;'>nunca foi tão doce.</span>"}],
        "t27_hero_descs":   [{"valor": "O diário digital inteligente que organiza os momentos mais preciosos dos seus filhos, para que você possa focar no que realmente importa: viver cada um deles."}],
        "t27_hero_btns":    [{"texto": "Criar Minha Conta Grátis", "url": "https://www.google.com/"}],

        # ── FUNCIONALIDADES ──────────────────────────────────────────────────
        "t27_func_titulos": [{"valor": "Tudo o que você precisa"}],
        "t27_func_items": [
            {"emoji": "📸",         "title": "Organização Mágica",  "desc": "Fotos e vídeos são organizados automaticamente por data e fase do crescimento."},
            {"emoji": "👨‍👩‍👧‍👦", "title": "Círculo da Família",   "desc": "Compartilhe momentos com avós e tios em um ambiente privado e seguro."},
            {"emoji": "🎨",         "title": "Livros de Memórias",  "desc": "Transforme seu diário digital em um álbum físico impresso com apenas um clique."},
        ],

        # ── TIMELINE ────────────────────────────────────────────────────────
        "t27_time_titulos": [{"valor": "Uma linha do tempo da vida deles"}],
        "t27_time_imgs":    [{"valor": "https://images.unsplash.com/photo-1519681393784-d120267933ba?w=800"}],
        "t27_time_items": [
            {"label": "Hoje - 2 Anos e 3 Meses", "desc": "O primeiro dia na escolinha! Nenhuma lágrima (pelo menos não do Leo).", "cor": "#9d8df1"},
            {"label": "Há 6 meses",               "desc": "Primeiros passos no jardim. A aventura começou!",                      "cor": "#666666"},
            {"label": "O Nascimento",             "desc": "O começo da trilha mais linda de nossas vidas.",                       "cor": "#666666"},
        ],

        # ── DEPOIMENTOS ─────────────────────────────────────────────────────
        "t27_depo_titulos": [{"valor": "Amado por mais de 50.000 famílias"}],
        "t27_depo_items": [
            {"texto": "\"O littletracks mudou a forma como guardo as fotos da minha filha. É tão fácil de usar e as sugestões de marcos são incríveis!\"", "autor": "Mariana S., Mãe da Alice"},
            {"texto": "\"Finalmente um lugar seguro para compartilhar fotos com a família sem precisar das redes sociais abertas.\"",                       "autor": "Ricardo T., Pai do Bento"},
        ],

        # ── PREÇOS ──────────────────────────────────────────────────────────
        "t27_price_titulos": [{"valor": "Escolha o seu plano"}],
        "t27_price_descs":   [{"valor": "Sem taxas escondidas. Cancele quando quiser."}],
        "t27_price_plans": [
            {"nome": "Básico",   "preco": "Grátis", "periodo": "",    "desc": "Para começar a trilha",         "popular": False, "badge": "",           "features": ["Até 500 fotos", "1 Perfil de criança", "Álbum digital básico"],                                    "btn_texto": "Escolher Básico",  "btn_url": "#"},
            {"nome": "Premium",  "preco": "R$ 19",  "periodo": "/mês","desc": "Para memórias infinitas",       "popular": True,  "badge": "MAIS POPULAR","features": ["Armazenamento Ilimitado", "Vídeos em 4K", "Compartilhamento ilimitado", "Backup automático"],     "btn_texto": "Assinar Premium",  "btn_url": "#"},
            {"nome": "Família",  "preco": "R$ 35",  "periodo": "/mês","desc": "Para toda a árvore genealógica","popular": False, "badge": "",           "features": ["Tudo do Premium", "Até 5 perfis de crianças", "Acesso de Admin para 4 pessoas"],                   "btn_texto": "Escolher Família", "btn_url": "#"},
        ],

        # ── FAQ ─────────────────────────────────────────────────────────────
        "t27_faq_titulos": [{"valor": "Dúvidas Frequentes"}],
        "t27_faq_items": [
            {"pergunta": "Meus dados estão seguros?",           "resposta": "Sim! Utilizamos criptografia de nível bancário e seus dados nunca são vendidos para terceiros."},
            {"pergunta": "Posso imprimir os álbuns no Brasil?", "resposta": "Sim, temos parceiros de impressão locais que entregam em todo o território nacional com acabamento premium."},
            {"pergunta": "Como convido os avós?",               "resposta": "Basta enviar um link mágico pelo WhatsApp ou e-mail. Eles não precisam criar senhas complicadas."},
        ],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t27_foot_logos": [{"valor": "🐾 littletracks"}],
        "t27_foot_links": [
            {"texto": "Instagram",    "url": "#"},
            {"texto": "Facebook",     "url": "#"},
            {"texto": "Blog",         "url": "#"},
            {"texto": "Termos de Uso","url": "#"},
        ],
        "t27_foot_copys": [{"valor": "© 2026 littletracks. Criado com ❤️ para as futuras gerações."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t27_obs": [{"valor": ""}],
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
            for i, cor in enumerate(st.session_state.t27_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t27_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t27_cor_n_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t27_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t27_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t27_cores) > 1 and _del_btn(f"t27_cor_del_{i}"):
                        st.session_state.t27_cores.pop(i); st.rerun()
            if _add_btn("t27_cor_add", "＋ Adicionar cor"):
                st.session_state.t27_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca  *(lado esquerdo)*")
            for i, item in enumerate(st.session_state.t27_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_nav_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t27_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t27_nav_logos) > 1 and _del_btn(f"t27_logo_del_{i}"):
                        st.session_state.t27_nav_logos.pop(i); st.rerun()
            if _add_btn("t27_logo_add", "＋ Adicionar logo"):
                st.session_state.t27_nav_logos.append({"valor": "🐾 marca"}); st.rerun()

            st.caption("Links do menu  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t27_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t27_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t27_nl_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t27_nav_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t27_nl_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t27_nav_links) > 1 and _del_btn(f"t27_nl_del_{i}"):
                        st.session_state.t27_nav_links.pop(i); st.rerun()
            if _add_btn("t27_nl_add", "＋ Adicionar link"):
                st.session_state.t27_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🐾 Hero Section</div>', unsafe_allow_html=True)

            st.caption("Título principal  *(use <br> para quebrar linha; <span> para colorir)*")
            for i, t in enumerate(st.session_state.t27_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t27_h_t_{i}", height=80, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t27_hero_titulos) > 1 and _del_btn(f"t27_h_t_del_{i}"):
                        st.session_state.t27_hero_titulos.pop(i); st.rerun()
            if _add_btn("t27_h_t_add", "＋ Adicionar título"):
                st.session_state.t27_hero_titulos.append({"valor": "Novo título."}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t27_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t27_h_d_{i}", height=90, label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t27_hero_descs) > 1 and _del_btn(f"t27_h_d_del_{i}"):
                        st.session_state.t27_hero_descs.pop(i); st.rerun()
            if _add_btn("t27_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t27_hero_descs.append({"valor": "Nova descrição."}); st.rerun()

            st.caption("Botões  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t27_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t27_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t27_hb_t_{i}", label_visibility="collapsed", placeholder="Texto")
                with c2:
                    st.session_state.t27_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t27_hb_u_{i}", label_visibility="collapsed", placeholder="URL")
                with c3:
                    if len(st.session_state.t27_hero_btns) > 1 and _del_btn(f"t27_hb_del_{i}"):
                        st.session_state.t27_hero_btns.pop(i); st.rerun()
            if _add_btn("t27_hb_add", "＋ Adicionar botão"):
                st.session_state.t27_hero_btns.append({"texto": "COMEÇAR", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FUNCIONALIDADES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">✨ Funcionalidades</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t27_func_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_func_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t27_ft_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t27_func_titulos) > 1 and _del_btn(f"t27_ft_del_{i}"):
                        st.session_state.t27_func_titulos.pop(i); st.rerun()
            if _add_btn("t27_ft_add", "＋ Adicionar título"):
                st.session_state.t27_func_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Cards  *(Emoji | Título | Descrição)*")
            for i, item in enumerate(st.session_state.t27_func_items):
                with st.expander(f"Funcionalidade {i+1}: {item['title']}"):
                    st.session_state.t27_func_items[i]["emoji"] = st.text_input(
                        "Emoji", item["emoji"], key=f"t27_fi_e_{i}")
                    st.session_state.t27_func_items[i]["title"] = st.text_input(
                        "Título", item["title"], key=f"t27_fi_t_{i}")
                    st.session_state.t27_func_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t27_fi_d_{i}", height=70)
                    if len(st.session_state.t27_func_items) > 1:
                        if st.button("🗑 Remover esta funcionalidade", key=f"t27_fi_del_{i}"):
                            st.session_state.t27_func_items.pop(i); st.rerun()
            if _add_btn("t27_fi_add", "＋ Adicionar funcionalidade"):
                st.session_state.t27_func_items.append({"emoji": "⭐", "title": "NOVO", "desc": "DESCRIÇÃO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # TIMELINE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📅 Linha do Tempo</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t27_time_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_time_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t27_tt_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t27_time_titulos) > 1 and _del_btn(f"t27_tt_del_{i}"):
                        st.session_state.t27_time_titulos.pop(i); st.rerun()
            if _add_btn("t27_tt_add", "＋ Adicionar título"):
                st.session_state.t27_time_titulos.append({"valor": "Nova linha do tempo"}); st.rerun()

            st.caption("Imagem lateral  *(URL)*")
            for i, img in enumerate(st.session_state.t27_time_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_time_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t27_ti_img_{i}", label_visibility="collapsed", placeholder="https://...")
                with c2:
                    if len(st.session_state.t27_time_imgs) > 1 and _del_btn(f"t27_ti_img_del_{i}"):
                        st.session_state.t27_time_imgs.pop(i); st.rerun()
            if _add_btn("t27_ti_img_add", "＋ Adicionar imagem"):
                st.session_state.t27_time_imgs.append({"valor": "https://"}); st.rerun()

            st.caption("Eventos  *(Data | Descrição | Cor)*")
            for i, item in enumerate(st.session_state.t27_time_items):
                with st.expander(f"Evento {i+1}: {item['label']}"):
                    st.session_state.t27_time_items[i]["label"] = st.text_input(
                        "Data/Título", item["label"], key=f"t27_ti_l_{i}")
                    st.session_state.t27_time_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t27_ti_d_{i}", height=70)
                    st.session_state.t27_time_items[i]["cor"] = st.color_picker(
                        "Cor do Círculo", item["cor"], key=f"t27_ti_c_{i}")
                    if len(st.session_state.t27_time_items) > 1:
                        if st.button("🗑 Remover este evento", key=f"t27_ti_del_{i}"):
                            st.session_state.t27_time_items.pop(i); st.rerun()
            if _add_btn("t27_ti_add", "＋ Adicionar evento"):
                st.session_state.t27_time_items.append({"label": "NOVO", "desc": "DESCRIÇÃO", "cor": "#666666"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # DEPOIMENTOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💬 Depoimentos</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t27_depo_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_depo_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t27_dt_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t27_depo_titulos) > 1 and _del_btn(f"t27_dt_del_{i}"):
                        st.session_state.t27_depo_titulos.pop(i); st.rerun()
            if _add_btn("t27_dt_add", "＋ Adicionar título"):
                st.session_state.t27_depo_titulos.append({"valor": "Amado por milhares"}); st.rerun()

            st.caption("Cards de depoimento  *(Texto | Autor)*")
            for i, item in enumerate(st.session_state.t27_depo_items):
                with st.expander(f"Depoimento {i+1}"):
                    st.session_state.t27_depo_items[i]["texto"] = st.text_area(
                        "Texto", item["texto"], key=f"t27_di_t_{i}", height=90)
                    st.session_state.t27_depo_items[i]["autor"] = st.text_input(
                        "Autor", item["autor"], key=f"t27_di_a_{i}")
                    if len(st.session_state.t27_depo_items) > 1:
                        if st.button("🗑 Remover este depoimento", key=f"t27_di_del_{i}"):
                            st.session_state.t27_depo_items.pop(i); st.rerun()
            if _add_btn("t27_di_add", "＋ Adicionar depoimento"):
                st.session_state.t27_depo_items.append({"texto": "ADOREI!", "autor": "NOME"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # PREÇOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💰 Planos de Preço</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t27_price_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_price_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t27_pt_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t27_price_titulos) > 1 and _del_btn(f"t27_pt_del_{i}"):
                        st.session_state.t27_price_titulos.pop(i); st.rerun()
            if _add_btn("t27_pt_add", "＋ Adicionar título"):
                st.session_state.t27_price_titulos.append({"valor": "Nossos Planos"}); st.rerun()

            st.caption("Subtítulo")
            for i, d in enumerate(st.session_state.t27_price_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_price_descs[i]["valor"] = st.text_input(
                        "Subtítulo", d["valor"], key=f"t27_pd_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t27_price_descs) > 1 and _del_btn(f"t27_pd_del_{i}"):
                        st.session_state.t27_price_descs.pop(i); st.rerun()
            if _add_btn("t27_pd_add", "＋ Adicionar subtítulo"):
                st.session_state.t27_price_descs.append({"valor": "Sem surpresas."}); st.rerun()

            st.caption("Planos")
            for i, plan in enumerate(st.session_state.t27_price_plans):
                with st.expander(f"Plano {i+1}: {plan['nome']}"):
                    st.session_state.t27_price_plans[i]["nome"] = st.text_input(
                        "Nome", plan["nome"], key=f"t27_pp_n_{i}")
                    st.session_state.t27_price_plans[i]["preco"] = st.text_input(
                        "Preço", plan["preco"], key=f"t27_pp_p_{i}")
                    st.session_state.t27_price_plans[i]["periodo"] = st.text_input(
                        "Período", plan["periodo"], key=f"t27_pp_per_{i}")
                    st.session_state.t27_price_plans[i]["desc"] = st.text_input(
                        "Descrição", plan["desc"], key=f"t27_pp_d_{i}")
                    st.session_state.t27_price_plans[i]["popular"] = st.checkbox(
                        "Destaque (Popular)", plan["popular"], key=f"t27_pp_pop_{i}")
                    st.session_state.t27_price_plans[i]["badge"] = st.text_input(
                        "Texto do Badge", plan["badge"], key=f"t27_pp_b_{i}")
                    st.caption("Vantagens  *(uma por linha)*")
                    feats_text = "\n".join(plan["features"])
                    new_feats = st.text_area(
                        "Vantagens", feats_text, key=f"t27_pp_f_{i}", height=90,
                        label_visibility="collapsed").split("\n")
                    st.session_state.t27_price_plans[i]["features"] = [f.strip() for f in new_feats if f.strip()]
                    st.session_state.t27_price_plans[i]["btn_texto"] = st.text_input(
                        "Texto Botão", plan["btn_texto"], key=f"t27_pp_bt_{i}")
                    st.session_state.t27_price_plans[i]["btn_url"] = st.text_input(
                        "URL Botão", plan["btn_url"], key=f"t27_pp_bu_{i}")
                    if len(st.session_state.t27_price_plans) > 1:
                        if st.button("🗑 Remover este plano", key=f"t27_pp_del_{i}"):
                            st.session_state.t27_price_plans.pop(i); st.rerun()
            if _add_btn("t27_pp_add", "＋ Adicionar plano"):
                st.session_state.t27_price_plans.append({
                    "nome": "NOVO", "preco": "R$ 0", "periodo": "/mês", "desc": "DESC",
                    "popular": False, "badge": "", "features": ["Vantagem 1"],
                    "btn_texto": "ASSINAR", "btn_url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FAQ
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">❓ FAQ</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t27_faq_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_faq_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t27_faqt_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t27_faq_titulos) > 1 and _del_btn(f"t27_faqt_del_{i}"):
                        st.session_state.t27_faq_titulos.pop(i); st.rerun()
            if _add_btn("t27_faqt_add", "＋ Adicionar título"):
                st.session_state.t27_faq_titulos.append({"valor": "Dúvidas"}); st.rerun()

            st.caption("Perguntas e respostas")
            for i, item in enumerate(st.session_state.t27_faq_items):
                with st.expander(f"Pergunta {i+1}"):
                    st.session_state.t27_faq_items[i]["pergunta"] = st.text_input(
                        "Pergunta", item["pergunta"], key=f"t27_faqi_p_{i}")
                    st.session_state.t27_faq_items[i]["resposta"] = st.text_area(
                        "Resposta", item["resposta"], key=f"t27_faqi_r_{i}", height=80)
                    if len(st.session_state.t27_faq_items) > 1:
                        if st.button("🗑 Remover esta pergunta", key=f"t27_faqi_del_{i}"):
                            st.session_state.t27_faq_items.pop(i); st.rerun()
            if _add_btn("t27_faqi_add", "＋ Adicionar pergunta"):
                st.session_state.t27_faq_items.append({"pergunta": "DÚVIDA?", "resposta": "RESPOSTA"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Logo do rodapé")
            for i, item in enumerate(st.session_state.t27_foot_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_foot_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t27_fl_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t27_foot_logos) > 1 and _del_btn(f"t27_fl_del_{i}"):
                        st.session_state.t27_foot_logos.pop(i); st.rerun()
            if _add_btn("t27_fl_add", "＋ Adicionar logo"):
                st.session_state.t27_foot_logos.append({"valor": "🐾 marca"}); st.rerun()

            st.caption("Links do rodapé  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t27_foot_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t27_foot_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t27_footl_t_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t27_foot_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t27_footl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t27_foot_links) > 1 and _del_btn(f"t27_footl_del_{i}"):
                        st.session_state.t27_foot_links.pop(i); st.rerun()
            if _add_btn("t27_footl_add", "＋ Adicionar link"):
                st.session_state.t27_foot_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t27_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t27_fcp_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t27_foot_copys) > 1 and _del_btn(f"t27_fcp_del_{i}"):
                        st.session_state.t27_foot_copys.pop(i); st.rerun()
            if _add_btn("t27_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t27_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t27_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t27_obs_{i}", height=80,
                        placeholder="Ex: Usar tons pastéis ainda mais suaves...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t27_obs) > 1 and _del_btn(f"t27_obs_del_{i}"):
                        st.session_state.t27_obs.pop(i); st.rerun()
            if _add_btn("t27_obs_add", "＋ Adicionar observação"):
                st.session_state.t27_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ENVIAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t27_send", type="primary"):
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
        page_icon="🐾",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
