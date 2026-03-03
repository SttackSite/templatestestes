import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img13.png"
TEMPLATE_NAME = "Template 13 — Ogreen Style (Sustentabilidade & Indústria) - COMPLETO"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores Ogreen
        "t13_cores": [
            {"nome": "Verde Principal", "valor": "#005a31"},
            {"nome": "Verde Limão (Stats)", "valor": "#8ec641"},
            {"nome": "Cor de Texto (Escuro)", "valor": "#333333"},
            {"nome": "Cor de Fundo (Claro)", "valor": "#f8f9fa"},
        ],
        # Header / Navbar
        "t13_logos": [{"valor": "ogreen"}],
        "t13_nav_links": [
            {"texto": "A ogreen", "url": "#about"},
            {"texto": "NOSSOS NEGÓCIOS", "url": "#business"},
            {"texto": "SUSTENTABILIDADE", "url": "#sustainability"},
            {"texto": "INVESTIDORES", "url": "#investors"},
            {"texto": "PRODUTOS", "url": "#products"},
        ],
        # Hero Section
        "t13_hero_titulos": [{"valor": "O FUTURO É RENOVÁVEL"}],
        "t13_hero_descs": [{"valor": "Líder na produção de papéis e cartões para embalagens, embalagens de papelão ondulado e sacos industriais."}],
        "t13_hero_imgs": [{"valor": "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?auto=format&fit=crop&w=1600&q=80"}],
        # Sobre a Ogreen
        "t13_about_titulos": [{"valor": "Sobre a ogreen"}],
        "t13_about_descs": [{"valor": "Com 125 anos de história, somos a maior produtora e exportadora de papéis para embalagens e soluções sustentáveis do Brasil. Nossa atuação é baseada no desenvolvimento sustentável, com florestas 100% plantadas e certificadas."}],
        "t13_about_imgs": [{"valor": "https://images.unsplash.com/photo-1542601906990-b4d3fb778b09?auto=format&fit=crop&w=800&q=80", "legenda": "Gestão Florestal Responsável"}],
        "t13_about_btns": [{"texto": "CONHEÇA NOSSA HISTÓRIA", "url": "https://www.google.com/"}],
        # Estatísticas (Stats)
        "t13_stats": [
            {"valor": "22", "label": "Fábricas no Brasil e Argentina"},
            {"valor": "125", "label": "Anos de Inovação"},
            {"valor": "719k", "label": "Hectares de Florestas"},
            {"valor": "25k", "label": "Colaboradores"},
        ],
        # Nossos Negócios (Business Cards)
        "t13_bus_secao_titulos": [{"valor": "Nossas Frentes de Atuação"}],
        "t13_bus_items": [
            {"img": "https://images.unsplash.com/photo-1603484477859-abe6a73f9366?w=500", "titulo": "Celulose", "desc": "Fibra curta, fibra longa e celulose fluff para diversas aplicações.", "url": "https://www.google.com/"},
            {"img": "https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=500", "titulo": "Embalagens", "desc": "Soluções inteligentes em papelão ondulado e sacos industriais sustentáveis.", "url": "https://www.google.com/"},
            {"img": "https://images.unsplash.com/photo-1603484477859-abe6a73f9366?w=500", "titulo": "Papéis", "desc": "Papel-cartão e Kraftliner de alta performance para o mercado.", "url": "https://www.google.com/"},
        ],
        # KODS - Sustentabilidade
        "t13_kods_titulos": [{"valor": "KODS - Objetivos ogreen para o Desenvolvimento Sustentável"}],
        "t13_kods_descs": [{"valor": "Nossa agenda de sustentabilidade está alinhada aos ODS da ONU, com metas claras até 2030 para biodiversidade, clima e impacto social."}],
        "t13_kods_items": [
            {"texto": "🌳 Conservação da Biodiversidade", "tipo": "info"},
            {"texto": "♻️ Economia Circular e Resíduo Zero", "tipo": "success"},
            {"texto": "💧 Gestão Eficiente de Recursos Hídricos", "tipo": "warning"},
        ],
        # Investidores (RI)
        "t13_ri_titulos": [{"valor": "Relações com Investidores"}],
        "t13_ri_metrics": [
            {"label": "KLBN11 (Units)", "value": "R$ 22,45", "delta": "+1.20%"},
        ],
        "t13_ri_cards": [
            {"titulo": "Central de Resultados", "desc": "Acesse os relatórios do 4T25 e demonstrações financeiras.", "btn_texto": "Acessar Central", "url": "https://www.google.com/"},
            {"titulo": "Governança Corporativa", "desc": "Transparência e ética em todos os níveis da companhia.", "btn_texto": "Ver Diretoria", "url": "https://www.google.com/"},
        ],
        # Footer
        "t13_foot_logos": [{"valor": "ogreen"}],
        "t13_foot_descs": [{"valor": "Líder no mercado de papéis e embalagens, focada na inovação e na sustentabilidade do ciclo da floresta ao consumidor final."}],
        "t13_foot_cols": [
            {"titulo": "NOSSOS SITES", "links": [{"texto": "Relações com Investidores", "url": "#"}, {"texto": "ogreen ForYou", "url": "#"}, {"texto": "Blog ogreen", "url": "#"}]},
            {"titulo": "CONTATO", "links": [{"texto": "Fale Conosco", "url": "#"}, {"texto": "Imprensa", "url": "#"}, {"texto": "Trabalhe Conosco", "url": "#"}]},
            {"titulo": "REDES SOCIAIS", "links": [{"texto": "LinkedIn", "url": "#"}, {"texto": "Instagram", "url": "#"}, {"texto": "YouTube", "url": "#"}]},
        ],
        "t13_foot_copys": [{"valor": "© 2026 ogreen S.A. | Todos os direitos reservados."}],
        # Observações
        "t13_obs": [{"valor": ""}],
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
            for i, cor in enumerate(st.session_state.t13_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t13_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t13_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t13_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t13_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t13_cores) > 1 and _del_btn(f"t13_cor_del_{i}"):
                        st.session_state.t13_cores.pop(i); st.rerun()
            if _add_btn("t13_cor_add", "＋ Adicionar cor"):
                st.session_state.t13_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Header)</div>', unsafe_allow_html=True)
            st.caption("Logo Principal")
            for i, logo in enumerate(st.session_state.t13_logos):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t13_logos[i]["valor"] = st.text_input("Logo", logo["valor"], key=f"t13_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t13_logos) > 1 and _del_btn(f"t13_logo_del_{i}"):
                        st.session_state.t13_logos.pop(i); st.rerun()
            if _add_btn("t13_logo_add", "＋ Adicionar logo"):
                st.session_state.t13_logos.append({"valor": "ogreen"}); st.rerun()
            
            st.caption("Links do Menu *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t13_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t13_nav_links[i]["texto"] = st.text_input("Texto", link["texto"], key=f"t13_nl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t13_nav_links[i]["url"] = st.text_input("URL", link["url"], key=f"t13_nl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t13_nav_links) > 1 and _del_btn(f"t13_nl_del_{i}"):
                        st.session_state.t13_nav_links.pop(i); st.rerun()
            if _add_btn("t13_nl_add", "＋ Adicionar link"):
                st.session_state.t13_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌲 Hero Banner</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t13_hero_titulos):
                st.session_state.t13_hero_titulos[i]["valor"] = st.text_input("Título Hero", t["valor"], key=f"t13_h_t_{i}")
            for i, d in enumerate(st.session_state.t13_hero_descs):
                st.session_state.t13_hero_descs[i]["valor"] = st.text_area("Descrição Hero", d["valor"], key=f"t13_h_d_{i}")
            for i, img in enumerate(st.session_state.t13_hero_imgs):
                st.session_state.t13_hero_imgs[i]["valor"] = st.text_input("URL Imagem Fundo", img["valor"], key=f"t13_h_i_{i}")

            # ══════════════════════════════════════════════════════════════════
            # SOBRE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📖 Seção Sobre</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t13_about_titulos):
                st.session_state.t13_about_titulos[i]["valor"] = st.text_input("Título Sobre", t["valor"], key=f"t13_at_{i}")
            for i, d in enumerate(st.session_state.t13_about_descs):
                st.session_state.t13_about_descs[i]["valor"] = st.text_area("Descrição Sobre", d["valor"], key=f"t13_ad_{i}")
            for i, item in enumerate(st.session_state.t13_about_imgs):
                st.session_state.t13_about_imgs[i]["valor"] = st.text_input("URL Imagem Lateral", item["valor"], key=f"t13_ai_i_{i}")
                st.session_state.t13_about_imgs[i]["legenda"] = st.text_input("Legenda da Imagem", item["legenda"], key=f"t13_ai_l_{i}")
            for i, btn in enumerate(st.session_state.t13_about_btns):
                c1, c2 = st.columns([5, 5])
                with c1: st.session_state.t13_about_btns[i]["texto"] = st.text_input("Texto Botão Sobre", btn["texto"], key=f"t13_ab_t_{i}")
                with c2: st.session_state.t13_about_btns[i]["url"] = st.text_input("URL Botão Sobre", btn["url"], key=f"t13_ab_u_{i}")

            # ══════════════════════════════════════════════════════════════════
            # ESTATÍSTICAS (STATS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Números de Impacto</div>', unsafe_allow_html=True)
            for i, stat in enumerate(st.session_state.t13_stats):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t13_stats[i]["valor"] = st.text_input("Número", stat["valor"], key=f"t13_st_v_{i}", label_visibility="collapsed")
                with c2: st.session_state.t13_stats[i]["label"] = st.text_input("Descrição", stat["label"], key=f"t13_st_l_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t13_stats) > 1 and _del_btn(f"t13_st_del_{i}"):
                        st.session_state.t13_stats.pop(i); st.rerun()
            if _add_btn("t13_st_add", "＋ Adicionar estatística"):
                st.session_state.t13_stats.append({"valor": "0", "label": "NOVO DADO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NEGÓCIOS (BUSINESS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏢 Frentes de Atuação</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t13_bus_secao_titulos):
                st.session_state.t13_bus_secao_titulos[i]["valor"] = st.text_input("Título Seção Negócios", t["valor"], key=f"t13_bst_{i}")
            
            for i, item in enumerate(st.session_state.t13_bus_items):
                with st.expander(f"Negócio {i+1}: {item['titulo']}"):
                    st.session_state.t13_bus_items[i]["titulo"] = st.text_input("Título", item["titulo"], key=f"t13_bi_t_{i}")
                    st.session_state.t13_bus_items[i]["desc"] = st.text_area("Descrição", item["desc"], key=f"t13_bi_d_{i}")
                    st.session_state.t13_bus_items[i]["img"] = st.text_input("URL Imagem", item["img"], key=f"t13_bi_i_{i}")
                    st.session_state.t13_bus_items[i]["url"] = st.text_input("URL Botão", item["url"], key=f"t13_bi_u_{i}")
                    if len(st.session_state.t13_bus_items) > 1 and _del_btn(f"t13_bi_del_{i}", "Remover negócio"):
                        st.session_state.t13_bus_items.pop(i); st.rerun()
            if _add_btn("t13_bi_add", "＋ Adicionar negócio"):
                st.session_state.t13_bus_items.append({"img": "", "titulo": "NOVO", "desc": "...", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # KODS - SUSTENTABILIDADE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">♻️ KODS (Sustentabilidade)</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t13_kods_titulos):
                st.session_state.t13_kods_titulos[i]["valor"] = st.text_area("Título KODS", t["valor"], key=f"t13_kt_{i}")
            for i, d in enumerate(st.session_state.t13_kods_descs):
                st.session_state.t13_kods_descs[i]["valor"] = st.text_area("Descrição KODS", d["valor"], key=f"t13_kd_{i}")
            
            st.caption("Objetivos *(Texto | Estilo)*")
            for i, item in enumerate(st.session_state.t13_kods_items):
                c1, c2, c3 = st.columns([5, 4, 1])
                with c1: st.session_state.t13_kods_items[i]["texto"] = st.text_input("Objetivo", item["texto"], key=f"t13_ki_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t13_kods_items[i]["tipo"] = st.selectbox("Estilo", ["info", "success", "warning", "error"], index=["info", "success", "warning", "error"].index(item["tipo"]), key=f"t13_ki_tp_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t13_kods_items) > 1 and _del_btn(f"t13_ki_del_{i}"):
                        st.session_state.t13_kods_items.pop(i); st.rerun()
            if _add_btn("t13_ki_add", "＋ Adicionar objetivo"):
                st.session_state.t13_kods_items.append({"texto": "NOVO OBJETIVO", "tipo": "info"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # INVESTIDORES (RI)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📈 Relações com Investidores</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t13_ri_titulos):
                st.session_state.t13_ri_titulos[i]["valor"] = st.text_input("Título RI", t["valor"], key=f"t13_rit_{i}")
            
            st.caption("Métricas de Ações *(Label | Valor | Variação)*")
            for i, met in enumerate(st.session_state.t13_ri_metrics):
                c1, c2, c3, c4 = st.columns([3, 3, 3, 1])
                with c1: st.session_state.t13_ri_metrics[i]["label"] = st.text_input("Ação", met["label"], key=f"t13_rim_l_{i}", label_visibility="collapsed")
                with c2: st.session_state.t13_ri_metrics[i]["value"] = st.text_input("Valor", met["value"], key=f"t13_rim_v_{i}", label_visibility="collapsed")
                with c3: st.session_state.t13_ri_metrics[i]["delta"] = st.text_input("Delta", met["delta"], key=f"t13_rim_d_{i}", label_visibility="collapsed")
                with c4:
                    if len(st.session_state.t13_ri_metrics) > 1 and _del_btn(f"t13_rim_del_{i}"):
                        st.session_state.t13_ri_metrics.pop(i); st.rerun()
            if _add_btn("t13_rim_add", "＋ Adicionar métrica"):
                st.session_state.t13_ri_metrics.append({"label": "ACAO", "value": "R$ 0,00", "delta": "0%"}); st.rerun()

            st.caption("Cards RI *(Título | Descrição | Botão | URL)*")
            for i, card in enumerate(st.session_state.t13_ri_cards):
                with st.expander(f"Card RI {i+1}: {card['titulo']}"):
                    st.session_state.t13_ri_cards[i]["titulo"] = st.text_input("Título", card["titulo"], key=f"t13_ric_t_{i}")
                    st.session_state.t13_ri_cards[i]["desc"] = st.text_area("Descrição", card["desc"], key=f"t13_ric_d_{i}")
                    st.session_state.t13_ri_cards[i]["btn_texto"] = st.text_input("Texto Botão", card["btn_texto"], key=f"t13_ric_bt_{i}")
                    st.session_state.t13_ri_cards[i]["url"] = st.text_input("URL Botão", card["url"], key=f"t13_ric_u_{i}")
                    if len(st.session_state.t13_ri_cards) > 1 and _del_btn(f"t13_ric_del_{i}", "Remover card"):
                        st.session_state.t13_ri_cards.pop(i); st.rerun()
            if _add_btn("t13_ric_add", "＋ Adicionar card RI"):
                st.session_state.t13_ri_cards.append({"titulo": "NOVO", "desc": "...", "btn_texto": "VER", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé Completo</div>', unsafe_allow_html=True)
            for i, logo in enumerate(st.session_state.t13_foot_logos):
                st.session_state.t13_foot_logos[i]["valor"] = st.text_input("Logo Footer", logo["valor"], key=f"t13_fl_{i}")
            for i, desc in enumerate(st.session_state.t13_foot_descs):
                st.session_state.t13_foot_descs[i]["valor"] = st.text_area("Descrição Footer", desc["valor"], key=f"t13_fd_{i}")
            
            for i, col in enumerate(st.session_state.t13_foot_cols):
                with st.expander(f"Coluna Footer {i+1}: {col['titulo']}"):
                    st.session_state.t13_foot_cols[i]["titulo"] = st.text_input("Título Coluna", col["titulo"], key=f"t13_fc_ti_{i}")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1: st.session_state.t13_foot_cols[i]["links"][j]["texto"] = st.text_input("Texto", link["texto"], key=f"t13_fc_l_t_{i}_{j}", label_visibility="collapsed")
                        with c2: st.session_state.t13_foot_cols[i]["links"][j]["url"] = st.text_input("URL", link["url"], key=f"t13_fc_l_u_{i}_{j}", label_visibility="collapsed")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t13_fc_l_del_{i}_{j}"):
                                st.session_state.t13_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t13_fc_l_add_{i}", "＋ Adicionar link"):
                        st.session_state.t13_foot_cols[i]["links"].append({"texto": "Novo Link", "url": "#"}); st.rerun()
                    if len(st.session_state.t13_foot_cols) > 1 and _del_btn(f"t13_fc_del_{i}", "Remover coluna"):
                        st.session_state.t13_foot_cols.pop(i); st.rerun()
            if _add_btn("t13_fc_add", "＋ Adicionar coluna footer"):
                st.session_state.t13_foot_cols.append({"titulo": "NOVA COLUNA", "links": [{"texto": "Link", "url": "#"}]}); st.rerun()

            for i, copy in enumerate(st.session_state.t13_foot_copys):
                st.session_state.t13_foot_copys[i]["valor"] = st.text_input("Copyright", copy["valor"], key=f"t13_fcp_{i}")

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t13_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t13_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t13_obs_{i}", height=80,
                        placeholder="Ex: Mudar a imagem do hero para uma floresta...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t13_obs) > 1 and _del_btn(f"t13_obs_del_{i}"):
                        st.session_state.t13_obs.pop(i); st.rerun()
            if _add_btn("t13_obs_add", "＋ Adicionar observação"):
                st.session_state.t13_obs.append({"valor": ""}); st.rerun()

            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t13_send", type="primary"):
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
