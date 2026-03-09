import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img20.png"
TEMPLATE_NAME      = "Template 20 — Moooi Style (Luxury Furniture & Lifestyle)"
TEMPLATE_ID        = "template_20"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t20_nome_cliente":  "",
        "t20_email_cliente": "",
        "t20_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t20_cores": [
            {"nome": "Fundo Principal (Branco)",  "valor": "#ffffff"},
            {"nome": "Texto Principal (Preto)",    "valor": "#000000"},
            {"nome": "Fundo Rodapé (Cinza Claro)", "valor": "#fafafa"},
            {"nome": "Bordas e Linhas",            "valor": "#eeeeee"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t20_nav_logos": [{"valor": "Moooi"}],
        "t20_nav_links": [
            {"texto": "Coleção",        "url": "seção Coleção de Produtos"},
            {"texto": "Estilo de Vida", "url": "seção Banner Histórias"},
            {"texto": "Histórias",      "url": "seção Banner Histórias"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t20_hero_labels":  [{"valor": "LANÇAMENTO DE COLEÇÃO"}],
        "t20_hero_titulos": [{"valor": "A Life Extraordinary"}],
        "t20_hero_btns":    [{"texto": "DESCUBRA O NOVO", "url": "https://wa.me/5511999999999"}],
        "t20_hero_imgs":    [{"valor": "https://images.unsplash.com/photo-1618221195710-dd6b41faaea6?auto=format&fit=crop&w=1600&q=80"}],

        # ── INTRODUÇÃO ──────────────────────────────────────────────────────
        "t20_intro_titulos": [{"valor": "Inspirando o Mundo desde 2001"}],
        "t20_intro_descs":   [{"valor": "A Moooi sempre foi sinônimo de um estilo de vida que é ao mesmo tempo lúdico e refinado. Nossas criações desafiam a gravidade, a luz e a imaginação, transformando espaços cotidianos em experiências extraordinárias."}],

        # ── PRODUTOS ────────────────────────────────────────────────────────
        "t20_product_items": [
            {"img": "https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=800", "nome": "Luminária Heracleum", "desc": "DESIGN POR MARCEL WANDERS", "btn_texto": "Ver Detalhes", "url": "seção de contato ao final da página", "margin_top": "0px"},
            {"img": "https://images.unsplash.com/photo-1567016432779-094069958ea5?w=800",  "nome": "Sofá Cloud",          "desc": "SENTANDO NAS NUVENS",       "btn_texto": "Ver Detalhes", "url": "seção de contato ao final da página", "margin_top": "80px"},
        ],

        # ── BANNER HISTÓRIAS ─────────────────────────────────────────────────
        "t20_story_imgs":    [{"valor": "https://images.unsplash.com/photo-1534349762230-e0cadf78f5db?w=1600"}],
        "t20_story_titulos": [{"valor": "Paredes que Contam Histórias"}],
        "t20_story_descs":   [{"valor": "Explore nossa coleção exclusiva de papéis de parede inspirados em animais extintos e mundos fantásticos."}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t20_foot_brand_names": [{"valor": "Moooi"}],
        "t20_foot_brand_descs": [{"valor": "A Life Extraordinary. Subscreva para receber inspiração semanal."}],
        "t20_foot_cols": [
            {"titulo": "PRODUTOS", "links": [{"texto": "Iluminação", "url": "seção Coleção de Produtos"}, {"texto": "Móveis", "url": "seção Coleção de Produtos"}, {"texto": "Acessórios", "url": "seção Coleção de Produtos"}, {"texto": "Tapetes", "url": "seção Coleção de Produtos"}]},
            {"titulo": "SERVIÇOS", "links": [{"texto": "Localizador de Lojas", "url": "https://wa.me/5511999999999"}, {"texto": "Atendimento", "url": "https://wa.me/5511999999999"}, {"texto": "Downloads 3D", "url": "https://wa.me/5511999999999"}]},
            {"titulo": "SOCIAL",   "links": [{"texto": "Instagram", "url": "https://instagram.com/"}, {"texto": "Pinterest", "url": "https://pinterest.com/"}, {"texto": "LinkedIn", "url": "https://linkedin.com/"}]},
        ],
        "t20_foot_copys": [{"valor": "© 2026 MOOOI B.V. TODOS OS DIREITOS RESERVADOS."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t20_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t20_nome_cliente,
            "email":     st.session_state.t20_email_cliente,
            "nome_site": st.session_state.t20_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t20_nome_site}",
        },
        "cores": st.session_state.t20_cores,
        "navbar": {
            "logos": st.session_state.t20_nav_logos,
            "links": st.session_state.t20_nav_links,
        },
        "hero": {
            "labels":  st.session_state.t20_hero_labels,
            "titulos": st.session_state.t20_hero_titulos,
            "botoes":  st.session_state.t20_hero_btns,
            "imagens": st.session_state.t20_hero_imgs,
        },
        "introducao": {
            "titulos": st.session_state.t20_intro_titulos,
            "descs":   st.session_state.t20_intro_descs,
        },
        "produtos": st.session_state.t20_product_items,
        "banner_historias": {
            "imagens": st.session_state.t20_story_imgs,
            "titulos": st.session_state.t20_story_titulos,
            "descs":   st.session_state.t20_story_descs,
        },
        "footer": {
            "brand_names": st.session_state.t20_foot_brand_names,
            "brand_descs": st.session_state.t20_foot_brand_descs,
            "colunas":     st.session_state.t20_foot_cols,
            "copyright":   st.session_state.t20_foot_copys,
        },
        "observacoes": st.session_state.t20_obs,
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
        @import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500&family=Inter:wght@300;400;600&display=swap');
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

            st.session_state.t20_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t20_nome_cliente,
                key="t20_nome_cliente_inp", placeholder="Ex: Fernanda Lima",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t20_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t20_email_cliente,
                key="t20_email_cliente_inp", placeholder="Ex: fernanda@loja.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: moooi, casalelite, decorluxo).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t20_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t20_nome_site,
                key="t20_nome_site_inp",
                placeholder="Ex: moooi  →  sttacksite.streamlit.app/?c=moooi",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t20_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t20_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t20_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t20_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t20_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t20_cores) > 1 and _del_btn(f"t20_cor_del_{i}"):
                        st.session_state.t20_cores.pop(i); st.rerun()
            if _add_btn("t20_cor_add", "＋ Adicionar cor"):
                st.session_state.t20_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca  *(centro)*")
            for i, item in enumerate(st.session_state.t20_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_nav_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t20_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: NomeDaMarca")
                with c2:
                    if len(st.session_state.t20_nav_logos) > 1 and _del_btn(f"t20_logo_del_{i}"):
                        st.session_state.t20_nav_logos.pop(i); st.rerun()
            if _add_btn("t20_logo_add", "＋ Adicionar logo"):
                st.session_state.t20_nav_logos.append({"valor": "Marca"}); st.rerun()

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t20_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t20_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t20_nl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t20_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t20_nl_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t20_nav_links) > 1 and _del_btn(f"t20_nl_del_{i}"):
                        st.session_state.t20_nav_links.pop(i); st.rerun()
            if _add_btn("t20_nl_add", "＋ Adicionar link"):
                st.session_state.t20_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">✨ Hero Section</div>', unsafe_allow_html=True)

            st.caption("Label superior  *(texto pequeno acima do título)*")
            for i, l in enumerate(st.session_state.t20_hero_labels):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_hero_labels[i]["valor"] = st.text_input(
                        "Label", l["valor"], key=f"t20_h_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: NOVA COLEÇÃO 2026")
                with c2:
                    if len(st.session_state.t20_hero_labels) > 1 and _del_btn(f"t20_h_l_del_{i}"):
                        st.session_state.t20_hero_labels.pop(i); st.rerun()
            if _add_btn("t20_h_l_add", "＋ Adicionar label"):
                st.session_state.t20_hero_labels.append({"valor": "Novo Label"}); st.rerun()

            st.caption("Título principal  *(tipografia elegante em destaque)*")
            for i, t in enumerate(st.session_state.t20_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_hero_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t20_h_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Uma Vida Extraordinária")
                with c2:
                    if len(st.session_state.t20_hero_titulos) > 1 and _del_btn(f"t20_h_t_del_{i}"):
                        st.session_state.t20_hero_titulos.pop(i); st.rerun()
            if _add_btn("t20_h_t_add", "＋ Adicionar título"):
                st.session_state.t20_hero_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagem de fundo do Hero:</strong> cole a URL do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanho ideal: <strong>1920 × 800 px</strong>. Prefira fotos de ambientes decorados ou produtos isolados.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Imagem de fundo  *(URL)*")
            for i, img in enumerate(st.session_state.t20_hero_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_hero_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t20_h_i_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... ou URL da imagem")
                with c2:
                    if len(st.session_state.t20_hero_imgs) > 1 and _del_btn(f"t20_h_i_del_{i}"):
                        st.session_state.t20_hero_imgs.pop(i); st.rerun()
            if _add_btn("t20_h_i_add", "＋ Adicionar imagem"):
                st.session_state.t20_hero_imgs.append({"valor": ""}); st.rerun()

            st.caption("Botão  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t20_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t20_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t20_hb_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: DESCUBRA A COLEÇÃO")
                with c2:
                    st.session_state.t20_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t20_hb_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t20_hero_btns) > 1 and _del_btn(f"t20_hb_del_{i}"):
                        st.session_state.t20_hero_btns.pop(i); st.rerun()
            if _add_btn("t20_hb_add", "＋ Adicionar botão"):
                st.session_state.t20_hero_btns.append({"texto": "DESCUBRA", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. INTRODUÇÃO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📖 Introdução da Marca</div>', unsafe_allow_html=True)

            st.caption("Título")
            for i, t in enumerate(st.session_state.t20_intro_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_intro_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t20_it_{i}", label_visibility="collapsed",
                        placeholder="Ex: Inspirando o Mundo desde 2001")
                with c2:
                    if len(st.session_state.t20_intro_titulos) > 1 and _del_btn(f"t20_it_del_{i}"):
                        st.session_state.t20_intro_titulos.pop(i); st.rerun()
            if _add_btn("t20_it_add", "＋ Adicionar título"):
                st.session_state.t20_intro_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição da marca  *(parágrafo de apresentação)*")
            for i, d in enumerate(st.session_state.t20_intro_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_intro_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t20_id_{i}", height=100,
                        label_visibility="collapsed",
                        placeholder="Conte a história e filosofia da sua marca em 2 a 3 frases")
                with c2:
                    if len(st.session_state.t20_intro_descs) > 1 and _del_btn(f"t20_id_del_{i}"):
                        st.session_state.t20_intro_descs.pop(i); st.rerun()
            if _add_btn("t20_id_add", "＋ Adicionar descrição"):
                st.session_state.t20_intro_descs.append({"valor": "Nova descrição."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. PRODUTOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🪑 Coleção de Produtos</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagens dos produtos:</strong> cole a URL do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanho recomendado: <strong>800 × 1000 px</strong> (retrato) para melhor visual editorial.<br><br>
                📐 <strong>Margem Superior:</strong> use valores como <code>0px</code>, <code>40px</code>, <code>80px</code>
                para criar o efeito de produtos em alturas diferentes (layout editorial).
            </div>
            """, unsafe_allow_html=True)

            st.caption("Cards de produto  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t20_product_items):
                with st.expander(f"Produto {i+1}: {item['nome']}"):
                    st.session_state.t20_product_items[i]["nome"] = st.text_input(
                        "Nome do Produto", item["nome"], key=f"t20_pi_n_{i}",
                        placeholder="Ex: Luminária Heracleum")
                    st.session_state.t20_product_items[i]["desc"] = st.text_input(
                        "Designer / Descrição curta", item["desc"], key=f"t20_pi_d_{i}",
                        placeholder="Ex: DESIGN POR FULANO ou EDIÇÃO LIMITADA")
                    st.session_state.t20_product_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t20_pi_i_{i}",
                        placeholder="https://i.imgur.com/... ou URL da imagem",
                        help="Cole a URL da imagem do imgur.com")
                    st.session_state.t20_product_items[i]["btn_texto"] = st.text_input(
                        "Texto do Botão", item["btn_texto"], key=f"t20_pi_bt_{i}",
                        placeholder="Ex: Ver Detalhes, Comprar, Saiba Mais")
                    st.session_state.t20_product_items[i]["url"] = st.text_input(
                        "URL do Link", item["url"], key=f"t20_pi_u_{i}",
                        placeholder="https:// ou seção de destino")
                    st.session_state.t20_product_items[i]["margin_top"] = st.text_input(
                        "Margem Superior  *(cria offset visual — ex: 0px, 80px)*",
                        item["margin_top"], key=f"t20_pi_m_{i}",
                        placeholder="Ex: 0px ou 80px")
                    if len(st.session_state.t20_product_items) > 1:
                        if st.button("🗑 Remover este produto", key=f"t20_pi_del_{i}"):
                            st.session_state.t20_product_items.pop(i); st.rerun()
            if _add_btn("t20_pi_add", "＋ Adicionar produto"):
                st.session_state.t20_product_items.append({
                    "img": "", "nome": "Novo Produto", "desc": "DESIGNER",
                    "btn_texto": "Ver Detalhes", "url": "", "margin_top": "0px"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. BANNER HISTÓRIAS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Banner Histórias</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagem do Banner:</strong> tamanho ideal <strong>1600 × 700 px</strong>.
                Prefira fotos de ambientes, texturas ou cenas de estilo de vida.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Imagem do banner  *(URL)*")
            for i, img in enumerate(st.session_state.t20_story_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_story_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t20_si_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... ou URL da imagem")
                with c2:
                    if len(st.session_state.t20_story_imgs) > 1 and _del_btn(f"t20_si_del_{i}"):
                        st.session_state.t20_story_imgs.pop(i); st.rerun()
            if _add_btn("t20_si_add", "＋ Adicionar imagem"):
                st.session_state.t20_story_imgs.append({"valor": ""}); st.rerun()

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t20_story_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_story_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t20_st_{i}", label_visibility="collapsed",
                        placeholder="Ex: Espaços que Contam Histórias")
                with c2:
                    if len(st.session_state.t20_story_titulos) > 1 and _del_btn(f"t20_st_del_{i}"):
                        st.session_state.t20_story_titulos.pop(i); st.rerun()
            if _add_btn("t20_st_add", "＋ Adicionar título"):
                st.session_state.t20_story_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t20_story_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_story_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t20_sd_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Descrição curta do que essa seção apresenta")
                with c2:
                    if len(st.session_state.t20_story_descs) > 1 and _del_btn(f"t20_sd_del_{i}"):
                        st.session_state.t20_story_descs.pop(i); st.rerun()
            if _add_btn("t20_sd_add", "＋ Adicionar descrição"):
                st.session_state.t20_story_descs.append({"valor": "Nova descrição."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé Completo</div>', unsafe_allow_html=True)

            st.caption("Nome da marca  *(tipografia serif em destaque)*")
            for i, name in enumerate(st.session_state.t20_foot_brand_names):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_foot_brand_names[i]["valor"] = st.text_input(
                        "Nome", name["valor"], key=f"t20_fn_{i}", label_visibility="collapsed",
                        placeholder="Ex: NomeDaMarca")
                with c2:
                    if len(st.session_state.t20_foot_brand_names) > 1 and _del_btn(f"t20_fn_del_{i}"):
                        st.session_state.t20_foot_brand_names.pop(i); st.rerun()
            if _add_btn("t20_fn_add", "＋ Adicionar nome"):
                st.session_state.t20_foot_brand_names.append({"valor": "Marca"}); st.rerun()

            st.caption("Descrição da marca  *(texto abaixo do logo)*")
            for i, desc in enumerate(st.session_state.t20_foot_brand_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_foot_brand_descs[i]["valor"] = st.text_area(
                        "Descrição", desc["valor"], key=f"t20_fd_{i}", height=70,
                        label_visibility="collapsed",
                        placeholder="Slogan ou breve descrição da marca para o rodapé")
                with c2:
                    if len(st.session_state.t20_foot_brand_descs) > 1 and _del_btn(f"t20_fd_del_{i}"):
                        st.session_state.t20_foot_brand_descs.pop(i); st.rerun()
            if _add_btn("t20_fd_add", "＋ Adicionar descrição"):
                st.session_state.t20_foot_brand_descs.append({"valor": "Nova descrição."}); st.rerun()

            st.caption("Colunas de links  *(clique para expandir e editar cada uma)*")
            for i, col in enumerate(st.session_state.t20_foot_cols):
                with st.expander(f"Coluna {i+1}: {col['titulo']}"):
                    st.session_state.t20_foot_cols[i]["titulo"] = st.text_input(
                        "Título Coluna", col["titulo"], key=f"t20_fc_t_{i}",
                        placeholder="Ex: PRODUTOS, SERVIÇOS, SOCIAL")
                    for j, link in enumerate(col["links"]):
                        c1, c2, c3 = st.columns([4, 4, 1])
                        with c1:
                            st.session_state.t20_foot_cols[i]["links"][j]["texto"] = st.text_input(
                                "Texto", link["texto"], key=f"t20_fc_l_t_{i}_{j}",
                                label_visibility="collapsed", placeholder="Texto do link")
                        with c2:
                            st.session_state.t20_foot_cols[i]["links"][j]["url"] = st.text_input(
                                "URL", link["url"], key=f"t20_fc_l_u_{i}_{j}",
                                label_visibility="collapsed", placeholder="https:// ou seção")
                        with c3:
                            if len(col["links"]) > 1 and _del_btn(f"t20_fc_l_del_{i}_{j}"):
                                st.session_state.t20_foot_cols[i]["links"].pop(j); st.rerun()
                    if _add_btn(f"t20_fc_l_add_{i}", "＋ Adicionar link"):
                        st.session_state.t20_foot_cols[i]["links"].append({"texto": "LINK", "url": ""}); st.rerun()
                    if len(st.session_state.t20_foot_cols) > 1:
                        if st.button("🗑 Remover esta coluna", key=f"t20_fc_del_{i}"):
                            st.session_state.t20_foot_cols.pop(i); st.rerun()
            if _add_btn("t20_fc_add", "＋ Adicionar coluna"):
                st.session_state.t20_foot_cols.append({"titulo": "NOVA", "links": [{"texto": "Link", "url": ""}]}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t20_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t20_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 EMPRESA. TODOS OS DIREITOS RESERVADOS.")
                with c2:
                    if len(st.session_state.t20_foot_copys) > 1 and _del_btn(f"t20_fcp_del_{i}"):
                        st.session_state.t20_foot_copys.pop(i); st.rerun()
            if _add_btn("t20_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t20_foot_copys.append({"valor": "© 2026"}); st.rerun()

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
                3. Cole a URL no campo correspondente acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Hero de fundo: <strong>1920 × 800 px</strong><br>
                • Produtos (retrato): <strong>800 × 1000 px</strong><br>
                • Banner Histórias: <strong>1600 × 700 px</strong><br>
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
                Ex: "adicionar seção de depoimentos", "adicionar seção de newsletter",
                "remover seção Banner", "adicionar mais produtos", "mudar fonte para algo mais clássico"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t20_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t20_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t20_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t20_obs) > 1 and _del_btn(f"t20_obs_del_{i}"):
                        st.session_state.t20_obs.pop(i); st.rerun()
            if _add_btn("t20_obs_add", "＋ Adicionar observação"):
                st.session_state.t20_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 10. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t20_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t20_email_cliente.strip() or "@" not in st.session_state.t20_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t20_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t20_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t20_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t20_nome_cliente}'*."
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
        page_icon="✨",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
