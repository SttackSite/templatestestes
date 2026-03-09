import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/editor/main/img11.png"
TEMPLATE_NAME      = "Template 11 — Pura Vida Brackets (E-commerce & Estilo de Vida)"
TEMPLATE_ID        = "template_11"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t11_nome_cliente":  "",
        "t11_email_cliente": "",
        "t11_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t11_cores": [
            {"nome": "Cor de Anúncio (Rosa)",      "valor": "#ffb6c1"},
            {"nome": "Cor de Preço (Rosa Quente)",  "valor": "#ff69b4"},
            {"nome": "Cor de Texto (Escuro)",       "valor": "#333333"},
            {"nome": "Cor de Fundo (Light)",        "valor": "#f9f9f9"},
        ],

        # ── BARRA DE ANÚNCIO ─────────────────────────────────────────────────
        "t11_announcements": [{"valor": "FRETE GRÁTIS EM PEDIDOS ACIMA DE R$ 150! 🌴"}],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t11_logos": [{"valor": "Pura Vida"}],
        "t11_nav_links": [
            {"texto": "Pulseiras", "url": "seção Vitrine de Produtos"},
            {"texto": "Joias",     "url": "seção Vitrine de Produtos"},
            {"texto": "Coleções",  "url": "seção Vitrine de Produtos"},
            {"texto": "Sale",      "url": "seção Vitrine de Produtos"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t11_hero_imgs":    [{"valor": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1500&q=80"}],
        "t11_hero_titulos": [{"valor": "VIVA O MOMENTO"}],
        "t11_hero_descs":   [{"valor": "Nossas peças são feitas à mão por artesãos ao redor do mundo, espalhando a energia Pura Vida."}],

        # ── PRODUTOS ────────────────────────────────────────────────────────
        "t11_prod_secao_titulos": [{"valor": "Novidades"}],
        "t11_prod_items": [
            {"nome": "Pack Shoreline", "preco": "45,00", "img": "https://images.unsplash.com/photo-1611591437281-460bfbe1220a?auto=format&fit=crop&w=400&q=80", "btn_txt": "Adicionar", "url": "https://wa.me/5511999999999"},
            {"nome": "Ocean Blue",     "preco": "32,00", "img": "https://images.unsplash.com/photo-1573408301185-9146fe634ad0?auto=format&fit=crop&w=400&q=80", "btn_txt": "Adicionar", "url": "https://wa.me/5511999999999"},
            {"nome": "Sunset Vibes",   "preco": "38,00", "img": "https://images.unsplash.com/photo-1535632066927-ab7c9ab60908?auto=format&fit=crop&w=400&q=80", "btn_txt": "Adicionar", "url": "https://wa.me/5511999999999"},
            {"nome": "Sand & Salt",    "preco": "29,00", "img": "https://images.unsplash.com/photo-1515562141207-7a88fb7ce338?auto=format&fit=crop&w=400&q=80", "btn_txt": "Adicionar", "url": "https://wa.me/5511999999999"},
        ],

        # ── IMPACTO SOCIAL ───────────────────────────────────────────────────
        "t11_imp_imgs":    [{"valor": "https://images.unsplash.com/photo-1484820540004-14229fe36ca4?auto=format&fit=crop&w=800&q=80"}],
        "t11_imp_titulos": [{"valor": "Retribuindo ao Planeta"}],
        "t11_imp_descs":   [{"valor": "Cada compra ajuda a apoiar causas ambientais e artesãos locais. Já doamos mais de R$ 4 milhões para instituições de caridade através de vocês."}],
        "t11_imp_btns":    [{"texto": "Saiba Mais", "url": "https://wa.me/5511999999999"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t11_foot_logos":   [{"valor": "Pura Vida"}],
        "t11_foot_copys":   [{"valor": "© 2026 Pura Vida Brackets. Siga-nos no Instagram @puravida"}],
        "t11_foot_sociais": [{"texto": "@puravida", "url": "https://wa.me/5511999999999"}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t11_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t11_nome_cliente,
            "email":     st.session_state.t11_email_cliente,
            "nome_site": st.session_state.t11_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t11_nome_site}",
        },
        "cores": st.session_state.t11_cores,
        "barra_anuncio": st.session_state.t11_announcements,
        "navbar": {
            "logos": st.session_state.t11_logos,
            "links": st.session_state.t11_nav_links,
        },
        "hero": {
            "imagens": st.session_state.t11_hero_imgs,
            "titulos": st.session_state.t11_hero_titulos,
            "descs":   st.session_state.t11_hero_descs,
        },
        "produtos": {
            "titulo_secao": st.session_state.t11_prod_secao_titulos,
            "itens":        st.session_state.t11_prod_items,
        },
        "impacto_social": {
            "imagens": st.session_state.t11_imp_imgs,
            "titulos": st.session_state.t11_imp_titulos,
            "descs":   st.session_state.t11_imp_descs,
            "botoes":  st.session_state.t11_imp_btns,
        },
        "footer": {
            "logos":    st.session_state.t11_foot_logos,
            "copyright":st.session_state.t11_foot_copys,
            "sociais":  st.session_state.t11_foot_sociais,
        },
        "observacoes": st.session_state.t11_obs,
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

            st.session_state.t11_nome_cliente = st.text_input(
                "Seu nome completo",
                value=st.session_state.t11_nome_cliente,
                key="t11_nome_cliente_inp",
                placeholder="Ex: João Silva",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t11_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t11_email_cliente,
                key="t11_email_cliente_inp",
                placeholder="Ex: joao@email.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: puravida, minhalojaonline, meusite).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t11_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t11_nome_site,
                key="t11_nome_site_inp",
                placeholder="Ex: puravida  →  sttacksite.streamlit.app/?c=puravida",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Identidade Visual</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t11_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t11_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t11_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t11_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t11_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t11_cores) > 1 and _del_btn(f"t11_cor_del_{i}"):
                        st.session_state.t11_cores.pop(i); st.rerun()
            if _add_btn("t11_cor_add", "＋ Adicionar cor"):
                st.session_state.t11_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. BARRA DE ANÚNCIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📢 Barra de Anúncio</div>', unsafe_allow_html=True)
            st.caption("Texto exibido na faixa colorida do topo  *(promoções, frete grátis etc.)*")
            for i, ann in enumerate(st.session_state.t11_announcements):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_announcements[i]["valor"] = st.text_input(
                        "Anúncio", ann["valor"], key=f"t11_ann_{i}", label_visibility="collapsed",
                        placeholder="Ex: FRETE GRÁTIS ACIMA DE R$ 150 🌴")
                with c2:
                    if len(st.session_state.t11_announcements) > 1 and _del_btn(f"t11_ann_del_{i}"):
                        st.session_state.t11_announcements.pop(i); st.rerun()
            if _add_btn("t11_ann_add", "＋ Adicionar anúncio"):
                st.session_state.t11_announcements.append({"valor": "NOVO ANÚNCIO 🌴"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Logo e Navegação</div>', unsafe_allow_html=True)

            st.caption("Nome da marca  *(exibido em fonte cursiva no logo)*")
            for i, logo in enumerate(st.session_state.t11_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_logos[i]["valor"] = st.text_input(
                        "Marca", logo["valor"], key=f"t11_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: Pura Vida ou Minha Marca")
                with c2:
                    if len(st.session_state.t11_logos) > 1 and _del_btn(f"t11_logo_del_{i}"):
                        st.session_state.t11_logos.pop(i); st.rerun()
            if _add_btn("t11_logo_add", "＋ Adicionar logo"):
                st.session_state.t11_logos.append({"valor": "Nova Marca"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🔗 <strong>URLs e destinos dos links:</strong> você pode colocar seu WhatsApp
                (<code>https://wa.me/55119XXXXXXXX</code>), Instagram, qualquer link — ou simplesmente
                descrever para qual seção o link deve levar (ex: <em>seção de produtos</em>).
            </div>
            """, unsafe_allow_html=True)

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t11_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t11_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t11_nl_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t11_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t11_nl_u_{i}", label_visibility="collapsed",
                        placeholder="Seção ou https://...")
                with c3:
                    if len(st.session_state.t11_nav_links) > 1 and _del_btn(f"t11_nl_del_{i}"):
                        st.session_state.t11_nav_links.pop(i); st.rerun()
            if _add_btn("t11_nl_add", "＋ Adicionar link ao menu"):
                st.session_state.t11_nav_links.append({"texto": "LINK", "url": "seção de destino"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌴 Hero Banner</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagem de fundo do Hero:</strong> cole a URL de uma foto do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanho ideal: <strong>1920 × 800 px</strong>. Prefira fotos paisagísticas ou de estilo de vida.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Imagem de fundo  *(URL da foto)*")
            for i, img in enumerate(st.session_state.t11_hero_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_hero_imgs[i]["valor"] = st.text_input(
                        "Imagem Hero", img["valor"], key=f"t11_h_i_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... ou URL da imagem")
                with c2:
                    if len(st.session_state.t11_hero_imgs) > 1 and _del_btn(f"t11_h_i_del_{i}"):
                        st.session_state.t11_hero_imgs.pop(i); st.rerun()
            if _add_btn("t11_h_i_add", "＋ Adicionar imagem hero"):
                st.session_state.t11_hero_imgs.append({"valor": ""}); st.rerun()

            st.caption("Título principal  *(geralmente em maiúsculas)*")
            for i, t in enumerate(st.session_state.t11_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_hero_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t11_h_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: VIVA O MOMENTO")
                with c2:
                    if len(st.session_state.t11_hero_titulos) > 1 and _del_btn(f"t11_h_t_del_{i}"):
                        st.session_state.t11_hero_titulos.pop(i); st.rerun()
            if _add_btn("t11_h_t_add", "＋ Adicionar título"):
                st.session_state.t11_hero_titulos.append({"valor": "NOVO TÍTULO"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t11_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t11_h_d_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Frase que apresenta sua marca ou produtos")
                with c2:
                    if len(st.session_state.t11_hero_descs) > 1 and _del_btn(f"t11_h_d_del_{i}"):
                        st.session_state.t11_hero_descs.pop(i); st.rerun()
            if _add_btn("t11_h_d_add", "＋ Adicionar descrição"):
                st.session_state.t11_hero_descs.append({"valor": "Nova descrição"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. PRODUTOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🛍️ Vitrine de Produtos</div>', unsafe_allow_html=True)

            st.caption("Título da vitrine")
            for i, t in enumerate(st.session_state.t11_prod_secao_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_prod_secao_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t11_pst_{i}", label_visibility="collapsed",
                        placeholder="Ex: Novidades ou Mais Vendidos")
                with c2:
                    if len(st.session_state.t11_prod_secao_titulos) > 1 and _del_btn(f"t11_pst_del_{i}"):
                        st.session_state.t11_prod_secao_titulos.pop(i); st.rerun()
            if _add_btn("t11_pst_add", "＋ Adicionar título"):
                st.session_state.t11_prod_secao_titulos.append({"valor": "Nova Seção"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagens dos produtos:</strong> cole a URL do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanho recomendado: <strong>400 × 400 px</strong> (quadrada).
            </div>
            """, unsafe_allow_html=True)

            st.caption("Cards de produto  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t11_prod_items):
                with st.expander(f"Produto {i+1}: {item['nome']}"):
                    st.session_state.t11_prod_items[i]["nome"] = st.text_input(
                        "Nome do Produto", item["nome"], key=f"t11_pi_n_{i}",
                        placeholder="Nome do produto")
                    st.session_state.t11_prod_items[i]["preco"] = st.text_input(
                        "Preço", item["preco"], key=f"t11_pi_p_{i}",
                        placeholder="Ex: 45,00")
                    st.session_state.t11_prod_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t11_pi_i_{i}",
                        placeholder="https://i.imgur.com/... ou URL da imagem",
                        help="Cole a URL da imagem do imgur.com")
                    st.session_state.t11_prod_items[i]["btn_txt"] = st.text_input(
                        "Texto do Botão", item["btn_txt"], key=f"t11_pi_bt_{i}",
                        placeholder="Ex: Adicionar ao Carrinho")
                    st.session_state.t11_prod_items[i]["url"] = st.text_input(
                        "URL do Botão", item["url"], key=f"t11_pi_u_{i}",
                        placeholder="https:// ou seção de destino")
                    if len(st.session_state.t11_prod_items) > 1:
                        if st.button("🗑 Remover este produto", key=f"t11_pi_del_{i}"):
                            st.session_state.t11_prod_items.pop(i); st.rerun()
            if _add_btn("t11_pi_add", "＋ Adicionar produto"):
                st.session_state.t11_prod_items.append({
                    "nome": "Novo Produto", "preco": "0,00",
                    "img": "", "btn_txt": "Adicionar", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. IMPACTO SOCIAL
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌍 Impacto Social / Causa</div>', unsafe_allow_html=True)

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagem lateral:</strong> cole a URL do
                <a href="https://imgur.com" target="_blank">imgur.com</a>.
                Tamanho recomendado: <strong>800 × 600 px</strong>.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Imagem  *(URL da foto ao lado do texto)*")
            for i, img in enumerate(st.session_state.t11_imp_imgs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_imp_imgs[i]["valor"] = st.text_input(
                        "Imagem", img["valor"], key=f"t11_is_i_{i}", label_visibility="collapsed",
                        placeholder="https://i.imgur.com/... ou URL da imagem")
                with c2:
                    if len(st.session_state.t11_imp_imgs) > 1 and _del_btn(f"t11_is_i_del_{i}"):
                        st.session_state.t11_imp_imgs.pop(i); st.rerun()
            if _add_btn("t11_is_i_add", "＋ Adicionar imagem"):
                st.session_state.t11_imp_imgs.append({"valor": ""}); st.rerun()

            st.caption("Título")
            for i, t in enumerate(st.session_state.t11_imp_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_imp_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t11_is_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: Retribuindo ao Planeta")
                with c2:
                    if len(st.session_state.t11_imp_titulos) > 1 and _del_btn(f"t11_is_t_del_{i}"):
                        st.session_state.t11_imp_titulos.pop(i); st.rerun()
            if _add_btn("t11_is_t_add", "＋ Adicionar título"):
                st.session_state.t11_imp_titulos.append({"valor": "Novo Título"}); st.rerun()

            st.caption("Descrição")
            for i, d in enumerate(st.session_state.t11_imp_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_imp_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t11_is_d_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Conte sobre sua causa, missão ou impacto social")
                with c2:
                    if len(st.session_state.t11_imp_descs) > 1 and _del_btn(f"t11_is_d_del_{i}"):
                        st.session_state.t11_imp_descs.pop(i); st.rerun()
            if _add_btn("t11_is_d_add", "＋ Adicionar descrição"):
                st.session_state.t11_imp_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Botão  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t11_imp_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t11_imp_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t11_isb_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t11_imp_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t11_isb_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t11_imp_btns) > 1 and _del_btn(f"t11_isb_del_{i}"):
                        st.session_state.t11_imp_btns.pop(i); st.rerun()
            if _add_btn("t11_isb_add", "＋ Adicionar botão"):
                st.session_state.t11_imp_btns.append({"texto": "Saiba Mais", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Logo do rodapé  *(exibido em fonte cursiva)*")
            for i, logo in enumerate(st.session_state.t11_foot_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_foot_logos[i]["valor"] = st.text_input(
                        "Logo Footer", logo["valor"], key=f"t11_fl_{i}", label_visibility="collapsed",
                        placeholder="Ex: Pura Vida ou Minha Marca")
                with c2:
                    if len(st.session_state.t11_foot_logos) > 1 and _del_btn(f"t11_fl_del_{i}"):
                        st.session_state.t11_foot_logos.pop(i); st.rerun()
            if _add_btn("t11_fl_add", "＋ Adicionar logo ao rodapé"):
                st.session_state.t11_foot_logos.append({"valor": "Nova Marca"}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t11_foot_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_foot_copys[i]["valor"] = st.text_input(
                        "Copyright", copy["valor"], key=f"t11_fcp_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 Minha Marca. Todos os direitos reservados.")
                with c2:
                    if len(st.session_state.t11_foot_copys) > 1 and _del_btn(f"t11_fcp_del_{i}"):
                        st.session_state.t11_foot_copys.pop(i); st.rerun()
            if _add_btn("t11_fcp_add", "＋ Adicionar linha de copyright"):
                st.session_state.t11_foot_copys.append({"valor": "© 2026"}); st.rerun()

            st.caption("Redes sociais  *(Texto/@ | URL)*")
            for i, soc in enumerate(st.session_state.t11_foot_sociais):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t11_foot_sociais[i]["texto"] = st.text_input(
                        "Rede", soc["texto"], key=f"t11_fs_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: @meuperfil")
                with c2:
                    st.session_state.t11_foot_sociais[i]["url"] = st.text_input(
                        "URL", soc["url"], key=f"t11_fs_u_{i}", label_visibility="collapsed",
                        placeholder="https://instagram.com/...")
                with c3:
                    if len(st.session_state.t11_foot_sociais) > 1 and _del_btn(f"t11_fs_del_{i}"):
                        st.session_state.t11_foot_sociais.pop(i); st.rerun()
            if _add_btn("t11_fs_add", "＋ Adicionar rede social"):
                st.session_state.t11_foot_sociais.append({"texto": "@perfil", "url": ""}); st.rerun()

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
                3. Cole a URL no campo correspondente nas seções acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Hero de fundo: <strong>1920 × 800 px</strong><br>
                • Produtos: <strong>400 × 400 px</strong> (quadrada)<br>
                • Impacto Social lateral: <strong>800 × 600 px</strong><br>
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
                Ex: "alterar a fonte cursiva do logo", "adicionar seção de depoimentos", "colocar vídeo do YouTube",
                "adicionar FAQ", "remover seção de impacto social", "adicionar mapa do Google"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, item in enumerate(st.session_state.t11_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t11_obs[i]["valor"] = st.text_area(
                        "Notas extras", item["valor"], key=f"t11_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t11_obs) > 1 and _del_btn(f"t11_obs_del_{i}"):
                        st.session_state.t11_obs.pop(i); st.rerun()
            if _add_btn("t11_obs_add", "＋ Adicionar observação"):
                st.session_state.t11_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 10. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t11_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t11_email_cliente.strip() or "@" not in st.session_state.t11_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t11_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t11_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t11_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t11_nome_cliente}'*."
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
        page_icon="✏️",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
