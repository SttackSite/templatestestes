import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img2.png"
TEMPLATE_NAME = "Template 2 — FitPro Academia"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores
        "t2_cores": [
            {"nome": "Cor principal (destaques, botões)", "valor": "#FF6B35"},
            {"nome": "Cor de fundo (seções escuras)",    "valor": "#1a1a1a"},
            {"nome": "Cor dos textos principais",       "valor": "#1a1a1a"},
            {"nome": "Cor dos subtextos",                "valor": "#666666"},
        ],
        # Navbar
        "t2_logos": [{"parte1": "FIT", "destaque": "PRO"}],
        "t2_nav_links": [
            {"texto": "Recursos", "url": "#Nossos Serviços"},
            {"texto": "Galeria",  "url": "#Por que escolher a FitPro"},
            {"texto": "Sobre",    "url": "#Planos e preços"},
            {"texto": "Contato",  "url": "#Começar agora"},
        ],
        "t2_nav_ctas": [
            {"texto": "Começar Agora", "url": "https://www.google.com/"},
        ],
        # Hero
        "t2_hero_titulos": [
            {"parte1": "Transforme seu", "destaque": "corpo", "parte2": "e mente"},
        ],
        "t2_hero_subtitulos": [
            {"valor": "Programas personalizados, treinadores experientes e ambiente de primeira qualidade. Alcance seus objetivos conosco."},
        ],
        "t2_hero_stats": [
            {"numero": "5.000+", "label": "Alunos Ativos"},
            {"numero": "15+",    "label": "Anos de Experiência"},
        ],
        "t2_hero_btns": [
            {"texto": "Agende uma Avaliação Gratuita", "url": "https://www.google.com/"},
        ],
        "t2_hero_images": [{"emoji": "🏋️‍♂️"}],
        # Seção de Serviços
        "t2_serv_titulos": [{"parte1": "Nossos", "destaque": "Serviços"}],
        "t2_serv_descs":   [{"valor": "Oferecemos uma variedade de programas e serviços para atender todos os seus objetivos fitness"}],
        "t2_serv_cards": [
            {"icone": "🏋️", "titulo": "Musculação",       "descricao": "Programas de treinamento com pesos para ganho de massa e força muscular."},
            {"icone": "🏃", "titulo": "Cardio",           "descricao": "Equipamentos modernos para treinos cardiovasculares de alta performance."},
            {"icone": "🧘", "titulo": "Yoga e Pilates",    "descricao": "Aulas de flexibilidade, equilíbrio e bem-estar mental."},
            {"icone": "👨‍🏫", "titulo": "Personal Training", "descricao": "Acompanhamento individual com treinadores certificados."},
            {"icone": "🥗", "titulo": "Nutrição",          "descricao": "Orientação nutricional personalizada para seus objetivos."},
            {"icone": "💪", "titulo": "Grupos Funcionais", "descricao": "Treinos em grupo para motivação e diversão."},
        ],
        # Seção de Diferenciais (Features)
        "t2_feat_titulos": [{"parte1": "Por que escolher a", "destaque": "FitPro"}],
        "t2_feat_descs":   [{"valor": "Diferenciais que fazem a diferença na sua jornada fitness"}],
        "t2_feat_boxes": [
            {"titulo": "Equipamentos Modernos",   "descricao": "Máquinas de última geração importadas, sempre mantidas em perfeito funcionamento."},
            {"titulo": "Treinadores Certificados", "descricao": "Profissionais qualificados e experientes para orientar seu treino."},
            {"titulo": "Ambiente Acolhedor",      "descricao": "Espaço limpo, climatizado e seguro para você treinar com conforto."},
            {"titulo": "Horários Flexíveis",      "descricao": "Aberto de segunda a domingo, com horários que se adaptam à sua rotina."},
            {"titulo": "Comunidade Ativa",        "descricao": "Faça parte de uma comunidade motivada e comprometida com resultados."},
            {"titulo": "Acompanhamento Contínuo", "descricao": "Avaliações periódicas para acompanhar sua evolução e ajustar treinos."},
        ],
        # Seção de Preços
        "t2_price_titulos": [{"parte1": "Planos e", "destaque": "Preços"}],
        "t2_price_descs":   [{"valor": "Escolha o plano que melhor se adequa aos seus objetivos"}],
        "t2_price_cards": [
            {"titulo": "Básico", "preco": "R$ 99", "periodo": "Por mês", "features": "Acesso à academia\nUso de todos os equipamentos\nVestiário e chuveiro", "btn_txt": "Escolher Plano", "url": "#"},
            {"titulo": "Premium", "preco": "R$ 199", "periodo": "Por mês", "features": "Acesso à academia\nAulas em grupo ilimitadas\n2 sessões personal/mês\nAvaliação física mensal", "btn_txt": "Escolher Plano", "url": "#"},
            {"titulo": "Elite", "preco": "R$ 399", "periodo": "Por mês", "features": "Acesso 24/7\nPersonal training ilimitado\nAulas em grupo ilimitadas\nSuplementos com desconto", "btn_txt": "Escolher Plano", "url": "#"},
        ],
        # Depoimentos
        "t2_test_titulos": [{"parte1": "Histórias de", "destaque": "Sucesso"}],
        "t2_test_descs":   [{"valor": "Veja como nossos alunos transformaram suas vidas"}],
        "t2_test_cards": [
            {"texto": '"Entrei na FitPro sem conhecimento nenhum sobre treino. Os profissionais me orientaram perfeitamente e em 6 meses consegui resultados incríveis. Recomendo muito!"', "autor": "Roberto Silva", "cargo": "Aluno há 2 anos"},
            {"texto": '"O ambiente é acolhedor, os treinadores são atenciosos e os resultados falam por si. Já perdi 20kg e ganhei muita confiança. Melhor decisão que tomei!"', "autor": "Juliana Costa", "cargo": "Aluna Premium"},
            {"texto": '"A comunidade da FitPro é incrível. Tenho amigos, motivação e profissionais que realmente se importam com meu progresso. Voltaria mil vezes!"', "autor": "Marcus Oliveira", "cargo": "Aluno Elite"},
        ],
        # CTA Final
        "t2_ctaf_titulos": [{"parte1": "Comece sua transformação", "destaque": "hoje"}],
        "t2_ctaf_descs":   [{"valor": "Agende uma avaliação gratuita e conheça nossas instalações. Nossos profissionais estão prontos para ajudá-lo!"}],
        "t2_ctaf_btns":    [{"texto": "Agende Sua Avaliação", "url": "https://www.google.com/"}],
        # Footer
        "t2_footer_infos": [{"valor": "Telefone: (99) 99999-9999 | Email: contato@fitpro.com.br"}],
        "t2_footer_addrs": [{"valor": "Endereço: Av. Principal, 1234 - São Paulo, SP"}],
        "t2_footer_copys": [{"valor": "© 2025 FitPro Academia. Todos os direitos reservados. Transformando vidas através do fitness."}],
        # Observações
        "t2_obs": [{"valor": ""}],
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
            for i, cor in enumerate(st.session_state.t2_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t2_cores[i]["nome"] = st.text_input(
                        "Nome da cor", cor["nome"], key=f"t2_cor_nome_{i}", label_visibility="collapsed",
                        placeholder="Nome da cor")
                with c2:
                    st.session_state.t2_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t2_cor_val_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t2_cores) > 1 and _del_btn(f"t2_cor_del_{i}"):
                        st.session_state.t2_cores.pop(i); st.rerun()
            if _add_btn("t2_cor_add", "＋ Adicionar cor"):
                st.session_state.t2_cores.append({"nome": "Indique aqui onde usar a cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca *(Texto Normal | Texto Destaque)*")
            for i, item in enumerate(st.session_state.t2_logos):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t2_logos[i]["parte1"] = st.text_input(
                        "Parte 1", item["parte1"], key=f"t2_logo_p1_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t2_logos[i]["destaque"] = st.text_input(
                        "Destaque", item["destaque"], key=f"t2_logo_dest_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t2_logos) > 1 and _del_btn(f"t2_logo_del_{i}"):
                        st.session_state.t2_logos.pop(i); st.rerun()
            if _add_btn("t2_logo_add", "＋ Adicionar logo"):
                st.session_state.t2_logos.append({"parte1": "NOVA", "destaque": "MARCA"}); st.rerun()

            st.caption("Links do menu *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t2_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t2_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t2_nl_txt_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t2_nav_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t2_nl_url_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t2_nav_links) > 1 and _del_btn(f"t2_nl_del_{i}"):
                        st.session_state.t2_nav_links.pop(i); st.rerun()
            if _add_btn("t2_nl_add", "＋ Adicionar link"):
                st.session_state.t2_nav_links.append({"texto": "Novo Link", "url": "#"}); st.rerun()

            st.caption("Botão CTA da Navbar *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t2_nav_ctas):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t2_nav_ctas[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t2_ncta_txt_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t2_nav_ctas[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t2_ncta_url_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t2_nav_ctas) > 1 and _del_btn(f"t2_ncta_del_{i}"):
                        st.session_state.t2_nav_ctas.pop(i); st.rerun()
            if _add_btn("t2_ncta_add", "＋ Adicionar CTA Navbar"):
                st.session_state.t2_nav_ctas.append({"texto": "Começar", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🦸 Hero (Seção Principal)</div>', unsafe_allow_html=True)

            st.caption("Títulos do hero *(Parte 1 | Destaque | Parte 2)*")
            for i, t in enumerate(st.session_state.t2_hero_titulos):
                c1, c2, c3, c4 = st.columns([3, 3, 3, 1])
                with c1:
                    st.session_state.t2_hero_titulos[i]["parte1"] = st.text_input("P1", t["parte1"], key=f"t2_ht_p1_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t2_hero_titulos[i]["destaque"] = st.text_input("Dest", t["destaque"], key=f"t2_ht_dest_{i}", label_visibility="collapsed")
                with c3:
                    st.session_state.t2_hero_titulos[i]["parte2"] = st.text_input("P2", t["parte2"], key=f"t2_ht_p2_{i}", label_visibility="collapsed")
                with c4:
                    if len(st.session_state.t2_hero_titulos) > 1 and _del_btn(f"t2_ht_del_{i}"):
                        st.session_state.t2_hero_titulos.pop(i); st.rerun()
            if _add_btn("t2_ht_add", "＋ Adicionar título hero"):
                st.session_state.t2_hero_titulos.append({"parte1": "Texto", "destaque": "Destaque", "parte2": ""}); st.rerun()

            st.caption("Subtítulos do hero")
            for i, s in enumerate(st.session_state.t2_hero_subtitulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t2_hero_subtitulos[i]["valor"] = st.text_area("Sub", s["valor"], key=f"t2_hs_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t2_hero_subtitulos) > 1 and _del_btn(f"t2_hs_del_{i}"):
                        st.session_state.t2_hero_subtitulos.pop(i); st.rerun()
            if _add_btn("t2_hs_add", "＋ Adicionar subtítulo"):
                st.session_state.t2_hero_subtitulos.append({"valor": "Novo subtítulo"}); st.rerun()

            st.caption("Estatísticas do Hero *(Número | Descrição)*")
            for i, stat in enumerate(st.session_state.t2_hero_stats):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t2_hero_stats[i]["numero"] = st.text_input("Num", stat["numero"], key=f"t2_hstat_n_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t2_hero_stats[i]["label"] = st.text_input("Lab", stat["label"], key=f"t2_hstat_l_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t2_hero_stats) > 1 and _del_btn(f"t2_hstat_del_{i}"):
                        st.session_state.t2_hero_stats.pop(i); st.rerun()
            if _add_btn("t2_hstat_add", "＋ Adicionar estatística"):
                st.session_state.t2_hero_stats.append({"numero": "0", "label": "Novo dado"}); st.rerun()

            st.caption("Botão Principal do Hero *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t2_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t2_hero_btns[i]["texto"] = st.text_input("Txt", btn["texto"], key=f"t2_hbtn_t_{i}", label_visibility="collapsed")
                with c2:
                    st.session_state.t2_hero_btns[i]["url"] = st.text_input("URL", btn["url"], key=f"t2_hbtn_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t2_hero_btns) > 1 and _del_btn(f"t2_hbtn_del_{i}"):
                        st.session_state.t2_hero_btns.pop(i); st.rerun()
            if _add_btn("t2_hbtn_add", "＋ Adicionar botão hero"):
                st.session_state.t2_hero_btns.append({"texto": "Saiba Mais", "url": "#"}); st.rerun()

            st.caption("Emoji/Ícone do Hero")
            for i, img in enumerate(st.session_state.t2_hero_images):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t2_hero_images[i]["emoji"] = st.text_input("Emoji", img["emoji"], key=f"t2_himg_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t2_hero_images) > 1 and _del_btn(f"t2_himg_del_{i}"):
                        st.session_state.t2_hero_images.pop(i); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # SERVIÇOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏋️ Serviços</div>', unsafe_allow_html=True)
            
            st.caption("Título da Seção de Serviços")
            for i, t in enumerate(st.session_state.t2_serv_titulos):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t2_serv_titulos[i]["parte1"] = st.text_input("P1", t["parte1"], key=f"t2_st_p1_{i}", label_visibility="collapsed")
                with c2: st.session_state.t2_serv_titulos[i]["destaque"] = st.text_input("Dest", t["destaque"], key=f"t2_st_dest_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t2_serv_titulos) > 1 and _del_btn(f"t2_st_del_{i}"):
                        st.session_state.t2_serv_titulos.pop(i); st.rerun()
            
            st.caption("Subtítulo de Serviços")
            for i, desc in enumerate(st.session_state.t2_serv_descs):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t2_serv_descs[i]["valor"] = st.text_area("Desc", desc["valor"], key=f"t2_sd_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t2_serv_descs) > 1 and _del_btn(f"t2_sd_del_{i}"):
                        st.session_state.t2_serv_descs.pop(i); st.rerun()
            if _add_btn("t2_sd_add", "＋ Adicionar subtítulo serviços"):
                st.session_state.t2_serv_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Cards de Serviços *(Ícone | Título | Descrição)*")
            for i, card in enumerate(st.session_state.t2_serv_cards):
                with st.expander(f"Serviço {i+1}: {card['titulo']}"):
                    st.session_state.t2_serv_cards[i]["icone"] = st.text_input("Ícone/Emoji", card["icone"], key=f"t2_sc_i_{i}")
                    st.session_state.t2_serv_cards[i]["titulo"] = st.text_input("Título", card["titulo"], key=f"t2_sc_t_{i}")
                    st.session_state.t2_serv_cards[i]["descricao"] = st.text_area("Descrição", card["descricao"], key=f"t2_sc_d_{i}")
                    if len(st.session_state.t2_serv_cards) > 1 and _del_btn(f"t2_sc_del_{i}", "Excluir este card"):
                        st.session_state.t2_serv_cards.pop(i); st.rerun()
            if _add_btn("t2_sc_add", "＋ Adicionar card de serviço"):
                st.session_state.t2_serv_cards.append({"icone": "✨", "titulo": "Novo Serviço", "descricao": "Descrição aqui"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # DIFERENCIAIS (FEATURES)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌟 Diferenciais</div>', unsafe_allow_html=True)
            
            st.caption("Título da Seção de Diferenciais")
            for i, t in enumerate(st.session_state.t2_feat_titulos):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t2_feat_titulos[i]["parte1"] = st.text_input("P1", t["parte1"], key=f"t2_ft_p1_{i}", label_visibility="collapsed")
                with c2: st.session_state.t2_feat_titulos[i]["destaque"] = st.text_input("Dest", t["destaque"], key=f"t2_ft_dest_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t2_feat_titulos) > 1 and _del_btn(f"t2_ft_del_{i}"):
                        st.session_state.t2_feat_titulos.pop(i); st.rerun()
            
            st.caption("Subtítulo de Diferenciais")
            for i, desc in enumerate(st.session_state.t2_feat_descs):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t2_feat_descs[i]["valor"] = st.text_area("Desc", desc["valor"], key=f"t2_fd_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t2_feat_descs) > 1 and _del_btn(f"t2_fd_del_{i}"):
                        st.session_state.t2_feat_descs.pop(i); st.rerun()
            if _add_btn("t2_fd_add", "＋ Adicionar subtítulo diferenciais"):
                st.session_state.t2_feat_descs.append({"valor": "Nova descrição"}); st.rerun()

            for i, box in enumerate(st.session_state.t2_feat_boxes):
                with st.expander(f"Diferencial {i+1}: {box['titulo']}"):
                    st.session_state.t2_feat_boxes[i]["titulo"] = st.text_input("Título", box["titulo"], key=f"t2_fb_t_{i}")
                    st.session_state.t2_feat_boxes[i]["descricao"] = st.text_area("Descrição", box["descricao"], key=f"t2_fb_d_{i}")
                    if len(st.session_state.t2_feat_boxes) > 1 and _del_btn(f"t2_fb_del_{i}", "Excluir diferencial"):
                        st.session_state.t2_feat_boxes.pop(i); st.rerun()
            if _add_btn("t2_fb_add", "＋ Adicionar diferencial"):
                st.session_state.t2_feat_boxes.append({"titulo": "Novo Diferencial", "descricao": "Explique aqui"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # PREÇOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💰 Planos e Preços</div>', unsafe_allow_html=True)
            
            st.caption("Título da Seção de Preços")
            for i, t in enumerate(st.session_state.t2_price_titulos):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t2_price_titulos[i]["parte1"] = st.text_input("P1", t["parte1"], key=f"t2_pt_p1_{i}", label_visibility="collapsed")
                with c2: st.session_state.t2_price_titulos[i]["destaque"] = st.text_input("Dest", t["destaque"], key=f"t2_pt_dest_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t2_price_titulos) > 1 and _del_btn(f"t2_pt_del_{i}"):
                        st.session_state.t2_price_titulos.pop(i); st.rerun()
            
            st.caption("Subtítulo de Preços")
            for i, desc in enumerate(st.session_state.t2_price_descs):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t2_price_descs[i]["valor"] = st.text_area("Desc", desc["valor"], key=f"t2_pd_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t2_price_descs) > 1 and _del_btn(f"t2_pd_del_{i}"):
                        st.session_state.t2_price_descs.pop(i); st.rerun()
            if _add_btn("t2_pd_add", "＋ Adicionar subtítulo preços"):
                st.session_state.t2_price_descs.append({"valor": "Nova descrição"}); st.rerun()

            for i, card in enumerate(st.session_state.t2_price_cards):
                with st.expander(f"Plano: {card['titulo']}"):
                    st.session_state.t2_price_cards[i]["titulo"] = st.text_input("Nome do Plano", card["titulo"], key=f"t2_pc_t_{i}")
                    st.session_state.t2_price_cards[i]["preco"] = st.text_input("Preço", card["preco"], key=f"t2_pc_p_{i}")
                    st.session_state.t2_price_cards[i]["periodo"] = st.text_input("Período", card["periodo"], key=f"t2_pc_per_{i}")
                    st.session_state.t2_price_cards[i]["features"] = st.text_area("Vantagens (uma por linha)", card["features"], key=f"t2_pc_f_{i}")
                    st.session_state.t2_price_cards[i]["btn_txt"] = st.text_input("Texto do Botão", card["btn_txt"], key=f"t2_pc_bt_{i}")
                    st.session_state.t2_price_cards[i]["url"] = st.text_input("Link do Botão", card["url"], key=f"t2_pc_u_{i}")
                    if len(st.session_state.t2_price_cards) > 1 and _del_btn(f"t2_pc_del_{i}", "Excluir plano"):
                        st.session_state.t2_price_cards.pop(i); st.rerun()
            if _add_btn("t2_pc_add", "＋ Adicionar novo plano"):
                st.session_state.t2_price_cards.append({"titulo": "Novo Plano", "preco": "R$ 0", "periodo": "mês", "features": "Vantagem 1", "btn_txt": "Assinar", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # DEPOIMENTOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💬 Depoimentos</div>', unsafe_allow_html=True)
            
            st.caption("Título da Seção de Depoimentos")
            for i, t in enumerate(st.session_state.t2_test_titulos):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t2_test_titulos[i]["parte1"] = st.text_input("P1", t["parte1"], key=f"t2_tt_p1_{i}", label_visibility="collapsed")
                with c2: st.session_state.t2_test_titulos[i]["destaque"] = st.text_input("Dest", t["destaque"], key=f"t2_tt_dest_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t2_test_titulos) > 1 and _del_btn(f"t2_tt_del_{i}"):
                        st.session_state.t2_test_titulos.pop(i); st.rerun()
            
            st.caption("Subtítulo de Depoimentos")
            for i, desc in enumerate(st.session_state.t2_test_descs):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t2_test_descs[i]["valor"] = st.text_area("Desc", desc["valor"], key=f"t2_td_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t2_test_descs) > 1 and _del_btn(f"t2_td_del_{i}"):
                        st.session_state.t2_test_descs.pop(i); st.rerun()
            if _add_btn("t2_td_add", "＋ Adicionar subtítulo depoimentos"):
                st.session_state.t2_test_descs.append({"valor": "Nova descrição"}); st.rerun()

            for i, test in enumerate(st.session_state.t2_test_cards):
                with st.expander(f"Depoimento de {test['autor']}"):
                    st.session_state.t2_test_cards[i]["texto"] = st.text_area("Texto", test["texto"], key=f"t2_tc_x_{i}")
                    st.session_state.t2_test_cards[i]["autor"] = st.text_input("Autor", test["autor"], key=f"t2_tc_a_{i}")
                    st.session_state.t2_test_cards[i]["cargo"] = st.text_input("Cargo/Função", test["cargo"], key=f"t2_tc_c_{i}")
                    if len(st.session_state.t2_test_cards) > 1 and _del_btn(f"t2_tc_del_{i}", "Excluir depoimento"):
                        st.session_state.t2_test_cards.pop(i); st.rerun()
            if _add_btn("t2_tc_add", "＋ Adicionar depoimento"):
                st.session_state.t2_test_cards.append({"texto": '"Excelente!"', "autor": "Nome", "cargo": "Cliente"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # CTA FINAL E FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📢 Chamada Final & Rodapé</div>', unsafe_allow_html=True)
            
            st.caption("Título CTA Final")
            for i, t in enumerate(st.session_state.t2_ctaf_titulos):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t2_ctaf_titulos[i]["parte1"] = st.text_input("P1", t["parte1"], key=f"t2_ctaft_p1_{i}", label_visibility="collapsed")
                with c2: st.session_state.t2_ctaf_titulos[i]["destaque"] = st.text_input("Dest", t["destaque"], key=f"t2_ctaft_d_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t2_ctaf_titulos) > 1 and _del_btn(f"t2_ctaft_del_{i}"):
                        st.session_state.t2_ctaf_titulos.pop(i); st.rerun()
            if _add_btn("t2_ctaft_add", "＋ Adicionar título CTA final"):
                st.session_state.t2_ctaf_titulos.append({"parte1": "Texto", "destaque": "Destaque"}); st.rerun()

            st.caption("Subtítulo CTA Final")
            for i, desc in enumerate(st.session_state.t2_ctaf_descs):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t2_ctaf_descs[i]["valor"] = st.text_area("Desc", desc["valor"], key=f"t2_ctafd_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t2_ctaf_descs) > 1 and _del_btn(f"t2_ctafd_del_{i}"):
                        st.session_state.t2_ctaf_descs.pop(i); st.rerun()
            if _add_btn("t2_ctafd_add", "＋ Adicionar subtítulo CTA final"):
                st.session_state.t2_ctaf_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Botões CTA Final *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t2_ctaf_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t2_ctaf_btns[i]["texto"] = st.text_input("Txt", btn["texto"], key=f"t2_ctafb_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t2_ctaf_btns[i]["url"] = st.text_input("URL", btn["url"], key=f"t2_ctafb_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t2_ctaf_btns) > 1 and _del_btn(f"t2_ctafb_del_{i}"):
                        st.session_state.t2_ctaf_btns.pop(i); st.rerun()
            if _add_btn("t2_ctafb_add", "＋ Adicionar botão CTA final"):
                st.session_state.t2_ctaf_btns.append({"texto": "Saiba Mais", "url": "#"}); st.rerun()

            st.caption("Informações de Contato")
            for i, info in enumerate(st.session_state.t2_footer_infos):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t2_footer_infos[i]["valor"] = st.text_input("Contato", info["valor"], key=f"t2_fi_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t2_footer_infos) > 1 and _del_btn(f"t2_fi_del_{i}"):
                        st.session_state.t2_footer_infos.pop(i); st.rerun()
            if _add_btn("t2_fi_add", "＋ Adicionar info contato"):
                st.session_state.t2_footer_infos.append({"valor": "Nova informação"}); st.rerun()

            st.caption("Endereços")
            for i, addr in enumerate(st.session_state.t2_footer_addrs):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t2_footer_addrs[i]["valor"] = st.text_input("Endereço", addr["valor"], key=f"t2_fa_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t2_footer_addrs) > 1 and _del_btn(f"t2_fa_del_{i}"):
                        st.session_state.t2_footer_addrs.pop(i); st.rerun()
            if _add_btn("t2_fa_add", "＋ Adicionar endereço"):
                st.session_state.t2_footer_addrs.append({"valor": "Novo endereço"}); st.rerun()

            st.caption("Copyright / Rodapé")
            for i, copy in enumerate(st.session_state.t2_footer_copys):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t2_footer_copys[i]["valor"] = st.text_input("Copy", copy["valor"], key=f"t2_fc_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t2_footer_copys) > 1 and _del_btn(f"t2_fc_del_{i}"):
                        st.session_state.t2_footer_copys.pop(i); st.rerun()
            if _add_btn("t2_fc_add", "＋ Adicionar copyright"):
                st.session_state.t2_footer_copys.append({"valor": "Novo copyright"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, obs in enumerate(st.session_state.t2_obs):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t2_obs[i]["valor"] = st.text_area("Obs", obs["valor"], key=f"t2_obs_{i}", label_visibility="collapsed", placeholder="Notas extras...")
                with c2:
                    if len(st.session_state.t2_obs) > 1 and _del_btn(f"t2_obs_del_{i}"):
                        st.session_state.t2_obs.pop(i); st.rerun()
            if _add_btn("t2_obs_add", "＋ Adicionar observação"):
                st.session_state.t2_obs.append({"valor": ""}); st.rerun()

            st.markdown("---")
            if st.button("🚀 FINALIZAR E GERAR SITE", use_container_width=True):
                st.balloons()
                st.success("Configurações salvas! O site está sendo processado.")

    with col_preview:
        st.markdown('<div class="panel-title">👁️ Preview Visual</div>', unsafe_allow_html=True)
        st.markdown('<div class="panel-subtitle">Referência visual do template — role para ver o site completo</div>', unsafe_allow_html=True)
        st.markdown(f"""
            <div class="template-img-wrapper">
                <img src="{TEMPLATE_IMAGE_URL}" alt="Template Preview">
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    render()
