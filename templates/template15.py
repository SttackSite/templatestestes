import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/editor/main/img15.png"
TEMPLATE_NAME      = "Template 15 — Hugo Bazin Style (Minimalist Portfolio)"
TEMPLATE_ID        = "template_15"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t15_nome_cliente":  "",
        "t15_email_cliente": "",
        "t15_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t15_cores": [
            {"nome": "Fundo (Cinza Claro)",       "valor": "#f6f6f6"},
            {"nome": "Texto (Preto)",              "valor": "#1a1a1a"},
            {"nome": "Texto Secundário (Cinza)",   "valor": "#666666"},
            {"nome": "Bordas (Cinza Médio)",       "valor": "#dddddd"},
        ],

        # ── HEADER ──────────────────────────────────────────────────────────
        "t15_header_nome": [{"valor": "Hugo Bazin — Digital Designer"}],
        "t15_header_info": [{"valor": "Paris, FR — 14:52 PM"}],

        # ── HERO ────────────────────────────────────────────────────────────
        "t15_hero_titulos":    [{"valor": "CREATING DIGITAL EXPERIENCES"}],
        "t15_hero_subtitulos": [{"valor": "Independent Designer & Art Director"}],

        # ── PROJETOS ────────────────────────────────────────────────────────
        "t15_project_items": [
            {"img": "https://images.unsplash.com/photo-1494438639946-1ebd1d20bf85?auto=format&fit=crop&w=1500&q=80", "titulo": "L'Art de Vivre",    "ano": "2024", "cat": "Visual Identity"},
            {"img": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=1500&q=80", "titulo": "Techno Frontier",   "ano": "2023", "cat": "Product Design"},
            {"img": "https://images.unsplash.com/photo-1449247709967-d4461a6a6103?auto=format&fit=crop&w=1500&q=80", "titulo": "Minimal Workspace", "ano": "2023", "cat": "CGI & Motion"},
            {"img": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=1500&q=80", "titulo": "Essential Watch",   "ano": "2022", "cat": "E-commerce"},
        ],

        # ── ABOUT ───────────────────────────────────────────────────────────
        "t15_about_textos": [{"valor": "Eu ajudo marcas a traduzirem sua essência em produtos digitais que as pessoas amam usar. Focado em simplicidade, estética e performance."}],

        # ── CONTATO ─────────────────────────────────────────────────────────
        "t15_contact_btns": [
            {"texto": "EMAIL ME", "url": "mailto:hello@hugobazin.com"},
            {"texto": "LINKEDIN", "url": "https://linkedin.com/"},
            {"texto": "DRIBBBLE", "url": "https://dribbble.com/"},
        ],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t15_foot_copys": [{"valor": "© 2026 Hugo Bazin"}],
        "t15_foot_descs": [{"valor": "Design & Development"}],
        "t15_foot_tops":  [{"texto": "Back to Top ↑", "url": "topo da página"}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t15_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t15_nome_cliente,
            "email":     st.session_state.t15_email_cliente,
            "nome_site": st.session_state.t15_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t15_nome_site}",
        },
        "cores": st.session_state.t15_cores,
        "header": {
            "nome": st.session_state.t15_header_nome,
            "info": st.session_state.t15_header_info,
        },
        "hero": {
            "titulos":    st.session_state.t15_hero_titulos,
            "subtitulos": st.session_state.t15_hero_subtitulos,
        },
        "projetos": st.session_state.t15_project_items,
        "sobre":    st.session_state.t15_about_textos,
        "contato":  st.session_state.t15_contact_btns,
        "footer": {
            "copyright":   st.session_state.t15_foot_copys,
            "descricao":   st.session_state.t15_foot_descs,
            "voltar_topo": st.session_state.t15_foot_tops,
        },
        "observacoes": st.session_state.t15_obs,
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

            st.session_state.t15_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t15_nome_cliente,
                key="t15_nome_cliente_inp", placeholder="Ex: Maria Souza",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t15_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Kiwify)",
                value=st.session_state.t15_email_cliente,
                key="t15_email_cliente_inp", placeholder="Ex: maria@email.com",
                help="Use o mesmo e-mail com o qual você comprou na Kiwify.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: hugobazin, meuportfolio, designermarcos).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t15_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t15_nome_site,
                key="t15_nome_site_inp",
                placeholder="Ex: hugobazin  →  sttacksite.streamlit.app/?c=hugobazin",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t15_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t15_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t15_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t15_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t15_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t15_cores) > 1 and _del_btn(f"t15_cor_del_{i}"):
                        st.session_state.t15_cores.pop(i); st.rerun()
            if _add_btn("t15_cor_add", "＋ Adicionar cor"):
                st.session_state.t15_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. HEADER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Cabeçalho (Minimal)</div>', unsafe_allow_html=True)

            st.caption("Nome e profissão  *(lado esquerdo do header)*")
            for i, item in enumerate(st.session_state.t15_header_nome):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t15_header_nome[i]["valor"] = st.text_input(
                        "Nome", item["valor"], key=f"t15_hn_{i}", label_visibility="collapsed",
                        placeholder="Ex: Seu Nome — Profissão")
                with c2:
                    if len(st.session_state.t15_header_nome) > 1 and _del_btn(f"t15_hn_del_{i}"):
                        st.session_state.t15_header_nome.pop(i); st.rerun()
            if _add_btn("t15_hn_add", "＋ Adicionar nome"):
                st.session_state.t15_header_nome.append({"valor": "Nome — Profissão"}); st.rerun()

            st.caption("Localização / fuso  *(lado direito do header)*")
            for i, item in enumerate(st.session_state.t15_header_info):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t15_header_info[i]["valor"] = st.text_input(
                        "Info", item["valor"], key=f"t15_hi_{i}", label_visibility="collapsed",
                        placeholder="Ex: São Paulo, BR — GMT-3")
                with c2:
                    if len(st.session_state.t15_header_info) > 1 and _del_btn(f"t15_hi_del_{i}"):
                        st.session_state.t15_header_info.pop(i); st.rerun()
            if _add_btn("t15_hi_add", "＋ Adicionar info"):
                st.session_state.t15_header_info.append({"valor": "Cidade, País — GMT"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🕶️ Hero Section</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Título grande:</strong> escreva o texto normalmente.
                Se quiser quebrar a linha em dois pedaços, use a Observações para indicar onde quebrar.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Título principal  *(exibido em letras grandes)*")
            for i, t in enumerate(st.session_state.t15_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t15_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t15_h_t_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Ex: CRIANDO EXPERIÊNCIAS DIGITAIS")
                with c2:
                    if len(st.session_state.t15_hero_titulos) > 1 and _del_btn(f"t15_h_t_del_{i}"):
                        st.session_state.t15_hero_titulos.pop(i); st.rerun()
            if _add_btn("t15_h_t_add", "＋ Adicionar título"):
                st.session_state.t15_hero_titulos.append({"valor": "NOVO TÍTULO"}); st.rerun()

            st.caption("Subtítulo  *(exibido em itálico abaixo do título)*")
            for i, s in enumerate(st.session_state.t15_hero_subtitulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t15_hero_subtitulos[i]["valor"] = st.text_input(
                        "Subtítulo", s["valor"], key=f"t15_h_s_{i}", label_visibility="collapsed",
                        placeholder="Ex: Designer Independente & Diretor de Arte")
                with c2:
                    if len(st.session_state.t15_hero_subtitulos) > 1 and _del_btn(f"t15_h_s_del_{i}"):
                        st.session_state.t15_hero_subtitulos.pop(i); st.rerun()
            if _add_btn("t15_h_s_add", "＋ Adicionar subtítulo"):
                st.session_state.t15_hero_subtitulos.append({"valor": "Novo subtítulo"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. PROJETOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Portfólio de Projetos</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagens dos projetos:</strong> cole a URL do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanho recomendado: <strong>1500 × 900 px</strong> (paisagem) para melhor visual.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Cards de projeto  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t15_project_items):
                with st.expander(f"Projeto {i+1}: {item['titulo']}"):
                    st.session_state.t15_project_items[i]["titulo"] = st.text_input(
                        "Título do Projeto", item["titulo"], key=f"t15_pi_t_{i}",
                        placeholder="Ex: Identidade Visual para Marca X")
                    st.session_state.t15_project_items[i]["cat"] = st.text_input(
                        "Categoria", item["cat"], key=f"t15_pi_c_{i}",
                        placeholder="Ex: Visual Identity, Branding, Web Design")
                    st.session_state.t15_project_items[i]["ano"] = st.text_input(
                        "Ano", item["ano"], key=f"t15_pi_a_{i}",
                        placeholder="Ex: 2025")
                    st.session_state.t15_project_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t15_pi_i_{i}",
                        placeholder="https://i.imgur.com/... ou URL da imagem",
                        help="Cole a URL da imagem do imgur.com")
                    if len(st.session_state.t15_project_items) > 1:
                        if st.button("🗑 Remover este projeto", key=f"t15_pi_del_{i}"):
                            st.session_state.t15_project_items.pop(i); st.rerun()
            if _add_btn("t15_pi_add", "＋ Adicionar projeto"):
                st.session_state.t15_project_items.append({
                    "img": "", "titulo": "NOVO PROJETO", "ano": "2026", "cat": "Visual Identity"
                }); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. ABOUT
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📖 Sobre / Filosofia</div>', unsafe_allow_html=True)
            st.caption("Texto de apresentação  *(exibido em destaque centralizado)*")
            for i, text in enumerate(st.session_state.t15_about_textos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t15_about_textos[i]["valor"] = st.text_area(
                        "Texto Sobre", text["valor"], key=f"t15_at_{i}", height=120,
                        label_visibility="collapsed",
                        placeholder="Descreva sua filosofia de trabalho, especialidade e proposta de valor")
                with c2:
                    if len(st.session_state.t15_about_textos) > 1 and _del_btn(f"t15_at_del_{i}"):
                        st.session_state.t15_about_textos.pop(i); st.rerun()
            if _add_btn("t15_at_add", "＋ Adicionar parágrafo"):
                st.session_state.t15_about_textos.append({"valor": "Novo parágrafo sobre o trabalho."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. CONTATO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">✉️ Links de Contato</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🔗 <strong>URLs aceitas:</strong> e-mail (<code>mailto:seuemail@gmail.com</code>),
                WhatsApp (<code>https://wa.me/55119XXXXXXXX</code>), LinkedIn, Instagram, Dribbble ou qualquer link.
            </div>
            """, unsafe_allow_html=True)
            st.caption("Botões de contato  *(Texto | URL)*")
            for i, btn in enumerate(st.session_state.t15_contact_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t15_contact_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t15_cb_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: EMAIL ME")
                with c2:
                    st.session_state.t15_contact_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t15_cb_u_{i}", label_visibility="collapsed",
                        placeholder="mailto: ou https://")
                with c3:
                    if len(st.session_state.t15_contact_btns) > 1 and _del_btn(f"t15_cb_del_{i}"):
                        st.session_state.t15_contact_btns.pop(i); st.rerun()
            if _add_btn("t15_cb_add", "＋ Adicionar link de contato"):
                st.session_state.t15_contact_btns.append({"texto": "LINK", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Copyright  *(lado esquerdo)*")
            for i, copy in enumerate(st.session_state.t15_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t15_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t15_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 Seu Nome")
                with c2:
                    if len(st.session_state.t15_foot_copys) > 1 and _del_btn(f"t15_fcp_del_{i}"):
                        st.session_state.t15_foot_copys.pop(i); st.rerun()
            if _add_btn("t15_fcp_add", "＋ Adicionar copyright"):
                st.session_state.t15_foot_copys.append({"valor": "© 2026"}); st.rerun()

            st.caption("Descrição  *(centro)*")
            for i, desc in enumerate(st.session_state.t15_foot_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t15_foot_descs[i]["valor"] = st.text_input(
                        "Descrição", desc["valor"], key=f"t15_fd_{i}", label_visibility="collapsed",
                        placeholder="Ex: Design & Desenvolvimento")
                with c2:
                    if len(st.session_state.t15_foot_descs) > 1 and _del_btn(f"t15_fd_del_{i}"):
                        st.session_state.t15_foot_descs.pop(i); st.rerun()
            if _add_btn("t15_fd_add", "＋ Adicionar descrição"):
                st.session_state.t15_foot_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Link 'Voltar ao topo'  *(Texto | Destino)*")
            for i, top in enumerate(st.session_state.t15_foot_tops):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t15_foot_tops[i]["texto"] = st.text_input(
                        "Texto", top["texto"], key=f"t15_ft_t_{i}", label_visibility="collapsed",
                        placeholder="Back to Top ↑")
                with c2:
                    st.session_state.t15_foot_tops[i]["url"] = st.text_input(
                        "Destino", top["url"], key=f"t15_ft_u_{i}", label_visibility="collapsed",
                        placeholder="topo da página")
                with c3:
                    if len(st.session_state.t15_foot_tops) > 1 and _del_btn(f"t15_ft_del_{i}"):
                        st.session_state.t15_foot_tops.pop(i); st.rerun()
            if _add_btn("t15_ft_add", "＋ Adicionar link"):
                st.session_state.t15_foot_tops.append({"texto": "Back to Top ↑", "url": "topo da página"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. IMAGENS
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
                • Imagens de projeto: <strong>1500 × 900 px</strong> (paisagem)<br>
                • Foto de perfil (se houver): <strong>400 × 400 px</strong> (quadrada)<br>
                • Logo: <strong>200 × 60 px</strong> (fundo transparente, PNG)<br><br>
                ❌ <strong>Não conseguiu subir a imagem?</strong> Envie para
                <strong>sttacksite@gmail.com</strong> com o assunto <em>"Imagem — [nome do seu site]"</em>.
            </div>
            """, unsafe_allow_html=True)

            # ══════════════════════════════════════════════════════════════════
            # 9. OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações / Pedidos Extras</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="warn-box">
                💬 <strong>Use este espaço para tudo que não encontrou nos campos acima!</strong><br>
                Ex: "mudar fonte para algo mais clássico", "adicionar seção de serviços",
                "colocar vídeo de apresentação", "adicionar FAQ", "adicionar link do Behance"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t15_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t15_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t15_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t15_obs) > 1 and _del_btn(f"t15_obs_del_{i}"):
                        st.session_state.t15_obs.pop(i); st.rerun()
            if _add_btn("t15_obs_add", "＋ Adicionar observação"):
                st.session_state.t15_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 10. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t15_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t15_email_cliente.strip() or "@" not in st.session_state.t15_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Kiwify).")
            if not st.session_state.t15_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t15_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t15_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t15_nome_cliente}'*."
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
        page_icon="🕶️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
