import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES VISUAIS DO EDITOR (Referência do Template 2)
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_NAME = "Template 2 — FitPro Academia"
# Se você tiver uma imagem de preview para este template, substitua a URL abaixo
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img2.png"

# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE (Dados Padrão do Template 2)
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores
        "t2_cores": [
            {"nome": "Cor de Destaque (Laranja)", "valor": "#FF6B35"},
            {"nome": "Fundo Dark (Hero/CTA)",    "valor": "#1a1a1a"},
            {"nome": "Cor dos Textos",           "valor": "#1a1a1a"},
        ],
        # Navbar
        "t2_logos": [{"texto": "FIT", "destaque": "PRO"}],
        "t2_nav_links": [
            {"texto": "Recursos", "url": "#recursos"},
            {"texto": "Galeria",  "url": "#galeria"},
            {"texto": "Sobre",    "url": "#sobre"},
            {"texto": "Contato",  "url": "#contato"},
        ],
        "t2_nav_cta": [{"texto": "Começar Agora", "url": "https://www.google.com/"}],
        
        # Hero
        "t2_hero_titulos": [{"parte1": "Transforme seu", "destaque": "corpo", "parte2": "e mente"}],
        "t2_hero_subtitulos": [{"valor": "Programas personalizados, treinadores experientes e ambiente de primeira qualidade."}],
        "t2_hero_stats": [
            {"numero": "5.000+", "label": "Alunos Ativos"},
            {"numero": "15+",    "label": "Anos de Experiência"},
        ],
        "t2_hero_btns": [{"texto": "Agende uma Avaliação Gratuita", "url": "https://www.google.com/"}],

        # Serviços (Cards com Ícones)
        "t2_servicos_header": [{"titulo": "Nossos", "destaque": "Serviços", "desc": "Oferecemos uma variedade de programas e serviços."}],
        "t2_servicos_cards": [
            {"icone": "🏋️", "titulo": "Musculação", "desc": "Treinamento com pesos para ganho de massa."},
            {"icone": "🏃", "titulo": "Cardio",     "desc": "Equipamentos modernos para alta performance."},
            {"icone": "🧘", "titulo": "Yoga",       "desc": "Aulas de flexibilidade e bem-estar mental."},
        ],

        # Diferenciais (Features)
        "t2_features_header": [{"titulo": "Por que escolher a", "destaque": "FitPro"}],
        "t2_features_boxes": [
            {"titulo": "Equipamentos Modernos", "desc": "Máquinas de última geração importadas."},
            {"titulo": "Treinadores Certificados", "desc": "Profissionais qualificados e experientes."},
        ],

        # Planos (Pricing)
        "t2_pricing_header": [{"titulo": "Planos e", "destaque": "Preços"}],
        "t2_pricing_cards": [
            {"nome": "Básico", "preco": "99", "periodo": "Por mês", "features": "Acesso à academia;Uso de equipamentos", "destaque": False},
            {"nome": "Premium", "preco": "199", "periodo": "Por mês", "features": "Aulas ilimitadas;Avaliação mensal", "destaque": True},
        ],

        # Depoimentos
        "t2_testemunhos": [
            {"texto": "Entrei sem conhecimento e em 6 meses consegui resultados incríveis.", "autor": "Roberto Silva", "info": "Aluno há 2 anos"},
        ],

        # CTA Final e Footer
        "t2_cta_final": [{"titulo": "Comece sua transformação", "destaque": "hoje", "btn_txt": "Agende Agora"}],
        "t2_footer_info": [{"contato": "Telefone: (99) 99999-9999 | Email: contato@fitpro.com.br", "endereco": "Av. Principal, 1234 - SP"}],
        
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
# RENDER PRINCIPAL DO EDITOR
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
            letter-spacing: 1px; color: #FF6B35;
            margin: 22px 0 8px; padding-bottom: 6px;
            border-bottom: 1px solid #e2e8f0;
        }
        .panel-title { font-size: 18px; font-weight: 700; color: #1a1a2e; }
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
        st.markdown(f'<div style="color:#64748b; font-size:13px; margin-bottom:14px;">{TEMPLATE_NAME}</div>', unsafe_allow_html=True)

        with st.container(height=720, border=False):

            # 🎨 CORES
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            for i, cor in enumerate(st.session_state.t2_cores):
                c1, c2 = st.columns([3, 1])
                st.session_state.t2_cores[i]["valor"] = c2.color_picker(cor["nome"], cor["valor"], key=f"t2_c_v_{i}")
                st.session_state.t2_cores[i]["nome"] = c1.text_input("Local", cor["nome"], key=f"t2_c_n_{i}")

            # 🔝 NAVBAR
            st.markdown('<div class="section-label">🔝 Navegação</div>', unsafe_allow_html=True)
            logo = st.session_state.t2_logos[0]
            c1, c2 = st.columns(2)
            logo["texto"] = c1.text_input("Logo Texto", logo["texto"], key="t2_logo_t")
            logo["destaque"] = c2.text_input("Logo Destaque", logo["destaque"], key="t2_logo_d")
            
            st.caption("Links do Menu")
            for i, link in enumerate(st.session_state.t2_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                link["texto"] = c1.text_input("Texto", link["texto"], key=f"t2_nl_t_{i}", label_visibility="collapsed")
                link["url"] = c2.text_input("Ancoragem/URL", link["url"], key=f"t2_nl_u_{i}", label_visibility="collapsed")
                if len(st.session_state.t2_nav_links) > 1 and c3.button("🗑", key=f"t2_nl_d_{i}"):
                    st.session_state.t2_nav_links.pop(i); st.rerun()
            if _add_btn("t2_nl_add", "＋ Link"):
                st.session_state.t2_nav_links.append({"texto": "Novo", "url": "#"}); st.rerun()

            # 🦸 HERO
            st.markdown('<div class="section-label">🦸 Seção Hero</div>', unsafe_allow_html=True)
            h = st.session_state.t2_hero_titulos[0]
            h["parte1"] = st.text_input("Título (Início)", h["parte1"])
            h["destaque"] = st.text_input("Título (Destaque)", h["destaque"])
            h["parte2"] = st.text_input("Título (Fim)", h["parte2"])
            st.session_state.t2_hero_subtitulos[0]["valor"] = st.text_area("Subtítulo", st.session_state.t2_hero_subtitulos[0]["valor"])
            
            st.caption("Estatísticas (Número | Rótulo)")
            for i, stat in enumerate(st.session_state.t2_hero_stats):
                c1, c2, c3 = st.columns([3, 5, 1])
                stat["numero"] = c1.text_input("Núm", stat["numero"], key=f"t2_st_n_{i}", label_visibility="collapsed")
                stat["label"] = c2.text_input("Label", stat["label"], key=f"t2_st_l_{i}", label_visibility="collapsed")
                if len(st.session_state.t2_hero_stats) > 1 and c3.button("🗑", key=f"t2_st_d_{i}"):
                    st.session_state.t2_hero_stats.pop(i); st.rerun()

            # 🏋️ SERVIÇOS
            st.markdown('<div class="section-label">🏋️ Serviços</div>', unsafe_allow_html=True)
            sh = st.session_state.t2_servicos_header[0]
            sh["destaque"] = st.text_input("Título Destaque", sh["destaque"], key="t2_sh_d")
            
            for i, card in enumerate(st.session_state.t2_servicos_cards):
                with st.expander(f"Serviço: {card['titulo']}"):
                    card["icone"] = st.text_input("Emoji/Ícone", card["icone"], key=f"t2_sc_i_{i}")
                    card["titulo"] = st.text_input("Título", card["titulo"], key=f"t2_sc_t_{i}")
                    card["desc"] = st.text_area("Descrição", card["desc"], key=f"t2_sc_d_{i}")
                    if _del_btn(f"t2_sc_del_{i}", "Excluir Serviço"):
                        st.session_state.t2_servicos_cards.pop(i); st.rerun()
            if _add_btn("t2_sc_add", "＋ Novo Serviço"):
                st.session_state.t2_servicos_cards.append({"icone": "💪", "titulo": "Novo", "desc": "Descrição"}); st.rerun()

            # 💰 PLANOS
            st.markdown('<div class="section-label">💰 Planos e Preços</div>', unsafe_allow_html=True)
            for i, plan in enumerate(st.session_state.t2_pricing_cards):
                with st.expander(f"Plano: {plan['nome']}"):
                    plan["nome"] = st.text_input("Nome do Plano", plan["nome"], key=f"t2_pl_n_{i}")
                    plan["preco"] = st.text_input("Preço (R$)", plan["preco"], key=f"t2_pl_p_{i}")
                    plan["features"] = st.text_area("Vantagens (separadas por ponto e vírgula ';')", plan["features"], key=f"t2_pl_f_{i}")
                    plan["destaque"] = st.toggle("Destacar este plano?", plan["destaque"], key=f"t2_pl_h_{i}")

            # 🔻 FOOTER & OBS
            st.markdown('<div class="section-label">🔻 Rodapé e Contato</div>', unsafe_allow_html=True)
            f_info = st.session_state.t2_footer_info[0]
            f_info["contato"] = st.text_input("Info Contato", f_info["contato"])
            f_info["endereco"] = st.text_input("Endereço", f_info["endereco"])

            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            st.session_state.t2_obs[0]["valor"] = st.text_area("Deseja mais alguma alteração?", placeholder="Ex: Mudar a fonte para uma mais agressiva...", label_visibility="collapsed")

            st.markdown("---")
            if st.button("✅ Enviar Personalização Academia", type="primary", use_container_width=True):
                st.success("Dados enviados! Vamos preparar sua academia digital.")
                st.balloons()

    with col_preview:
        st.markdown('<p style="font-size:12px; color:#94a3b8; text-align:center;">📌 Referência visual do Template Academia</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}" /></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(page_title=f"Editor — {TEMPLATE_NAME}", page_icon="💪", layout="wide")
    render()
