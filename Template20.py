import streamlit as st
import json
from datetime import datetime
import base64

# ========== CONFIGURAÇÃO DA PÁGINA ==========
st.set_page_config(
    page_title="Painel de Customização - Template 28",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== ESTADO DA SESSÃO ==========
if "customizations" not in st.session_state:
    st.session_state.customizations = {
        "hero": {
            "title": "O que está desaparecendo?",
            "subtitle": "Um memorial para a sexta extinção em massa.",
            "keep_default": False
        },
        "manifesto": {
            "title": "Nós não podemos proteger o que não lembramos.",
            "description": '"What Is Missing?" é um memorial permanente dedicado às espécies e habitats que já perdemos e àqueles que ainda podemos salvar. Ao contrário de um memorial físico estático, ele vive no espaço digital, conectando histórias de extinção com soluções para o futuro.',
            "keep_default": False
        },
        "stats": {
            "stat1_number": "70%",
            "stat1_text": "Da vida selvagem do planeta desapareceu nos últimos 50 anos.",
            "stat2_number": "1 Milhão",
            "stat2_text": "De espécies estão atualmente sob risco de extinção.",
            "keep_default": False
        },
        "timeline": {
            "items": [
                {"year": "1900s", "title": "O Céu Escurecido", "description": "Relatos de quando os bandos de pombos-passageiros eram tão vastos que bloqueavam o sol por horas em sua passagem."},
                {"year": "1950s", "title": "Silêncio nos Rios", "description": "O desaparecimento gradual do esturjão e de outras espécies migratórias que antes fervilhavam nas águas doces."},
                {"year": "2024", "title": "O Canto Solitário", "description": "O último registro sonoro de espécies de pássaros em florestas tropicais que não encontram mais pares para acasalamento."}
            ],
            "keep_default": False
        },
        "cta": {
            "title": "Ainda há tempo.",
            "description": "O projeto também destaca planos de conservação e visões de um mundo onde a humanidade e a natureza coexistem em equilíbrio. Proteja um habitat. Restaure uma floresta. Reduza sua pegada.",
            "button_text": "Saiba Mais",
            "button_url": "https://www.google.com/",
            "keep_default": False
        },
        "footer": {
            "text": "WHAT IS MISSING? FOUNDATION © 2026 <br> CIÊNCIA / ARTE / ATIVISMO",
            "keep_default": False
        },
        "colors": {
            "background": "#000000",
            "text": "#ffffff",
            "accent": "#ffffff",
            "keep_default": False
        }
    }

if "selected_section" not in st.session_state:
    st.session_state.selected_section = "hero"

# ========== FUNÇÃO PARA GERAR HTML DO PREVIEW ==========
def generate_preview_html():
    """Gera o HTML completo do preview"""
    html = f"""
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Preview Template 28</title>
        <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;1,300&family=Inter:wght@200;300&display=swap" rel="stylesheet">
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                background-color: {st.session_state.customizations['colors']['background']};
                color: {st.session_state.customizations['colors']['text']};
                font-family: 'Inter', sans-serif;
                font-weight: 200;
                line-height: 1.6;
            }}
            
            h1, h2, h3 {{
                font-family: 'Cormorant Garamond', serif;
                font-style: italic;
                font-weight: 300;
                letter-spacing: 1px;
            }}
            
            .container {{
                padding: 60px 40px;
                max-width: 1200px;
                margin: 0 auto;
            }}
            
            .hero {{
                text-align: center;
                padding: 80px 40px;
                margin-bottom: 40px;
            }}
            
            .hero h1 {{
                font-size: 48px;
                margin-bottom: 20px;
                line-height: 1.2;
            }}
            
            .hero p {{
                font-size: 20px;
                opacity: 0.7;
            }}
            
            .divider {{
                border: none;
                border-top: 1px solid rgba(255,255,255,0.2);
                margin: 40px 0;
            }}
            
            .manifesto {{
                text-align: center;
                margin: 60px 0;
            }}
            
            .manifesto h2 {{
                font-size: 36px;
                margin-bottom: 30px;
                line-height: 1.3;
            }}
            
            .manifesto p {{
                font-size: 16px;
                opacity: 0.8;
                max-width: 900px;
                margin: 0 auto;
                line-height: 1.8;
            }}
            
            .stats {{
                display: flex;
                gap: 40px;
                margin: 60px 0;
                text-align: center;
            }}
            
            .stat {{
                flex: 1;
            }}
            
            .stat-number {{
                font-size: 56px;
                font-family: 'Cormorant Garamond', serif;
                font-style: italic;
                margin-bottom: 15px;
            }}
            
            .stat-text {{
                font-size: 13px;
                text-transform: uppercase;
                letter-spacing: 2px;
                opacity: 0.7;
            }}
            
            .cta {{
                text-align: center;
                margin: 60px 0;
                padding: 60px 40px;
                background: rgba(255,255,255,0.05);
                border-radius: 8px;
            }}
            
            .cta h2 {{
                font-size: 42px;
                margin-bottom: 25px;
            }}
            
            .cta p {{
                font-size: 16px;
                opacity: 0.8;
                max-width: 800px;
                margin: 0 auto 40px auto;
                line-height: 1.8;
            }}
            
            .cta-button {{
                display: inline-block;
                background: white;
                color: black;
                padding: 14px 35px;
                border-radius: 6px;
                text-decoration: none;
                font-weight: bold;
                font-size: 14px;
                cursor: pointer;
                transition: all 0.3s;
            }}
            
            .cta-button:hover {{
                background: rgba(255,255,255,0.9);
                transform: translateY(-2px);
            }}
            
            .footer {{
                text-align: center;
                padding: 40px;
                font-size: 12px;
                opacity: 0.5;
                letter-spacing: 1px;
                border-top: 1px solid rgba(255,255,255,0.2);
                margin-top: 60px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <!-- HERO -->
            <div class="hero">
                <h1>{st.session_state.customizations['hero']['title']}</h1>
                <p>{st.session_state.customizations['hero']['subtitle']}</p>
            </div>
            
            <hr class="divider">
            
            <!-- MANIFESTO -->
            <div class="manifesto">
                <h2>{st.session_state.customizations['manifesto']['title']}</h2>
                <p>{st.session_state.customizations['manifesto']['description']}</p>
            </div>
            
            <hr class="divider">
            
            <!-- STATS -->
            <div class="stats">
                <div class="stat">
                    <div class="stat-number">{st.session_state.customizations['stats']['stat1_number']}</div>
                    <div class="stat-text">{st.session_state.customizations['stats']['stat1_text']}</div>
                </div>
                <div class="stat">
                    <div class="stat-number">{st.session_state.customizations['stats']['stat2_number']}</div>
                    <div class="stat-text">{st.session_state.customizations['stats']['stat2_text']}</div>
                </div>
            </div>
            
            <hr class="divider">
            
            <!-- CTA -->
            <div class="cta">
                <h2>{st.session_state.customizations['cta']['title']}</h2>
                <p>{st.session_state.customizations['cta']['description']}</p>
                <a href="{st.session_state.customizations['cta']['button_url']}" target="_blank" class="cta-button">
                    {st.session_state.customizations['cta']['button_text']}
                </a>
            </div>
            
            <!-- FOOTER -->
            <div class="footer">
                {st.session_state.customizations['footer']['text']}
            </div>
        </div>
    </body>
    </html>
    """
    return html

# ========== LAYOUT PRINCIPAL ==========
col_nav, col_preview, col_edit = st.columns([1, 1.5, 1.5])

# ========== COLUNA 1: NAVEGAÇÃO DE SEÇÕES ==========
with col_nav:
    st.markdown("### 📋 Seções")
    st.markdown("---")
    
    sections = {
        "hero": "🎯 Hero (Topo)",
        "manifesto": "📝 Manifesto",
        "stats": "📊 Estatísticas",
        "timeline": "⏳ Linha do Tempo",
        "cta": "🎬 Chamada para Ação",
        "footer": "🔗 Rodapé",
        "colors": "🎨 Cores"
    }
    
    for section_id, section_name in sections.items():
        if st.button(
            section_name,
            key=f"btn_{section_id}",
            use_container_width=True,
            type="primary" if st.session_state.selected_section == section_id else "secondary"
        ):
            st.session_state.selected_section = section_id
            st.rerun()

# ========== COLUNA 2: PREVIEW EM TEMPO REAL ==========
with col_preview:
    st.markdown("### 👁️ Preview")
    st.markdown("---")
    
    # Gerar HTML e renderizar em iframe
    preview_html = generate_preview_html()
    
    # Usar components.html para renderizar
    st.components.v1.html(preview_html, height=700, scrolling=True)

# ========== COLUNA 3: PAINEL DE EDIÇÃO ==========
with col_edit:
    st.markdown("### ✏️ Editar Seção")
    st.markdown("---")
    
    section = st.session_state.selected_section
    
    # ========== HERO ==========
    if section == "hero":
        st.markdown("#### 🎯 Hero (Topo Principal)")
        
        st.session_state.customizations["hero"]["title"] = st.text_input(
            "Título Principal",
            value=st.session_state.customizations["hero"]["title"],
            key="hero_title"
        )
        
        st.session_state.customizations["hero"]["subtitle"] = st.text_area(
            "Subtítulo",
            value=st.session_state.customizations["hero"]["subtitle"],
            key="hero_subtitle",
            height=80
        )
        
        st.session_state.customizations["hero"]["keep_default"] = st.checkbox(
            "Manter padrão (sem customização)",
            value=st.session_state.customizations["hero"]["keep_default"],
            key="hero_keep"
        )
        
        st.info("💡 Edite o título e subtítulo do topo da página. O preview atualiza em tempo real!")
    
    # ========== MANIFESTO ==========
    elif section == "manifesto":
        st.markdown("#### 📝 Manifesto")
        
        st.session_state.customizations["manifesto"]["title"] = st.text_input(
            "Título do Manifesto",
            value=st.session_state.customizations["manifesto"]["title"],
            key="manifesto_title"
        )
        
        st.session_state.customizations["manifesto"]["description"] = st.text_area(
            "Descrição",
            value=st.session_state.customizations["manifesto"]["description"],
            key="manifesto_desc",
            height=120
        )
        
        st.session_state.customizations["manifesto"]["keep_default"] = st.checkbox(
            "Manter padrão (sem customização)",
            value=st.session_state.customizations["manifesto"]["keep_default"],
            key="manifesto_keep"
        )
        
        st.info("💡 Customize o conteúdo principal da página.")
    
    # ========== ESTATÍSTICAS ==========
    elif section == "stats":
        st.markdown("#### 📊 Estatísticas")
        
        col_s1, col_s2 = st.columns(2)
        
        with col_s1:
            st.session_state.customizations["stats"]["stat1_number"] = st.text_input(
                "Número 1",
                value=st.session_state.customizations["stats"]["stat1_number"],
                key="stat1_num"
            )
            st.session_state.customizations["stats"]["stat1_text"] = st.text_area(
                "Descrição 1",
                value=st.session_state.customizations["stats"]["stat1_text"],
                key="stat1_text",
                height=80
            )
        
        with col_s2:
            st.session_state.customizations["stats"]["stat2_number"] = st.text_input(
                "Número 2",
                value=st.session_state.customizations["stats"]["stat2_number"],
                key="stat2_num"
            )
            st.session_state.customizations["stats"]["stat2_text"] = st.text_area(
                "Descrição 2",
                value=st.session_state.customizations["stats"]["stat2_text"],
                key="stat2_text",
                height=80
            )
        
        st.session_state.customizations["stats"]["keep_default"] = st.checkbox(
            "Manter padrão (sem customização)",
            value=st.session_state.customizations["stats"]["keep_default"],
            key="stats_keep"
        )
        
        st.info("💡 Customize os números e descrições das estatísticas.")
    
    # ========== LINHA DO TEMPO ==========
    elif section == "timeline":
        st.markdown("#### ⏳ Linha do Tempo")
        
        for i, item in enumerate(st.session_state.customizations["timeline"]["items"]):
            st.markdown(f"**Item {i+1}**")
            
            col_t1, col_t2 = st.columns([1, 2])
            
            with col_t1:
                st.session_state.customizations["timeline"]["items"][i]["year"] = st.text_input(
                    "Ano/Período",
                    value=item["year"],
                    key=f"timeline_year_{i}"
                )
            
            with col_t2:
                st.session_state.customizations["timeline"]["items"][i]["title"] = st.text_input(
                    "Título",
                    value=item["title"],
                    key=f"timeline_title_{i}"
                )
            
            st.session_state.customizations["timeline"]["items"][i]["description"] = st.text_area(
                "Descrição",
                value=item["description"],
                key=f"timeline_desc_{i}",
                height=70
            )
            
            st.divider()
        
        st.session_state.customizations["timeline"]["keep_default"] = st.checkbox(
            "Manter padrão (sem customização)",
            value=st.session_state.customizations["timeline"]["keep_default"],
            key="timeline_keep"
        )
        
        st.info("💡 Customize os eventos da linha do tempo.")
    
    # ========== CHAMADA PARA AÇÃO ==========
    elif section == "cta":
        st.markdown("#### 🎬 Chamada para Ação")
        
        st.session_state.customizations["cta"]["title"] = st.text_input(
            "Título",
            value=st.session_state.customizations["cta"]["title"],
            key="cta_title"
        )
        
        st.session_state.customizations["cta"]["description"] = st.text_area(
            "Descrição",
            value=st.session_state.customizations["cta"]["description"],
            key="cta_desc",
            height=100
        )
        
        st.session_state.customizations["cta"]["button_text"] = st.text_input(
            "Texto do Botão",
            value=st.session_state.customizations["cta"]["button_text"],
            key="cta_btn_text"
        )
        
        st.session_state.customizations["cta"]["button_url"] = st.text_input(
            "URL do Botão",
            value=st.session_state.customizations["cta"]["button_url"],
            key="cta_btn_url"
        )
        
        st.session_state.customizations["cta"]["keep_default"] = st.checkbox(
            "Manter padrão (sem customização)",
            value=st.session_state.customizations["cta"]["keep_default"],
            key="cta_keep"
        )
        
        st.info("💡 Customize a seção de chamada para ação.")
    
    # ========== RODAPÉ ==========
    elif section == "footer":
        st.markdown("#### 🔗 Rodapé")
        
        st.session_state.customizations["footer"]["text"] = st.text_area(
            "Texto do Rodapé (use <br> para quebra de linha)",
            value=st.session_state.customizations["footer"]["text"],
            key="footer_text",
            height=100
        )
        
        st.session_state.customizations["footer"]["keep_default"] = st.checkbox(
            "Manter padrão (sem customização)",
            value=st.session_state.customizations["footer"]["keep_default"],
            key="footer_keep"
        )
        
        st.info("💡 Customize o texto do rodapé.")
    
    # ========== CORES ==========
    elif section == "colors":
        st.markdown("#### 🎨 Cores")
        
        st.session_state.customizations["colors"]["background"] = st.color_picker(
            "Cor de Fundo",
            value=st.session_state.customizations["colors"]["background"],
            key="color_bg"
        )
        
        st.session_state.customizations["colors"]["text"] = st.color_picker(
            "Cor do Texto",
            value=st.session_state.customizations["colors"]["text"],
            key="color_text"
        )
        
        st.session_state.customizations["colors"]["accent"] = st.color_picker(
            "Cor de Destaque",
            value=st.session_state.customizations["colors"]["accent"],
            key="color_accent"
        )
        
        st.session_state.customizations["colors"]["keep_default"] = st.checkbox(
            "Manter padrão (sem customização)",
            value=st.session_state.customizations["colors"]["keep_default"],
            key="colors_keep"
        )
        
        st.info("💡 Customize as cores principais da página.")

# ========== SEÇÃO DE DOWNLOAD ==========
st.markdown("---")
st.markdown("### 💾 Salvar Customizações")

col_download, col_reset = st.columns(2)

with col_download:
    # Preparar JSON para download
    customization_data = {
        "template_id": 28,
        "template_name": "What Is Missing? - Memorial Global",
        "user_email": "cliente@example.com",
        "created_at": datetime.now().isoformat(),
        "customizations": st.session_state.customizations
    }
    
    json_str = json.dumps(customization_data, indent=2, ensure_ascii=False)
    
    st.download_button(
        label="📥 Baixar Customizações (JSON)",
        data=json_str,
        file_name=f"customization_template28_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
        mime="application/json",
        use_container_width=True
    )

with col_reset:
    if st.button("🔄 Resetar para Padrão", use_container_width=True):
        st.session_state.customizations = {
            "hero": {
                "title": "O que está desaparecendo?",
                "subtitle": "Um memorial para a sexta extinção em massa.",
                "keep_default": False
            },
            "manifesto": {
                "title": "Nós não podemos proteger o que não lembramos.",
                "description": '"What Is Missing?" é um memorial permanente dedicado às espécies e habitats que já perdemos e àqueles que ainda podemos salvar. Ao contrário de um memorial físico estático, ele vive no espaço digital, conectando histórias de extinção com soluções para o futuro.',
                "keep_default": False
            },
            "stats": {
                "stat1_number": "70%",
                "stat1_text": "Da vida selvagem do planeta desapareceu nos últimos 50 anos.",
                "stat2_number": "1 Milhão",
                "stat2_text": "De espécies estão atualmente sob risco de extinção.",
                "keep_default": False
            },
            "timeline": {
                "items": [
                    {"year": "1900s", "title": "O Céu Escurecido", "description": "Relatos de quando os bandos de pombos-passageiros eram tão vastos que bloqueavam o sol por horas em sua passagem."},
                    {"year": "1950s", "title": "Silêncio nos Rios", "description": "O desaparecimento gradual do esturjão e de outras espécies migratórias que antes fervilhavam nas águas doces."},
                    {"year": "2024", "title": "O Canto Solitário", "description": "O último registro sonoro de espécies de pássaros em florestas tropicais que não encontram mais pares para acasalamento."}
                ],
                "keep_default": False
            },
            "cta": {
                "title": "Ainda há tempo.",
                "description": "O projeto também destaca planos de conservação e visões de um mundo onde a humanidade e a natureza coexistem em equilíbrio. Proteja um habitat. Restaure uma floresta. Reduza sua pegada.",
                "button_text": "Saiba Mais",
                "button_url": "https://www.google.com/",
                "keep_default": False
            },
            "footer": {
                "text": "WHAT IS MISSING? FOUNDATION © 2026 <br> CIÊNCIA / ARTE / ATIVISMO",
                "keep_default": False
            },
            "colors": {
                "background": "#000000",
                "text": "#ffffff",
                "accent": "#ffffff",
                "keep_default": False
            }
        }
        st.rerun()

# ========== INFORMAÇÕES ==========
st.markdown("---")
st.markdown("""
### 📌 Como Funciona

1. **Selecione uma seção** no painel esquerdo
2. **Edite os campos** no painel de edição
3. **Veja o preview** atualizar em tempo real
4. **Baixe o JSON** quando terminar
5. **Envie para o designer** para implementação final

### ✅ Seções Disponíveis

- **Hero**: Título e subtítulo do topo
- **Manifesto**: Conteúdo principal
- **Estatísticas**: Números e descrições
- **Linha do Tempo**: Eventos e marcos
- **CTA**: Chamada para ação
- **Rodapé**: Informações finais
- **Cores**: Paleta de cores

### 💡 Dica

Você pode marcar "Manter padrão" em qualquer seção se não quiser customizá-la!
""")
