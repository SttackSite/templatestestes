import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/editor/main/img22.png"
TEMPLATE_NAME      = "Template 22 — Zajno Motion Style (Digital Design Studio)"
TEMPLATE_ID        = "template_22"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t22_nome_cliente":  "",
        "t22_email_cliente": "",
        "t22_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t22_cores": [
            {"nome": "Fundo (Preto)",           "valor": "#0b0b0b"},
            {"nome": "Texto Principal (Branco)", "valor": "#ffffff"},
            {"nome": "Bordas e Linhas",          "valor": "#1a1a1a"},
            {"nome": "Texto Secundário (Cinza)", "valor": "#888888"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t22_nav_logos": [{"valor": "Zajno / Motion"}],
        "t22_nav_links": [
            {"texto": "Trabalhos", "url": "seção Showcase de Projetos"},
            {"texto": "Estúdio",   "url": "seção Manifesto do Estúdio"},
            {"texto": "Contato",   "url": "seção Rodapé de Contato"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t22_hero_titulos": [{"valor": "MOVIMENTO É A NOSSA LINGUAGEM"}],
        "t22_hero_descs":   [{"valor": "Somos um estúdio de design focado em criar experiências digitais que ganham vida através do movimento e da tecnologia de ponta."}],

        # ── PROJETOS ────────────────────────────────────────────────────────
        "t22_project_items": [
            {"img": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=800",  "category": "Motion Graphics / 2024", "nome": "Cyber Identity"},
            {"img": "https://images.unsplash.com/photo-1614850523296-d8c1af93d400?w=800","category": "Interface Design / 2023","nome": "Liquid UI"},
            {"img": "https://images.unsplash.com/photo-1633167606207-d840b5070fc2?w=800","category": "Art Direction / 2024",   "nome": "Astro Forms"},
            {"img": "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800","category": "3D Animation / 2024",    "nome": "Glass Echo"},
        ],

        # ── MANIFESTO ───────────────────────────────────────────────────────
        "t22_manifest_titulos": [{"valor": "Nós não apenas movemos pixels. Nós contamos histórias que definem o futuro das marcas."}],
        "t22_manifest_descs":   [{"valor": "Trabalhamos com marcas audaciosas para transformar ideias complexas em interações digitais simples, memoráveis e impactantes."}],

        # ── FOOTER (CTA) ─────────────────────────────────────────────────────
        "t22_foot_labels":  [{"valor": "Pronto para elevar sua marca?"}],
        "t22_foot_titulos": [{"valor": "VAMOS CRIAR JUNTOS"}],
        "t22_foot_emails":  [{"valor": "studio@zajno.com"}],
        "t22_foot_btns":    [{"texto": "Iniciar Projeto", "url": "https://wa.me/5511999999999"}],
        "t22_foot_copys":   [{"valor": "© 2026 Zajno Studio — São Paulo / Remoto"}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t22_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t22_nome_cliente,
            "email":     st.session_state.t22_email_cliente,
            "nome_site": st.session_state.t22_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t22_nome_site}",
        },
        "cores": st.session_state.t22_cores,
        "navbar": {
            "logos": st.session_state.t22_nav_logos,
            "links": st.session_state.t22_nav_links,
        },
        "hero": {
            "titulos": st.session_state.t22_hero_titulos,
            "descs":   st.session_state.t22_hero_descs,
        },
        "projetos": st.session_state.t22_project_items,
        "manifesto": {
            "titulos": st.session_state.t22_manifest_titulos,
            "descs":   st.session_state.t22_manifest_descs,
        },
        "footer_cta": {
            "labels":   st.session_state.t22_foot_labels,
            "titulos":  st.session_state.t22_foot_titulos,
            "emails":   st.session_state.t22_foot_emails,
            "botoes":   st.session_state.t22_foot_btns,
            "copyright": st.session_state.t22_foot_copys,
        },
        "observacoes": st.session_state.t22_obs,
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
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
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

            st.session_state.t22_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t22_nome_cliente,
                key="t22_nome_cliente_inp", placeholder="Ex: Ana Lima",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t22_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t22_email_cliente,
                key="t22_email_cliente_inp", placeholder="Ex: ana@estudio.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: zajno, motionstudio, anadesign).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t22_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t22_nome_site,
                key="t22_nome_site_inp",
                placeholder="Ex: zajno  →  sttacksite.streamlit.app/?c=zajno",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t22_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t22_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t22_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t22_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t22_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t22_cores) > 1 and _del_btn(f"t22_cor_del_{i}"):
                        st.session_state.t22_cores.pop(i); st.rerun()
            if _add_btn("t22_cor_add", "＋ Adicionar cor"):
                st.session_state.t22_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome do estúdio  *(lado esquerdo)*")
            for i, item in enumerate(st.session_state.t22_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t22_nav_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t22_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: Seu Estúdio / Motion")
                with c2:
                    if len(st.session_state.t22_nav_logos) > 1 and _del_btn(f"t22_logo_del_{i}"):
                        st.session_state.t22_nav_logos.pop(i); st.rerun()
            if _add_btn("t22_logo_add", "＋ Adicionar logo"):
                st.session_state.t22_nav_logos.append({"valor": "Estúdio"}); st.rerun()

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t22_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t22_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t22_nl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t22_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t22_nl_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t22_nav_links) > 1 and _del_btn(f"t22_nl_del_{i}"):
                        st.session_state.t22_nav_links.pop(i); st.rerun()
            if _add_btn("t22_nl_add", "＋ Adicionar link"):
                st.session_state.t22_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎬 Hero Section</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Título em letras enormes:</strong> escreva o texto normalmente.
                Se quiser que parte apareça em linha diferente, descreva isso na seção Observações.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Título principal  *(exibido em letras enormes)*")
            for i, t in enumerate(st.session_state.t22_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t22_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t22_h_t_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Ex: DESIGN É A NOSSA LINGUAGEM")
                with c2:
                    if len(st.session_state.t22_hero_titulos) > 1 and _del_btn(f"t22_h_t_del_{i}"):
                        st.session_state.t22_hero_titulos.pop(i); st.rerun()
            if _add_btn("t22_h_t_add", "＋ Adicionar título"):
                st.session_state.t22_hero_titulos.append({"valor": "NOVO TÍTULO"}); st.rerun()

            st.caption("Descrição  *(parágrafo abaixo do título)*")
            for i, d in enumerate(st.session_state.t22_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t22_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t22_h_d_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Descreva o estúdio, sua proposta e especialidade em 2-3 frases")
                with c2:
                    if len(st.session_state.t22_hero_descs) > 1 and _del_btn(f"t22_h_d_del_{i}"):
                        st.session_state.t22_hero_descs.pop(i); st.rerun()
            if _add_btn("t22_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t22_hero_descs.append({"valor": "Nova descrição do estúdio."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. SHOWCASE DE PROJETOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Showcase de Projetos</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagens dos projetos:</strong> cole a URL do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanho recomendado: <strong>800 × 600 px</strong> (paisagem) para melhor visual no grid.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Cards de projeto  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t22_project_items):
                with st.expander(f"Projeto {i+1}: {item['nome']}"):
                    st.session_state.t22_project_items[i]["nome"] = st.text_input(
                        "Título do Projeto", item["nome"], key=f"t22_pi_n_{i}",
                        placeholder="Ex: Brand Identity para Empresa X")
                    st.session_state.t22_project_items[i]["category"] = st.text_input(
                        "Categoria / Ano", item["category"], key=f"t22_pi_c_{i}",
                        placeholder="Ex: Motion Graphics / 2025")
                    st.session_state.t22_project_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t22_pi_i_{i}",
                        placeholder="https://i.imgur.com/... ou URL da imagem",
                        help="Cole a URL da imagem do imgur.com — 800×600 px ideal")
                    if len(st.session_state.t22_project_items) > 1:
                        if st.button("🗑 Remover este projeto", key=f"t22_pi_del_{i}"):
                            st.session_state.t22_project_items.pop(i); st.rerun()
            if _add_btn("t22_pi_add", "＋ Adicionar projeto"):
                st.session_state.t22_project_items.append({
                    "img": "", "category": "MOTION / 2026", "nome": "NOVO PROJETO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. MANIFESTO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📜 Manifesto do Estúdio</div>', unsafe_allow_html=True)

            st.caption("Título  *(frase de impacto sobre a filosofia do estúdio)*")
            for i, t in enumerate(st.session_state.t22_manifest_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t22_manifest_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t22_mt_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Ex: Nós não apenas criamos marcas. Nós criamos memórias.")
                with c2:
                    if len(st.session_state.t22_manifest_titulos) > 1 and _del_btn(f"t22_mt_del_{i}"):
                        st.session_state.t22_manifest_titulos.pop(i); st.rerun()
            if _add_btn("t22_mt_add", "＋ Adicionar título"):
                st.session_state.t22_manifest_titulos.append({"valor": "Novo manifesto."}); st.rerun()

            st.caption("Descrição  *(complemento da filosofia)*")
            for i, d in enumerate(st.session_state.t22_manifest_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t22_manifest_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t22_md_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Descreva o método, valores ou diferencial do estúdio")
                with c2:
                    if len(st.session_state.t22_manifest_descs) > 1 and _del_btn(f"t22_md_del_{i}"):
                        st.session_state.t22_manifest_descs.pop(i); st.rerun()
            if _add_btn("t22_md_add", "＋ Adicionar descrição"):
                st.session_state.t22_manifest_descs.append({"valor": "Nova descrição."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. FOOTER (CTA)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">✉️ Rodapé (CTA de Contato)</div>', unsafe_allow_html=True)

            st.caption("Label CTA  *(texto pequeno acima do título)*")
            for i, l in enumerate(st.session_state.t22_foot_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t22_foot_labels[i]["valor"] = st.text_input(
                        "Label", l["valor"], key=f"t22_fl_{i}", label_visibility="collapsed",
                        placeholder="Ex: Vamos conversar?")
                with c2:
                    if len(st.session_state.t22_foot_labels) > 1 and _del_btn(f"t22_fl_del_{i}"):
                        st.session_state.t22_foot_labels.pop(i); st.rerun()
            if _add_btn("t22_fl_add", "＋ Adicionar label"):
                st.session_state.t22_foot_labels.append({"valor": "Novo Label"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Título CTA:</strong> escreva o texto normalmente.
                Se quiser quebrar em linhas diferentes, descreva isso na seção Observações.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Título CTA  *(chamada principal do rodapé)*")
            for i, t in enumerate(st.session_state.t22_foot_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t22_foot_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t22_ft_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Ex: VAMOS CRIAR JUNTOS")
                with c2:
                    if len(st.session_state.t22_foot_titulos) > 1 and _del_btn(f"t22_ft_del_{i}"):
                        st.session_state.t22_foot_titulos.pop(i); st.rerun()
            if _add_btn("t22_ft_add", "＋ Adicionar título"):
                st.session_state.t22_foot_titulos.append({"valor": "NOVO TÍTULO"}); st.rerun()

            st.caption("E-mail de contato  *(exibido como link clicável)*")
            for i, e in enumerate(st.session_state.t22_foot_emails):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t22_foot_emails[i]["valor"] = st.text_input(
                        "Email", e["valor"], key=f"t22_fe_{i}", label_visibility="collapsed",
                        placeholder="email@estudio.com",
                        help="Este e-mail será exibido no rodapé como link de contato.")
                with c2:
                    if len(st.session_state.t22_foot_emails) > 1 and _del_btn(f"t22_fe_del_{i}"):
                        st.session_state.t22_foot_emails.pop(i); st.rerun()
            if _add_btn("t22_fe_add", "＋ Adicionar email"):
                st.session_state.t22_foot_emails.append({"valor": "email@estudio.com"}); st.rerun()

            st.caption("Botão de ação  *(Texto | URL ou WhatsApp)*")
            for i, btn in enumerate(st.session_state.t22_foot_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t22_foot_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t22_fb_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Iniciar Projeto")
                with c2:
                    st.session_state.t22_foot_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t22_fb_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou mailto:...")
                with c3:
                    if len(st.session_state.t22_foot_btns) > 1 and _del_btn(f"t22_fb_del_{i}"):
                        st.session_state.t22_foot_btns.pop(i); st.rerun()
            if _add_btn("t22_fb_add", "＋ Adicionar botão"):
                st.session_state.t22_foot_btns.append({"texto": "CONTATO", "url": ""}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t22_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t22_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t22_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 Seu Estúdio — São Paulo")
                with c2:
                    if len(st.session_state.t22_foot_copys) > 1 and _del_btn(f"t22_fcp_del_{i}"):
                        st.session_state.t22_foot_copys.pop(i); st.rerun()
            if _add_btn("t22_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t22_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. IMAGENS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Guia de Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Como adicionar imagens ao seu site:</strong><br><br>
                1. Acesse <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a>
                   (gratuito, sem cadastro) e faça o upload da sua imagem.<br>
                2. Clique com o botão direito na imagem → <em>Copiar endereço da imagem</em> — a URL termina em
                   <code>.jpg</code>, <code>.png</code> ou <code>.webp</code>.<br>
                3. Cole a URL no campo de imagem do projeto correspondente acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Projetos (showcase): <strong>800 × 600 px</strong> (paisagem)<br>
                • Logo: <strong>200 × 60 px</strong> (fundo transparente, PNG)<br><br>
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
                Ex: "tornar o layout mais cinematográfico", "adicionar seção de serviços",
                "adicionar depoimentos de clientes", "adicionar link para case study de cada projeto"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t22_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t22_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t22_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t22_obs) > 1 and _del_btn(f"t22_obs_del_{i}"):
                        st.session_state.t22_obs.pop(i); st.rerun()
            if _add_btn("t22_obs_add", "＋ Adicionar observação"):
                st.session_state.t22_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 9. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t22_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t22_email_cliente.strip() or "@" not in st.session_state.t22_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t22_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t22_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t22_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t22_nome_cliente}'*."
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
        page_icon="🎬",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
