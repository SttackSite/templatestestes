import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES E CONSTANTES
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img2.png" # Substituir se necessário
TEMPLATE_NAME = "Template 2 — FitPro Academia"

# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE (Baseado no Template 2 Puro)
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    if "t2_init" not in st.session_state:
        defaults = {
            # Cores
            "t2_cores": [
                {"nome": "Cor de Destaque (Botões/Bordas)", "valor": "#FF6B35"},
                {"nome": "Cor de Fundo Escuro (Hero)",      "valor": "#1a1a1a"},
                {"nome": "Cor de Fundo Claro",              "valor": "#f5f5f5"},
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
            "t2_hero": [{"titulo_p1": "Transforme seu", "destaque": "corpo", "titulo_p2": "e mente", 
                        "subtitulo": "Programas personalizados, treinadores experientes e ambiente de primeira qualidade.",
                        "btn_texto": "Agende uma Avaliação Gratuita", "btn_url": "https://www.google.com/"}],
            "t2_hero_stats": [
                {"num": "5.000+", "label": "Alunos Ativos"},
                {"num": "15+",    "label": "Anos de Experiência"},
            ],

            # Serviços
            "t2_servicos_header": [{"titulo": "Nossos", "destaque": "Serviços", "desc": "Oferecemos uma variedade de programas e serviços para todos os níveis."}],
            "t2_servicos_cards": [
                {"icone": "🏋️", "titulo": "Musculação", "desc": "Treinamento com pesos de última geração."},
                {"icone": "🏃", "titulo": "Cardio", "desc": "Equipamentos modernos para queima calórica."},
                {"icone": "🧘", "titulo": "Yoga", "desc": "Aulas para flexibilidade e paz mental."},
            ],

            # Galeria (Seção que faltava)
            "t2_galeria": [
                {"url": "https://images.unsplash.com/photo-1534438327276-14e5300c3a48"},
                {"url": "https://images.unsplash.com/photo-1571902943202-507ec2618e8f"},
                {"url": "https://images.unsplash.com/photo-1540497077202-7c8a3999166f"},
            ],

            # Planos (Pricing)
            "t2_pricing_cards": [
                {"nome": "Básico", "preco": "99", "periodo": "mês", "features": "Acesso à academia;Equipamentos;Vestiário", "destaque": False},
                {"nome": "Elite", "preco": "199", "periodo": "mês", "features": "Aulas ilimitadas;Avaliação mensal;Personal Trainer", "destaque": True},
            ],

            # Depoimentos
            "t2_testemunhos": [
                {"texto": "Entrei sem conhecimento e hoje sou outra pessoa.", "autor": "Marcus Oliveira", "info": "Aluno Elite"},
            ],

            # CTA Final e Footer
            "t2_cta_final": [{"titulo": "Comece sua transformação", "destaque": "hoje", "btn": "Agende Agora"}],
            "t2_footer": [{"tel": "(99) 99999-9999", "email": "contato@fitpro.com.br", "end": "Av. Principal, 1234 - SP"}],
            
            # Observações (CORRIGIDO: Agora é uma string simples para facilitar o salvamento)
            "t2_obs_valor": ""
        }
        for k, v in defaults.items():
            st.session_state[k] = v
        st.session_state["t2_init"] = True

# ─────────────────────────────────────────────────────────────────────────────
# RENDER PRINCIPAL
# ─────────────────────────────────────────────────────────────────────────────
def render():
    _init()

    st.markdown("""
    <style>
        .section-label { font-size: 11px; font-weight: 700; text-transform: uppercase; color: #FF6B35; margin-top: 20px; border-bottom: 1px solid #eee; }
        .template-img-wrapper { height: 80vh; overflow-y: auto; border-radius: 8px; border: 1px solid #ddd; }
        .template-img-wrapper img { width: 100%; }
    </style>
    """, unsafe_allow_html=True)

    col_form, col_preview = st.columns([1.2, 2], gap="large")

    with col_form:
        st.subheader("✏️ Editor " + TEMPLATE_NAME)
        
        with st.container(height=700, border=False):
            # --- CORES ---
            st.markdown('<div class="section-label">🎨 Cores da Marca</div>', unsafe_allow_html=True)
            for i, cor in enumerate(st.session_state.t2_cores):
                st.session_state.t2_cores[i]["valor"] = st.color_picker(cor["nome"], cor["valor"], key=f"t2_c_{i}")

            # --- NAVBAR ---
            st.markdown('<div class="section-label">🔝 Menu Superior</div>', unsafe_allow_html=True)
            c1, c2 = st.columns(2)
            st.session_state.t2_logos[0]["texto"] = c1.text_input("Logo", st.session_state.t2_logos[0]["texto"])
            st.session_state.t2_logos[0]["destaque"] = c2.text_input("Logo Destaque", st.session_state.t2_logos[0]["destaque"])

            # --- HERO ---
            st.markdown('<div class="section-label">🦸 Seção Principal (Hero)</div>', unsafe_allow_html=True)
            h = st.session_state.t2_hero[0]
            h["titulo_p1"] = st.text_input("Título (Parte 1)", h["titulo_p1"])
            h["destaque"] = st.text_input("Título (Destaque)", h["destaque"])
            h["titulo_p2"] = st.text_input("Título (Parte 2)", h["titulo_p2"])
            h["subtitulo"] = st.text_area("Subtítulo", h["subtitulo"])

            # --- SERVIÇOS ---
            st.markdown('<div class="section-label">💪 Serviços e Aulas</div>', unsafe_allow_html=True)
            for i, s in enumerate(st.session_state.t2_servicos_cards):
                with st.expander(f"Serviço {i+1}: {s['titulo']}"):
                    s["icone"] = st.text_input("Emoji/Ícone", s["icone"], key=f"s_i_{i}")
                    s["titulo"] = st.text_input("Nome", s["titulo"], key=f"s_t_{i}")
                    s["desc"] = st.text_area("Descrição", s["desc"], key=f"s_d_{i}")

            # --- GALERIA (NOVO) ---
            st.markdown('<div class="section-label">🖼️ Galeria de Fotos</div>', unsafe_allow_html=True)
            for i, img in enumerate(st.session_state.t2_galeria):
                st.session_state.t2_galeria[i]["url"] = st.text_input(f"URL Imagem {i+1}", img["url"], key=f"gal_{i}")

            # --- PLANOS ---
            st.markdown('<div class="section-label">💰 Planos</div>', unsafe_allow_html=True)
            for i, p in enumerate(st.session_state.t2_pricing_cards):
                with st.expander(f"Plano: {p['nome']}"):
                    p["nome"] = st.text_input("Nome", p["nome"], key=f"p_n_{i}")
                    p["preco"] = st.text_input("Preço", p["preco"], key=f"p_p_{i}")
                    p["features"] = st.text_area("Vantagens (use ; )", p["features"], key=f"p_f_{i}")
                    p["destaque"] = st.toggle("Destacar Plano?", p["destaque"], key=f"p_h_{i}")

            # --- RODAPÉ ---
            st.markdown('<div class="section-label">📍 Contato e Rodapé</div>', unsafe_allow_html=True)
            f = st.session_state.t2_footer[0]
            f["tel"] = st.text_input("Telefone", f["tel"])
            f["email"] = st.text_input("E-mail", f["email"])
            f["end"] = st.text_input("Endereço", f["end"])

            # --- OBSERVAÇÕES (CONSERTADO) ---
            st.markdown('<div class="section-label">📝 Observações para a Equipe</div>', unsafe_allow_html=True)
            # Salvando diretamente na variável de estado para garantir persistência
            st.session_state.t2_obs_valor = st.text_area(
                "Algum detalhe extra que deseja mudar?", 
                value=st.session_state.t2_obs_valor,
                placeholder="Ex: Gostaria de mudar as fontes para uma estilo itálico...",
                key="input_obs_t2"
            )

            st.markdown("---")
            if st.button("✅ Finalizar Personalização", type="primary", use_container_width=True):
                st.success("Dados enviados com sucesso!")
                st.balloons()

    with col_preview:
        st.markdown('<p style="text-align:center; color:gray; font-size:12px;">Visualização do Template Original</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}"></div>', unsafe_allow_html=True)

if __name__ == "__main__":
    st.set_page_config(page_title="Editor Template 2", layout="wide")
    render()
