import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/editor/main/img34.png"
TEMPLATE_NAME      = "Template 34 — Frequency Style (Breathwork Experience)"
TEMPLATE_ID        = "template_34"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t34_nome_cliente":  "",
        "t34_email_cliente": "",
        "t34_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t34_cores": [
            {"nome": "Fundo (preto profundo)",   "valor": "#050505"},
            {"nome": "Acento (verde-limão)",      "valor": "#b5ff00"},
            {"nome": "Roxo (gradiente)",          "valor": "#4a148c"},
            {"nome": "Texto (branco)",            "valor": "#ffffff"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t34_nav_logos": [{"texto": "FREQUENCY"}],
        "t34_nav_links": [
            {"texto": "A Jornada", "url": "seção Benefícios"},
            {"texto": "Estúdios",  "url": "seção Agenda"},
            {"texto": "Digital",   "url": "seção Agenda"},
        ],
        "t34_nav_ctas": [{"texto": "Membro", "url": "https://wa.me/5511999999999"}],

        # ── HERO ────────────────────────────────────────────────────────────
        "t34_hero_labels":  [{"valor": "Sinta sua própria energia"}],
        "t34_hero_titulos": [{"valor": "Mude sua respiração. Mude sua consciência."}],
        "t34_hero_btns":    [{"texto": "COMECE SUA VIAGEM", "url": "seção Benefícios"}],

        # ── MÍDIA ───────────────────────────────────────────────────────────
        "t34_media_imgs": [{"url": "https://images.unsplash.com/photo-1511216335778-7cb8f49fa7a3?w=1600", "texto": "O poder de se reconectar."}],

        # ── BENEFÍCIOS ──────────────────────────────────────────────────────
        "t34_ben_headers": [{"valor": "Por que Frequency?"}],
        "t34_ben_items": [
            {"titulo": "Clareza Mental",      "desc": "Remova o ruído cotidiano e acesse estados profundos de foco através de técnicas rítmicas de respiração.", "btn_texto": "SAIBA MAIS", "btn_url": "https://wa.me/5511999999999"},
            {"titulo": "Liberação Emocional", "desc": "Acesse e processe emoções estocadas no corpo de forma segura e guiada por especialistas.",               "btn_texto": "SAIBA MAIS", "btn_url": "https://wa.me/5511999999999"},
            {"titulo": "Conexão Vital",       "desc": "Sinta o fluxo de energia vital percorrendo seu sistema, revitalizando cada célula do seu ser.",            "btn_texto": "SAIBA MAIS", "btn_url": "https://wa.me/5511999999999"},
        ],

        # ── AULAS / AGENDA ──────────────────────────────────────────────────
        "t34_aulas_labels":  [{"valor": "Aulas Ao Vivo"}],
        "t34_aulas_titulos": [{"valor": "Encontre seu ritmo."}],
        "t34_aulas_btns":    [{"texto": "VER AGENDA COMPLETA", "url": "https://wa.me/5511999999999"}],
        "t34_aulas_items": [
            {"nome": "Breathwork Fundamental", "horario": "Segundas | 19:00", "url": "https://wa.me/5511999999999"},
            {"nome": "Jornada de Expansão",    "horario": "Quartas | 20:30",  "url": "https://wa.me/5511999999999"},
            {"nome": "Detox Dopaminérgico",    "horario": "Sábados | 10:00",  "url": "https://wa.me/5511999999999"},
        ],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t34_foot_logos": [{"texto": "FREQUENCY"}],
        "t34_foot_links": [
            {"texto": "Instagram",              "url": "https://instagram.com/"},
            {"texto": "Spotify",                "url": "https://spotify.com/"},
            {"texto": "Política de Privacidade","url": "https://wa.me/5511999999999"},
            {"texto": "Contato",                "url": "mailto:contato@meusite.com"},
        ],
        "t34_foot_copys": [{"valor": "© 2026 FREQUENCY BREATHWORK. TODOS OS DIREITOS RESERVADOS. SINTA A FREQUÊNCIA."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t34_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t34_nome_cliente,
            "email":     st.session_state.t34_email_cliente,
            "nome_site": st.session_state.t34_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t34_nome_site}",
        },
        "cores": st.session_state.t34_cores,
        "navbar": {
            "logos": st.session_state.t34_nav_logos,
            "links": st.session_state.t34_nav_links,
            "cta":   st.session_state.t34_nav_ctas,
        },
        "hero": {
            "labels":  st.session_state.t34_hero_labels,
            "titulos": st.session_state.t34_hero_titulos,
            "botoes":  st.session_state.t34_hero_btns,
        },
        "midia": st.session_state.t34_media_imgs,
        "beneficios": {
            "headers": st.session_state.t34_ben_headers,
            "items":   st.session_state.t34_ben_items,
        },
        "agenda": {
            "labels":  st.session_state.t34_aulas_labels,
            "titulos": st.session_state.t34_aulas_titulos,
            "botoes":  st.session_state.t34_aulas_btns,
            "aulas":   st.session_state.t34_aulas_items,
        },
        "footer": {
            "logos":     st.session_state.t34_foot_logos,
            "links":     st.session_state.t34_foot_links,
            "copyright": st.session_state.t34_foot_copys,
        },
        "observacoes": st.session_state.t34_obs,
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

            st.session_state.t34_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t34_nome_cliente,
                key="t34_nome_cliente_inp", placeholder="Ex: Marina Breathwork",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t34_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Kiwify)",
                value=st.session_state.t34_email_cliente,
                key="t34_email_cliente_inp", placeholder="Ex: marina@frequency.com",
                help="Use o mesmo e-mail com o qual você comprou na Kiwify.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: frequency, breathwork, meuestudio).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t34_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t34_nome_site,
                key="t34_nome_site_inp",
                placeholder="Ex: frequency  →  sttacksite.streamlit.app/?c=frequency",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🌑 <strong>Template dark:</strong> fundo preto profundo com acento em verde-limão.
                O "Acento" é a cor usada em labels, botões e destaques — troque por qualquer cor vibrante
                que contraste bem com fundo escuro (ex: laranja, ciano, branco).
            </div>
            """, unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t34_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t34_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t34_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t34_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t34_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t34_cores) > 1 and _del_btn(f"t34_cor_del_{i}"):
                        st.session_state.t34_cores.pop(i); st.rerun()
            if _add_btn("t34_cor_add", "＋ Adicionar cor"):
                st.session_state.t34_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo  *(nome da marca em letras grandes — CAIXA ALTA)*")
            for i, item in enumerate(st.session_state.t34_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t34_nav_logos[i]["texto"] = st.text_input(
                        "Logo", item["texto"], key=f"t34_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: FREQUENCY ou NOME DO ESTÚDIO")
                with c2:
                    if len(st.session_state.t34_nav_logos) > 1 and _del_btn(f"t34_logo_del_{i}"):
                        st.session_state.t34_nav_logos.pop(i); st.rerun()
            if _add_btn("t34_logo_add", "＋ Adicionar logo"):
                st.session_state.t34_nav_logos.append({"texto": "MARCA"}); st.rerun()

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t34_nav_links):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1:
                    st.session_state.t34_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t34_navl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto")
                with c2:
                    st.session_state.t34_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t34_navl_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t34_nav_links) > 1 and _del_btn(f"t34_navl_del_{i}"):
                        st.session_state.t34_nav_links.pop(i); st.rerun()
            if _add_btn("t34_navl_add", "＋ Adicionar link"):
                st.session_state.t34_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            st.caption("Botão destaque  *(cor de acento — geralmente CTA de inscrição/membro)*")
            for i, cta in enumerate(st.session_state.t34_nav_ctas):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1:
                    st.session_state.t34_nav_ctas[i]["texto"] = st.text_input(
                        "Texto", cta["texto"], key=f"t34_ncta_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Membro ou ASSINAR")
                with c2:
                    st.session_state.t34_nav_ctas[i]["url"] = st.text_input(
                        "URL", cta["url"], key=f"t34_ncta_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link de inscrição")
                with c3:
                    if len(st.session_state.t34_nav_ctas) > 1 and _del_btn(f"t34_ncta_del_{i}"):
                        st.session_state.t34_nav_ctas.pop(i); st.rerun()
            if _add_btn("t34_ncta_add", "＋ Adicionar CTA"):
                st.session_state.t34_nav_ctas.append({"texto": "CTA", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🧘 Hero Section</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Título:</strong> escreva normalmente. Se quiser que parte do título apareça
                com opacidade reduzida (efeito "desvanecer" do template original), descreva nas
                Observações — ex: "quero a palavra 'consciência.' com menor opacidade".
            </div>
            """, unsafe_allow_html=True)

            st.caption("Label  *(texto em verde-limão acima do título)*")
            for i, l in enumerate(st.session_state.t34_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t34_hero_labels[i]["valor"] = st.text_input(
                        "Label", l["valor"], key=f"t34_h_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: Sinta sua própria energia")
                with c2:
                    if len(st.session_state.t34_hero_labels) > 1 and _del_btn(f"t34_h_l_del_{i}"):
                        st.session_state.t34_hero_labels.pop(i); st.rerun()
            if _add_btn("t34_h_l_add", "＋ Adicionar label"):
                st.session_state.t34_hero_labels.append({"valor": ""}); st.rerun()

            st.caption("Título principal  *(fonte serif itálica grande)*")
            for i, t in enumerate(st.session_state.t34_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t34_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t34_h_t_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Ex: Mude sua respiração. Mude sua consciência.")
                with c2:
                    if len(st.session_state.t34_hero_titulos) > 1 and _del_btn(f"t34_h_t_del_{i}"):
                        st.session_state.t34_hero_titulos.pop(i); st.rerun()
            if _add_btn("t34_h_t_add", "＋ Adicionar título"):
                st.session_state.t34_hero_titulos.append({"valor": ""}); st.rerun()

            st.caption("Botão CTA  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t34_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t34_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t34_hb_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: COMECE SUA VIAGEM")
                with c2:
                    st.session_state.t34_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t34_hb_u_{i}", label_visibility="collapsed",
                        placeholder="seção Benefícios ou https://wa.me/...")
                with c3:
                    if len(st.session_state.t34_hero_btns) > 1 and _del_btn(f"t34_hb_del_{i}"):
                        st.session_state.t34_hero_btns.pop(i); st.rerun()
            if _add_btn("t34_hb_add", "＋ Adicionar botão"):
                st.session_state.t34_hero_btns.append({"texto": "COMEÇAR", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. MÍDIA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎬 Seção de Mídia</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 Imagem larga que aparece entre o hero e os benefícios, com escurecimento e texto em overlay.
                Tamanho ideal: <strong>1600 × 700 px</strong> (paisagem, tema meditação/natureza/respiração).
            </div>
            """, unsafe_allow_html=True)
            st.caption("Imagem de fundo  *(URL | Frase em itálico em overlay)*")
            for i, m in enumerate(st.session_state.t34_media_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t34_media_imgs[i]["url"] = st.text_input(
                        "URL", m["url"], key=f"t34_mi_u_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... — 1600×700 px ideal")
                    st.session_state.t34_media_imgs[i]["texto"] = st.text_input(
                        "Frase em overlay", m["texto"], key=f"t34_mi_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: O poder de se reconectar.")
                with c2:
                    if len(st.session_state.t34_media_imgs) > 1 and _del_btn(f"t34_mi_del_{i}"):
                        st.session_state.t34_media_imgs.pop(i); st.rerun()
            if _add_btn("t34_mi_add", "＋ Adicionar mídia"):
                st.session_state.t34_media_imgs.append({"url": "", "texto": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. BENEFÍCIOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">✨ Benefícios (Cards)</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, bh in enumerate(st.session_state.t34_ben_headers):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t34_ben_headers[i]["valor"] = st.text_input(
                        "Título", bh["valor"], key=f"t34_b_h_{i}", label_visibility="collapsed",
                        placeholder="Ex: Por que Frequency?")
                with c2:
                    if len(st.session_state.t34_ben_headers) > 1 and _del_btn(f"t34_b_h_del_{i}"):
                        st.session_state.t34_ben_headers.pop(i); st.rerun()
            if _add_btn("t34_b_h_add", "＋ Adicionar título"):
                st.session_state.t34_ben_headers.append({"valor": "Por que nós?"}); st.rerun()

            st.caption("Cards de benefício  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t34_ben_items):
                with st.expander(f"Benefício {i+1}: {item['titulo']}"):
                    st.session_state.t34_ben_items[i]["titulo"] = st.text_input(
                        "Título", item["titulo"], key=f"t34_bi_t_{i}",
                        placeholder="Ex: Clareza Mental")
                    st.session_state.t34_ben_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t34_bi_d_{i}", height=80,
                        placeholder="Descreva este benefício em 2-3 frases.")
                    c1, c2 = st.columns(2)
                    with c1:
                        st.session_state.t34_ben_items[i]["btn_texto"] = st.text_input(
                            "Texto Botão", item["btn_texto"], key=f"t34_bi_bt_{i}",
                            placeholder="Ex: SAIBA MAIS")
                    with c2:
                        st.session_state.t34_ben_items[i]["btn_url"] = st.text_input(
                            "URL Botão", item["btn_url"], key=f"t34_bi_bu_{i}",
                            placeholder="https://wa.me/... ou link")
                    if len(st.session_state.t34_ben_items) > 1:
                        if st.button("🗑 Remover este card", key=f"t34_bi_del_{i}"):
                            st.session_state.t34_ben_items.pop(i); st.rerun()
            if _add_btn("t34_bi_add", "＋ Adicionar benefício"):
                st.session_state.t34_ben_items.append({
                    "titulo": "Novo Benefício", "desc": "",
                    "btn_texto": "SAIBA MAIS", "btn_url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. AGENDA DE AULAS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📅 Agenda de Aulas</div>', unsafe_allow_html=True)

            st.caption("Label  *(texto em verde-limão acima do título da agenda)*")
            for i, al in enumerate(st.session_state.t34_aulas_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t34_aulas_labels[i]["valor"] = st.text_input(
                        "Label", al["valor"], key=f"t34_a_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: Aulas Ao Vivo")
                with c2:
                    if len(st.session_state.t34_aulas_labels) > 1 and _del_btn(f"t34_a_l_del_{i}"):
                        st.session_state.t34_aulas_labels.pop(i); st.rerun()
            if _add_btn("t34_a_l_add", "＋ Adicionar label"):
                st.session_state.t34_aulas_labels.append({"valor": ""}); st.rerun()

            st.caption("Título da agenda")
            for i, at in enumerate(st.session_state.t34_aulas_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t34_aulas_titulos[i]["valor"] = st.text_input(
                        "Título", at["valor"], key=f"t34_a_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Encontre seu ritmo.")
                with c2:
                    if len(st.session_state.t34_aulas_titulos) > 1 and _del_btn(f"t34_a_t_del_{i}"):
                        st.session_state.t34_aulas_titulos.pop(i); st.rerun()
            if _add_btn("t34_a_t_add", "＋ Adicionar título"):
                st.session_state.t34_aulas_titulos.append({"valor": ""}); st.rerun()

            st.caption("Botão da agenda  *(Texto | URL)*")
            for i, abtn in enumerate(st.session_state.t34_aulas_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t34_aulas_btns[i]["texto"] = st.text_input(
                        "Texto", abtn["texto"], key=f"t34_ab_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: VER AGENDA COMPLETA")
                with c2:
                    st.session_state.t34_aulas_btns[i]["url"] = st.text_input(
                        "URL", abtn["url"], key=f"t34_ab_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link da agenda")
                with c3:
                    if len(st.session_state.t34_aulas_btns) > 1 and _del_btn(f"t34_ab_del_{i}"):
                        st.session_state.t34_aulas_btns.pop(i); st.rerun()
            if _add_btn("t34_ab_add", "＋ Adicionar botão"):
                st.session_state.t34_aulas_btns.append({"texto": "VER AGENDA", "url": ""}); st.rerun()

            st.caption("Itens da agenda  *(Nome da aula | Dia e Horário | URL de inscrição)*")
            for i, item in enumerate(st.session_state.t34_aulas_items):
                c1, c2, c3, c4 = st.columns([4, 4, 3, 1])
                with c1:
                    st.session_state.t34_aulas_items[i]["nome"] = st.text_input(
                        "Nome", item["nome"], key=f"t34_ai_n_{i}", label_visibility="collapsed",
                        placeholder="Ex: Breathwork Fundamental")
                with c2:
                    st.session_state.t34_aulas_items[i]["horario"] = st.text_input(
                        "Horário", item["horario"], key=f"t34_ai_h_{i}", label_visibility="collapsed",
                        placeholder="Ex: Segundas | 19:00")
                with c3:
                    st.session_state.t34_aulas_items[i]["url"] = st.text_input(
                        "URL", item["url"], key=f"t34_ai_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/...")
                with c4:
                    if len(st.session_state.t34_aulas_items) > 1 and _del_btn(f"t34_ai_del_{i}"):
                        st.session_state.t34_aulas_items.pop(i); st.rerun()
            if _add_btn("t34_ai_add", "＋ Adicionar aula"):
                st.session_state.t34_aulas_items.append({"nome": "Nova Aula", "horario": "Dia | Hora", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Logo do rodapé")
            for i, fl in enumerate(st.session_state.t34_foot_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t34_foot_logos[i]["texto"] = st.text_input(
                        "Logo", fl["texto"], key=f"t34_f_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: FREQUENCY ou NOME DA MARCA")
                with c2:
                    if len(st.session_state.t34_foot_logos) > 1 and _del_btn(f"t34_f_l_del_{i}"):
                        st.session_state.t34_foot_logos.pop(i); st.rerun()
            if _add_btn("t34_f_l_add", "＋ Adicionar logo"):
                st.session_state.t34_foot_logos.append({"texto": "MARCA"}); st.rerun()

            st.caption("Links do rodapé  *(Texto | URL, Instagram, Spotify, mailto:email, etc.)*")
            for i, flink in enumerate(st.session_state.t34_foot_links):
                c1, c2, c3 = st.columns([4, 5, 1])
                with c1:
                    st.session_state.t34_foot_links[i]["texto"] = st.text_input(
                        "Texto", flink["texto"], key=f"t34_fl_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Instagram ou Contato")
                with c2:
                    st.session_state.t34_foot_links[i]["url"] = st.text_input(
                        "URL", flink["url"], key=f"t34_fl_u_{i}", label_visibility="collapsed",
                        placeholder="https://instagram.com/... ou mailto:email@...")
                with c3:
                    if len(st.session_state.t34_foot_links) > 1 and _del_btn(f"t34_fl_del_{i}"):
                        st.session_state.t34_foot_links.pop(i); st.rerun()
            if _add_btn("t34_fl_add", "＋ Adicionar link"):
                st.session_state.t34_foot_links.append({"texto": "LINK", "url": ""}); st.rerun()

            st.caption("Copyright  *(texto de encerramento — pode ter duas linhas)*")
            for i, fcp in enumerate(st.session_state.t34_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t34_foot_copys[i]["valor"] = st.text_area(
                        "Copyright", fcp["valor"], key=f"t34_fcp_{i}", height=70,
                        label_visibility="collapsed",
                        placeholder="Ex: © 2026 NOME DA MARCA. TODOS OS DIREITOS RESERVADOS.")
                with c2:
                    if len(st.session_state.t34_foot_copys) > 1 and _del_btn(f"t34_fcp_del_{i}"):
                        st.session_state.t34_foot_copys.pop(i); st.rerun()
            if _add_btn("t34_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t34_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. IMAGENS — GUIA
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Guia de Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Tamanhos recomendados:</strong><br>
                • Seção de Mídia (faixa larga): <strong>1600 × 700 px</strong>
                (paisagem, tema meditação/natureza/respiração — funciona melhor com fotos escuras)<br>
                • Logo: <strong>200 × 60 px</strong> (PNG com fundo transparente)<br><br>
                <strong>Como subir imagens:</strong><br>
                1. Acesse <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a> (gratuito, sem cadastro).<br>
                2. Faça upload → botão direito na imagem → <em>Copiar endereço da imagem</em>.<br>
                3. Cole no campo correspondente acima.<br><br>
                ❌ <strong>Não conseguiu?</strong> Envie para <strong>sttacksite@gmail.com</strong>
                com o assunto <em>"Imagem — [nome do seu site]"</em>.
            </div>
            """, unsafe_allow_html=True)

            # ══════════════════════════════════════════════════════════════════
            # 9. OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações / Pedidos Extras</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="warn-box">
                💬 <strong>Use este espaço para tudo que não encontrou nos campos acima!</strong><br>
                Ex: "manter atmosfera dark e minimalista", "quero 'consciência.' com menor opacidade no título",
                "adicionar seção de depoimentos", "adicionar preços/planos de assinatura"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t34_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t34_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t34_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t34_obs) > 1 and _del_btn(f"t34_obs_del_{i}"):
                        st.session_state.t34_obs.pop(i); st.rerun()
            if _add_btn("t34_obs_add", "＋ Adicionar observação"):
                st.session_state.t34_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 10. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t34_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t34_email_cliente.strip() or "@" not in st.session_state.t34_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Kiwify).")
            if not st.session_state.t34_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t34_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t34_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t34_nome_cliente}'*."
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
        page_icon="🧘",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
