import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/editor/main/img27.png"
TEMPLATE_NAME      = "Template 27 — LittleTracks Style (Kids & Family App)"
TEMPLATE_ID        = "template_27"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t27_nome_cliente":  "",
        "t27_email_cliente": "",
        "t27_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t27_cores": [
            {"nome": "Roxo Principal",  "valor": "#9d8df1"},
            {"nome": "Azul Suave",      "valor": "#a0d2eb"},
            {"nome": "Rosa",            "valor": "#ffafcc"},
            {"nome": "Amarelo",         "valor": "#ffee93"},
            {"nome": "Fundo Principal", "valor": "#fdfcf0"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t27_nav_logos": [{"valor": "🐾 littletracks"}],
        "t27_nav_links": [
            {"texto": "O App",           "url": "seção Hero"},
            {"texto": "Funcionalidades", "url": "seção Funcionalidades"},
            {"texto": "Preços",          "url": "seção Planos de Preço"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t27_hero_titulos": [{"valor": "Guardar memórias nunca foi tão doce."}],
        "t27_hero_descs":   [{"valor": "O diário digital inteligente que organiza os momentos mais preciosos dos seus filhos, para que você possa focar no que realmente importa: viver cada um deles."}],
        "t27_hero_btns":    [{"texto": "Criar Minha Conta Grátis", "url": "https://wa.me/5511999999999"}],

        # ── FUNCIONALIDADES ──────────────────────────────────────────────────
        "t27_func_titulos": [{"valor": "Tudo o que você precisa"}],
        "t27_func_items": [
            {"emoji": "📸", "title": "Organização Mágica",  "desc": "Fotos e vídeos são organizados automaticamente por data e fase do crescimento."},
            {"emoji": "👨‍👩‍👧‍👦", "title": "Círculo da Família", "desc": "Compartilhe momentos com avós e tios em um ambiente privado e seguro."},
            {"emoji": "🎨", "title": "Livros de Memórias",  "desc": "Transforme seu diário digital em um álbum físico impresso com apenas um clique."},
        ],

        # ── TIMELINE ────────────────────────────────────────────────────────
        "t27_time_titulos": [{"valor": "Uma linha do tempo da vida deles"}],
        "t27_time_imgs":    [{"valor": "https://images.unsplash.com/photo-1519681393784-d120267933ba?w=800"}],
        "t27_time_items": [
            {"label": "Hoje - 2 Anos e 3 Meses", "desc": "O primeiro dia na escolinha! Nenhuma lágrima (pelo menos não do Leo).", "cor": "#9d8df1"},
            {"label": "Há 6 meses",               "desc": "Primeiros passos no jardim. A aventura começou!",                      "cor": "#666666"},
            {"label": "O Nascimento",             "desc": "O começo da trilha mais linda de nossas vidas.",                       "cor": "#666666"},
        ],

        # ── DEPOIMENTOS ─────────────────────────────────────────────────────
        "t27_depo_titulos": [{"valor": "Amado por mais de 50.000 famílias"}],
        "t27_depo_items": [
            {"texto": "O littletracks mudou a forma como guardo as fotos da minha filha. É tão fácil de usar e as sugestões de marcos são incríveis!", "autor": "Mariana S., Mãe da Alice"},
            {"texto": "Finalmente um lugar seguro para compartilhar fotos com a família sem precisar das redes sociais abertas.",                       "autor": "Ricardo T., Pai do Bento"},
        ],

        # ── PREÇOS ──────────────────────────────────────────────────────────
        "t27_price_titulos": [{"valor": "Escolha o seu plano"}],
        "t27_price_descs":   [{"valor": "Sem taxas escondidas. Cancele quando quiser."}],
        "t27_price_plans": [
            {"nome": "Básico",  "preco": "Grátis", "periodo": "",     "desc": "Para começar a trilha",          "popular": False, "badge": "",            "features": ["Até 500 fotos", "1 Perfil de criança", "Álbum digital básico"],                                 "btn_texto": "Escolher Básico",  "btn_url": "https://wa.me/5511999999999"},
            {"nome": "Premium", "preco": "R$ 19",  "periodo": "/mês", "desc": "Para memórias infinitas",        "popular": True,  "badge": "MAIS POPULAR", "features": ["Armazenamento Ilimitado", "Vídeos em 4K", "Compartilhamento ilimitado", "Backup automático"], "btn_texto": "Assinar Premium",  "btn_url": "https://wa.me/5511999999999"},
            {"nome": "Família", "preco": "R$ 35",  "periodo": "/mês", "desc": "Para toda a árvore genealógica", "popular": False, "badge": "",            "features": ["Tudo do Premium", "Até 5 perfis de crianças", "Acesso de Admin para 4 pessoas"],              "btn_texto": "Escolher Família", "btn_url": "https://wa.me/5511999999999"},
        ],

        # ── FAQ ─────────────────────────────────────────────────────────────
        "t27_faq_titulos": [{"valor": "Dúvidas Frequentes"}],
        "t27_faq_items": [
            {"pergunta": "Meus dados estão seguros?",           "resposta": "Sim! Utilizamos criptografia de nível bancário e seus dados nunca são vendidos para terceiros."},
            {"pergunta": "Posso imprimir os álbuns no Brasil?", "resposta": "Sim, temos parceiros de impressão locais que entregam em todo o território nacional com acabamento premium."},
            {"pergunta": "Como convido os avós?",               "resposta": "Basta enviar um link mágico pelo WhatsApp ou e-mail. Eles não precisam criar senhas complicadas."},
        ],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t27_foot_logos": [{"valor": "🐾 littletracks"}],
        "t27_foot_links": [
            {"texto": "Instagram",     "url": "https://instagram.com/"},
            {"texto": "Facebook",      "url": "https://facebook.com/"},
            {"texto": "Blog",          "url": "https://wa.me/5511999999999"},
            {"texto": "Termos de Uso", "url": "https://wa.me/5511999999999"},
        ],
        "t27_foot_copys": [{"valor": "© 2026 littletracks. Criado com carinho para as futuras gerações."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t27_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t27_nome_cliente,
            "email":     st.session_state.t27_email_cliente,
            "nome_site": st.session_state.t27_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t27_nome_site}",
        },
        "cores": st.session_state.t27_cores,
        "navbar": {
            "logos": st.session_state.t27_nav_logos,
            "links": st.session_state.t27_nav_links,
        },
        "hero": {
            "titulos": st.session_state.t27_hero_titulos,
            "descs":   st.session_state.t27_hero_descs,
            "botoes":  st.session_state.t27_hero_btns,
        },
        "funcionalidades": {
            "titulos": st.session_state.t27_func_titulos,
            "items":   st.session_state.t27_func_items,
        },
        "timeline": {
            "titulos": st.session_state.t27_time_titulos,
            "imagens": st.session_state.t27_time_imgs,
            "eventos": st.session_state.t27_time_items,
        },
        "depoimentos": {
            "titulos": st.session_state.t27_depo_titulos,
            "items":   st.session_state.t27_depo_items,
        },
        "precos": {
            "titulos": st.session_state.t27_price_titulos,
            "descs":   st.session_state.t27_price_descs,
            "planos":  st.session_state.t27_price_plans,
        },
        "faq": {
            "titulos": st.session_state.t27_faq_titulos,
            "items":   st.session_state.t27_faq_items,
        },
        "footer": {
            "logos":     st.session_state.t27_foot_logos,
            "links":     st.session_state.t27_foot_links,
            "copyright": st.session_state.t27_foot_copys,
        },
        "observacoes": st.session_state.t27_obs,
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

            st.session_state.t27_nome_cliente = st.text_input(
                "Seu nome completo", value=st.session_state.t27_nome_cliente,
                key="t27_nome_cliente_inp", placeholder="Ex: Ana Paula Souza",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t27_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t27_email_cliente,
                key="t27_email_cliente_inp", placeholder="Ex: ana@meuapp.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: littletracks, memoriasdoleo, familiasilva).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t27_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t27_nome_site,
                key="t27_nome_site_inp",
                placeholder="Ex: littletracks  →  sttacksite.streamlit.app/?c=littletracks",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🎨 <strong>Paleta colorida:</strong> este template usa várias cores pastel para criar
                um visual alegre e acolhedor. Você pode ajustar cada cor mantendo o estilo suave,
                ou mudar completamente para a identidade da sua marca!
            </div>
            """, unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t27_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t27_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t27_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t27_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t27_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t27_cores) > 1 and _del_btn(f"t27_cor_del_{i}"):
                        st.session_state.t27_cores.pop(i); st.rerun()
            if _add_btn("t27_cor_add", "＋ Adicionar cor"):
                st.session_state.t27_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca  *(você pode incluir emoji — ex: 🐾 nome)*")
            for i, item in enumerate(st.session_state.t27_nav_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_nav_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t27_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: 🐾 nome do app ou NOME DA MARCA",
                        help="Você pode usar emojis no nome! Ex: 🌟 MeuApp")
                with c2:
                    if len(st.session_state.t27_nav_logos) > 1 and _del_btn(f"t27_logo_del_{i}"):
                        st.session_state.t27_nav_logos.pop(i); st.rerun()
            if _add_btn("t27_logo_add", "＋ Adicionar logo"):
                st.session_state.t27_nav_logos.append({"valor": "🐾 marca"}); st.rerun()

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t27_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t27_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t27_nl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t27_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t27_nl_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t27_nav_links) > 1 and _del_btn(f"t27_nl_del_{i}"):
                        st.session_state.t27_nav_links.pop(i); st.rerun()
            if _add_btn("t27_nl_add", "＋ Adicionar link"):
                st.session_state.t27_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🐾 Hero Section</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                💡 <strong>Título principal:</strong> escreva o texto normalmente.
                Se quiser que parte do título apareça em outra cor (destaque), descreva isso na seção
                Observações — ex: "quero a segunda linha em roxo". Nossa equipe aplica para você!
            </div>
            """, unsafe_allow_html=True)

            st.caption("Título principal  *(frase que resume o propósito do app)*")
            for i, t in enumerate(st.session_state.t27_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t27_h_t_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Ex: Guardar memórias nunca foi tão doce.")
                with c2:
                    if len(st.session_state.t27_hero_titulos) > 1 and _del_btn(f"t27_h_t_del_{i}"):
                        st.session_state.t27_hero_titulos.pop(i); st.rerun()
            if _add_btn("t27_h_t_add", "＋ Adicionar título"):
                st.session_state.t27_hero_titulos.append({"valor": "Novo título."}); st.rerun()

            st.caption("Descrição  *(2-3 frases explicando o produto)*")
            for i, d in enumerate(st.session_state.t27_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t27_h_d_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Descreva o app em 2-3 frases: o que ele faz, para quem é e qual o benefício.")
                with c2:
                    if len(st.session_state.t27_hero_descs) > 1 and _del_btn(f"t27_h_d_del_{i}"):
                        st.session_state.t27_hero_descs.pop(i); st.rerun()
            if _add_btn("t27_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t27_hero_descs.append({"valor": "Nova descrição."}); st.rerun()

            st.caption("Botão CTA  *(Texto | URL ou WhatsApp)*")
            for i, btn in enumerate(st.session_state.t27_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t27_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t27_hb_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Criar Minha Conta Grátis")
                with c2:
                    st.session_state.t27_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t27_hb_u_{i}", label_visibility="collapsed",
                        placeholder="https://wa.me/... ou link de cadastro")
                with c3:
                    if len(st.session_state.t27_hero_btns) > 1 and _del_btn(f"t27_hb_del_{i}"):
                        st.session_state.t27_hero_btns.pop(i); st.rerun()
            if _add_btn("t27_hb_add", "＋ Adicionar botão"):
                st.session_state.t27_hero_btns.append({"texto": "COMEÇAR", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. FUNCIONALIDADES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">✨ Funcionalidades</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t27_func_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_func_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t27_ft_{i}", label_visibility="collapsed",
                        placeholder="Ex: Tudo o que você precisa")
                with c2:
                    if len(st.session_state.t27_func_titulos) > 1 and _del_btn(f"t27_ft_del_{i}"):
                        st.session_state.t27_func_titulos.pop(i); st.rerun()
            if _add_btn("t27_ft_add", "＋ Adicionar título"):
                st.session_state.t27_func_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Cards  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t27_func_items):
                with st.expander(f"Funcionalidade {i+1}: {item['title']}"):
                    st.session_state.t27_func_items[i]["emoji"] = st.text_input(
                        "Emoji", item["emoji"], key=f"t27_fi_e_{i}",
                        placeholder="Cole um emoji aqui — ex: 📸 🎨 ⭐",
                        help="Um único emoji que representa esta funcionalidade.")
                    st.session_state.t27_func_items[i]["title"] = st.text_input(
                        "Título", item["title"], key=f"t27_fi_t_{i}",
                        placeholder="Ex: Organização Mágica")
                    st.session_state.t27_func_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t27_fi_d_{i}", height=70,
                        placeholder="Descreva esta funcionalidade em 1-2 frases.")
                    if len(st.session_state.t27_func_items) > 1:
                        if st.button("🗑 Remover esta funcionalidade", key=f"t27_fi_del_{i}"):
                            st.session_state.t27_func_items.pop(i); st.rerun()
            if _add_btn("t27_fi_add", "＋ Adicionar funcionalidade"):
                st.session_state.t27_func_items.append({"emoji": "⭐", "title": "Nova Funcionalidade", "desc": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. TIMELINE
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📅 Linha do Tempo</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t27_time_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_time_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t27_tt_{i}", label_visibility="collapsed",
                        placeholder="Ex: Uma linha do tempo da vida deles")
                with c2:
                    if len(st.session_state.t27_time_titulos) > 1 and _del_btn(f"t27_tt_del_{i}"):
                        st.session_state.t27_time_titulos.pop(i); st.rerun()
            if _add_btn("t27_tt_add", "＋ Adicionar título"):
                st.session_state.t27_time_titulos.append({"valor": "Nova linha do tempo"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagem lateral da timeline:</strong> tamanho ideal <strong>600 × 800 px</strong>
                (retrato). Cole a URL do <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Use uma foto de criança, família ou momento especial.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Imagem lateral  *(URL)*")
            for i, img in enumerate(st.session_state.t27_time_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_time_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t27_ti_img_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... ou URL da imagem")
                with c2:
                    if len(st.session_state.t27_time_imgs) > 1 and _del_btn(f"t27_ti_img_del_{i}"):
                        st.session_state.t27_time_imgs.pop(i); st.rerun()
            if _add_btn("t27_ti_img_add", "＋ Adicionar imagem"):
                st.session_state.t27_time_imgs.append({"valor": ""}); st.rerun()

            st.caption("Eventos da timeline  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t27_time_items):
                with st.expander(f"Evento {i+1}: {item['label']}"):
                    st.session_state.t27_time_items[i]["label"] = st.text_input(
                        "Data/Título", item["label"], key=f"t27_ti_l_{i}",
                        placeholder="Ex: Hoje - 2 Anos e 3 Meses")
                    st.session_state.t27_time_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t27_ti_d_{i}", height=70,
                        placeholder="Descreva este momento especial com carinho...")
                    st.session_state.t27_time_items[i]["cor"] = st.color_picker(
                        "Cor do Círculo", item["cor"], key=f"t27_ti_c_{i}")
                    if len(st.session_state.t27_time_items) > 1:
                        if st.button("🗑 Remover este evento", key=f"t27_ti_del_{i}"):
                            st.session_state.t27_time_items.pop(i); st.rerun()
            if _add_btn("t27_ti_add", "＋ Adicionar evento"):
                st.session_state.t27_time_items.append({"label": "Novo Evento", "desc": "", "cor": "#9d8df1"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. DEPOIMENTOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💬 Depoimentos</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t27_depo_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_depo_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t27_dt_{i}", label_visibility="collapsed",
                        placeholder="Ex: Amado por mais de 50.000 famílias")
                with c2:
                    if len(st.session_state.t27_depo_titulos) > 1 and _del_btn(f"t27_dt_del_{i}"):
                        st.session_state.t27_depo_titulos.pop(i); st.rerun()
            if _add_btn("t27_dt_add", "＋ Adicionar título"):
                st.session_state.t27_depo_titulos.append({"valor": "Amado por milhares"}); st.rerun()

            st.caption("Cards de depoimento  *(sem aspas — escreva o texto normalmente)*")
            for i, item in enumerate(st.session_state.t27_depo_items):
                with st.expander(f"Depoimento {i+1}"):
                    st.session_state.t27_depo_items[i]["texto"] = st.text_area(
                        "Texto", item["texto"], key=f"t27_di_t_{i}", height=90,
                        placeholder="Escreva o depoimento aqui, sem aspas.")
                    st.session_state.t27_depo_items[i]["autor"] = st.text_input(
                        "Autor", item["autor"], key=f"t27_di_a_{i}",
                        placeholder="Ex: Mariana S., Mãe da Alice")
                    if len(st.session_state.t27_depo_items) > 1:
                        if st.button("🗑 Remover este depoimento", key=f"t27_di_del_{i}"):
                            st.session_state.t27_depo_items.pop(i); st.rerun()
            if _add_btn("t27_di_add", "＋ Adicionar depoimento"):
                st.session_state.t27_depo_items.append({"texto": "", "autor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. PREÇOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💰 Planos de Preço</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t27_price_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_price_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t27_pt_{i}", label_visibility="collapsed",
                        placeholder="Ex: Escolha o seu plano")
                with c2:
                    if len(st.session_state.t27_price_titulos) > 1 and _del_btn(f"t27_pt_del_{i}"):
                        st.session_state.t27_price_titulos.pop(i); st.rerun()
            if _add_btn("t27_pt_add", "＋ Adicionar título"):
                st.session_state.t27_price_titulos.append({"valor": "Nossos Planos"}); st.rerun()

            st.caption("Subtítulo")
            for i, d in enumerate(st.session_state.t27_price_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_price_descs[i]["valor"] = st.text_input(
                        "Subtítulo", d["valor"], key=f"t27_pd_{i}", label_visibility="collapsed",
                        placeholder="Ex: Sem taxas escondidas. Cancele quando quiser.")
                with c2:
                    if len(st.session_state.t27_price_descs) > 1 and _del_btn(f"t27_pd_del_{i}"):
                        st.session_state.t27_price_descs.pop(i); st.rerun()
            if _add_btn("t27_pd_add", "＋ Adicionar subtítulo"):
                st.session_state.t27_price_descs.append({"valor": "Sem surpresas."}); st.rerun()

            st.caption("Planos  *(clique para expandir e editar cada um)*")
            for i, plan in enumerate(st.session_state.t27_price_plans):
                with st.expander(f"Plano {i+1}: {plan['nome']}"):
                    st.session_state.t27_price_plans[i]["nome"] = st.text_input(
                        "Nome", plan["nome"], key=f"t27_pp_n_{i}", placeholder="Ex: Básico, Premium, Família")
                    c1, c2 = st.columns(2)
                    with c1:
                        st.session_state.t27_price_plans[i]["preco"] = st.text_input(
                            "Preço", plan["preco"], key=f"t27_pp_p_{i}", placeholder="Ex: R$ 19 ou Grátis")
                    with c2:
                        st.session_state.t27_price_plans[i]["periodo"] = st.text_input(
                            "Período", plan["periodo"], key=f"t27_pp_per_{i}", placeholder="Ex: /mês ou vazio")
                    st.session_state.t27_price_plans[i]["desc"] = st.text_input(
                        "Descrição", plan["desc"], key=f"t27_pp_d_{i}",
                        placeholder="Ex: Para começar a trilha")
                    st.session_state.t27_price_plans[i]["popular"] = st.checkbox(
                        "Destaque (Popular)", plan["popular"], key=f"t27_pp_pop_{i}",
                        help="Marque para destacar este plano com bordas coloridas e badge.")
                    st.session_state.t27_price_plans[i]["badge"] = st.text_input(
                        "Texto do Badge", plan["badge"], key=f"t27_pp_b_{i}",
                        placeholder="Ex: MAIS POPULAR (deixe vazio para não exibir)")
                    st.caption("Vantagens  *(uma por linha)*")
                    feats_text = "\n".join(plan["features"])
                    new_feats = st.text_area(
                        "Vantagens", feats_text, key=f"t27_pp_f_{i}", height=90,
                        label_visibility="collapsed",
                        placeholder="Armazenamento Ilimitado\nVídeos em 4K\nBackup automático").split("\n")
                    st.session_state.t27_price_plans[i]["features"] = [f.strip() for f in new_feats if f.strip()]
                    c1, c2 = st.columns(2)
                    with c1:
                        st.session_state.t27_price_plans[i]["btn_texto"] = st.text_input(
                            "Texto Botão", plan["btn_texto"], key=f"t27_pp_bt_{i}",
                            placeholder="Ex: Assinar Premium")
                    with c2:
                        st.session_state.t27_price_plans[i]["btn_url"] = st.text_input(
                            "URL Botão", plan["btn_url"], key=f"t27_pp_bu_{i}",
                            placeholder="https://wa.me/... ou link de checkout")
                    if len(st.session_state.t27_price_plans) > 1:
                        if st.button("🗑 Remover este plano", key=f"t27_pp_del_{i}"):
                            st.session_state.t27_price_plans.pop(i); st.rerun()
            if _add_btn("t27_pp_add", "＋ Adicionar plano"):
                st.session_state.t27_price_plans.append({
                    "nome": "NOVO", "preco": "R$ 0", "periodo": "/mês", "desc": "",
                    "popular": False, "badge": "", "features": ["Vantagem 1"],
                    "btn_texto": "ASSINAR", "btn_url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. FAQ
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">❓ FAQ — Perguntas Frequentes</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t27_faq_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_faq_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t27_faqt_{i}", label_visibility="collapsed",
                        placeholder="Ex: Dúvidas Frequentes")
                with c2:
                    if len(st.session_state.t27_faq_titulos) > 1 and _del_btn(f"t27_faqt_del_{i}"):
                        st.session_state.t27_faq_titulos.pop(i); st.rerun()
            if _add_btn("t27_faqt_add", "＋ Adicionar título"):
                st.session_state.t27_faq_titulos.append({"valor": "Dúvidas"}); st.rerun()

            st.caption("Perguntas e respostas")
            for i, item in enumerate(st.session_state.t27_faq_items):
                with st.expander(f"Pergunta {i+1}: {item['pergunta'][:40]}..."):
                    st.session_state.t27_faq_items[i]["pergunta"] = st.text_input(
                        "Pergunta", item["pergunta"], key=f"t27_faqi_p_{i}",
                        placeholder="Ex: Meus dados estão seguros?")
                    st.session_state.t27_faq_items[i]["resposta"] = st.text_area(
                        "Resposta", item["resposta"], key=f"t27_faqi_r_{i}", height=80,
                        placeholder="Escreva a resposta de forma clara e tranquilizadora...")
                    if len(st.session_state.t27_faq_items) > 1:
                        if st.button("🗑 Remover esta pergunta", key=f"t27_faqi_del_{i}"):
                            st.session_state.t27_faq_items.pop(i); st.rerun()
            if _add_btn("t27_faqi_add", "＋ Adicionar pergunta"):
                st.session_state.t27_faq_items.append({"pergunta": "", "resposta": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 9. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Logo do rodapé  *(pode usar emoji)*")
            for i, item in enumerate(st.session_state.t27_foot_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_foot_logos[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t27_fl_{i}", label_visibility="collapsed",
                        placeholder="Ex: 🐾 littletracks")
                with c2:
                    if len(st.session_state.t27_foot_logos) > 1 and _del_btn(f"t27_fl_del_{i}"):
                        st.session_state.t27_foot_logos.pop(i); st.rerun()
            if _add_btn("t27_fl_add", "＋ Adicionar logo"):
                st.session_state.t27_foot_logos.append({"valor": "🐾 marca"}); st.rerun()

            st.caption("Links do rodapé  *(Texto | URL)*")
            for i, link in enumerate(st.session_state.t27_foot_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t27_foot_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t27_footl_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Instagram")
                with c2:
                    st.session_state.t27_foot_links[i]["url"] = st.text_input(
                        "URL", link["url"], key=f"t27_footl_u_{i}", label_visibility="collapsed",
                        placeholder="https://instagram.com/...")
                with c3:
                    if len(st.session_state.t27_foot_links) > 1 and _del_btn(f"t27_footl_del_{i}"):
                        st.session_state.t27_foot_links.pop(i); st.rerun()
            if _add_btn("t27_footl_add", "＋ Adicionar link"):
                st.session_state.t27_foot_links.append({"texto": "LINK", "url": ""}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t27_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t27_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 littletracks. Criado com carinho para as futuras gerações.")
                with c2:
                    if len(st.session_state.t27_foot_copys) > 1 and _del_btn(f"t27_fcp_del_{i}"):
                        st.session_state.t27_foot_copys.pop(i); st.rerun()
            if _add_btn("t27_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t27_foot_copys.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 10. IMAGENS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Guia de Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Como adicionar imagens ao seu site:</strong><br><br>
                1. Acesse <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a>
                   (gratuito, sem cadastro) e faça o upload da sua imagem.<br>
                2. Clique com o botão direito na imagem → <em>Copiar endereço da imagem</em> — a URL termina em
                   <code>.jpg</code>, <code>.png</code> ou <code>.webp</code>.<br>
                3. Cole a URL no campo de imagem correspondente acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Imagem lateral da timeline: <strong>600 × 800 px</strong> (retrato, foto de criança)<br>
                • Logo: <strong>200 × 60 px</strong> (fundo transparente, PNG)<br><br>
                ❌ <strong>Não conseguiu subir a imagem?</strong> Envie para
                <strong>sttacksite@gmail.com</strong> com o assunto <em>"Imagem — [nome do seu site]"</em>.
            </div>
            """, unsafe_allow_html=True)

            # ══════════════════════════════════════════════════════════════════
            # 11. OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações / Pedidos Extras</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="warn-box">
                💬 <strong>Use este espaço para tudo que não encontrou nos campos acima!</strong><br>
                Ex: "usar tons pastéis ainda mais suaves", "quero a segunda linha do título em roxo",
                "adicionar seção de parceiros", "alterar ordem das seções"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t27_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t27_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t27_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t27_obs) > 1 and _del_btn(f"t27_obs_del_{i}"):
                        st.session_state.t27_obs.pop(i); st.rerun()
            if _add_btn("t27_obs_add", "＋ Adicionar observação"):
                st.session_state.t27_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 12. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t27_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t27_email_cliente.strip() or "@" not in st.session_state.t27_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t27_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t27_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t27_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t27_nome_cliente}'*."
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
        page_icon="🐾",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
