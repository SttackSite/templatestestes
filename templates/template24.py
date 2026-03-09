import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/editor/main/img24.png"
TEMPLATE_NAME      = "Template 24 — YOLU Night Care Style (Beauty & Cosmetics)"
TEMPLATE_ID        = "template_24"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t24_nome_cliente":  "",
        "t24_email_cliente": "",
        "t24_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t24_cores": [
            {"nome": "Fundo Início (Azul Escuro)", "valor": "#050a14"},
            {"nome": "Fundo Meio (Azul Noite)",    "valor": "#0f1c3d"},
            {"nome": "Fundo Fim (Roxo Profundo)",  "valor": "#1e1b4b"},
            {"nome": "Texto Principal (Branco)",   "valor": "#ffffff"},
            {"nome": "Destaque (Dourado Suave)",   "valor": "#d4af37"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t24_nav_logos": [{"valor": "YOLU"}],
        "t24_nav_links": [
            {"texto": "CONCEITO", "url": "seção Conceito"},
            {"texto": "PRODUTOS", "url": "seção Vitrine de Produtos"},
            {"texto": "CONTATO",  "url": "seção Rodapé"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t24_hero_labels":  [{"valor": "BELEZA QUE NASCE À NOITE"}],
        "t24_hero_titulos": [{"valor": "A Night Calm Experience"}],
        "t24_hero_descs":   [{"valor": "Reparação profunda enquanto você dorme. Sinta a tranquilidade da noite em cada fio."}],
        "t24_hero_imgs":    [{"valor": "https://images.unsplash.com/photo-1519681393784-d120267933ba?w=1600"}],

        # ── CONCEITO ────────────────────────────────────────────────────────
        "t24_concept_titulos": [{"valor": "Por que Cuidados Noturnos?"}],
        "t24_concept_descs":   [{"valor": "Durante a noite, o seu cabelo está livre das agressões externas do dia. É o momento perfeito para a penetração intensa de nutrientes. Nossa fórmula inspirada no sono reparador protege as cutículas do atrito com o travesseiro, garantindo um despertar radiante."}],

        # ── PRODUTOS ────────────────────────────────────────────────────────
        "t24_product_items": [
            {"img": "https://images.unsplash.com/photo-1626784215021-2e39ccf971cd?w=600", "nome": "Calm Night Repair",  "category": "SHAMPOO & TRATAMENTO", "desc": "Para cabelos secos e indisciplinados. Foco em hidratação profunda.",          "btn_text": "SAIBA MAIS", "btn_url": "https://wa.me/5511999999999"},
            {"img": "https://images.unsplash.com/photo-1626784215021-2e39ccf971cd?w=600", "nome": "Relax Night Repair", "category": "CUIDADO INTENSIVO",     "desc": "Para cabelos danificados por processos químicos. Foco em reconstrução.", "btn_text": "SAIBA MAIS", "btn_url": "https://wa.me/5511999999999"},
        ],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t24_foot_brand_names": [{"valor": "YOLU"}],
        "t24_foot_copys":       [{"valor": "© 2026 YOLU. Todos os direitos reservados."}],
        "t24_foot_cols": [
            {"titulo": "REDES SOCIAIS", "links": [
                {"texto": "INSTAGRAM", "url": "https://instagram.com/"},
                {"texto": "TWITTER",   "url": "https://twitter.com/"},
                {"texto": "TIKTOK",    "url": "https://tiktok.com/"},
            ]},
        ],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t24_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t24_nome_cliente,
            "email":     st.session_state.t24_email_cliente,
            "nome_site": st.session_state.t24_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t24_nome_site}",
        },
        "cores": st.session_state.t24_cores,
        "navbar": {
            "logos": st.session_state.t24_nav_logos,
            "links": st.session_state.t24_nav_links,
        },
        "hero": {
            "labels":  st.session_state.t24_hero_labels,
            "titulos": st.session_state.t24_hero_titulos,
            "descs":   st.session_state.t24_hero_descs,
            "imagens": st.session_state.t24_hero_imgs,
        },
        "conceito": {
            "titulos": st.session_state.t24_concept_titulos,
            "descs":   st.session_state.t24_concept_descs,
        },
        "produtos": st.session_state.t24_product_items,
        "footer": {
            "brand_names": st.session_state.t24_foot_brand_names,
            "colunas":     st.session_state.t24_foot_cols,
            "copyright":   st.session_state.t24_foot_copys,
        },
        "observacoes": st.session_state.t24_obs,
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

            st.session_state.t24_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t24_nome_cliente,
                key="t24_nome_cliente_inp", placeholder="Ex: Camila Ribeiro",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t24_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t24_email_cliente,
                key="t24_email_cliente_inp", placeholder="Ex: camila@marca.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: yolu, nightcare, belezanoturna).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t24_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t24_nome_site,
                key="t24_nome_site_inp",
                placeholder="Ex: yolu  →  sttacksite.streamlit.app/?c=yolu",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual (Gradiente)</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🌙 <strong>Este template usa gradiente de fundo:</strong> as três primeiras cores formam
                uma transição do topo ao fundo da página — do azul escuro ao roxo profundo.
                Você pode mantê-las ou criar sua própria paleta noturna!
            </div>
            """, unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t24_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t24_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t24_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t24_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t24_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t24_cores) > 1 and _del_btn(f"t24_cor_del_{i}"):
                        st.session_state.t24_cores.pop(i); st.rerun()
            if _add_btn("t24_cor_add", "＋ Adicionar cor"):
                st.session_state.t24_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca  *(lado esquerdo)*")
            for i, item in enumerate(st.session_state.t24_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t24_nav_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t24_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: YOLU ou NOME DA MARCA")
                with c2:
                    if len(st.session_state.t24_nav_logos) > 1 and _del_btn(f"t24_logo_del_{i}"):
                        st.session_state.t24_nav_logos.pop(i); st.rerun()
            if _add_btn("t24_logo_add", "＋ Adicionar logo"):
                st.session_state.t24_nav_logos.append({"valor": "MARCA"}); st.rerun()

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t24_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t24_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t24_nl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t24_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t24_nl_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t24_nav_links) > 1 and _del_btn(f"t24_nl_del_{i}"):
                        st.session_state.t24_nav_links.pop(i); st.rerun()
            if _add_btn("t24_nl_add", "＋ Adicionar link"):
                st.session_state.t24_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌙 Hero Section</div>', unsafe_allow_html=True)

            st.caption("Label  *(texto pequeno em letras maiúsculas — linha de categoria)*")
            for i, l in enumerate(st.session_state.t24_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t24_hero_labels[i]["valor"] = st.text_input(
                        "Label", l["valor"], key=f"t24_h_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: BELEZA QUE NASCE À NOITE")
                with c2:
                    if len(st.session_state.t24_hero_labels) > 1 and _del_btn(f"t24_h_l_del_{i}"):
                        st.session_state.t24_hero_labels.pop(i); st.rerun()
            if _add_btn("t24_h_l_add", "＋ Adicionar label"):
                st.session_state.t24_hero_labels.append({"valor": "NOVO LABEL"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Título principal:</strong> escreva o texto normalmente.
                Se quiser quebrar em linhas diferentes, descreva isso na seção Observações.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Título principal  *(nome do produto ou campanha)*")
            for i, t in enumerate(st.session_state.t24_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t24_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t24_h_t_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Ex: A Night Calm Experience")
                with c2:
                    if len(st.session_state.t24_hero_titulos) > 1 and _del_btn(f"t24_h_t_del_{i}"):
                        st.session_state.t24_hero_titulos.pop(i); st.rerun()
            if _add_btn("t24_h_t_add", "＋ Adicionar título"):
                st.session_state.t24_hero_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição  *(frase de impacto sobre o produto)*")
            for i, d in enumerate(st.session_state.t24_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t24_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t24_h_d_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Ex: Reparação profunda enquanto você dorme.")
                with c2:
                    if len(st.session_state.t24_hero_descs) > 1 and _del_btn(f"t24_h_d_del_{i}"):
                        st.session_state.t24_hero_descs.pop(i); st.rerun()
            if _add_btn("t24_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t24_hero_descs.append({"valor": "Nova descrição."}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagem de fundo do hero:</strong> cole a URL do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanho ideal: <strong>1600 × 900 px</strong> — prefira fotos noturnas, estreladas
                ou com iluminação suave para manter a atmosfera do template.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Imagem de fundo  *(URL)*")
            for i, img in enumerate(st.session_state.t24_hero_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t24_hero_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t24_h_i_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... ou URL da imagem")
                with c2:
                    if len(st.session_state.t24_hero_imgs) > 1 and _del_btn(f"t24_h_i_del_{i}"):
                        st.session_state.t24_hero_imgs.pop(i); st.rerun()
            if _add_btn("t24_h_i_add", "＋ Adicionar imagem"):
                st.session_state.t24_hero_imgs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. CONCEITO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📜 Seção de Conceito</div>', unsafe_allow_html=True)

            st.caption("Título  *(pergunta ou afirmação sobre o diferencial)*")
            for i, t in enumerate(st.session_state.t24_concept_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t24_concept_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t24_ct_{i}", label_visibility="collapsed",
                        placeholder="Ex: Por que Cuidados Noturnos?")
                with c2:
                    if len(st.session_state.t24_concept_titulos) > 1 and _del_btn(f"t24_ct_del_{i}"):
                        st.session_state.t24_concept_titulos.pop(i); st.rerun()
            if _add_btn("t24_ct_add", "＋ Adicionar título"):
                st.session_state.t24_concept_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição  *(texto explicando a filosofia e diferencial do produto)*")
            for i, d in enumerate(st.session_state.t24_concept_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t24_concept_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t24_cd_{i}", height=100,
                        label_visibility="collapsed",
                        placeholder="Explique o que torna seu produto especial, seus ingredientes, benefícios...")
                with c2:
                    if len(st.session_state.t24_concept_descs) > 1 and _del_btn(f"t24_cd_del_{i}"):
                        st.session_state.t24_concept_descs.pop(i); st.rerun()
            if _add_btn("t24_cd_add", "＋ Adicionar descrição"):
                st.session_state.t24_concept_descs.append({"valor": "Nova descrição."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. PRODUTOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🧴 Vitrine de Produtos</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagens dos produtos:</strong> tamanho ideal <strong>600 × 800 px</strong>
                (retrato). Prefira fotos com fundo escuro ou transparente para manter a atmosfera noturna
                do template. Cole a URL do <a href="https://imgur.com" target="_blank">imgur.com</a>.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Cards de produto  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t24_product_items):
                with st.expander(f"Produto {i+1}: {item['nome']}"):
                    st.session_state.t24_product_items[i]["nome"] = st.text_input(
                        "Nome do Produto", item["nome"], key=f"t24_pi_n_{i}",
                        placeholder="Ex: Calm Night Repair")
                    st.session_state.t24_product_items[i]["category"] = st.text_input(
                        "Categoria", item["category"], key=f"t24_pi_c_{i}",
                        placeholder="Ex: SHAMPOO & TRATAMENTO")
                    st.session_state.t24_product_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t24_pi_d_{i}", height=80,
                        placeholder="Descreva o tipo de cabelo indicado e o benefício principal")
                    st.session_state.t24_product_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t24_pi_i_{i}",
                        placeholder="https://i.imgur.com/... ou URL da imagem",
                        help="Foto do produto — 600×800 px, fundo escuro ideal")
                    c1, c2 = st.columns(2)
                    with c1:
                        st.session_state.t24_product_items[i]["btn_text"] = st.text_input(
                            "Texto Botão", item["btn_text"], key=f"t24_pi_bt_{i}",
                            placeholder="Ex: SAIBA MAIS")
                    with c2:
                        st.session_state.t24_product_items[i]["btn_url"] = st.text_input(
                            "URL Botão", item["btn_url"], key=f"t24_pi_bu_{i}",
                            placeholder="https://wa.me/... ou link da loja")
                    if len(st.session_state.t24_product_items) > 1:
                        if st.button("🗑 Remover este produto", key=f"t24_pi_del_{i}"):
                            st.session_state.t24_product_items.pop(i); st.rerun()
            if _add_btn("t24_pi_add", "＋ Adicionar produto"):
                st.session_state.t24_product_items.append({
                    "img": "", "nome": "NOVO PRODUTO", "category": "CATEGORIA",
                    "desc": "", "btn_text": "SAIBA MAIS", "btn_url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Nome da marca")
            for i, name in enumerate(st.session_state.t24_foot_brand_names):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t24_foot_brand_names[i]["valor"] = st.text_input(
                        "Nome", name["valor"], key=f"t24_fn_{i}", label_visibility="collapsed",
                        placeholder="Ex: YOLU ou NOME DA MARCA")
                with c2:
                    if len(st.session_state.t24_foot_brand_names) > 1 and _del_btn(f"t24_fn_del_{i}"):
                        st.session_state.t24_foot_brand_names.pop(i); st.rerun()
            if _add_btn("t24_fn_add", "＋ Adicionar nome"):
                st.session_state.t24_foot_brand_names.append({"valor": "MARCA"}); st.rerun()

            st.caption("Colunas de links  *(redes sociais e outros links)*")
            for i, col in enumerate(st.session_state.t24_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t24_foot_cols[i]["titulo"] = st.text_input(
                        "Título Coluna", col["titulo"], key=f"t24_fc_t_{i}",
                        placeholder="Ex: REDES SOCIAIS ou COMPRAR")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1:
                            st.session_state.t24_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t24_fc_l_t_{i}_{j}",
                                label_visibility="collapsed", placeholder="Texto do link")
                        with c2:
                            st.session_state.t24_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t24_fc_l_u_{i}_{j}",
                                label_visibility="collapsed", placeholder="https://instagram.com/...")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t24_fc_l_del_{i}_{j}"):
                                st.session_state.t24_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t24_fc_l_add_{i}", "＋ Adicionar link"):
                        st.session_state.t24_foot_cols[i]["links"].append({"texto": "LINK", "url": ""}); st.rerun()
                    if len(st.session_state.t24_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t24_fc_del_{i}"):
                            st.session_state.t24_foot_cols.pop(i); st.rerun()
            if _add_btn("t24_fc_add", "＋ Adicionar coluna"):
                st.session_state.t24_foot_cols.append({"titulo": "NOVA", "links": [{"texto": "Link", "url": ""}]}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t24_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t24_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t24_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 SUA MARCA. Todos os direitos reservados.")
                with c2:
                    if len(st.session_state.t24_foot_copys) > 1 and _del_btn(f"t24_fcp_del_{i}"):
                        st.session_state.t24_foot_copys.pop(i); st.rerun()
            if _add_btn("t24_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t24_foot_copys.append({"valor": "© 2026"}); st.rerun()

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
                3. Cole a URL no campo correspondente acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Hero (fundo): <strong>1600 × 900 px</strong> (paisagem, noturna/estrelada)<br>
                • Produtos: <strong>600 × 800 px</strong> (retrato, fundo escuro ideal)<br>
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
                Ex: "usar tons mais puxados para o dourado", "adicionar seção de depoimentos",
                "adicionar lista de ingredientes", "adicionar FAQ sobre os produtos"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t24_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t24_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t24_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t24_obs) > 1 and _del_btn(f"t24_obs_del_{i}"):
                        st.session_state.t24_obs.pop(i); st.rerun()
            if _add_btn("t24_obs_add", "＋ Adicionar observação"):
                st.session_state.t24_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 9. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t24_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t24_email_cliente.strip() or "@" not in st.session_state.t24_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t24_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t24_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t24_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t24_nome_cliente}'*."
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
        page_icon="🌙",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
