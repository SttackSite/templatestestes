import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# URL DA IMAGEM DO TEMPLATE — SUBSTITUA PELO LINK DA SUA IMAGEM
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img32.png"
TEMPLATE_NAME = "Template 32 — SCENCO Style (Museum & Heritage)"


# ─────────────────────────────────────────────────────────────────────────────
# INICIALIZAÇÃO DO SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # Cores Scenco
        "t32_cores": [
            {"nome": "Fundo (un-bg)", "valor": "#F5F5F0"},
            {"nome": "Preto (un-black)", "valor": "#1A1A1A"},
            {"nome": "Azul (un-blue)", "valor": "#0070FF"},
            {"nome": "Acento (un-accent)", "valor": "#B58D3D"},
        ],
        # Navbar
        "t32_nav_logos": [{"texto": "SCENCO"}],
        "t32_nav_links": [
            {"texto": "Exposições", "url": "#colecao"},
            {"texto": "Coleções", "url": "#colecao"},
            {"texto": "História", "url": "#mapa"},
        ],
        "t32_nav_ctas": [{"texto": "Explorar →", "url": "#mapa"}],
        # Hero Section
        "t32_hero_labels": [{"valor": "Museu Digital do Patrimônio Mundial"}],
        "t32_hero_titulos": [{"valor": "UMA JORNADA<br>PELO <span style='font-family:serif; font-style:italic'>Tempo.</span>"}],
        "t32_hero_imgs": [{"url": "https://images.unsplash.com/photo-1548013146-72479768bbaa?w=1600"}],
        "t32_hero_quotes": [{"valor": "\"O patrimônio é o nosso legado do passado, o que vivemos hoje e o que transmitimos às gerações futuras.\""}],
        # Coleção (Grid Assimétrico)
        "t32_col_items": [
            {
                "lado": "Esquerda",
                "label": "Arquitetura & Ruínas",
                "titulo": "Templos de<br>Angkor Wat",
                "desc": "Explore a complexidade do maior monumento religioso do mundo, uma obra-prima da civilização Khmer que resistiu aos séculos.",
                "btn_texto": "VER COLEÇÃO COMPLETA",
                "btn_url": "https://www.google.com/",
                "img_url": "https://images.unsplash.com/photo-1569350080881-22442426302e?w=800"
            },
            {
                "lado": "Direita",
                "label": "Arquitetura & Ruínas", # Label não aparece no original da direita mas incluí para flexibilidade
                "titulo": "A Magia de<br>Mont-Saint-Michel",
                "desc": "Uma abadia gótica situada em uma ilha rochosa no coração de uma baía imensa, desafiando as marés e o horizonte.",
                "btn_texto": "EXPLORAR LOCAL",
                "btn_url": "https://www.google.com/",
                "img_url": "https://images.unsplash.com/photo-1503917988258-f197e2f4192d?w=800"
            }
        ],
        # Mapa Global
        "t32_map_headers": [{"label": "Mapa Global", "titulo": "Onde a História Vive"}],
        "t32_map_imgs": [{"url": "https://images.unsplash.com/photo-1521295121783-8a321d551ad2?w=1600", "texto": "CARREGANDO MAPA INTERATIVO..."}],
        # Footer
        "t32_foot_brands": [{"nome": "SCENCO", "desc": "O Museu do Patrimônio Mundial da SCENCO é uma iniciativa para preservar a memória cultural através da inovação digital."}],
        "t32_foot_cols": [
            {
                "titulo": "EXPLORAR",
                "links": [
                    {"texto": "África", "url": "https://www.google.com/"},
                    {"texto": "Américas", "url": "https://www.google.com/"},
                    {"texto": "Ásia & Pacífico", "url": "https://www.google.com/"},
                    {"texto": "Europa", "url": "https://www.google.com/"},
                ]
            },
            {
                "titulo": "CRÉDITOS",
                "links": [
                    {"texto": "Curadoria Digital", "url": "https://www.google.com/"},
                    {"texto": "Parceiros Tecnológicos", "url": "https://www.google.com/"},
                    {"texto": "Open Data", "url": "https://www.google.com/"},
                ]
            },
            {
                "titulo": "SIGA-NOS",
                "links": [
                    {"texto": "Instagram", "url": "https://www.google.com/"},
                    {"texto": "Twitter", "url": "https://www.google.com/"},
                    {"texto": "Youtube", "url": "https://www.google.com/"},
                ]
            }
        ],
        "t32_foot_copys": [{"valor": "SCENCO WORLD HERITAGE CENTRE © 2026."}],
        "t32_foot_legal": [
            {"texto": "POLÍTICAS DE PRESERVAÇÃO DIGITAL", "url": "https://www.google.com/"},
            {"texto": "TERMOS DE USO", "url": "https://www.google.com/"},
        ],
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

            # 🎨 CORES
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            for i, cor in enumerate(st.session_state.t32_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1: st.session_state.t32_cores[i]["nome"] = st.text_input("Nome", cor["nome"], key=f"t32_cor_n_{i}", label_visibility="collapsed")
                with c2: st.session_state.t32_cores[i]["valor"] = st.color_picker("Cor", cor["valor"], key=f"t32_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t32_cores) > 1 and _del_btn(f"t32_cor_del_{i}"):
                        st.session_state.t32_cores.pop(i); st.rerun()
            if _add_btn("t32_cor_add", "＋ Adicionar cor"):
                st.session_state.t32_cores.append({"nome": "Nova Cor", "valor": "#FFFFFF"}); st.rerun()

            # 🔝 NAVBAR
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t32_nav_logos):
                st.session_state.t32_nav_logos[i]["texto"] = st.text_input("Nome Marca", item["texto"], key=f"t32_nav_l_t_{i}")
            
            st.caption("Links do Menu")
            for i, link in enumerate(st.session_state.t32_nav_links):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1: st.session_state.t32_nav_links[i]["texto"] = st.text_input("Texto", link["texto"], key=f"t32_navl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t32_nav_links[i]["url"] = st.text_input("URL", link["url"], key=f"t32_navl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t32_nav_links) > 1 and _del_btn(f"t32_navl_del_{i}"):
                        st.session_state.t32_nav_links.pop(i); st.rerun()
            if _add_btn("t32_navl_add", "＋ Adicionar link"):
                st.session_state.t32_nav_links.append({"texto": "LINK", "url": "#"}); st.rerun()

            st.caption("Link de Destaque (Accent)")
            for i, cta in enumerate(st.session_state.t32_nav_ctas):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1: st.session_state.t32_nav_ctas[i]["texto"] = st.text_input("Texto", cta["texto"], key=f"t32_ncta_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t32_nav_ctas[i]["url"] = st.text_input("URL", cta["url"], key=f"t32_ncta_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t32_nav_ctas) > 1 and _del_btn(f"t32_ncta_del_{i}"):
                        st.session_state.t32_nav_ctas.pop(i); st.rerun()
            if _add_btn("t32_ncta_add", "＋ Adicionar CTA"):
                st.session_state.t32_nav_ctas.append({"texto": "Explorar →", "url": "#"}); st.rerun()

            # 🏛️ HERO SECTION
            st.markdown('<div class="section-label">🏛️ Hero Section</div>', unsafe_allow_html=True)
            for i, l in enumerate(st.session_state.t32_hero_labels):
                st.session_state.t32_hero_labels[i]["valor"] = st.text_input("Label Hero", l["valor"], key=f"t32_h_l_{i}")
            for i, t in enumerate(st.session_state.t32_hero_titulos):
                st.session_state.t32_hero_titulos[i]["valor"] = st.text_area("Título Hero (HTML)", t["valor"], key=f"t32_h_t_{i}")
            for i, img in enumerate(st.session_state.t32_hero_imgs):
                st.session_state.t32_hero_imgs[i]["url"] = st.text_input("URL Imagem Hero", img["url"], key=f"t32_h_img_{i}")
            for i, q in enumerate(st.session_state.t32_hero_quotes):
                st.session_state.t32_hero_quotes[i]["valor"] = st.text_area("Citação Hero", q["valor"], key=f"t32_h_q_{i}")

            # 🖼️ COLEÇÃO (GRID)
            st.markdown('<div class="section-label">🖼️ Coleções em Destaque</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t32_col_items):
                with st.expander(f"Item {i+1}: {item['titulo'].replace('<br>', ' ')}"):
                    st.session_state.t32_col_items[i]["lado"] = st.selectbox("Lado (Design)", ["Esquerda", "Direita"], index=0 if item["lado"]=="Esquerda" else 1, key=f"t32_ci_l_{i}")
                    st.session_state.t32_col_items[i]["label"] = st.text_input("Label", item["label"], key=f"t32_ci_lb_{i}")
                    st.session_state.t32_col_items[i]["titulo"] = st.text_area("Título (HTML)", item["titulo"], key=f"t32_ci_t_{i}")
                    st.session_state.t32_col_items[i]["desc"] = st.text_area("Descrição", item["desc"], key=f"t32_ci_d_{i}")
                    st.session_state.t32_col_items[i]["img_url"] = st.text_input("URL Imagem", item["img_url"], key=f"t32_ci_img_{i}")
                    st.session_state.t32_col_items[i]["btn_texto"] = st.text_input("Texto Botão", item["btn_texto"], key=f"t32_ci_bt_{i}")
                    st.session_state.t32_col_items[i]["btn_url"] = st.text_input("URL Botão", item["btn_url"], key=f"t32_ci_bu_{i}")
                    if len(st.session_state.t32_col_items) > 1 and _del_btn(f"t32_ci_del_{i}", "Remover item"):
                        st.session_state.t32_col_items.pop(i); st.rerun()
            if _add_btn("t32_ci_add", "＋ Adicionar item na coleção"):
                st.session_state.t32_col_items.append({"lado": "Esquerda", "label": "NOVA", "titulo": "NOVO TÍTULO", "desc": "DESC", "btn_texto": "VER MAIS", "btn_url": "#", "img_url": "https://images.unsplash.com/photo-1548013146-72479768bbaa?w=800"}); st.rerun()

            # 🗺️ MAPA GLOBAL
            st.markdown('<div class="section-label">🗺️ Mapa Global</div>', unsafe_allow_html=True)
            for i, h in enumerate(st.session_state.t32_map_headers):
                st.session_state.t32_map_headers[i]["label"] = st.text_input("Label Mapa", h["label"], key=f"t32_ml_{i}")
                st.session_state.t32_map_headers[i]["titulo"] = st.text_input("Título Mapa", h["titulo"], key=f"t32_mt_{i}")
            for i, m in enumerate(st.session_state.t32_map_imgs):
                st.session_state.t32_map_imgs[i]["url"] = st.text_input("URL Fundo Mapa", m["url"], key=f"t32_mi_u_{i}")
                st.session_state.t32_map_imgs[i]["texto"] = st.text_input("Texto Overlay Mapa", m["texto"], key=f"t32_mi_t_{i}")

            # 👣 FOOTER
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)
            for i, b in enumerate(st.session_state.t32_foot_brands):
                st.session_state.t32_foot_brands[i]["nome"] = st.text_input("Nome Marca Footer", b["nome"], key=f"t32_fb_n_{i}")
                st.session_state.t32_foot_brands[i]["desc"] = st.text_area("Descrição Footer", b["desc"], key=f"t32_fb_d_{i}")

            st.caption("Colunas de Links")
            for i, col in enumerate(st.session_state.t32_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t32_foot_cols[i]["titulo"] = st.text_input("Título Coluna", col["titulo"], key=f"t32_fc_t_{i}")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1: st.session_state.t32_foot_cols[i]["links"][j]["texto"] = st.text_input("Texto", link["texto"], key=f"t32_fcl_t_{i}_{j}", label_visibility="collapsed")
                        with c2: st.session_state.t32_foot_cols[i]["links"][j]["url"] = st.text_input("URL", link["url"], key=f"t32_fcl_u_{i}_{j}", label_visibility="collapsed")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t32_fcl_del_{i}_{j}"):
                                st.session_state.t32_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t32_fcl_add_{i}", "＋ Adicionar link"):
                        st.session_state.t32_foot_cols[i]["links"].append({"texto": "LINK", "url": "#"}); st.rerun()
                    
                    if len(st.session_state.t32_foot_cols) > 1 and _del_btn(f"t32_fc_del_{i}", "Remover coluna"):
                        st.session_state.t32_foot_cols.pop(i); st.rerun()
            if _add_btn("t32_fc_add", "＋ Adicionar coluna"):
                st.session_state.t32_foot_cols.append({"titulo": "NOVA", "links": [{"texto": "LINK", "url": "#"}]}); st.rerun()

            for i, copy in enumerate(st.session_state.t32_foot_copys):
                st.session_state.t32_foot_copys[i]["valor"] = st.text_input("Copyright", copy["valor"], key=f"t32_fcp_{i}")
            
            st.caption("Links Legais")
            for i, link in enumerate(st.session_state.t32_foot_legal):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1: st.session_state.t32_foot_legal[i]["texto"] = st.text_input("Texto Legal", link["texto"], key=f"t32_fl_t_{i}", label_visibility="collapsed")
                with c2: st.session_state.t32_foot_legal[i]["url"] = st.text_input("URL Legal", link["url"], key=f"t32_fl_u_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t32_foot_legal) > 1 and _del_btn(f"t32_fl_del_{i}"):
                        st.session_state.t32_foot_legal.pop(i); st.rerun()
            if _add_btn("t32_fl_add", "＋ Adicionar link legal"):
                st.session_state.t32_foot_legal.append({"texto": "LINK", "url": "#"}); st.rerun()

            # 📝 OBSERVAÇÕES
            st.markdown('<div class="section-label">📝 Observações Adicionais</div>', unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t13_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t13_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t32_obs_{i}", height=80,
                        placeholder="Ex: Usar tons pastéis ainda mais suaves...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t13_obs) > 1 and _del_btn(f"t32_obs_del_{i}"):
                        st.session_state.t13_obs.pop(i); st.rerun()
            if _add_btn("t32_obs_add", "＋ Adicionar observação"):
                st.session_state.t13_obs.append({"valor": ""}); st.rerun()

            st.markdown("---")
            if st.button("✅ Finalizar e Enviar para a Equipe", key="t32_send", type="primary"):
                st.success("✅ Suas informações foram enviadas! Nossa equipe aplicará as alterações em breve.")
                st.balloons()

    # 🖼️ PAINEL DIREITO
    with col_preview:
        st.markdown('<p class="img-caption">📌 Referência visual do template — role para ver o site completo</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="template-img-wrapper"><img src="{TEMPLATE_IMAGE_URL}" alt="Preview do template" /></div>', unsafe_allow_html=True)


if __name__ == "__main__":
    st.set_page_config(
        page_title=f"Editor — {TEMPLATE_NAME}",
        page_icon="🏛️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
