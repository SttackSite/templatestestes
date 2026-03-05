import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img6.png"
TEMPLATE_NAME = "Template 6 — Alta Precisão (Bautz Style )"


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
        
        # Catálogo de Componentes (Templates)
        "t6_cat_label": [{"valor": "// CATÁLOGO DE COMPONENTES"}],
        "t6_cat_titulos": [{"valor": "MODELOS DISPONÍVEIS"}],
        "t6_cat_items": [
            {"nome": "STRUCTURAL MINIMAL", "ref": "BTZ-01", "img": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=600", "desc": "Estrutura modular com 100% de pontuação no Core Web Vitals.", "btn_txt": "INSPECIONAR BTZ-01", "url": "#"},
            {"nome": "DYNAMIC FLOW",        "ref": "BTZ-02", "img": "https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=600", "desc": "Estrutura modular com 100% de pontuação no Core Web Vitals.", "btn_txt": "INSPECIONAR BTZ-02", "url": "#"},
            {"nome": "CORPORATE CORE",      "ref": "BTZ-03", "img": "https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=600", "desc": "Estrutura modular com 100% de pontuação no Core Web Vitals.", "btn_txt": "INSPECIONAR BTZ-03", "url": "#"},
        ],
        
        # Logos de Confiança
        "t6_logos_label": [{"valor": "TRUSTED BY INDUSTRY LEADERS:"}],
        "t6_logos": [
            {"valor": "MATTEL"}, {"valor": "SIEMENS"}, {"valor": "BMW"}, {"valor": "BASF"},
        ],
        
        # Aplicações (Cards )
        "t6_apps_titulo": [{"valor": "APLICAÇÕES DO SISTEMA"}],
        "t6_apps": [
            {"num": "01", "label": "AUTONOMIA",    "titulo": "Crie e customize em minutos sem depender de terceiros ou agências lentas."},
            {"num": "02", "label": "RENTABILIDADE", "titulo": "Venda sites profissionais com margem de lucro industrial para o mercado B2B."},
            {"num": "03", "label": "PERFORMANCE",  "titulo": "Aumente a conversão dos seus produtos com layouts validados por testes de stress."},
        ],
        
        # Fluxo de Implementação (Workflow)
        "t6_flow_titulo": [{"valor": "Fluxo de Implementação"}],
        "t6_flow": [
            {"num": "01", "titulo": "AQUISIÇÃO DO MÓDULO", "desc": "Acesso imediato ao repositório de códigos fonte após a validação."},
            {"num": "02", "titulo": "ASSEMBLY (MONTAGEM)", "desc": "Substitua textos e imagens seguindo o nosso manual de diretrizes visuais."},
            {"num": "03", "titulo": "DEPLOYMENT",          "desc": "Conecte o seu domínio e publique o site em servidores de alta velocidade."},
            {"num": "04", "titulo": "OPERAÇÃO",            "desc": "Seu site está pronto para gerar resultados com manutenção zero."},
        ],
        
        # Planos Industriais
        "t6_planos_titulo": [{"valor": "PLANOS DE ACESSO"}],
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
        "t6_footer_center": [{"valor": "© 2026 ALL RIGHTS RESERVED"}],
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

def _render_editable_list(session_key, fields, expander_title_field, add_button_label, default_item):
    st.markdown(f'<div class="section-label">{add_button_label.replace("＋ Adicionar ", "")}</div>', unsafe_allow_html=True)
    
    for i, item in enumerate(st.session_state[session_key]):
        expander_title = f"{expander_title_field} {i+1}: {item.get(expander_title_field.lower(), '')}"
        with st.expander(expander_title):
            for field_key, (field_type, field_label, *field_options) in fields.items():
                if field_type == "text_input":
                    st.session_state[session_key][i][field_key] = st.text_input(field_label, item[field_key], key=f"{session_key}_{i}_{field_key}")
                elif field_type == "text_area":
                    st.session_state[session_key][i][field_key] = st.text_area(field_label, item[field_key], key=f"{session_key}_{i}_{field_key}")
                elif field_type == "checkbox":
                    st.session_state[session_key][i][field_key] = st.checkbox(field_label, value=item[field_key], key=f"{session_key}_{i}_{field_key}")

            if len(st.session_state[session_key]) > 1 and _del_btn(f"{session_key}_del_{i}", f"Remover {expander_title_field}"):
                st.session_state[session_key].pop(i)
                st.rerun()

    if _add_btn(f"{session_key}_add", add_button_label):
        st.session_state[session_key].append(default_item)
        st.rerun()

def _render_single_editable(session_key, field_key, label):
    if session_key not in st.session_state:
        return
    for i, item in enumerate(st.session_state[session_key]):
        st.session_state[session_key][i][field_key] = st.text_input(label, item[field_key], key=f"{session_key}_{i}_{field_key}")

# ─────────────────────────────────────────────────────────────────────────────
# RENDER PRINCIPAL
# ─────────────────────────────────────────────────────────────────────────────
def render():
    _init()

    # CSS Styles
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap' );
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
        
        /* Estilos para o Preview (simulando o site final) */
        .preview-container { padding: 40px; background-color: white; color: #1a1a1a; }
        .preview-hero-mono { font-size: 14px; font-weight: 600; color: #555; margin-bottom: 10px; text-transform: uppercase; }
        .preview-hero-title { font-size: 48px; font-weight: 700; line-height: 1.1; margin-bottom: 20px; }
        .preview-hero-subtitle { font-size: 18px; color: #555; max-width: 600px; margin-bottom: 30px; }
        .preview-section-title { font-size: 24px; font-weight: 700; text-align: center; margin: 60px 0 30px; }
        .preview-section-label { font-size: 12px; font-weight: 600; color: #999; text-align: center; margin-bottom: 10px; }

    </style>
    """, unsafe_allow_html=True)

    col_form, col_preview = st.columns([1, 2], gap="medium")

    # ════════════════════════════════════════════════════════════════════════
    # PAINEL ESQUERDO — FORMULÁRIO DE EDIÇÃO
    # ════════════════════════════════════════════════════════════════════════
    with col_form:
        st.markdown('<div class="panel-title">✏️ Editor de Template</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="panel-subtitle">{TEMPLATE_NAME}</div>', unsafe_allow_html=True)

        with st.container(height=720, border=False):
            
            st.markdown('<div class="section-label">🎨 Cores Industriais</div>', unsafe_allow_html=True)
            for i, cor in enumerate(st.session_state.t6_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t6_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t6_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t6_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t6_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t6_cores) > 1 and _del_btn(f"t6_cor_del_{i}"):
                        st.session_state.t6_cores.pop(i); st.rerun()

            st.markdown('<div class="section-label">🏗️ Hero (Engenharia)</div>', unsafe_allow_html=True)
            _render_single_editable("t6_hero_mono", "valor", "Mono Label")
            _render_single_editable("t6_hero_titulos", "valor", "Título Principal")
            _render_single_editable("t6_hero_subtitulos", "valor", "Subtítulo")
            st.caption("Botão do Hero *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t6_hero_btns):
                c1, c2 = st.columns([5, 5])
                with c1: st.session_state.t6_hero_btns[i]["texto"] = st.text_input("Texto", btn["texto"], key=f"t6_h_btn_t_{i}")
                with c2: st.session_state.t6_hero_btns[i]["url"] = st.text_input("URL", btn["url"], key=f"t6_h_btn_u_{i}")

            st.markdown('<div class="section-label">📦 Catálogo de Componentes</div>', unsafe_allow_html=True)
            _render_single_editable("t6_cat_label", "valor", "Label da Seção (Ex: // CATÁLOGO)")
            _render_single_editable("t6_cat_titulos", "valor", "Título da Seção")
            _render_editable_list(
                "t6_cat_items",
                {"nome": ("text_input", "Nome"), "ref": ("text_input", "REF (Código)"), "img": ("text_input", "URL Imagem"), "desc": ("text_area", "Descrição"), "btn_txt": ("text_input", "Texto do Botão"), "url": ("text_input", "URL Botão")},
                "Componente", "＋ Adicionar Componente",
                {"nome": "NOVO MODELO", "ref": "BTZ-00", "img": "", "desc": "...", "btn_txt": "INSPECIONAR", "url": "#"}
            )

            st.markdown('<div class="section-label">🤝 Marcas de Confiança</div>', unsafe_allow_html=True)
            _render_single_editable("t6_logos_label", "valor", "Título da Seção (Ex: TRUSTED BY)")
            for i, logo in enumerate(st.session_state.t6_logos):
                c1, c2 = st.columns([9, 1])
                with c1: st.session_state.t6_logos[i]["valor"] = st.text_input("Marca", logo["valor"], key=f"t6_l_v_{i}", label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_logos) > 1 and _del_btn(f"t6_l_del_{i}"):
                        st.session_state.t6_logos.pop(i); st.rerun()
            if _add_btn("t6_l_add", "＋ Adicionar Marca"):
                st.session_state.t6_logos.append({"valor": "NOVA MARCA"}); st.rerun()

            st.markdown('<div class="section-label">🛠️ Aplicações do Sistema</div>', unsafe_allow_html=True)
            _render_single_editable("t6_apps_titulo", "valor", "Título da Seção")
            _render_editable_list(
                "t6_apps",
                {"num": ("text_input", "Número"), "label": ("text_input", "Rótulo"), "titulo": ("text_area", "Descrição")},
                "Aplicação", "＋ Adicionar Aplicação",
                {"num": "04", "label": "NOVO", "titulo": "..."}
            )

            st.markdown('<div class="section-label">⚙️ Fluxo de Implementação</div>', unsafe_allow_html=True)
            _render_single_editable("t6_flow_titulo", "valor", "Título da Seção")
            _render_editable_list(
                "t6_flow",
                {"num": ("text_input", "Número"), "titulo": ("text_input", "Título"), "desc": ("text_area", "Descrição")},
                "Passo", "＋ Adicionar Passo",
                {"num": "05", "titulo": "NOVO", "desc": "..."}
            )

            st.markdown('<div class="section-label">💰 Planos de Acesso</div>', unsafe_allow_html=True)
            _render_single_editable("t6_planos_titulo", "valor", "Título da Seção")
            _render_editable_list(
                "t6_planos",
                {"nome": ("text_input", "Nome"), "valor": ("text_input", "Preço"), "features": ("text_area", "Features (uma por linha)"), "btn_txt": ("text_input", "Texto Botão"), "url": ("text_input", "URL Botão"), "destaque": ("checkbox", "Destaque (Fundo Preto)")},
                "Plano", "＋ Adicionar Plano",
                {"nome": "NOVO", "valor": "R$ 0", "features": "...", "btn_txt": "ADQUIRIR", "url": "#", "destaque": False}
            )

            st.markdown('<div class="section-label">❓ FAQ & Rodapé</div>', unsafe_allow_html=True)
            _render_editable_list(
                "t6_faqs",
                {"pergunta": ("text_input", "Pergunta"), "resposta": ("text_area", "Resposta")},
                "FAQ", "＋ Adicionar FAQ",
                {"pergunta": "Pergunta?", "resposta": "Resposta..."}
            )
            st.caption("Textos do Rodapé")
            _render_single_editable("t6_footer_left", "valor", "Footer Left")
            _render_single_editable("t6_footer_center", "valor", "Footer Center")
            _render_single_editable("t6_footer_right", "valor", "Footer Right")

            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            _render_single_editable("t6_obs", "valor", "Observações")

            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t6_send", type="primary"):
                st.success("✅ Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
                st.balloons()

    # ════════════════════════════════════════════════════════════════════════
    # PAINEL DIREITO — PREVIEW (AGORA COM OS NOVOS ELEMENTOS)
    # ════════════════════════════════════════════════════════════════════════
    with col_preview:
        st.markdown('<p class="img-caption">📌 Preview dinâmico do template — role para ver o site completo</p>', unsafe_allow_html=True)
        
        # Construindo o HTML do preview dinamicamente
        preview_html = '<div class="preview-container">'

        # Hero Section
        preview_html += f'<div class="preview-hero-mono">{st.session_state.t6_hero_mono[0]["valor"]}</div>'
        preview_html += f'<div class="preview-hero-title">{st.session_state.t6_hero_titulos[0]["valor"]}</div>'
        preview_html += f'<div class="preview-hero-subtitle">{st.session_state.t6_hero_subtitulos[0]["valor"]}</div>'
        # Adicione aqui outros elementos do preview conforme necessário...

        # Catálogo Section
        preview_html += f'<div class="preview-section-label">{st.session_state.t6_cat_label[0]["valor"]}</div>'
        preview_html += f'<div class="preview-section-title">{st.session_state.t6_cat_titulos[0]["valor"]}</div>'
        
        # Logos Section
        preview_html += f'<div class="preview-section-label" style="text-align: left; margin-top: 60px;">{st.session_state.t6_logos_label[0]["valor"]}</div>'
        
        # Aplicações Section
        preview_html += f'<div class="preview-section-title">{st.session_state.t6_apps_titulo[0]["valor"]}</div>'

        # Fluxo Section
        preview_html += f'<div class="preview-section-title">{st.session_state.t6_flow_titulo[0]["valor"]}</div>'

        # Planos Section
        preview_html += f'<div class="preview-section-title">{st.session_state.t6_planos_titulo[0]["valor"]}</div>'

        # Footer
        preview_html += f'<div style="text-align: center; margin-top: 60px; font-size: 12px; color: #999;">{st.session_state.t6_footer_center[0]["valor"]}</div>'

        preview_html += '</div>'

        # Usando um container com scroll para o preview, e mostrando a imagem de referência abaixo
        with st.container(height=720, border=True):
            st.markdown(preview_html, unsafe_allow_html=True)
            st.markdown(f'<img src="{TEMPLATE_IMAGE_URL}" alt="Referência visual do template" style="width: 100%; opacity: 0.3; margin-top: 20px;" />', unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(
        page_title=f"Editor — {TEMPLATE_NAME}",
        page_icon="✏️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
