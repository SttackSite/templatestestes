import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/editor/main/img18.png"
TEMPLATE_NAME      = "Template 18 — Daniel Aristizábal Style (Digital Studio)"
TEMPLATE_ID        = "template_18"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t18_nome_cliente":  "",
        "t18_email_cliente": "",
        "t18_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t18_cores": [
            {"nome": "Fundo (Preto)",                 "valor": "#000000"},
            {"nome": "Texto (Branco)",                 "valor": "#ffffff"},
            {"nome": "Bordas/Linhas (Cinza)",          "valor": "#222222"},
            {"nome": "Texto Secundário (Cinza Médio)", "valor": "#666666"},
        ],

        # ── HEADER ──────────────────────────────────────────────────────────
        "t18_header_nomes": [{"valor": "Daniel Aristizábal"}],
        "t18_header_links": [
            {"texto": "Index",   "url": "seção Portfólio"},
            {"texto": "Studio",  "url": "seção The Studio"},
            {"texto": "Archive", "url": "seção Portfólio"},
            {"texto": "Shop",    "url": "https://wa.me/5511999999999"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t18_hero_titulos": [{"valor": "DANIEL ARISTIZABAL"}],
        "t18_hero_descs":   [{"valor": "Digital Art Director and Motion Designer. Merging surrealism with CGI to explore new visual languages. Based in Medellín, working globally."}],

        # ── PROJETOS ────────────────────────────────────────────────────────
        "t18_project_items": [
            {"img": "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=1200", "nome": "Digital Surrealism",   "year": "2024", "col_size": 2},
            {"img": "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?w=600",    "nome": "Chrome Study",         "year": "2023", "col_size": 1},
            {"img": "https://images.unsplash.com/photo-1633167606207-d840b5070fc2?w=600",  "nome": "Organic Forms",        "year": "2024", "col_size": 1},
            {"img": "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?w=600",  "nome": "Color Theory",         "year": "2023", "col_size": 1},
            {"img": "https://images.unsplash.com/photo-1558591710-4b4a1ae0f04d?w=600",    "nome": "Texture Flow",         "year": "2022", "col_size": 1},
            {"img": "https://images.unsplash.com/photo-1574169208507-84376144848b?w=600",  "nome": "CGI Sculpture",        "year": "2024", "col_size": 1},
            {"img": "https://images.unsplash.com/photo-1620641788421-7a1c342ea42e?w=1200", "nome": "Metaverse Landscapes", "year": "2024", "col_size": 2},
        ],

        # ── STUDIO ──────────────────────────────────────────────────────────
        "t18_studio_titulos": [{"valor": "THE STUDIO"}],
        "t18_studio_descs":   [{"valor": "Nós operamos na intersecção entre o design clássico e o futurismo digital. Especializados em CGI, direção de arte e identidades visuais que desafiam a lógica."}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t18_foot_col_titles": [
            {"valor": "CONNECT"},
            {"valor": "NEW BUSINESS"},
        ],
        "t18_foot_socials": [
            {"texto": "Instagram", "url": "https://instagram.com/"},
            {"texto": "Behance",   "url": "https://behance.net/"},
            {"texto": "LinkedIn",  "url": "https://linkedin.com/"},
            {"texto": "Vimeo",     "url": "https://vimeo.com/"},
        ],
        "t18_foot_emails": [{"texto": "studio@aristizabal.net", "url": "mailto:studio@aristizabal.net"}],
        "t18_foot_copys":  [{"valor": "© 2026 DANIEL ARISTIZÁBAL STUDIO — ALL RIGHTS RESERVED"}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t18_obs": [{"valor": ""}],
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

def _build_json():
    return {
        "template":      TEMPLATE_ID,
        "template_nome": TEMPLATE_NAME,
        "identificacao": {
            "nome":      st.session_state.t18_nome_cliente,
            "email":     st.session_state.t18_email_cliente,
            "nome_site": st.session_state.t18_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t18_nome_site}",
        },
        "cores": st.session_state.t18_cores,
        "header": {
            "nomes": st.session_state.t18_header_nomes,
            "links": st.session_state.t18_header_links,
        },
        "hero": {
            "titulos": st.session_state.t18_hero_titulos,
            "descs":   st.session_state.t18_hero_descs,
        },
        "projetos": st.session_state.t18_project_items,
        "studio": {
            "titulos": st.session_state.t18_studio_titulos,
            "descs":   st.session_state.t18_studio_descs,
        },
        "footer": {
            "col_titles": st.session_state.t18_foot_col_titles,
            "sociais":    st.session_state.t18_foot_socials,
            "emails":     st.session_state.t18_foot_emails,
            "copyright":  st.session_state.t18_foot_copys,
        },
        "observacoes": st.session_state.t18_obs,
    }

def _enviar_resend(payload: dict):
    """Retorna (sucesso: bool, mensagem_erro: str) via Gmail SMTP"""
    try:
        nome    = payload["identificacao"]["nome"]
        subject = f"[Novo Pedido] {TEMPLATE_NAME} — {nome}"
        body_html = f"<pre style='font-family:monospace;font-size:13px'>{json.dumps(payload, ensure_ascii=False, indent=2)}</pre>"

        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"]    = GMAIL_USER
        msg["To"]      = DESTINO_EMAIL
        msg.attach(MIMEText(body_html, "html", "utf-8"))

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=15) as server:
            server.login(GMAIL_USER, GMAIL_PASS)
            server.sendmail(GMAIL_USER, DESTINO_EMAIL, msg.as_string())
        return True, ""
    except Exception as ex:
        return False, str(ex)


# ─────────────────────────────────────────────────────────────────────────────
# RENDER PRINCIPAL
# ─────────────────────────────────────────────────────────────────────────────
def render():
    _init()

    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&family=JetBrains+Mono:wght@300;400;700&display=swap');
        html, body, [data-testid="stAppViewContainer"] { font-family: 'JetBrains Mono', monospace; background: #f4f6fb; }
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
        .info-box {
            background: #eff6ff; border: 1px solid #bfdbfe;
            border-radius: 10px; padding: 14px 16px; margin-bottom: 10px;
            font-size: 13px; color: #1e40af; line-height: 1.6;
        }
        .info-box strong { color: #1e3a8a; }
        .warn-box {
            background: #fefce8; border: 1px solid #fde68a;
            border-radius: 10px; padding: 14px 16px; margin-bottom: 10px;
            font-size: 13px; color: #92400e; line-height: 1.6;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        👋 <strong>Bem-vindo ao editor do seu site!</strong><br>
        Preencha os campos abaixo para personalizar o seu site. Não precisa ser técnico — é só digitar!
        Você também poderá vir aqui e ajustar seu site quantas vezes quiser.<br><br>
        💡 <strong>Tem alguma ideia que não encontrou aqui?</strong> Use o campo <em>Observações</em> no final
        para descrever o que deseja. Nossa equipe analisa tudo e aplica para você. 😊
    </div>
    """, unsafe_allow_html=True)

    col_form, col_preview = st.columns([1, 2], gap="medium")

    with col_form:
        st.markdown('<div class="panel-title">✏️ Editor de Template</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="panel-subtitle">{TEMPLATE_NAME}</div>', unsafe_allow_html=True)

        with st.container(height=720, border=False):

            # ══════════════════════════════════════════════════════════════════
            # 0. IDENTIFICAÇÃO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👤 Seus Dados</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin-top:4px">
                Preencha seus dados antes de começar. Usamos essas informações para identificar seu pedido e
                entrar em contato quando o site estiver pronto. 🚀
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t18_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t18_nome_cliente,
                key="t18_nome_cliente_inp", placeholder="Ex: Daniel Silva",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t18_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Kiwify)",
                value=st.session_state.t18_email_cliente,
                key="t18_email_cliente_inp", placeholder="Ex: daniel@studio.com",
                help="Use o mesmo e-mail com o qual você comprou na Kiwify.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: danielstudio, meucgi, studiovisual).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t18_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t18_nome_site,
                key="t18_nome_site_inp",
                placeholder="Ex: danielstudio  →  sttacksite.streamlit.app/?c=danielstudio",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t18_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t18_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t18_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t18_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t18_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t18_cores) > 1 and _del_btn(f"t18_cor_del_{i}"):
                        st.session_state.t18_cores.pop(i); st.rerun()
            if _add_btn("t18_cor_add", "＋ Adicionar cor"):
                st.session_state.t18_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. HEADER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Cabeçalho (Header)</div>', unsafe_allow_html=True)

            st.caption("Nome do estúdio / artista  *(lado esquerdo)*")
            for i, item in enumerate(st.session_state.t18_header_nomes):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t18_header_nomes[i]["valor"] = st.text_input(
                        "Nome", item["valor"], key=f"t18_hn_{i}", label_visibility="collapsed",
                        placeholder="Ex: Seu Nome ou Nome do Estúdio")
                with c2:
                    if len(st.session_state.t18_header_nomes) > 1 and _del_btn(f"t18_hn_del_{i}"):
                        st.session_state.t18_header_nomes.pop(i); st.rerun()
            if _add_btn("t18_hn_add", "＋ Adicionar nome"):
                st.session_state.t18_header_nomes.append({"valor": "Estúdio"}); st.rerun()

            st.caption("Menu de navegação  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t18_header_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t18_header_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t18_hl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t18_header_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t18_hl_u_{i}", label_visibility="collapsed",
                        placeholder="Seção ou https://...")
                with c3:
                    if len(st.session_state.t18_header_links) > 1 and _del_btn(f"t18_hl_del_{i}"):
                        st.session_state.t18_header_links.pop(i); st.rerun()
            if _add_btn("t18_hl_add", "＋ Adicionar link ao menu"):
                st.session_state.t18_header_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💥 Hero Section</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Título em letras gigantes:</strong> escreva o texto normalmente.
                Se quiser que alguma parte apareça em linha diferente, descreva isso na seção Observações.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Título principal  *(exibido em letras enormes)*")
            for i, t in enumerate(st.session_state.t18_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t18_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t18_h_t_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Ex: SEU NOME OU ESTÚDIO")
                with c2:
                    if len(st.session_state.t18_hero_titulos) > 1 and _del_btn(f"t18_h_t_del_{i}"):
                        st.session_state.t18_hero_titulos.pop(i); st.rerun()
            if _add_btn("t18_h_t_add", "＋ Adicionar título"):
                st.session_state.t18_hero_titulos.append({"valor": "NOVO TÍTULO"}); st.rerun()

            st.caption("Descrição  *(texto abaixo do título — cargo, especialidade, localização)*")
            for i, d in enumerate(st.session_state.t18_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t18_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t18_h_d_{i}", height=100,
                        label_visibility="collapsed",
                        placeholder="Ex: Diretor de Arte e Designer de Movimento. Baseado em São Paulo, trabalhando globalmente.")
                with c2:
                    if len(st.session_state.t18_hero_descs) > 1 and _del_btn(f"t18_h_d_del_{i}"):
                        st.session_state.t18_hero_descs.pop(i); st.rerun()
            if _add_btn("t18_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t18_hero_descs.append({"valor": "Nova descrição do estúdio."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. PROJETOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Portfólio de Projetos</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagens dos projetos:</strong> cole a URL do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanhos recomendados: <strong>1200 × 800 px</strong> para projetos largos (col 2)
                e <strong>600 × 800 px</strong> para projetos normais (col 1).
                <br><br>
                📐 <strong>Largura da coluna:</strong> projetos com col_size=2 ocupam o dobro do espaço,
                ideais para trabalhos de destaque.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Cards de projeto  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t18_project_items):
                with st.expander(f"Projeto {i+1}: {item['nome']}"):
                    st.session_state.t18_project_items[i]["nome"] = st.text_input(
                        "Nome do Projeto", item["nome"], key=f"t18_pi_n_{i}",
                        placeholder="Ex: Identidade Visual para Marca X")
                    st.session_state.t18_project_items[i]["year"] = st.text_input(
                        "Ano", item["year"], key=f"t18_pi_y_{i}",
                        placeholder="Ex: 2025")
                    st.session_state.t18_project_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t18_pi_i_{i}",
                        placeholder="https://i.imgur.com/... ou URL da imagem",
                        help="Cole a URL da imagem do imgur.com")
                    st.session_state.t18_project_items[i]["col_size"] = st.selectbox(
                        "Largura  *(1 = normal | 2 = larga/destaque)*",
                        [1, 2], index=item["col_size"] - 1, key=f"t18_pi_s_{i}")
                    if len(st.session_state.t18_project_items) > 1:
                        if st.button("🗑 Remover este projeto", key=f"t18_pi_del_{i}"):
                            st.session_state.t18_project_items.pop(i); st.rerun()
            if _add_btn("t18_pi_add", "＋ Adicionar projeto"):
                st.session_state.t18_project_items.append({"img": "", "nome": "NOVO PROJETO", "year": "2026", "col_size": 1}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. STUDIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏢 The Studio</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t18_studio_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t18_studio_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t18_st_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: O ESTÚDIO ou SOBRE MIM")
                with c2:
                    if len(st.session_state.t18_studio_titulos) > 1 and _del_btn(f"t18_st_t_del_{i}"):
                        st.session_state.t18_studio_titulos.pop(i); st.rerun()
            if _add_btn("t18_st_t_add", "＋ Adicionar título"):
                st.session_state.t18_studio_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição do estúdio / manifesto")
            for i, d in enumerate(st.session_state.t18_studio_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t18_studio_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t18_st_d_{i}", height=100,
                        label_visibility="collapsed",
                        placeholder="Descreva a filosofia, especialidades e diferenciais do estúdio")
                with c2:
                    if len(st.session_state.t18_studio_descs) > 1 and _del_btn(f"t18_st_d_del_{i}"):
                        st.session_state.t18_studio_descs.pop(i); st.rerun()
            if _add_btn("t18_st_d_add", "＋ Adicionar descrição"):
                st.session_state.t18_studio_descs.append({"valor": "Nova descrição do estúdio."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé Minimalista</div>', unsafe_allow_html=True)

            st.caption("Títulos das colunas  *(Coluna 1: redes | Coluna 2: contato)*")
            for i, title in enumerate(st.session_state.t18_foot_col_titles):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t18_foot_col_titles[i]["valor"] = st.text_input(
                        f"Título Coluna {i+1}", title["valor"], key=f"t18_fct_{i}",
                        label_visibility="collapsed",
                        placeholder="Ex: CONECTE-SE ou NOVOS PROJETOS")
                with c2:
                    if len(st.session_state.t18_foot_col_titles) > 1 and _del_btn(f"t18_fct_del_{i}"):
                        st.session_state.t18_foot_col_titles.pop(i); st.rerun()
            if _add_btn("t18_fct_add", "＋ Adicionar título de coluna"):
                st.session_state.t18_foot_col_titles.append({"valor": "NOVA COLUNA"}); st.rerun()

            st.caption("Redes sociais  *(Coluna 1 — Nome | URL)*")
            for i, social in enumerate(st.session_state.t18_foot_socials):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t18_foot_socials[i]["texto"] = st.text_input(
                        "Nome", social["texto"], key=f"t18_fs_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Instagram")
                with c2:
                    st.session_state.t18_foot_socials[i]["url"] = st.text_input(
                        "URL", social["url"], key=f"t18_fs_u_{i}", label_visibility="collapsed",
                        placeholder="https://instagram.com/seuperfil")
                with c3:
                    if len(st.session_state.t18_foot_socials) > 1 and _del_btn(f"t18_fs_del_{i}"):
                        st.session_state.t18_foot_socials.pop(i); st.rerun()
            if _add_btn("t18_fs_add", "＋ Adicionar rede social"):
                st.session_state.t18_foot_socials.append({"texto": "Social", "url": ""}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📧 <strong>E-mail de contato:</strong> o link deve começar com <code>mailto:</code>
                para abrir o app de e-mail ao clicar. Ex: <code>mailto:studio@meusite.com</code>
            </div>
            """, unsafe_allow_html=True)

            st.caption("E-mail de contato  *(Coluna 2 — Texto | mailto:)*")
            for i, email in enumerate(st.session_state.t18_foot_emails):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t18_foot_emails[i]["texto"] = st.text_input(
                        "Email", email["texto"], key=f"t18_fe_t_{i}", label_visibility="collapsed",
                        placeholder="email@exemplo.com")
                with c2:
                    st.session_state.t18_foot_emails[i]["url"] = st.text_input(
                        "Link mailto", email["url"], key=f"t18_fe_u_{i}", label_visibility="collapsed",
                        placeholder="mailto:email@exemplo.com")
                with c3:
                    if len(st.session_state.t18_foot_emails) > 1 and _del_btn(f"t18_fe_del_{i}"):
                        st.session_state.t18_foot_emails.pop(i); st.rerun()
            if _add_btn("t18_fe_add", "＋ Adicionar contato"):
                st.session_state.t18_foot_emails.append({"texto": "email@site.com", "url": "mailto:email@site.com"}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t18_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t18_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t18_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 SEU NOME — TODOS OS DIREITOS RESERVADOS")
                with c2:
                    if len(st.session_state.t18_foot_copys) > 1 and _del_btn(f"t18_fcp_del_{i}"):
                        st.session_state.t18_foot_copys.pop(i); st.rerun()
            if _add_btn("t18_fcp_add", "＋ Adicionar copyright"):
                st.session_state.t18_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. IMAGENS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Guia de Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Como adicionar imagens ao seu portfólio:</strong><br><br>
                1. Acesse <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a>
                   (gratuito, sem cadastro) e faça o upload da sua imagem.<br>
                2. Clique com o botão direito na imagem → <em>Copiar endereço da imagem</em> — a URL termina em
                   <code>.jpg</code>, <code>.png</code> ou <code>.webp</code>.<br>
                3. Cole a URL no campo de imagem do projeto correspondente acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Projetos destaque (largura 2): <strong>1200 × 800 px</strong><br>
                • Projetos normais (largura 1): <strong>600 × 800 px</strong><br>
                • Logo / foto de perfil: <strong>400 × 400 px</strong> (quadrada)<br><br>
                ❌ <strong>Não conseguiu subir a imagem?</strong> Envie para
                <strong>sttacksite@gmail.com</strong> com o assunto <em>"Imagem — [nome do seu site]"</em>.
            </div>
            """, unsafe_allow_html=True)

            # ══════════════════════════════════════════════════════════════════
            # 8. OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações / Pedidos Extras</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="warn-box">
                💬 <strong>Use este espaço para tudo que não encontrou nos campos acima!</strong><br>
                Ex: "adicionar efeitos de distorção CGI", "mudar layout do portfólio",
                "adicionar seção de clientes ou depoimentos", "adicionar link para loja"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t18_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t18_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t18_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t18_obs) > 1 and _del_btn(f"t18_obs_del_{i}"):
                        st.session_state.t18_obs.pop(i); st.rerun()
            if _add_btn("t18_obs_add", "＋ Adicionar observação"):
                st.session_state.t18_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 9. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t18_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t18_email_cliente.strip() or "@" not in st.session_state.t18_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Kiwify).")
            if not st.session_state.t18_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t18_send", type="primary",
                         disabled=len(erros) > 0):
                payload = _build_json()
                sucesso, erro_msg = _enviar_resend(payload)
                if erro_msg:
                    st.error(f"🔴 Erro ao enviar: {erro_msg}")
                if sucesso:
                    st.success(
                        "🎉 **Pedido enviado com sucesso!**\n\n"
                        "Nossa equipe já recebeu suas informações e entrará em contato assim que o site "
                        "estiver em produção. Caso surja alguma dúvida, falaremos com você pelo e-mail "
                        f"informado. 😊\n\n"
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t18_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t18_nome_cliente}'*."
                    )
                    st.code(json.dumps(payload, ensure_ascii=False, indent=2), language="json")

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
        page_icon="🎨",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
