import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img6.png"
TEMPLATE_NAME = "Template 6 — Alta Precisão (Bautz Style)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores Técnicas
        "t6_cores": [
            {"nome": "Cor de Destaque (Azul Técnico)", "valor": "#0047bb"},
            {"nome": "Cor de Fundo (Gray Soft)",       "valor": "#f5f5f7"},
            {"nome": "Cor do Texto (Deep Black)",      "valor": "#1a1a1a"},
        ],
        # Hero (Engenharia)
        "t6_hero_mono": [{"valor": "Codeless Architecture v2.0"}],
        "t6_hero_titulos": [{"valor": "SITES DE ALTA PRECISÃO."}],
        "t6_hero_subtitulos": [{"valor": "Desenvolva a sua presença digital com a eficiência de um processo industrial. Templates otimizados para velocidade, conversão e autonomia total."}],
        "t6_hero_btns": [{"texto": "CONFIGURAR AGORA", "url": "#catalogo"}],
        # Aplicações (Cards)
        "t6_apps_titulos": [{"valor": "APLICAÇÕES DO SISTEMA"}],
        # Catálogo de Componentes (Templates)
        "t6_cat_subtitulos": [{"valor": "// CATÁLOGO DE COMPONENTES"}],
        "t6_cat_titulos": [{"valor": "MODELOS DISPONÍVEIS"}],
        "t6_cat_items": [
            {"nome": "STRUCTURAL MINIMAL", "ref": "BTZ-01", "img": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=600", "desc": "Estrutura modular com 100% de pontuação no Core Web Vitals.", "url": "#", "btn_txt": "INSPECIONAR BTZ-01"},
            {"nome": "DYNAMIC FLOW",        "ref": "BTZ-02", "img": "https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=600", "desc": "Estrutura modular com 100% de pontuação no Core Web Vitals.", "url": "#", "btn_txt": "INSPECIONAR BTZ-02"},
            {"nome": "CORPORATE CORE",      "ref": "BTZ-03", "img": "https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=600", "desc": "Estrutura modular com 100% de pontuação no Core Web Vitals.", "url": "#", "btn_txt": "INSPECIONAR BTZ-03"},
        ],
        # Logos de Confiança
        "t6_logos_titulos": [{"valor": "TRUSTED BY INDUSTRY LEADERS:"}],
        "t6_logos": [
            {"valor": "MATTEL"}, {"valor": "SIEMENS"}, {"valor": "BMW"}, {"valor": "BASF"},
        ],
        # Aplicações (Cards)
        "t6_apps": [
            {"num": "01", "label": "AUTONOMIA",    "titulo": "Crie e customize em minutos sem depender de terceiros ou agências lentas."},
            {"num": "02", "label": "RENTABILIDADE", "titulo": "Venda sites profissionais com margem de lucro industrial para o mercado B2B."},
            {"num": "03", "label": "PERFORMANCE",  "titulo": "Aumente a conversão dos seus produtos com layouts validados por testes de stress."},
        ],
        # Fluxo de Implementação (Workflow)
        "t6_flow_titulos": [{"valor": "FLUXO DE IMPLEMENTAÇÃO"}],
        "t6_flow": [
            {"num": "01", "titulo": "AQUISIÇÃO DO MÓDULO", "desc": "Acesso imediato ao repositório de códigos fonte após a validação."},
            {"num": "02", "titulo": "ASSEMBLY (MONTAGEM)", "desc": "Substitua textos e imagens seguindo o nosso manual de diretrizes visuais."},
            {"num": "03", "titulo": "DEPLOYMENT",          "desc": "Conecte o seu domínio e publique o site em servidores de alta velocidade."},
            {"num": "04", "titulo": "OPERAÇÃO",            "desc": "Seu site está pronto para gerar resultados com manutenção zero."},
        ],
        # Planos Industriais
        "t6_planos_titulos": [{"valor": "PLANOS DE ACESSO"}],
        "t6_planos": [
            {"nome": "BASIC UNIT", "valor": "R$ 97",  "features": "1 Template Modular\nManual de Montagem", "btn_txt": "ADQUIRIR BASIC", "url": "#", "destaque": False},
            {"nome": "FULL STACK",  "valor": "R$ 197", "features": "Todos os Templates\nSuporte Técnico Direto\nUpdates de Engenharia", "btn_txt": "ADQUIRIR FULL", "url": "#", "destaque": True},
            {"nome": "ENTERPRISE", "valor": "R$ 497", "features": "Licença Comercial\nWhitelabel Ready\nConsultoria de Deploy", "btn_txt": "ADQUIRIR ENTERPRISE", "url": "#", "destaque": False},
        ],
        # FAQ
        "t6_faqs": [
            {"pergunta": "O CÓDIGO É OTIMIZADO PARA SEO?", "resposta": "Sim, todos os modelos seguem a semântica correta de HTML5 para máxima indexação."},
            {"pergunta": "POSSO ALTERAR AS CORES E FONTES?", "resposta": "Absolutamente. O sistema é modular e permite alterações rápidas no ficheiro de estilos."},
        ],
        # Footer
        "t6_footer_left":  [{"valor": "SITE PRO / ENGINEERING DIVISION"}],
        "t6_footer_right": [{"valor": "BUILD_V.4.0.1"}],
        # Observações
        "t6_obs": [{"valor": ""}],
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
            st.markdown('<div class="section-label">🎨 Cores Industriais</div>', unsafe_allow_html=True)
            for i, cor in enumerate(st.session_state.t6_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t6_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t6_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t6_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t6_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t6_cores) > 1 and _del_btn(f"t6_cor_del_{i}"):
                        st.session_state.t6_cores.pop(i); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏗️ Hero (Engenharia)</div>', unsafe_allow_html=True)
            st.caption("Label Mono")
            for i, m in enumerate(st.session_state.t6_hero_mono):
                st.session_state.t6_hero_mono[i]["valor"] = st.text_input("Mono Label", m["valor"], key=f"t6_h_m_{i}")

            st.caption("Título")
            for i, t in enumerate(st.session_state.t6_hero_titulos):
                st.session_state.t6_hero_titulos[i]["valor"] = st.text_input("Título", t["valor"], key=f"t6_h_t_{i}")

            st.caption("Descrição do Hero")
            for i, s in enumerate(st.session_state.t6_hero_subtitulos):
                st.session_state.t6_hero_subtitulos[i]["valor"] = st.text_area("Descrição do Hero", s["valor"], key=f"t6_h_s_{i}")
            
            st.caption("Botão do Hero *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t6_hero_btns):
                c1, c2 = st.columns([5, 5])
                with c1: st.session_state.t6_hero_btns[i]["texto"] = st.text_input("Texto", btn["texto"], key=f"t6_h_btn_t_{i}")
                with c2: st.session_state.t6_hero_btns[i]["url"] = st.text_input("URL", btn["url"], key=f"t6_h_btn_u_{i}")

            # ══════════════════════════════════════════════════════════════════
            # CATÁLOGO (TEMPLATES)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📦 Catálogo de Componentes</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t6_cat_subtitulos):
                st.session_state.t6_cat_subtitulos[i]["valor"] = st.text_input("Subtítulo da Seção", t["valor"], key=f"t6_cat_sub_{i}")
            for i, t in enumerate(st.session_state.t6_cat_titulos):
                st.session_state.t6_cat_titulos[i]["valor"] = st.text_input("Título da Seção", t["valor"], key=f"t6_cat_t_{i}")
            
            for i, item in enumerate(st.session_state.t6_cat_items):
                with st.expander(f"Componente {i+1}: {item['nome']}"):
                    st.session_state.t6_cat_items[i]["nome"] = st.text_input("Nome", item["nome"], key=f"t6_ci_n_{i}")
                    st.session_state.t6_cat_items[i]["ref"] = st.text_input("REF (Código)", item["ref"], key=f"t6_ci_r_{i}")
                    st.session_state.t6_cat_items[i]["img"] = st.text_input("URL Imagem", item["img"], key=f"t6_ci_i_{i}")
                    st.session_state.t6_cat_items[i]["desc"] = st.text_area("Descrição", item["desc"], key=f"t6_ci_d_{i}")
                    st.session_state.t6_cat_items[i]["btn_txt"] = st.text_input("Texto Botão", item["btn_txt"], key=f"t6_ci_bt_{i}")
                    st.session_state.t6_cat_items[i]["url"] = st.text_input("URL Botão", item["url"], key=f"t6_ci_u_{i}")
                    if len(st.session_state.t6_cat_items) > 1 and _del_btn(f"t6_ci_del_{i}", "Remover Componente"):
                        st.session_state.t6_cat_items.pop(i); st.rerun()
            if _add_btn("t6_ci_add", "＋ Adicionar Componente"):
                st.session_state.t6_cat_items.append({"nome": "NOVO MODELO", "ref": "BTZ-00", "img": "", "desc": "...", "btn_txt": "INSPECIONAR", "url": "#"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # LOGOS DE CONFIANÇA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🤝 Marcas de Confiança</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t6_logos_titulos):
                st.session_state.t6_logos_titulos[i]["valor"] = st.text_input("Título da Seção", t["valor"], key=f"t6_l_t_{i}")
            for i, logo in enumerate(st.session_state.t6_logos):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t6_logos[i]["valor"] = st.text_input("Marca", logo["valor"], key=f"t6_l_v_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_logos) > 1 and _del_btn(f"t6_l_del_{i}"):
                        st.session_state.t6_logos.pop(i); st.rerun()
            if _add_btn("t6_l_add", "＋ Adicionar Marca"):
                st.session_state.t6_logos.append({"valor": "NOVA MARCA"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # APLICAÇÕES (CARDS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💡 Aplicações do Sistema</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t6_apps_titulos):
                st.session_state.t6_apps_titulos[i]["valor"] = st.text_input("Título da Seção (Aplicações)", t["valor"], key=f"t6_apps_t_{i}")
            
            for i, app in enumerate(st.session_state.t6_apps):
                with st.expander(f"Aplicação {app['num']}: {app['label']}"):
                    st.session_state.t6_apps[i]["num"] = st.text_input("Número", app["num"], key=f"t6_a_n_{i}")
                    st.session_state.t6_apps[i]["label"] = st.text_input("Rótulo", app["label"], key=f"t6_a_l_{i}")
                    st.session_state.t6_apps[i]["titulo"] = st.text_area("Descrição", app["titulo"], key=f"t6_a_t_{i}")
                    if len(st.session_state.t6_apps) > 1 and _del_btn(f"t6_a_del_{i}", "Remover"):
                        st.session_state.t6_apps.pop(i); st.rerun()
            if _add_btn("t6_a_add", "＋ Adicionar Aplicação"):
                st.session_state.t6_apps.append({"num": "04", "label": "NOVO", "titulo": "..."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FLUXO (WORKFLOW)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔄 Fluxo de Implementação</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t6_flow_titulos):
                st.session_state.t6_flow_titulos[i]["valor"] = st.text_input("Título da Seção", t["valor"], key=f"t6_f_t_{i}")
            for i, f in enumerate(st.session_state.t6_flow):
                with st.expander(f"Passo {f['num']}: {f['titulo']}"):
                    st.session_state.t6_flow[i]["num"] = st.text_input("Número", f["num"], key=f"t6_f_n_{i}")
                    st.session_state.t6_flow[i]["titulo"] = st.text_input("Título", f["titulo"], key=f"t6_f_ti_{i}")
                    st.session_state.t6_flow[i]["desc"] = st.text_area("Descrição", f["desc"], key=f"t6_f_d_{i}")
                    if len(st.session_state.t6_flow) > 1 and _del_btn(f"t6_f_del_{i}", "Remover Passo"):
                        st.session_state.t6_flow.pop(i); st.rerun()
            if _add_btn("t6_f_add", "＋ Adicionar Passo ao Fluxo"):
                st.session_state.t6_flow.append({"num": "05", "titulo": "NOVO PASSO", "desc": "..."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # PLANOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💳 Planos Industriais</div>', unsafe_allow_html=True)
            for i, t in enumerate(st.session_state.t6_planos_titulos):
                st.session_state.t6_planos_titulos[i]["valor"] = st.text_input("Título da Seção", t["valor"], key=f"t6_p_t_{i}")
            for i, plano in enumerate(st.session_state.t6_planos):
                with st.expander(f"Plano: {plano['nome']}"):
                    st.session_state.t6_planos[i]["nome"] = st.text_input("Nome", plano["nome"], key=f"t6_p_n_{i}")
                    st.session_state.t6_planos[i]["valor"] = st.text_input("Valor", plano["valor"], key=f"t6_p_v_{i}")
                    st.session_state.t6_planos[i]["features"] = st.text_area("Features (uma por linha)", plano["features"], key=f"t6_p_f_{i}")
                    st.session_state.t6_planos[i]["btn_txt"] = st.text_input("Texto Botão", plano["btn_txt"], key=f"t6_p_bt_{i}")
                    st.session_state.t6_planos[i]["url"] = st.text_input("URL Botão", plano["url"], key=f"t6_p_u_{i}")
                    st.session_state.t6_planos[i]["destaque"] = st.checkbox("Destaque", plano["destaque"], key=f"t6_p_d_{i}")
                    if len(st.session_state.t6_planos) > 1 and _del_btn(f"t6_p_del_{i}", "Remover Plano"):
                        st.session_state.t6_planos.pop(i); st.rerun()
            if _add_btn("t6_p_add", "＋ Adicionar Plano"):
                st.session_state.t6_planos.append({"nome": "NOVO PLANO", "valor": "R$ 0", "features": "...", "btn_txt": "ASSINAR", "url": "#", "destaque": False}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # FAQ
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">❓ Perguntas Frequentes</div>', unsafe_allow_html=True)
            for i, faq in enumerate(st.session_state.t6_faqs):
                with st.expander(f"FAQ {i+1}: {faq['pergunta'][:30]}..."):
                    st.session_state.t6_faqs[i]["pergunta"] = st.text_input("Pergunta", faq["pergunta"], key=f"t6_faq_p_{i}")
                    st.session_state.t6_faqs[i]["resposta"] = st.text_area("Resposta", faq["resposta"], key=f"t6_faq_r_{i}")
                    if len(st.session_state.t6_faqs) > 1 and _del_btn(f"t6_faq_del_{i}", "Remover Pergunta"):
                        st.session_state.t6_faqs.pop(i); st.rerun()
            if _add_btn("t6_faq_add", "＋ Adicionar Pergunta"):
                st.session_state.t6_faqs.append({"pergunta": "NOVA PERGUNTA", "resposta": "..."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # RODAPÉ
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏁 Rodapé</div>', unsafe_allow_html=True)
            st.caption("Texto do Rodapé (Esquerda)")
            for i, f in enumerate(st.session_state.t6_footer_left):
                st.session_state.t6_footer_left[i]["valor"] = st.text_input("Esquerda", f["valor"], key=f"t6_fl_{i}")
            st.caption("Texto do Rodapé (Direita)")
            for i, f in enumerate(st.session_state.t6_footer_right):
                st.session_state.t6_footer_right[i]["valor"] = st.text_input("Direita", f["valor"], key=f"t6_fr_{i}")

    with col_preview:
        st.markdown('<div class="panel-title">👁️ Visualização Real</div>', unsafe_allow_html=True)
        st.markdown('<div class="panel-subtitle">Interface do usuário final</div>', unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown(f'''
            <div class="template-img-wrapper">
                <div class="img-caption">Visualização do Template Selecionado</div>
                <img src="{TEMPLATE_IMAGE_URL}" alt="Preview do Template">
            </div>
            ''', unsafe_allow_html=True)
            st.info("💡 As alterações feitas no editor serão aplicadas ao código final do seu site.")

if __name__ == "__main__":
    render()
