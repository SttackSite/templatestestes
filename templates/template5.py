import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/editor/main/img5.png"
TEMPLATE_NAME      = "Template 5 — Interstellar (Site Pro)"
TEMPLATE_ID        = "template_5"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t5_nome_cliente":  "",
        "t5_email_cliente": "",
        "t5_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t5_cores": [
            {"nome": "Cor Principal (Cyan)",     "valor": "#00f2ff"},
            {"nome": "Cor Secundária (Magenta)", "valor": "#ff00ff"},
            {"nome": "Cor de Fundo (Space)",     "valor": "#02040a"},
        ],

        # ── HERO ────────────────────────────────────────────────────────────
        "t5_hero_status":  [{"valor": "[ STATUS: PRONTO PARA LANÇAMENTO ]"}],
        "t5_hero_titulos": [{"valor": "CONSTRUA SUA ESTAÇÃO DIGITAL."}],
        "t5_hero_descs":   [{"valor": "Aprenda a criar seu novo site profissional em minutos, sem a dependência de um programador. Economize 80% do tempo e lance sua marca na velocidade da luz."}],
        "t5_hero_btns":    [{"texto": "INICIAR SEQUÊNCIA →", "url": "seção Esquadrão ao final da página"}],

        # ── GALERIA (SHIPS) ──────────────────────────────────────────────────
        "t5_ship_subtitulos": [{"valor": "// EXPLORAR CATÁLOGO DE TEMPLATES"}],
        "t5_ship_titulos":    [{"valor": "ESQUADRÃO DE ELITE"}],
        "t5_ships": [
            {"nome": "NEON PULSE",    "tier": "LEGENDARY", "img": "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=600", "desc": "Configurado para máxima conversão e SEO otimizado.", "btn_txt": "VER DATA-SHEET NEON",    "btn_url": "https://wa.me/5511999999999"},
            {"nome": "QUANTUM SUITE", "tier": "EPIC",      "img": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=600",    "desc": "Configurado para máxima conversão e SEO otimizado.", "btn_txt": "VER DATA-SHEET QUANTUM", "btn_url": "https://wa.me/5511999999999"},
            {"nome": "VOID MINIMAL",  "tier": "RARE",      "img": "https://images.unsplash.com/photo-1634017839464-5c339ebe3cb4?w=600", "desc": "Configurado para máxima conversão e SEO otimizado.", "btn_txt": "VER DATA-SHEET VOID",    "btn_url": "https://wa.me/5511999999999"},
        ],

        # ── ESTATÍSTICAS ────────────────────────────────────────────────────
        "t5_stats_titulos": [{"valor": "NÚMEROS QUE FALAM"}],
        "t5_stats": [
            {"valor": "1.2K", "label": "SITES PUBLICADOS"},
            {"valor": "98%",  "label": "SATISFAÇÃO"},
            {"valor": "24/7", "label": "UPLINK SUPORTE"},
            {"valor": "80%",  "label": "MAIS RÁPIDO"},
        ],

        # ── MISSÕES ─────────────────────────────────────────────────────────
        "t5_missoes_titulos": [{"valor": "OBJETIVOS DA MISSÃO"}],
        "t5_missoes": [
            {"valor": "Quer criar seu próprio site e customizá-lo em minutos pelo menor preço de mercado."},
            {"valor": "Deseja trabalhar vendendo sites de elite para terceiros com alta margem."},
            {"valor": "Precisa escalar a conversão de seus produtos físicos ou digitais."},
        ],

        # ── PROTOCOLO ───────────────────────────────────────────────────────
        "t5_protocolo_titulos": [{"valor": "PROTOCOLO DE LANÇAMENTO"}],
        "t5_passos": [
            {"num": "01", "titulo": "DOWNLOAD DOS ASSETS",   "desc": "Após a compra, todos os templates são disponibilizados no seu painel de comando."},
            {"num": "02", "titulo": "CUSTOMIZAÇÃO DE DADOS", "desc": "Siga nosso passo a passo visual para inserir suas informações e imagens."},
            {"num": "03", "titulo": "DEPLOY EM SEGUNDOS",    "desc": "Configure sua URL personalizada e suba os arquivos para a rede global."},
            {"num": "04", "titulo": "SISTEMA ONLINE",        "desc": "Seu site está no ar e pronto para operações em larga escala."},
        ],

        # ── PREÇOS ──────────────────────────────────────────────────────────
        "t5_precos_titulos": [{"valor": "ACESSO À FROTA"}],
        "t5_precos": [
            {"plano": "PILOT ACCESS",     "valor": "R$ 97",  "features": "1 Template de Elite\nSuporte Básico",                         "btn_txt": "SELECIONAR PILOT",   "url": "https://wa.me/5511999999999"},
            {"plano": "COMMANDER BUNDLE", "valor": "R$ 197", "features": "Todos os Templates\nAcesso à Comunidade\nSuporte Prioritário", "btn_txt": "ADQUIRIR COMMANDER", "url": "https://wa.me/5511999999999"},
            {"plano": "ADMIRAL PASS",     "valor": "R$ 497", "features": "Licença Comercial\nMentoria 1:1\nUpdates Vitalícios",          "btn_txt": "TORNAR-SE ADMIRAL",  "url": "https://wa.me/5511999999999"},
        ],

        # ── FAQ ─────────────────────────────────────────────────────────────
        "t5_faq_titulos": [{"valor": "DATABASE"}],
        "t5_faqs": [
            {"pergunta": "COMO É FEITA A TRANSFERÊNCIA DOS ARQUIVOS?", "resposta": "Os códigos são entregues em formato digital pronto para deploy direto via GitHub ou hospedagens estáticas."},
            {"pergunta": "TEREI SUPORTE NA CONFIGURAÇÃO DO DOMÍNIO?",  "resposta": "Sim, fornecemos manuais detalhados e suporte técnico para garantir que sua URL personalizada funcione perfeitamente."},
        ],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t5_footer": [{"valor": "© 2026 SITE PRO // INTERSTELLAR DESIGN // ALL RIGHTS RESERVED"}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t5_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t5_nome_cliente,
            "email":     st.session_state.t5_email_cliente,
            "nome_site": st.session_state.t5_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t5_nome_site}",
        },
        "cores": st.session_state.t5_cores,
        "hero": {
            "status":   st.session_state.t5_hero_status,
            "titulos":  st.session_state.t5_hero_titulos,
            "descs":    st.session_state.t5_hero_descs,
            "botoes":   st.session_state.t5_hero_btns,
        },
        "galeria": {
            "subtitulos": st.session_state.t5_ship_subtitulos,
            "titulos":    st.session_state.t5_ship_titulos,
            "naves":      st.session_state.t5_ships,
        },
        "estatisticas": {
            "titulos": st.session_state.t5_stats_titulos,
            "nodes":   st.session_state.t5_stats,
        },
        "missoes": {
            "titulos":   st.session_state.t5_missoes_titulos,
            "objetivos": st.session_state.t5_missoes,
        },
        "protocolo": {
            "titulos": st.session_state.t5_protocolo_titulos,
            "passos":  st.session_state.t5_passos,
        },
        "precos": {
            "titulos": st.session_state.t5_precos_titulos,
            "planos":  st.session_state.t5_precos,
        },
        "faq": {
            "titulos":   st.session_state.t5_faq_titulos,
            "perguntas": st.session_state.t5_faqs,
        },
        "footer":      st.session_state.t5_footer,
        "observacoes": st.session_state.t5_obs,
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

    # ── Aviso inicial ─────────────────────────────────────────────────────────
    st.markdown("""
    <div class="info-box">
        👋 <strong>Bem-vindo ao editor do seu site!</strong><br>
        Preencha os campos abaixo para personalizar o seu site. Não precisa ser técnico — é só digitar!
        Você também poderá vir aqui e ajustar seu site quantas vezes quiser.<br><br>
        💡 <strong>Tem alguma ideia que não encontrou aqui?</strong> Use o campo <em>Observações</em> no final
        para descrever o que deseja (ex: "quero uma fonte diferente", "adicionar um vídeo", "mudar o layout da seção X").
        Nossa equipe analisa tudo e aplica para você. 😊
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

            st.session_state.t5_nome_cliente = st.text_input(
                "Seu nome completo",
                value=st.session_state.t5_nome_cliente,
                key="t5_nome_cliente_inp",
                placeholder="Ex: João Silva",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t5_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t5_email_cliente,
                key="t5_email_cliente_inp",
                placeholder="Ex: joao@email.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: joaosilva, sitepro2026, interstellar).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t5_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t5_nome_site,
                key="t5_nome_site_inp",
                placeholder="Ex: sitepro2026  →  sttacksite.streamlit.app/?c=sitepro2026",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Cores Espaciais</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t5_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t5_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t5_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t5_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t5_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t5_cores) > 1 and _del_btn(f"t5_cor_del_{i}"):
                        st.session_state.t5_cores.pop(i); st.rerun()
            if _add_btn("t5_cor_add", "＋ Adicionar cor"):
                st.session_state.t5_cores.append({"nome": "Descreva onde usar esta cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌌 Hero (Comando Central)</div>', unsafe_allow_html=True)

            st.caption("Status  *(texto pequeno em cyan acima do título — ex: [ STATUS: PRONTO ])*")
            for i, s in enumerate(st.session_state.t5_hero_status):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t5_hero_status[i]["valor"] = st.text_input(
                        "Status", s["valor"], key=f"t5_h_stat_{i}", label_visibility="collapsed",
                        placeholder="Ex: [ STATUS: PRONTO PARA LANÇAMENTO ]")
                with c2:
                    if len(st.session_state.t5_hero_status) > 1 and _del_btn(f"t5_h_stat_del_{i}"):
                        st.session_state.t5_hero_status.pop(i); st.rerun()
            if _add_btn("t5_h_stat_add", "＋ Adicionar status"):
                st.session_state.t5_hero_status.append({"valor": "[ NOVO STATUS ]"}); st.rerun()

            st.caption("Título principal  *(exibido em destaque com efeito glow neon)*")
            for i, t in enumerate(st.session_state.t5_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t5_hero_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t5_h_tit_{i}", label_visibility="collapsed",
                        placeholder="Título principal em maiúsculas")
                with c2:
                    if len(st.session_state.t5_hero_titulos) > 1 and _del_btn(f"t5_h_tit_del_{i}"):
                        st.session_state.t5_hero_titulos.pop(i); st.rerun()
            if _add_btn("t5_h_tit_add", "＋ Adicionar título"):
                st.session_state.t5_hero_titulos.append({"valor": "NOVO TÍTULO."}); st.rerun()

            st.caption("Descrição  *(frase de apoio abaixo do título)*")
            for i, d in enumerate(st.session_state.t5_hero_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t5_hero_descs[i]["valor"] = st.text_area(
                        "Descrição", d["valor"], key=f"t5_h_desc_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Frase que explica o que você oferece")
                with c2:
                    if len(st.session_state.t5_hero_descs) > 1 and _del_btn(f"t5_h_desc_del_{i}"):
                        st.session_state.t5_hero_descs.pop(i); st.rerun()
            if _add_btn("t5_h_desc_add", "＋ Adicionar descrição"):
                st.session_state.t5_hero_descs.append({"valor": "Nova descrição..."}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🔗 <strong>URLs e destinos dos botões:</strong> você pode colocar seu WhatsApp
                (<code>https://wa.me/55119XXXXXXXX</code>), Instagram, qualquer link — ou simplesmente
                descrever para qual seção o botão deve levar (ex: <em>seção de contato ao final da página</em>).
            </div>
            """, unsafe_allow_html=True)

            st.caption("Botão  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t5_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t5_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t5_h_btn_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t5_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t5_h_btn_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t5_hero_btns) > 1 and _del_btn(f"t5_h_btn_del_{i}"):
                        st.session_state.t5_hero_btns.pop(i); st.rerun()
            if _add_btn("t5_h_btn_add", "＋ Adicionar botão"):
                st.session_state.t5_hero_btns.append({"texto": "COMEÇAR →", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. GALERIA (SHIPS)
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🚀 Esquadrão (Galeria de Cards)</div>', unsafe_allow_html=True)

            st.caption("Subtítulo da seção  *(texto pequeno acima do título)*")
            for i, t in enumerate(st.session_state.t5_ship_subtitulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t5_ship_subtitulos[i]["valor"] = st.text_input(
                        "Subtítulo", t["valor"], key=f"t5_sh_sub_{i}", label_visibility="collapsed",
                        placeholder="Ex: // EXPLORAR CATÁLOGO")
                with c2:
                    if len(st.session_state.t5_ship_subtitulos) > 1 and _del_btn(f"t5_sh_sub_del_{i}"):
                        st.session_state.t5_ship_subtitulos.pop(i); st.rerun()
            if _add_btn("t5_sh_sub_add", "＋ Adicionar subtítulo"):
                st.session_state.t5_ship_subtitulos.append({"valor": "// NOVO SUBTÍTULO"}); st.rerun()

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t5_ship_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t5_ship_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t5_sh_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: ESQUADRÃO DE ELITE")
                with c2:
                    if len(st.session_state.t5_ship_titulos) > 1 and _del_btn(f"t5_sh_t_del_{i}"):
                        st.session_state.t5_ship_titulos.pop(i); st.rerun()
            if _add_btn("t5_sh_t_add", "＋ Adicionar título"):
                st.session_state.t5_ship_titulos.append({"valor": "NOVO TÍTULO"}); st.rerun()

            st.caption("Cards  *(clique para expandir e editar cada um)*")
            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagens dos cards:</strong> cole a URL de uma imagem do
                <a href="https://imgur.com" target="_blank">imgur.com</a> no campo URL Imagem.
                Tamanho recomendado: <strong>600 × 400 px</strong>.
                Sem imagem? Deixe em branco e descreva nas Observações.
            </div>
            """, unsafe_allow_html=True)
            for i, ship in enumerate(st.session_state.t5_ships):
                with st.expander(f"Card {i+1}: {ship['nome']}"):
                    st.session_state.t5_ships[i]["nome"] = st.text_input(
                        "Nome", ship["nome"], key=f"t5_s_n_{i}",
                        placeholder="Nome do card em maiúsculas")
                    st.session_state.t5_ships[i]["tier"] = st.text_input(
                        "Tier / Categoria", ship["tier"], key=f"t5_s_tr_{i}",
                        placeholder="Ex: LEGENDARY, EPIC, RARE, COMMON")
                    st.session_state.t5_ships[i]["img"] = st.text_input(
                        "URL da Imagem", ship["img"], key=f"t5_s_img_{i}",
                        placeholder="https://i.imgur.com/... ou deixe vazio",
                        help="Cole a URL da imagem do imgur.com (termina em .jpg, .png etc.)")
                    st.session_state.t5_ships[i]["desc"] = st.text_area(
                        "Descrição", ship["desc"], key=f"t5_s_d_{i}", height=70,
                        placeholder="Descrição breve do card")
                    st.session_state.t5_ships[i]["btn_txt"] = st.text_input(
                        "Texto do Botão", ship["btn_txt"], key=f"t5_s_bt_{i}")
                    st.session_state.t5_ships[i]["btn_url"] = st.text_input(
                        "URL do Botão", ship["btn_url"], key=f"t5_s_bu_{i}",
                        placeholder="https:// ou seção de destino")
                    if len(st.session_state.t5_ships) > 1:
                        if st.button("🗑 Remover este card", key=f"t5_s_del_{i}"):
                            st.session_state.t5_ships.pop(i); st.rerun()
            if _add_btn("t5_s_add", "＋ Adicionar Card ao Esquadrão"):
                st.session_state.t5_ships.append({
                    "nome": "NOVA NAVE", "tier": "RARE", "img": "",
                    "desc": "Descrição do card.", "btn_txt": "VER DATA-SHEET", "btn_url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. ESTATÍSTICAS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📊 Data Nodes (Estatísticas)</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t5_stats_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t5_stats_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t5_st_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: NÚMEROS QUE FALAM")
                with c2:
                    if len(st.session_state.t5_stats_titulos) > 1 and _del_btn(f"t5_st_t_del_{i}"):
                        st.session_state.t5_stats_titulos.pop(i); st.rerun()
            if _add_btn("t5_st_t_add", "＋ Adicionar título"):
                st.session_state.t5_stats_titulos.append({"valor": "DADOS"}); st.rerun()

            st.caption("Nodes  *(Valor | Rótulo)*")
            for i, stat in enumerate(st.session_state.t5_stats):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t5_stats[i]["valor"] = st.text_input(
                        "Valor", stat["valor"], key=f"t5_st_v_{i}", label_visibility="collapsed",
                        placeholder="Ex: 98%")
                with c2:
                    st.session_state.t5_stats[i]["label"] = st.text_input(
                        "Rótulo", stat["label"], key=f"t5_st_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: SATISFAÇÃO")
                with c3:
                    if len(st.session_state.t5_stats) > 1 and _del_btn(f"t5_st_del_{i}"):
                        st.session_state.t5_stats.pop(i); st.rerun()
            if _add_btn("t5_st_add", "＋ Adicionar Data Node"):
                st.session_state.t5_stats.append({"valor": "0", "label": "NOVO DADO"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. MISSÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎯 Objetivos da Missão</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t5_missoes_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t5_missoes_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t5_m_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: OBJETIVOS DA MISSÃO")
                with c2:
                    if len(st.session_state.t5_missoes_titulos) > 1 and _del_btn(f"t5_m_t_del_{i}"):
                        st.session_state.t5_missoes_titulos.pop(i); st.rerun()
            if _add_btn("t5_m_t_add", "＋ Adicionar título"):
                st.session_state.t5_missoes_titulos.append({"valor": "MISSÕES"}); st.rerun()

            st.caption("Objetivos  *(cada linha é uma caixa com borda colorida)*")
            for i, missao in enumerate(st.session_state.t5_missoes):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t5_missoes[i]["valor"] = st.text_input(
                        "Missão", missao["valor"], key=f"t5_m_v_{i}", label_visibility="collapsed",
                        placeholder="Descreva para quem este produto é ideal")
                with c2:
                    if len(st.session_state.t5_missoes) > 1 and _del_btn(f"t5_m_del_{i}"):
                        st.session_state.t5_missoes.pop(i); st.rerun()
            if _add_btn("t5_m_add", "＋ Adicionar Objetivo"):
                st.session_state.t5_missoes.append({"valor": "Novo objetivo da missão..."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. PROTOCOLO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🛸 Protocolo de Lançamento</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t5_protocolo_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t5_protocolo_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t5_p_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: PROTOCOLO DE LANÇAMENTO")
                with c2:
                    if len(st.session_state.t5_protocolo_titulos) > 1 and _del_btn(f"t5_p_t_del_{i}"):
                        st.session_state.t5_protocolo_titulos.pop(i); st.rerun()
            if _add_btn("t5_p_t_add", "＋ Adicionar título"):
                st.session_state.t5_protocolo_titulos.append({"valor": "PROTOCOLO"}); st.rerun()

            st.caption("Passos  *(clique para expandir e editar cada um)*")
            for i, passo in enumerate(st.session_state.t5_passos):
                with st.expander(f"Passo {passo['num']}: {passo['titulo']}"):
                    st.session_state.t5_passos[i]["num"] = st.text_input(
                        "Número do passo", passo["num"], key=f"t5_ps_num_{i}",
                        placeholder="Ex: 01, 02, 03...")
                    st.session_state.t5_passos[i]["titulo"] = st.text_input(
                        "Título do passo", passo["titulo"], key=f"t5_ps_tit_{i}")
                    st.session_state.t5_passos[i]["desc"] = st.text_area(
                        "Descrição", passo["desc"], key=f"t5_ps_desc_{i}", height=80,
                        placeholder="Explique o que acontece neste passo")
                    if len(st.session_state.t5_passos) > 1:
                        if st.button("🗑 Remover este passo", key=f"t5_ps_del_{i}"):
                            st.session_state.t5_passos.pop(i); st.rerun()
            if _add_btn("t5_ps_add", "＋ Adicionar Passo"):
                n = len(st.session_state.t5_passos) + 1
                st.session_state.t5_passos.append({"num": f"{n:02d}", "titulo": "NOVO PASSO", "desc": "Descrição do passo."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. PREÇOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💳 Acesso à Frota (Preços)</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t5_precos_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t5_precos_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t5_pr_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: ACESSO À FROTA")
                with c2:
                    if len(st.session_state.t5_precos_titulos) > 1 and _del_btn(f"t5_pr_t_del_{i}"):
                        st.session_state.t5_precos_titulos.pop(i); st.rerun()
            if _add_btn("t5_pr_t_add", "＋ Adicionar título"):
                st.session_state.t5_precos_titulos.append({"valor": "PLANOS"}); st.rerun()

            st.caption("Planos  *(clique para expandir e editar cada um)*")
            for i, preco in enumerate(st.session_state.t5_precos):
                with st.expander(f"Plano {i+1}: {preco['plano']}"):
                    st.session_state.t5_precos[i]["plano"] = st.text_input(
                        "Nome do Plano", preco["plano"], key=f"t5_pr_p_{i}")
                    st.session_state.t5_precos[i]["valor"] = st.text_input(
                        "Preço", preco["valor"], key=f"t5_pr_v_{i}",
                        placeholder="Ex: R$ 97")
                    st.session_state.t5_precos[i]["features"] = st.text_area(
                        "Vantagens (uma por linha)", preco["features"], key=f"t5_pr_f_{i}", height=100,
                        placeholder="Feature 1\nFeature 2\nFeature 3")
                    st.session_state.t5_precos[i]["btn_txt"] = st.text_input(
                        "Texto do Botão", preco["btn_txt"], key=f"t5_pr_bt_{i}")
                    st.session_state.t5_precos[i]["url"] = st.text_input(
                        "URL do Botão", preco["url"], key=f"t5_pr_u_{i}",
                        placeholder="https:// ou seção de destino",
                        help="Pode ser seu link de pagamento, WhatsApp etc.")
                    if len(st.session_state.t5_precos) > 1:
                        if st.button("🗑 Remover este plano", key=f"t5_pr_del_{i}"):
                            st.session_state.t5_precos.pop(i); st.rerun()
            if _add_btn("t5_pr_add", "＋ Adicionar Plano"):
                st.session_state.t5_precos.append({
                    "plano": "NOVO PLANO", "valor": "R$ 0",
                    "features": "Feature 1", "btn_txt": "SELECIONAR", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. FAQ
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">❓ Database (FAQ)</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t5_faq_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t5_faq_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t5_faq_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: DATABASE ou PERGUNTAS FREQUENTES")
                with c2:
                    if len(st.session_state.t5_faq_titulos) > 1 and _del_btn(f"t5_faq_t_del_{i}"):
                        st.session_state.t5_faq_titulos.pop(i); st.rerun()
            if _add_btn("t5_faq_t_add", "＋ Adicionar título"):
                st.session_state.t5_faq_titulos.append({"valor": "FAQ"}); st.rerun()

            st.caption("Perguntas e respostas  *(clique para expandir e editar cada uma)*")
            for i, faq in enumerate(st.session_state.t5_faqs):
                with st.expander(f"FAQ {i+1}: {faq['pergunta'][:50]}..."):
                    st.session_state.t5_faqs[i]["pergunta"] = st.text_input(
                        "Pergunta", faq["pergunta"], key=f"t5_faq_p_{i}",
                        placeholder="ESCREVA A PERGUNTA EM MAIÚSCULAS")
                    st.session_state.t5_faqs[i]["resposta"] = st.text_area(
                        "Resposta", faq["resposta"], key=f"t5_faq_r_{i}", height=80,
                        placeholder="Escreva a resposta de forma clara e objetiva")
                    if len(st.session_state.t5_faqs) > 1:
                        if st.button("🗑 Remover esta pergunta", key=f"t5_faq_del_{i}"):
                            st.session_state.t5_faqs.pop(i); st.rerun()
            if _add_btn("t5_faq_add", "＋ Adicionar FAQ"):
                st.session_state.t5_faqs.append({"pergunta": "NOVA PERGUNTA?", "resposta": "Resposta aqui."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 9. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">⚓ Rodapé</div>', unsafe_allow_html=True)
            for i, f in enumerate(st.session_state.t5_footer):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t5_footer[i]["valor"] = st.text_input(
                        "Copyright", f["valor"], key=f"t5_ft_v_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 MINHA EMPRESA // ALL RIGHTS RESERVED")
                with c2:
                    if len(st.session_state.t5_footer) > 1 and _del_btn(f"t5_ft_del_{i}"):
                        st.session_state.t5_footer.pop(i); st.rerun()
            if _add_btn("t5_ft_add", "＋ Adicionar linha"):
                st.session_state.t5_footer.append({"valor": "© 2026"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 10. IMAGENS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Como adicionar imagens ao seu site:</strong><br><br>
                1. Acesse <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a>
                   (gratuito, sem cadastro) e faça o upload da sua imagem.<br>
                2. Clique com o botão direito na imagem → <em>Copiar endereço da imagem</em> — a URL termina em
                   <code>.jpg</code>, <code>.png</code> ou <code>.webp</code>.<br>
                3. Cole essa URL no campo <em>URL da Imagem</em> dentro de cada card acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Cards do Esquadrão: <strong>600 × 400 px</strong><br>
                • Banner / Hero: <strong>1920 × 800 px</strong><br>
                • Logo: <strong>200 × 60 px</strong> (fundo transparente, formato PNG)<br><br>
                ❌ <strong>Não conseguiu subir a imagem?</strong> Envie diretamente para
                <strong>sttacksite@gmail.com</strong> com o assunto <em>"Imagem — [nome do seu site]"</em>
                e diga onde ela deve ser inserida. Nossa equipe cuida disso para você. 😊
            </div>
            """, unsafe_allow_html=True)

            # ══════════════════════════════════════════════════════════════════
            # 11. OBSERVAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📝 Observações / Pedidos Extras</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="warn-box">
                💬 <strong>Use este espaço para tudo que não encontrou nos campos acima!</strong><br>
                Ex: "quero mudar a fonte", "adicionar uma seção de FAQ", "colocar vídeo do YouTube",
                "texto em negrito no título", "remover a seção X", "adicionar mapa do Google"...
                Nossa equipe lê cada observação e aplica para você! 🙌
            </div>
            """, unsafe_allow_html=True)
            for i, obs in enumerate(st.session_state.t5_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t5_obs[i]["valor"] = st.text_area(
                        "Observações", obs["valor"], key=f"t5_obs_v_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t5_obs) > 1 and _del_btn(f"t5_obs_del_{i}"):
                        st.session_state.t5_obs.pop(i); st.rerun()
            if _add_btn("t5_obs_add", "＋ Adicionar observação"):
                st.session_state.t5_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 12. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t5_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t5_email_cliente.strip() or "@" not in st.session_state.t5_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t5_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t5_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t5_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t5_nome_cliente}'*."
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
        page_icon="🌌",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
