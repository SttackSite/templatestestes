import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img17.png"
TEMPLATE_NAME      = "Template 17 — Breakfast Style (Brutalist Agency)"
TEMPLATE_ID        = "template_17"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t17_nome_cliente":  "",
        "t17_email_cliente": "",
        "t17_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t17_cores": [
            {"nome": "Fundo (Branco)",          "valor": "#ffffff"},
            {"nome": "Texto (Preto)",            "valor": "#000000"},
            {"nome": "Bordas (Preto)",           "valor": "#000000"},
            {"nome": "Texto Secundário (Cinza)", "valor": "#888888"},
        ],

        # ── HEADER ──────────────────────────────────────────────────────────
        "t17_header_logos":    [{"valor": "Breakfast."}],
        "t17_header_taglines": [{"valor": "Design & Technology"}],

        # ── HERO ────────────────────────────────────────────────────────────
        "t17_hero_titulos": [{"valor": "WE DESIGN DIGITAL EXPERIENCES"}],

        # ── PROJETOS ────────────────────────────────────────────────────────
        "t17_project_items": [
            {"img": "https://images.unsplash.com/photo-1558655146-d09347e92766?w=800",  "nome": "Solar System",      "client": "Editorial"},
            {"img": "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=800", "nome": "Neon Future",       "client": "Web Design"},
            {"img": "https://images.unsplash.com/photo-1525547719571-a2d4ac8945e2?w=800", "nome": "Cyber Identity",    "client": "Branding"},
            {"img": "https://images.unsplash.com/photo-1509343256512-d77a5cb3791b?w=800", "nome": "Monochrome Studio", "client": "CGI"},
        ],

        # ── FILOSOFIA ───────────────────────────────────────────────────────
        "t17_filosofia_textos": [{"valor": "Independent studio for strategy, design and code. We turn complex ideas into simple, functional and beautiful digital products."}],

        # ── SERVIÇOS ────────────────────────────────────────────────────────
        "t17_servico_items": [
            {"titulo": "STRATEGY", "desc": "Product Discovery / User Research / Brand Positioning"},
            {"titulo": "DESIGN",   "desc": "UI/UX Design / Visual Identity / Motion Graphics"},
            {"titulo": "CODE",     "desc": "React / Webflow / Headless CMS / E-commerce"},
        ],

        # ── CTA ─────────────────────────────────────────────────────────────
        "t17_cta_titulos": [{"valor": "LET'S TALK?"}],
        "t17_cta_btns":    [{"texto": "Start a Project", "url": "https://wa.me/5511999999999"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t17_foot_logos":   [{"valor": "Breakfast."}],
        "t17_foot_infos":   [{"valor": "Rua de Trás, Porto, Portugal"}],
        "t17_foot_emails":  [{"texto": "hello@wearebreakfast.com", "url": "mailto:hello@wearebreakfast.com"}],
        "t17_foot_socials": [
            {"texto": "INSTAGRAM", "url": "https://instagram.com/"},
            {"texto": "LINKEDIN",  "url": "https://linkedin.com/"},
            {"texto": "TWITTER",   "url": "https://twitter.com/"},
        ],
        "t17_foot_copys": [{"valor": "© 2026 ALL RIGHTS RESERVED"}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t17_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t17_nome_cliente,
            "email":     st.session_state.t17_email_cliente,
            "nome_site": st.session_state.t17_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t17_nome_site}",
        },
        "cores": st.session_state.t17_cores,
        "header": {
            "logos":    st.session_state.t17_header_logos,
            "taglines": st.session_state.t17_header_taglines,
        },
        "hero":      st.session_state.t17_hero_titulos,
        "projetos":  st.session_state.t17_project_items,
        "filosofia": st.session_state.t17_filosofia_textos,
        "servicos":  st.session_state.t17_servico_items,
        "cta": {
            "titulos": st.session_state.t17_cta_titulos,
            "botoes":  st.session_state.t17_cta_btns,
        },
        "footer": {
            "logos":    st.session_state.t17_foot_logos,
            "infos":    st.session_state.t17_foot_infos,
            "emails":   st.session_state.t17_foot_emails,
            "sociais":  st.session_state.t17_foot_socials,
            "copyright":st.session_state.t17_foot_copys,
        },
        "observacoes": st.session_state.t17_obs,
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

            st.session_state.t17_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t17_nome_cliente,
                key="t17_nome_cliente_inp", placeholder="Ex: Ana Costa",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t17_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t17_email_cliente,
                key="t17_email_cliente_inp", placeholder="Ex: ana@agencia.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: minhaagencia, breakfast, studiocriativo).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t17_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t17_nome_site,
                key="t17_nome_site_inp",
                placeholder="Ex: minhaagencia  →  sttacksite.streamlit.app/?c=minhaagencia",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t17_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t17_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t17_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t17_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t17_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t17_cores) > 1 and _del_btn(f"t17_cor_del_{i}"):
                        st.session_state.t17_cores.pop(i); st.rerun()
            if _add_btn("t17_cor_add", "＋ Adicionar cor"):
                st.session_state.t17_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. HEADER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Cabeçalho (Header)</div>', unsafe_allow_html=True)

            st.caption("Nome / Logo da agência  *(lado esquerdo)*")
            for i, item in enumerate(st.session_state.t17_header_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t17_header_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t17_hl_{i}", label_visibility="collapsed",
                        placeholder="Ex: MinhaAgência. ou Studio X")
                with c2:
                    if len(st.session_state.t17_header_logos) > 1 and _del_btn(f"t17_hl_del_{i}"):
                        st.session_state.t17_header_logos.pop(i); st.rerun()
            if _add_btn("t17_hl_add", "＋ Adicionar logo"):
                st.session_state.t17_header_logos.append({"valor": "Agência."}); st.rerun()

            st.caption("Tagline  *(lado direito do header)*")
            for i, item in enumerate(st.session_state.t17_header_taglines):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t17_header_taglines[i]["valor"] = st.text_input(
                        "Tagline", item["valor"], key=f"t17_ht_{i}", label_visibility="collapsed",
                        placeholder="Ex: Design & Tecnologia")
                with c2:
                    if len(st.session_state.t17_header_taglines) > 1 and _del_btn(f"t17_ht_del_{i}"):
                        st.session_state.t17_header_taglines.pop(i); st.rerun()
            if _add_btn("t17_ht_add", "＋ Adicionar tagline"):
                st.session_state.t17_header_taglines.append({"valor": "Nova Tagline"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💥 Hero Section</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Título em letras gigantes:</strong> escreva o texto normalmente.
                Se quiser que alguma parte apareça em linha diferente, descreva na seção de Observações.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Título principal  *(exibido em letras grandes, em maiúsculas)*")
            for i, t in enumerate(st.session_state.t17_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t17_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t17_h_t_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Ex: CRIAMOS EXPERIÊNCIAS DIGITAIS")
                with c2:
                    if len(st.session_state.t17_hero_titulos) > 1 and _del_btn(f"t17_h_t_del_{i}"):
                        st.session_state.t17_hero_titulos.pop(i); st.rerun()
            if _add_btn("t17_h_t_add", "＋ Adicionar título"):
                st.session_state.t17_hero_titulos.append({"valor": "NOVO TÍTULO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. PROJETOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Portfólio de Projetos</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagens dos projetos:</strong> cole a URL do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanho recomendado: <strong>800 × 600 px</strong>.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Cards de projeto  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t17_project_items):
                with st.expander(f"Projeto {i+1}: {item['nome']}"):
                    st.session_state.t17_project_items[i]["nome"] = st.text_input(
                        "Nome do Projeto", item["nome"], key=f"t17_pi_n_{i}",
                        placeholder="Ex: Identidade Visual para X")
                    st.session_state.t17_project_items[i]["client"] = st.text_input(
                        "Tipo / Categoria", item["client"], key=f"t17_pi_c_{i}",
                        placeholder="Ex: Editorial, Branding, Web Design")
                    st.session_state.t17_project_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t17_pi_i_{i}",
                        placeholder="https://i.imgur.com/... ou URL da imagem",
                        help="Cole a URL da imagem do imgur.com")
                    if len(st.session_state.t17_project_items) > 1:
                        if st.button("🗑 Remover este projeto", key=f"t17_pi_del_{i}"):
                            st.session_state.t17_project_items.pop(i); st.rerun()
            if _add_btn("t17_pi_add", "＋ Adicionar projeto"):
                st.session_state.t17_project_items.append({"img": "", "nome": "NOVO PROJETO", "client": "Editorial"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. FILOSOFIA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📖 Filosofia da Agência</div>', unsafe_allow_html=True)
            st.caption("Texto exibido em destaque  *(grande, negrito)*")
            for i, text in enumerate(st.session_state.t17_filosofia_textos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t17_filosofia_textos[i]["valor"] = st.text_area(
                        "Texto", text["valor"], key=f"t17_ft_{i}", height=120,
                        label_visibility="collapsed",
                        placeholder="Descreva a filosofia, missão e diferencial da agência em poucas frases marcantes")
                with c2:
                    if len(st.session_state.t17_filosofia_textos) > 1 and _del_btn(f"t17_ft_del_{i}"):
                        st.session_state.t17_filosofia_textos.pop(i); st.rerun()
            if _add_btn("t17_ft_add", "＋ Adicionar parágrafo"):
                st.session_state.t17_filosofia_textos.append({"valor": "Novo parágrafo de filosofia."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. SERVIÇOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🛠️ Nossos Serviços</div>', unsafe_allow_html=True)
            st.caption("Cards de serviço  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t17_servico_items):
                with st.expander(f"Serviço {i+1}: {item['titulo']}"):
                    st.session_state.t17_servico_items[i]["titulo"] = st.text_input(
                        "Título do Serviço", item["titulo"], key=f"t17_si_t_{i}",
                        placeholder="Ex: STRATEGY, DESIGN, CODE")
                    st.session_state.t17_servico_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t17_si_d_{i}", height=80,
                        placeholder="Liste as entregas deste serviço separadas por / ou descreva em texto")
                    if len(st.session_state.t17_servico_items) > 1:
                        if st.button("🗑 Remover este serviço", key=f"t17_si_del_{i}"):
                            st.session_state.t17_servico_items.pop(i); st.rerun()
            if _add_btn("t17_si_add", "＋ Adicionar serviço"):
                st.session_state.t17_servico_items.append({"titulo": "NOVO SERVIÇO", "desc": "Descrição do serviço."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. CTA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📞 Chamada para Ação (CTA)</div>', unsafe_allow_html=True)

            st.caption("Título da CTA  *(exibido em letras grandes)*")
            for i, t in enumerate(st.session_state.t17_cta_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t17_cta_titulos[i]["valor"] = st.text_input(
                        "Título CTA", t["valor"], key=f"t17_ct_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: VAMOS CONVERSAR?")
                with c2:
                    if len(st.session_state.t17_cta_titulos) > 1 and _del_btn(f"t17_ct_del_{i}"):
                        st.session_state.t17_cta_titulos.pop(i); st.rerun()
            if _add_btn("t17_ct_add", "＋ Adicionar título"):
                st.session_state.t17_cta_titulos.append({"valor": "FALE CONOSCO?"}); st.rerun()

            st.caption("Botão  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t17_cta_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t17_cta_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t17_cb_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Iniciar um Projeto")
                with c2:
                    st.session_state.t17_cta_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t17_cb_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou mailto:")
                with c3:
                    if len(st.session_state.t17_cta_btns) > 1 and _del_btn(f"t17_cb_del_{i}"):
                        st.session_state.t17_cta_btns.pop(i); st.rerun()
            if _add_btn("t17_cb_add", "＋ Adicionar botão"):
                st.session_state.t17_cta_btns.append({"texto": "CONTATO", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé Brutalista</div>', unsafe_allow_html=True)

            st.caption("Nome / Logo")
            for i, logo in enumerate(st.session_state.t17_foot_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t17_foot_logos[i]["valor"] = st.text_input(
                        "Logo Footer", logo["valor"], key=f"t17_fl_{i}", label_visibility="collapsed",
                        placeholder="Ex: MinhaAgência.")
                with c2:
                    if len(st.session_state.t17_foot_logos) > 1 and _del_btn(f"t17_fl_del_{i}"):
                        st.session_state.t17_foot_logos.pop(i); st.rerun()
            if _add_btn("t17_fl_add", "＋ Adicionar logo"):
                st.session_state.t17_foot_logos.append({"valor": "Agência."}); st.rerun()

            st.caption("Endereço / Localização")
            for i, info in enumerate(st.session_state.t17_foot_infos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t17_foot_infos[i]["valor"] = st.text_input(
                        "Endereço", info["valor"], key=f"t17_fi_{i}", label_visibility="collapsed",
                        placeholder="Ex: Av. Paulista, 1000 — São Paulo, SP")
                with c2:
                    if len(st.session_state.t17_foot_infos) > 1 and _del_btn(f"t17_fi_del_{i}"):
                        st.session_state.t17_foot_infos.pop(i); st.rerun()
            if _add_btn("t17_fi_add", "＋ Adicionar endereço"):
                st.session_state.t17_foot_infos.append({"valor": "Rua, Cidade, País"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📧 <strong>E-mail de contato:</strong> o link deve começar com <code>mailto:</code>
                para abrir o aplicativo de e-mail ao clicar. Ex: <code>mailto:contato@minhaagencia.com</code>
            </div>
            """, unsafe_allow_html=True)

            st.caption("E-mail  *(Texto visível | mailto:seu@email.com)*")
            for i, email in enumerate(st.session_state.t17_foot_emails):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t17_foot_emails[i]["texto"] = st.text_input(
                        "Texto", email["texto"], key=f"t17_fe_t_{i}", label_visibility="collapsed",
                        placeholder="email@exemplo.com")
                with c2:
                    st.session_state.t17_foot_emails[i]["url"] = st.text_input(
                        "URL", email["url"], key=f"t17_fe_u_{i}", label_visibility="collapsed",
                        placeholder="mailto:email@exemplo.com")
                with c3:
                    if len(st.session_state.t17_foot_emails) > 1 and _del_btn(f"t17_fe_del_{i}"):
                        st.session_state.t17_foot_emails.pop(i); st.rerun()
            if _add_btn("t17_fe_add", "＋ Adicionar e-mail"):
                st.session_state.t17_foot_emails.append({"texto": "email@exemplo.com", "url": "mailto:email@exemplo.com"}); st.rerun()

            st.caption("Redes sociais  *(Nome | URL)*")
            for i, social in enumerate(st.session_state.t17_foot_socials):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t17_foot_socials[i]["texto"] = st.text_input(
                        "Nome", social["texto"], key=f"t17_fs_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: INSTAGRAM")
                with c2:
                    st.session_state.t17_foot_socials[i]["url"] = st.text_input(
                        "URL", social["url"], key=f"t17_fs_u_{i}", label_visibility="collapsed",
                        placeholder="https://instagram.com/suaagencia")
                with c3:
                    if len(st.session_state.t17_foot_socials) > 1 and _del_btn(f"t17_fs_del_{i}"):
                        st.session_state.t17_foot_socials.pop(i); st.rerun()
            if _add_btn("t17_fs_add", "＋ Adicionar rede social"):
                st.session_state.t17_foot_socials.append({"texto": "SOCIAL", "url": ""}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t17_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t17_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t17_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 TODOS OS DIREITOS RESERVADOS")
                with c2:
                    if len(st.session_state.t17_foot_copys) > 1 and _del_btn(f"t17_fcp_del_{i}"):
                        st.session_state.t17_foot_copys.pop(i); st.rerun()
            if _add_btn("t17_fcp_add", "＋ Adicionar copyright"):
                st.session_state.t17_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 9. IMAGENS
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
                • Imagens de projeto: <strong>800 × 600 px</strong><br>
                • Logo: <strong>200 × 60 px</strong> (fundo transparente, PNG)<br><br>
                ❌ <strong>Não conseguiu subir a imagem?</strong> Envie para
                <strong>sttacksite@gmail.com</strong> com o assunto <em>"Imagem — [nome do seu site]"</em>.
            </div>
            """, unsafe_allow_html=True)

            # ══════════════════════════════════════════════════════════════════
            # 10. OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações / Pedidos Extras</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="warn-box">
                💬 <strong>Use este espaço para tudo que não encontrou nos campos acima!</strong><br>
                Ex: "mudar fonte para algo mais brutalista", "adicionar seção de clientes",
                "adicionar vídeo showreel", "adicionar FAQ", "adicionar formulário de contato"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t17_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t17_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t17_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t17_obs) > 1 and _del_btn(f"t17_obs_del_{i}"):
                        st.session_state.t17_obs.pop(i); st.rerun()
            if _add_btn("t17_obs_add", "＋ Adicionar observação"):
                st.session_state.t17_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 11. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t17_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t17_email_cliente.strip() or "@" not in st.session_state.t17_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t17_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t17_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t17_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t17_nome_cliente}'*."
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
        page_icon="🍳",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
