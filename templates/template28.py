import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img28.png"
TEMPLATE_NAME      = "Template 28 — HGQ Coaching Style (Business & Leadership)"
TEMPLATE_ID        = "template_28"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t28_nome_cliente":  "",
        "t28_email_cliente": "",
        "t28_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t28_cores": [
            {"nome": "Azul Principal",  "valor": "#003366"},
            {"nome": "Amarelo Accent",  "valor": "#ffcc00"},
            {"nome": "Texto Principal", "valor": "#333333"},
            {"nome": "Cinza de Fundo",  "valor": "#f2f2f2"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t28_nav_logos": [{"valor": "HGQ."}],
        "t28_nav_links": [
            {"texto": "TREINAMENTOS", "url": "seção Nossas Soluções"},
            {"texto": "FORMAÇÕES",    "url": "seção Nossas Soluções"},
            {"texto": "SOBRE",        "url": "seção Depoimentos"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t28_hero_imgs":       [{"valor": "https://images.unsplash.com/photo-1475721027785-f74dea327912?w=1600"}],
        "t28_hero_subtitulos": [{"valor": "VOCÊ NASCEU PARA ALGO MAIOR"}],
        "t28_hero_titulos":    [{"valor": "TRANSFORME A SUA PAIXÃO POR AJUDAR PESSOAS EM UMA PROFISSÃO LUCRATIVA."}],
        "t28_hero_descs":      [{"valor": "Participe da maior comunidade de coaches e líderes que estão mudando o Brasil."}],
        "t28_hero_btns":       [{"texto": "QUERO COMEÇAR AGORA", "url": "https://wa.me/5511999999999"}],

        # ── PROGRAMAS ───────────────────────────────────────────────────────
        "t28_prog_titulos": [{"valor": "NOSSAS SOLUÇÕES"}],
        "t28_prog_items": [
            {"title": "FORMAÇÃO EM COACHING", "subtitle": "O Começo de Tudo",  "desc": "O treinamento número 1 para quem deseja dominar as ferramentas e começar a atender.", "btn_texto": "VER DETALHES", "btn_url": "https://wa.me/5511999999999"},
            {"title": "MENTORIA IMPACTO",     "subtitle": "Alta Performance",  "desc": "Para profissionais que já faturam e querem escalar o seu negócio e impacto.",           "btn_texto": "VER DETALHES", "btn_url": "https://wa.me/5511999999999"},
            {"title": "LIDERANÇA PRO",        "subtitle": "Gestão de Equipes", "desc": "Desenvolva a mentalidade de um líder que inspira e gera resultados fora da curva.",     "btn_texto": "VER DETALHES", "btn_url": "https://wa.me/5511999999999"},
        ],

        # ── NÚMEROS ─────────────────────────────────────────────────────────
        "t28_stat_items": [
            {"valor": "+100k", "label": "Alunos Formados"},
            {"valor": "+15",   "label": "Anos de Experiência"},
            {"valor": "4.9/5", "label": "Avaliação Média"},
        ],

        # ── DEPOIMENTOS ─────────────────────────────────────────────────────
        "t28_depo_titulos": [{"valor": "O QUE DIZEM NOSSOS ALUNOS"}],
        "t28_depo_items": [
            {"texto": "Minha vida mudou completamente após o treinamento. Hoje tenho clareza de propósito e faturo 3x mais.", "autor": "Maria Oliveira"},
            {"texto": "O melhor investimento que fiz na minha carreira. As ferramentas são práticas e os resultados imediatos.", "autor": "João Pedro"},
        ],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t28_foot_titulos": [{"valor": "INSTITUTO DE COACHING E LIDERANÇA"}],
        "t28_foot_links": [
            {"texto": "Termos de Uso",            "url": "https://wa.me/5511999999999"},
            {"texto": "Políticas de Privacidade",  "url": "https://wa.me/5511999999999"},
        ],
        "t28_foot_copys": [{"valor": "© 2026 Todos os direitos reservados."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t28_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t28_nome_cliente,
            "email":     st.session_state.t28_email_cliente,
            "nome_site": st.session_state.t28_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t28_nome_site}",
        },
        "cores": st.session_state.t28_cores,
        "navbar": {
            "logos": st.session_state.t28_nav_logos,
            "links": st.session_state.t28_nav_links,
        },
        "hero": {
            "imagens":    st.session_state.t28_hero_imgs,
            "subtitulos": st.session_state.t28_hero_subtitulos,
            "titulos":    st.session_state.t28_hero_titulos,
            "descs":      st.session_state.t28_hero_descs,
            "botoes":     st.session_state.t28_hero_btns,
        },
        "programas": {
            "titulos": st.session_state.t28_prog_titulos,
            "items":   st.session_state.t28_prog_items,
        },
        "numeros": st.session_state.t28_stat_items,
        "depoimentos": {
            "titulos": st.session_state.t28_depo_titulos,
            "items":   st.session_state.t28_depo_items,
        },
        "footer": {
            "titulos":   st.session_state.t28_foot_titulos,
            "links":     st.session_state.t28_foot_links,
            "copyright": st.session_state.t28_foot_copys,
        },
        "observacoes": st.session_state.t28_obs,
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

            st.session_state.t28_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t28_nome_cliente,
                key="t28_nome_cliente_inp", placeholder="Ex: Carlos Henrique",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t28_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t28_email_cliente,
                key="t28_email_cliente_inp", placeholder="Ex: carlos@institutocoaching.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: hgq, institutocoaching, liderancapro).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t28_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t28_nome_site,
                key="t28_nome_site_inp",
                placeholder="Ex: hgq  →  sttacksite.streamlit.app/?c=hgq",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t28_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t28_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t28_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t28_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t28_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t28_cores) > 1 and _del_btn(f"t28_cor_del_{i}"):
                        st.session_state.t28_cores.pop(i); st.rerun()
            if _add_btn("t28_cor_add", "＋ Adicionar cor"):
                st.session_state.t28_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Logo com ponto colorido:</strong> se quiser que o ponto final do logo
                apareça em outra cor (como amarelo), descreva isso na seção Observações.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Logo / Nome da marca  *(lado esquerdo)*")
            for i, item in enumerate(st.session_state.t28_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t28_nav_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t28_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: HGQ. ou NOME DO INSTITUTO")
                with c2:
                    if len(st.session_state.t28_nav_logos) > 1 and _del_btn(f"t28_logo_del_{i}"):
                        st.session_state.t28_nav_logos.pop(i); st.rerun()
            if _add_btn("t28_logo_add", "＋ Adicionar logo"):
                st.session_state.t28_nav_logos.append({"valor": "MARCA."}); st.rerun()

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t28_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t28_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t28_nl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t28_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t28_nl_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t28_nav_links) > 1 and _del_btn(f"t28_nl_del_{i}"):
                        st.session_state.t28_nav_links.pop(i); st.rerun()
            if _add_btn("t28_nl_add", "＋ Adicionar link"):
                st.session_state.t28_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">⚡ Hero Section</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagem de fundo do hero:</strong> tamanho ideal <strong>1600 × 900 px</strong>.
                Cole a URL do <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Use uma foto de palco, evento, apresentação ou mentoria para criar autoridade.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Imagem de fundo  *(URL)*")
            for i, img in enumerate(st.session_state.t28_hero_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t28_hero_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t28_h_img_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... ou URL da imagem")
                with c2:
                    if len(st.session_state.t28_hero_imgs) > 1 and _del_btn(f"t28_h_img_del_{i}"):
                        st.session_state.t28_hero_imgs.pop(i); st.rerun()
            if _add_btn("t28_h_img_add", "＋ Adicionar imagem"):
                st.session_state.t28_hero_imgs.append({"valor": ""}); st.rerun()

            st.caption("Subtítulo  *(texto em destaque acima do título principal)*")
            for i, s in enumerate(st.session_state.t28_hero_subtitulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t28_hero_subtitulos[i]["valor"] = st.text_input(
                        "Subtítulo", s["valor"], key=f"t28_h_s_{i}", label_visibility="collapsed",
                        placeholder="Ex: VOCÊ NASCEU PARA ALGO MAIOR")
                with c2:
                    if len(st.session_state.t28_hero_subtitulos) > 1 and _del_btn(f"t28_h_s_del_{i}"):
                        st.session_state.t28_hero_subtitulos.pop(i); st.rerun()
            if _add_btn("t28_h_s_add", "＋ Adicionar subtítulo"):
                st.session_state.t28_hero_subtitulos.append({"valor": "NOVO SUBTÍTULO"}); st.rerun()

            st.caption("Título principal  *(frase de impacto em maiúsculas)*")
            for i, t in enumerate(st.session_state.t28_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t28_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t28_h_t_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Ex: TRANSFORME SUA PAIXÃO EM UMA PROFISSÃO LUCRATIVA.")
                with c2:
                    if len(st.session_state.t28_hero_titulos) > 1 and _del_btn(f"t28_h_t_del_{i}"):
                        st.session_state.t28_hero_titulos.pop(i); st.rerun()
            if _add_btn("t28_h_t_add", "＋ Adicionar título"):
                st.session_state.t28_hero_titulos.append({"valor": "NOVO TÍTULO."}); st.rerun()

            st.caption("Descrição  *(frase de apoio)*")
            for i, d in enumerate(st.session_state.t28_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t28_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t28_h_d_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Ex: Participe da maior comunidade de coaches do Brasil.")
                with c2:
                    if len(st.session_state.t28_hero_descs) > 1 and _del_btn(f"t28_h_d_del_{i}"):
                        st.session_state.t28_hero_descs.pop(i); st.rerun()
            if _add_btn("t28_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t28_hero_descs.append({"valor": "Nova descrição."}); st.rerun()

            st.caption("Botão CTA  *(Texto | URL ou WhatsApp)*")
            for i, btn in enumerate(st.session_state.t28_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t28_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t28_hb_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: QUERO COMEÇAR AGORA")
                with c2:
                    st.session_state.t28_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t28_hb_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link de inscrição")
                with c3:
                    if len(st.session_state.t28_hero_btns) > 1 and _del_btn(f"t28_hb_del_{i}"):
                        st.session_state.t28_hero_btns.pop(i); st.rerun()
            if _add_btn("t28_hb_add", "＋ Adicionar botão"):
                st.session_state.t28_hero_btns.append({"texto": "COMEÇAR", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. PROGRAMAS (CARDS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📚 Nossas Soluções (Cards)</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t28_prog_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t28_prog_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t28_pt_{i}", label_visibility="collapsed",
                        placeholder="Ex: NOSSAS SOLUÇÕES ou NOSSOS PROGRAMAS")
                with c2:
                    if len(st.session_state.t28_prog_titulos) > 1 and _del_btn(f"t28_pt_del_{i}"):
                        st.session_state.t28_prog_titulos.pop(i); st.rerun()
            if _add_btn("t28_pt_add", "＋ Adicionar título"):
                st.session_state.t28_prog_titulos.append({"valor": "NOSSAS SOLUÇÕES"}); st.rerun()

            st.caption("Cards de programa  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t28_prog_items):
                with st.expander(f"Programa {i+1}: {item['title']}"):
                    st.session_state.t28_prog_items[i]["title"] = st.text_input(
                        "Título", item["title"], key=f"t28_pi_t_{i}",
                        placeholder="Ex: FORMAÇÃO EM COACHING")
                    st.session_state.t28_prog_items[i]["subtitle"] = st.text_input(
                        "Subtítulo", item["subtitle"], key=f"t28_pi_s_{i}",
                        placeholder="Ex: O Começo de Tudo")
                    st.session_state.t28_prog_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t28_pi_d_{i}", height=80,
                        placeholder="Descreva o programa, para quem é indicado e o principal resultado.")
                    c1, c2 = st.columns(2)
                    with c1:
                        st.session_state.t28_prog_items[i]["btn_texto"] = st.text_input(
                            "Texto Botão", item["btn_texto"], key=f"t28_pi_bt_{i}",
                            placeholder="Ex: VER DETALHES")
                    with c2:
                        st.session_state.t28_prog_items[i]["btn_url"] = st.text_input(
                            "URL Botão", item["btn_url"], key=f"t28_pi_bu_{i}",
                            placeholder="https://wa.me/... ou link de inscrição")
                    if len(st.session_state.t28_prog_items) > 1:
                        if st.button("🗑 Remover este programa", key=f"t28_pi_del_{i}"):
                            st.session_state.t28_prog_items.pop(i); st.rerun()
            if _add_btn("t28_pi_add", "＋ Adicionar solução"):
                st.session_state.t28_prog_items.append({
                    "title": "NOVO PROGRAMA", "subtitle": "Subtítulo", "desc": "",
                    "btn_texto": "VER DETALHES", "btn_url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. NÚMEROS (STATS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Números de Impacto</div>', unsafe_allow_html=True)
            st.caption("Números que mostram sua autoridade  *(Valor | Rótulo)*")
            for i, stat in enumerate(st.session_state.t28_stat_items):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t28_stat_items[i]["valor"] = st.text_input(
                        "Valor", stat["valor"], key=f"t28_st_v_{i}", label_visibility="collapsed",
                        placeholder="Ex: +100k ou 4.9/5")
                with c2:
                    st.session_state.t28_stat_items[i]["label"] = st.text_input(
                        "Rótulo", stat["label"], key=f"t28_st_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: Alunos Formados")
                with c3:
                    if len(st.session_state.t28_stat_items) > 1 and _del_btn(f"t28_st_del_{i}"):
                        st.session_state.t28_stat_items.pop(i); st.rerun()
            if _add_btn("t28_st_add", "＋ Adicionar número"):
                st.session_state.t28_stat_items.append({"valor": "0", "label": "Resultado"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. DEPOIMENTOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💬 Depoimentos</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t28_depo_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t28_depo_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t28_dt_{i}", label_visibility="collapsed",
                        placeholder="Ex: O QUE DIZEM NOSSOS ALUNOS")
                with c2:
                    if len(st.session_state.t28_depo_titulos) > 1 and _del_btn(f"t28_dt_del_{i}"):
                        st.session_state.t28_depo_titulos.pop(i); st.rerun()
            if _add_btn("t28_dt_add", "＋ Adicionar título"):
                st.session_state.t28_depo_titulos.append({"valor": "O QUE DIZEM"}); st.rerun()

            st.caption("Cards de depoimento  *(sem aspas — escreva o texto normalmente)*")
            for i, item in enumerate(st.session_state.t28_depo_items):
                with st.expander(f"Depoimento {i+1}: {item['autor']}"):
                    st.session_state.t28_depo_items[i]["texto"] = st.text_area(
                        "Texto", item["texto"], key=f"t28_di_t_{i}", height=90,
                        placeholder="Escreva o depoimento aqui, sem aspas.")
                    st.session_state.t28_depo_items[i]["autor"] = st.text_input(
                        "Autor", item["autor"], key=f"t28_di_a_{i}",
                        placeholder="Ex: Maria Oliveira — Coach Profissional")
                    if len(st.session_state.t28_depo_items) > 1:
                        if st.button("🗑 Remover este depoimento", key=f"t28_di_del_{i}"):
                            st.session_state.t28_depo_items.pop(i); st.rerun()
            if _add_btn("t28_di_add", "＋ Adicionar depoimento"):
                st.session_state.t28_depo_items.append({"texto": "", "autor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Título do rodapé  *(nome completo do instituto)*")
            for i, t in enumerate(st.session_state.t28_foot_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t28_foot_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t28_ftt_{i}", label_visibility="collapsed",
                        placeholder="Ex: INSTITUTO DE COACHING E LIDERANÇA")
                with c2:
                    if len(st.session_state.t28_foot_titulos) > 1 and _del_btn(f"t28_ftt_del_{i}"):
                        st.session_state.t28_foot_titulos.pop(i); st.rerun()
            if _add_btn("t28_ftt_add", "＋ Adicionar título"):
                st.session_state.t28_foot_titulos.append({"valor": "INSTITUTO"}); st.rerun()

            st.caption("Links do rodapé  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t28_foot_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t28_foot_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t28_footl_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Termos de Uso")
                with c2:
                    st.session_state.t28_foot_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t28_footl_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link da página")
                with c3:
                    if len(st.session_state.t28_foot_links) > 1 and _del_btn(f"t28_footl_del_{i}"):
                        st.session_state.t28_foot_links.pop(i); st.rerun()
            if _add_btn("t28_footl_add", "＋ Adicionar link"):
                st.session_state.t28_foot_links.append({"texto": "LINK", "url": ""}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t28_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t28_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t28_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 NOME DO INSTITUTO. Todos os direitos reservados.")
                with c2:
                    if len(st.session_state.t28_foot_copys) > 1 and _del_btn(f"t28_fcp_del_{i}"):
                        st.session_state.t28_foot_copys.pop(i); st.rerun()
            if _add_btn("t28_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t28_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. IMAGENS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Guia de Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Como adicionar imagens ao seu site:</strong><br><br>
                1. Acesse <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a>
                   (gratuito, sem cadastro) e faça o upload da sua imagem.<br>
                2. Clique com o botão direito na imagem → <em>Copiar endereço da imagem</em> — a URL termina em
                   <code>.jpg</code>, <code>.png</code> ou <code>.webp</code>.<br>
                3. Cole a URL no campo de imagem do hero acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Hero (fundo): <strong>1600 × 900 px</strong> (paisagem, foto de palco ou evento)<br>
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
                Ex: "usar tom mais corporativo", "quero o ponto do logo em amarelo",
                "adicionar seção de biografia do mentor", "adicionar vídeo de apresentação"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t28_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t28_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t28_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t28_obs) > 1 and _del_btn(f"t28_obs_del_{i}"):
                        st.session_state.t28_obs.pop(i); st.rerun()
            if _add_btn("t28_obs_add", "＋ Adicionar observação"):
                st.session_state.t28_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 10. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t28_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t28_email_cliente.strip() or "@" not in st.session_state.t28_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t28_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t28_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t28_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t28_nome_cliente}'*."
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
        page_icon="🎓",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
