import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img8.png"
TEMPLATE_NAME = "Template 8 — Patrus Tech (Logística & Inovação)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores Patrus
        "t8_cores": [
            {"nome": "Cor Principal (Laranja)", "valor": "#ff6b00"},
            {"nome": "Cor de Fundo (Dark)",     "valor": "#1a1a1a"},
            {"nome": "Cor de Texto Principal", "valor": "#333333"},
            {"nome": "Cor Neutra (Gray)",      "valor": "#f4f4f4"},
        ],
        # Navbar
        "t8_logos": [{"valor": "PATRUS TECH"}],
        "t8_nav_links": [
            {"texto": "SOLUÇÕES",  "url": "#ecossistema"},
            {"texto": "TECNOLOGIA", "url": "#diferenciais"},
            {"texto": "TRACKING",   "url": "#verticais"},
        ],
        # Hero
        "t8_hero_labels": [{"valor": "Inovação em Movimento"}],
        "t8_hero_titulos": [{"valor": "TECNOLOGIA QUE IMPULSIONA A <span class=\"highlight\">LOGÍSTICA DO FUTURO.</span>"}],
        "t8_hero_descs": [{"valor": "Dados em tempo real, inteligência artificial e a maior frota conectada do país."}],
        "t8_hero_btns": [{"texto": "CONHEÇA NOSSAS SOLUÇÕES", "url": "#ecossistema"}],
        # Ecossistema Digital (Tecnologias)
        "t8_eco_titulos": [{"valor": "ECOSSISTEMA <span class=\"highlight\">DIGITAL</span>"}],
        "t8_eco_cards": [
            {"titulo": "Telemetria Avançada", "desc": "Monitoramento em tempo real de cada unidade da frota, garantindo segurança e pontualidade.", "img": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=600", "url": "https://www.google.com/"},
            {"titulo": "IA de Roteirização",  "desc": "Algoritmos complexos que otimizam rotas para redução de custos e emissão de CO2.", "img": "https://images.unsplash.com/photo-1518770660439-4636190af475?w=600", "url": "https://www.google.com/"},
            {"titulo": "Gestão 360°",         "desc": "Painéis de BI exclusivos para clientes com transparência total sobre a operação.", "img": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600", "url": "https://www.google.com/"},
        ],
        # Estatísticas (Stats)
        "t8_stats": [
            {"valor": "+85",  "label": "CIDADES ATENDIDAS"},
            {"valor": "3.5k", "label": "VEÍCULOS CONECTADOS"},
            {"valor": "100%", "label": "RASTREAMENTO"},
        ],
        # Diferenciais (Por que a Patrus Tech?)
        "t8_diff_titulos": [{"valor": "POR QUE A <span class=\"highlight\">PATRUS TECH?</span>"}],
        "t8_diff_items": [
            {"num": "01", "titulo": "SEGURANÇA DE DADOS",    "desc": "Infraestrutura em nuvem com criptografia de ponta a ponta."},
            {"num": "02", "titulo": "EFICIÊNCIA OPERACIONAL", "desc": "Redução comprovada de 20% no tempo de entrega via otimização digital."},
            {"num": "03", "titulo": "SUSTENTABILIDADE TECH", "desc": "Uso de tecnologia para monitoramento e compensação de carbono."},
            {"num": "04", "titulo": "SUPORTE ESPECIALIZADO", "desc": "Equipe de engenharia de dados disponível para integrações via API."},
        ],
        # Verticais (Serviços/Planos)
        "t8_vert_titulos": [{"valor": "NOSSAS VERTICAIS"}],
        "t8_vert_cards": [
            {"titulo": "LOGÍSTICA 4.0", "desc": "Sistemas integrados de gestão de armazém e transporte.", "url": "https://www.google.com/", "destaque": False},
            {"titulo": "API CONNECT",   "desc": "Integração direta com o seu ERP para automação total.", "url": "https://www.google.com/", "destaque": True},
            {"titulo": "BI ANALYTICS",  "desc": "Decisões baseadas em dados históricos e preditivos.", "url": "https://www.google.com/", "destaque": False},
        ],
        # Footer
        "t8_footer_logos": [{"valor": "PATRUS <span style=\"color:#ff6b00\">TECH</span>"}],
        "t8_footer_copys": [{"valor": "© 2026 Patrus Transportes. Inovação em cada quilômetro."}],
        # Observações
        "t8_obs": [{"valor": ""}],
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
            st.markdown('<div class="section-label">🎨 Identidade Patrus</div>', unsafe_allow_html=True)
            for i, cor in enumerate(st.session_state.t8_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t8_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t8_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t8_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t8_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t8_cores) > 1 and _del_btn(f"t8_cor_del_{i}"):
                        st.session_state.t8_cores.pop(i); st.rerun()
            if _add_btn("t8_cor_add", "＋ Adicionar cor"):
                st.session_state.t8_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)
            st.caption("Logo Tech")
            for i, logo in enumerate(st.session_state.t8_logos):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t8_logos[i]["valor"] = st.text_input("Logo", logo["valor"], key=f"t8_logo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t8_logos) > 1 and _del_btn(f"t8_logo_del_{i}"):
                        st.session_state.t8_logos.pop(i); st.rerun()
            
            st.caption("Links do Menu *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t8_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t8_nav_links[i]["texto"] = st.text_input("Texto", link["texto"], key=f"t8_nl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t8_nav_links[i]["url"] = st.text_input("URL", link["url"], key=f"t8_nl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t8_nav_links) > 1 and _del_btn(f"t8_nl_del_{i}"):
                        st.session_state.t8_nav_links.pop(i); st.rerun()
            if _add_btn("t8_nl_add", "＋ Adicionar link"):
                st.session_state.t8_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🚛 Hero (Inovação)</div>', unsafe_allow_html=True)
            for i, label in enumerate(st.session_state.t8_hero_labels):
                st.session_state.t8_hero_labels[i]["valor"] = st.text_input("Label", label["valor"], key=f"t8_h_l_{i}")
            for i, t in enumerate(st.session_state.t8_hero_titulos):
                st.session_state.t8_hero_titulos[i]["valor"] = st.text_area("Título (use <span class=\"highlight\">)", t["valor"], key=f"t8_h_t_{i}")
            for i, d in enumerate(st.session_state.t8_hero_descs):
                st.session_state.t8_hero_descs[i]["valor"] = st.text_area("Descrição", d["valor"], key=f"t8_h_d_{i}")
            
            st.caption("Botões do Hero *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t8_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t8_hero_btns[i]["texto"] = st.text_input("Texto", btn["texto"], key=f"t8_hb_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t8_hero_btns[i]["url"] = st.text_input("URL", btn["url"], key=f"t8_hb_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t8_hero_btns) > 1 and _del_btn(f"t8_hb_del_{i}"):
                        st.session_state.t8_hero_btns.pop(i); st.rerun()
            if _add_btn("t8_hb_add", "＋ Adicionar botão hero"):
                st.session_state.t8_hero_btns.append({"texto": "BOTÃO", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # ECOSSISTEMA DIGITAL (TECNOLOGIAS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌐 Ecossistema Digital</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t8_eco_titulos):
                st.session_state.t8_eco_titulos[i]["valor"] = st.text_input("Título Seção", t["valor"], key=f"t8_et_{i}")
            
            for i, card in enumerate(st.session_state.t8_eco_cards):
                with st.expander(f"Tecnologia {i+1}: {card['titulo']}"):
                    st.session_state.t8_eco_cards[i]["titulo"] = st.text_input("Título", card["titulo"], key=f"t8_ec_t_{i}")
                    st.session_state.t8_eco_cards[i]["img"] = st.text_input("URL Imagem", card["img"], key=f"t8_ec_i_{i}")
                    st.session_state.t8_eco_cards[i]["desc"] = st.text_area("Descrição", card["desc"], key=f"t8_ec_d_{i}")
                    st.session_state.t8_eco_cards[i]["url"] = st.text_input("URL Botão", card["url"], key=f"t8_ec_u_{i}")
                    if len(st.session_state.t8_eco_cards) > 1 and _del_btn(f"t8_ec_del_{i}", "Remover card"):
                        st.session_state.t8_eco_cards.pop(i); st.rerun()
            if _add_btn("t8_ec_add", "＋ Adicionar tecnologia"):
                st.session_state.t8_eco_cards.append({"titulo": "Nova Tech", "desc": "...", "img": "", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # STATS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Estatísticas Operacionais</div>', unsafe_allow_html=True)
            for i, stat in enumerate(st.session_state.t8_stats):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t8_stats[i]["valor"] = st.text_input("Valor", stat["valor"], key=f"t8_st_v_{i}", label_visibility="collapsed")
                with c2: st.session_state.t8_stats[i]["label"] = st.text_input("Rótulo", stat["label"], key=f"t8_st_l_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t8_stats) > 1 and _del_btn(f"t8_st_del_{i}"):
                        st.session_state.t8_stats.pop(i); st.rerun()
            if _add_btn("t8_st_add", "＋ Adicionar estatística"):
                st.session_state.t8_stats.append({"valor": "0", "label": "NOVO DADO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # DIFERENCIAIS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏆 Diferenciais Competitivos</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t8_diff_titulos):
                st.session_state.t8_diff_titulos[i]["valor"] = st.text_input("Título Diferenciais", t["valor"], key=f"t8_dt_{i}")
            
            for i, item in enumerate(st.session_state.t8_diff_items):
                with st.expander(f"Diferencial {item['num']}: {item['titulo']}"):
                    st.session_state.t8_diff_items[i]["num"] = st.text_input("Número", item["num"], key=f"t8_di_n_{i}")
                    st.session_state.t8_diff_items[i]["titulo"] = st.text_input("Título", item["titulo"], key=f"t8_di_t_{i}")
                    st.session_state.t8_diff_items[i]["desc"] = st.text_area("Descrição", item["desc"], key=f"t8_di_d_{i}")
                    if len(st.session_state.t8_diff_items) > 1 and _del_btn(f"t8_di_del_{i}", "Remover item"):
                        st.session_state.t8_diff_items.pop(i); st.rerun()
            if _add_btn("t8_di_add", "＋ Adicionar diferencial"):
                st.session_state.t8_diff_items.append({"num": "05", "titulo": "Novo Diferencial", "desc": "..."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # VERTICAIS (SERVIÇOS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🛣️ Nossas Verticais (Serviços)</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t8_vert_titulos):
                st.session_state.t8_vert_titulos[i]["valor"] = st.text_input("Título Verticais", t["valor"], key=f"t8_vt_{i}")
            
            for i, card in enumerate(st.session_state.t8_vert_cards):
                with st.expander(f"Vertical {i+1}: {card['titulo']}"):
                    st.session_state.t8_vert_cards[i]["titulo"] = st.text_input("Título", card["titulo"], key=f"t8_vc_t_{i}")
                    st.session_state.t8_vert_cards[i]["desc"] = st.text_area("Descrição", card["desc"], key=f"t8_vc_d_{i}")
                    st.session_state.t8_vert_cards[i]["url"] = st.text_input("URL Botão", card["url"], key=f"t8_vc_u_{i}")
                    st.session_state.t8_vert_cards[i]["destaque"] = st.checkbox("Destaque (Borda Laranja)", value=card["destaque"], key=f"t8_vc_dt_{i}")
                    if len(st.session_state.t8_vert_cards) > 1 and _del_btn(f"t8_vc_del_{i}", "Remover vertical"):
                        st.session_state.t8_vert_cards.pop(i); st.rerun()
            if _add_btn("t8_vc_add", "＋ Adicionar vertical"):
                st.session_state.t8_vert_cards.append({"titulo": "Nova Vertical", "desc": "...", "url": "#", "destaque": False}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)
            for i, logo in enumerate(st.session_state.t8_footer_logos):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t8_footer_logos[i]["valor"] = st.text_input("Logo Rodapé", logo["valor"], key=f"t8_flogo_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t8_footer_logos) > 1 and _del_btn(f"t8_flogo_del_{i}"):
                        st.session_state.t8_footer_logos.pop(i); st.rerun()
            if _add_btn("t8_flogo_add", "＋ Adicionar logo rodapé"):
                st.session_state.t8_footer_logos.append({"valor": "NOVA LOGO"}); st.rerun()

            for i, copy in enumerate(st.session_state.t8_footer_copys):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t8_footer_copys[i]["valor"] = st.text_input("Copyright", copy["valor"], key=f"t8_fcopy_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t8_footer_copys) > 1 and _del_btn(f"t8_fcopy_del_{i}"):
                        st.session_state.t8_footer_copys.pop(i); st.rerun()
            if _add_btn("t8_fcopy_add", "＋ Adicionar copyright"):
                st.session_state.t8_footer_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t8_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t8_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t8_obs_{i}", height=80,
                        placeholder="Ex: Mudar a imagem de fundo do hero...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t8_obs) > 1 and _del_btn(f"t8_obs_del_{i}"):
                        st.session_state.t8_obs.pop(i); st.rerun()
            if _add_btn("t8_obs_add", "＋ Adicionar observação"):
                st.session_state.t8_obs.append({"valor": ""}); st.rerun()

            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t8_send", type="primary"):
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
