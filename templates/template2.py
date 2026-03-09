import streamlit as st
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/editor/main/img2.png"
TEMPLATE_NAME      = "Template 2 — FitPro Academia"
TEMPLATE_ID        = "template_2"
GMAIL_USER         = st.secrets.get("GMAIL_USER", "")
GMAIL_PASS         = st.secrets.get("GMAIL_PASS", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t2_nome_cliente":  "",
        "t2_email_cliente": "",
        "t2_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t2_cores": [
            {"nome": "Cor principal (destaques, botões)", "valor": "#FF6B35"},
            {"nome": "Cor de fundo (seções escuras)",     "valor": "#1a1a1a"},
            {"nome": "Cor dos textos principais",         "valor": "#1a1a1a"},
            {"nome": "Cor dos subtextos",                 "valor": "#666666"},
        ],

        # ── NAVBAR ──────────────────────────────────────────────────────────
        "t2_logos": [{"parte1": "FIT", "destaque": "PRO"}],
        "t2_nav_links": [
            {"texto": "Serviços", "url": "seção Nossos Serviços"},
            {"texto": "Galeria",  "url": "seção Por que nos escolher"},
            {"texto": "Sobre",    "url": "seção Planos e Preços"},
            {"texto": "Contato",  "url": "seção de contato ao final da página"},
        ],
        "t2_nav_ctas": [{"texto": "Começar Agora", "url": "https://wa.me/5511999999999"}],

        # ── HERO ────────────────────────────────────────────────────────────
        "t2_hero_titulos":    [{"parte1": "Transforme seu", "destaque": "corpo", "parte2": "e mente"}],
        "t2_hero_subtitulos": [{"valor": "Programas personalizados, treinadores experientes e ambiente de primeira qualidade. Alcance seus objetivos conosco."}],
        "t2_hero_stats": [
            {"numero": "5.000+", "label": "Alunos Ativos"},
            {"numero": "15+",    "label": "Anos de Experiência"},
        ],
        "t2_hero_btns":   [{"texto": "Agende uma Avaliação Gratuita", "url": "https://wa.me/5511999999999"}],
        "t2_hero_images": [{"emoji": "🏋️‍♂️"}],

        # ── SERVIÇOS ────────────────────────────────────────────────────────
        "t2_serv_titulos": [{"parte1": "Nossos", "destaque": "Serviços"}],
        "t2_serv_descs":   [{"valor": "Oferecemos uma variedade de programas e serviços para atender todos os seus objetivos fitness"}],
        "t2_serv_cards": [
            {"icone": "🏋️", "titulo": "Musculação",       "descricao": "Programas de treinamento com pesos para ganho de massa e força muscular."},
            {"icone": "🏃", "titulo": "Cardio",           "descricao": "Equipamentos modernos para treinos cardiovasculares de alta performance."},
            {"icone": "🧘", "titulo": "Yoga e Pilates",    "descricao": "Aulas de flexibilidade, equilíbrio e bem-estar mental."},
            {"icone": "👨‍🏫", "titulo": "Personal Training", "descricao": "Acompanhamento individual com treinadores certificados."},
            {"icone": "🥗", "titulo": "Nutrição",          "descricao": "Orientação nutricional personalizada para seus objetivos."},
            {"icone": "💪", "titulo": "Grupos Funcionais", "descricao": "Treinos em grupo para motivação e diversão."},
        ],

        # ── DIFERENCIAIS ────────────────────────────────────────────────────
        "t2_feat_titulos": [{"parte1": "Por que escolher a", "destaque": "FitPro"}],
        "t2_feat_descs":   [{"valor": "Diferenciais que fazem a diferença na sua jornada fitness"}],
        "t2_feat_boxes": [
            {"titulo": "Equipamentos Modernos",   "descricao": "Máquinas de última geração importadas, sempre mantidas em perfeito funcionamento."},
            {"titulo": "Treinadores Certificados", "descricao": "Profissionais qualificados e experientes para orientar seu treino."},
            {"titulo": "Ambiente Acolhedor",       "descricao": "Espaço limpo, climatizado e seguro para você treinar com conforto."},
            {"titulo": "Horários Flexíveis",       "descricao": "Aberto de segunda a domingo, com horários que se adaptam à sua rotina."},
            {"titulo": "Comunidade Ativa",         "descricao": "Faça parte de uma comunidade motivada e comprometida com resultados."},
            {"titulo": "Acompanhamento Contínuo",  "descricao": "Avaliações periódicas para acompanhar sua evolução e ajustar treinos."},
        ],

        # ── PREÇOS ──────────────────────────────────────────────────────────
        "t2_price_titulos": [{"parte1": "Planos e", "destaque": "Preços"}],
        "t2_price_descs":   [{"valor": "Escolha o plano que melhor se adequa aos seus objetivos"}],
        "t2_price_cards": [
            {"titulo": "Básico",  "preco": "R$ 99",  "periodo": "Por mês", "features": "Acesso à academia\nUso de todos os equipamentos\nVestiário e chuveiro",                              "btn_txt": "Escolher Plano", "url": "https://wa.me/5511999999999"},
            {"titulo": "Premium", "preco": "R$ 199", "periodo": "Por mês", "features": "Acesso à academia\nAulas em grupo ilimitadas\n2 sessões personal/mês\nAvaliação física mensal",      "btn_txt": "Escolher Plano", "url": "https://wa.me/5511999999999"},
            {"titulo": "Elite",   "preco": "R$ 399", "periodo": "Por mês", "features": "Acesso 24/7\nPersonal training ilimitado\nAulas em grupo ilimitadas\nSuplementos com desconto",      "btn_txt": "Escolher Plano", "url": "https://wa.me/5511999999999"},
        ],

        # ── DEPOIMENTOS ─────────────────────────────────────────────────────
        "t2_test_titulos": [{"parte1": "Histórias de", "destaque": "Sucesso"}],
        "t2_test_descs":   [{"valor": "Veja como nossos alunos transformaram suas vidas"}],
        "t2_test_cards": [
            {"texto": "Entrei na FitPro sem conhecimento nenhum sobre treino. Os profissionais me orientaram perfeitamente e em 6 meses consegui resultados incríveis. Recomendo muito!", "autor": "Roberto Silva",  "cargo": "Aluno há 2 anos"},
            {"texto": "O ambiente é acolhedor, os treinadores são atenciosos e os resultados falam por si. Já perdi 20kg e ganhei muita confiança. Melhor decisão que tomei!",            "autor": "Juliana Costa",  "cargo": "Aluna Premium"},
            {"texto": "A comunidade da FitPro é incrível. Tenho amigos, motivação e profissionais que realmente se importam com meu progresso. Voltaria mil vezes!",                     "autor": "Marcus Oliveira", "cargo": "Aluno Elite"},
        ],

        # ── CTA FINAL ───────────────────────────────────────────────────────
        "t2_ctaf_titulos": [{"parte1": "Comece sua transformação", "destaque": "hoje"}],
        "t2_ctaf_descs":   [{"valor": "Agende uma avaliação gratuita e conheça nossas instalações. Nossos profissionais estão prontos para ajudá-lo!"}],
        "t2_ctaf_btns":    [{"texto": "Agende Sua Avaliação", "url": "https://wa.me/5511999999999"}],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t2_footer_infos": [{"valor": "Telefone: (99) 99999-9999 | Email: contato@fitpro.com.br"}],
        "t2_footer_addrs": [{"valor": "Endereço: Av. Principal, 1234 - São Paulo, SP"}],
        "t2_footer_copys": [{"valor": "© 2025 FitPro Academia. Todos os direitos reservados. Transformando vidas através do fitness."}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t2_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t2_nome_cliente,
            "email":     st.session_state.t2_email_cliente,
            "nome_site": st.session_state.t2_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t2_nome_site}",
        },
        "cores": st.session_state.t2_cores,
        "navbar": {
            "logos": st.session_state.t2_logos,
            "links": st.session_state.t2_nav_links,
            "cta":   st.session_state.t2_nav_ctas,
        },
        "hero": {
            "titulos":    st.session_state.t2_hero_titulos,
            "subtitulos": st.session_state.t2_hero_subtitulos,
            "stats":      st.session_state.t2_hero_stats,
            "botoes":     st.session_state.t2_hero_btns,
            "imagens":    st.session_state.t2_hero_images,
        },
        "servicos": {
            "titulos":    st.session_state.t2_serv_titulos,
            "descricoes": st.session_state.t2_serv_descs,
            "cards":      st.session_state.t2_serv_cards,
        },
        "diferenciais": {
            "titulos":    st.session_state.t2_feat_titulos,
            "descricoes": st.session_state.t2_feat_descs,
            "boxes":      st.session_state.t2_feat_boxes,
        },
        "precos": {
            "titulos":    st.session_state.t2_price_titulos,
            "descricoes": st.session_state.t2_price_descs,
            "cards":      st.session_state.t2_price_cards,
        },
        "depoimentos": {
            "titulos":    st.session_state.t2_test_titulos,
            "descricoes": st.session_state.t2_test_descs,
            "cards":      st.session_state.t2_test_cards,
        },
        "cta_final": {
            "titulos":    st.session_state.t2_ctaf_titulos,
            "descricoes": st.session_state.t2_ctaf_descs,
            "botoes":     st.session_state.t2_ctaf_btns,
        },
        "footer": {
            "infos":      st.session_state.t2_footer_infos,
            "enderecos":  st.session_state.t2_footer_addrs,
            "copyright":  st.session_state.t2_footer_copys,
        },
        "observacoes": st.session_state.t2_obs,
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

            st.session_state.t2_nome_cliente = st.text_input(
                "Seu nome completo",
                value=st.session_state.t2_nome_cliente,
                key="t2_nome_cliente_inp",
                placeholder="Ex: João Silva",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t2_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t2_email_cliente,
                key="t2_email_cliente_inp",
                placeholder="Ex: joao@email.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: joaosilva, minhaclinica, fitpro2026).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t2_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t2_nome_site,
                key="t2_nome_site_inp",
                placeholder="Ex: fitpro2026  →  sttacksite.streamlit.app/?c=fitpro2026",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Cores</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t2_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t2_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t2_cor_nome_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t2_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t2_cor_val_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t2_cores) > 1 and _del_btn(f"t2_cor_del_{i}"):
                        st.session_state.t2_cores.pop(i); st.rerun()
            if _add_btn("t2_cor_add", "＋ Adicionar cor"):
                st.session_state.t2_cores.append({"nome": "Descreva onde usar esta cor", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo  *(Texto Normal | Texto em Laranja)*")
            for i, item in enumerate(st.session_state.t2_logos):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t2_logos[i]["parte1"] = st.text_input(
                        "Normal", item["parte1"], key=f"t2_logo_p1_{i}", label_visibility="collapsed",
                        placeholder="Texto normal")
                with c2:
                    st.session_state.t2_logos[i]["destaque"] = st.text_input(
                        "Destaque", item["destaque"], key=f"t2_logo_dest_{i}", label_visibility="collapsed",
                        placeholder="Texto laranja")
                with c3:
                    if len(st.session_state.t2_logos) > 1 and _del_btn(f"t2_logo_del_{i}"):
                        st.session_state.t2_logos.pop(i); st.rerun()
            if _add_btn("t2_logo_add", "＋ Adicionar logo"):
                st.session_state.t2_logos.append({"parte1": "NOVA", "destaque": "MARCA"}); st.rerun()

            st.caption("Links do menu  *(Texto exibido | Para onde leva ao clicar)*")
            for i, link in enumerate(st.session_state.t2_nav_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t2_nav_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t2_nl_txt_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t2_nav_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t2_nl_url_{i}", label_visibility="collapsed",
                        placeholder="Seção ou https://...",
                        help="Descreva a seção do site ou cole um link externo (WhatsApp, Instagram etc.)")
                with c3:
                    if len(st.session_state.t2_nav_links) > 1 and _del_btn(f"t2_nl_del_{i}"):
                        st.session_state.t2_nav_links.pop(i); st.rerun()
            if _add_btn("t2_nl_add", "＋ Adicionar link"):
                st.session_state.t2_nav_links.append({"texto": "Novo Link", "url": "seção de destino"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🔗 <strong>URLs e destinos dos botões:</strong> você pode colocar seu WhatsApp
                (<code>https://wa.me/55119XXXXXXXX</code>), Instagram, qualquer link — ou simplesmente
                descrever para qual seção o botão deve levar (ex: <em>seção de contato ao final da página</em>).
            </div>
            """, unsafe_allow_html=True)

            st.caption("Botão CTA da navbar  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t2_nav_ctas):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t2_nav_ctas[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t2_ncta_txt_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t2_nav_ctas[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t2_ncta_url_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t2_nav_ctas) > 1 and _del_btn(f"t2_ncta_del_{i}"):
                        st.session_state.t2_nav_ctas.pop(i); st.rerun()
            if _add_btn("t2_ncta_add", "＋ Adicionar CTA navbar"):
                st.session_state.t2_nav_ctas.append({"texto": "Começar", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🦸 Hero (Seção Principal)</div>', unsafe_allow_html=True)

            st.caption("Título  *(Parte 1 | Destaque laranja | Parte 2)*")
            for i, t in enumerate(st.session_state.t2_hero_titulos):
                c1, c2, c3, c4 = st.columns([3, 3, 3, 1])
                with c1:
                    st.session_state.t2_hero_titulos[i]["parte1"] = st.text_input(
                        "P1", t["parte1"], key=f"t2_ht_p1_{i}", label_visibility="collapsed",
                        placeholder="Texto normal")
                with c2:
                    st.session_state.t2_hero_titulos[i]["destaque"] = st.text_input(
                        "Dest", t["destaque"], key=f"t2_ht_dest_{i}", label_visibility="collapsed",
                        placeholder="Destaque laranja")
                with c3:
                    st.session_state.t2_hero_titulos[i]["parte2"] = st.text_input(
                        "P2", t["parte2"], key=f"t2_ht_p2_{i}", label_visibility="collapsed",
                        placeholder="Texto normal 2")
                with c4:
                    if len(st.session_state.t2_hero_titulos) > 1 and _del_btn(f"t2_ht_del_{i}"):
                        st.session_state.t2_hero_titulos.pop(i); st.rerun()
            if _add_btn("t2_ht_add", "＋ Adicionar título hero"):
                st.session_state.t2_hero_titulos.append({"parte1": "Texto", "destaque": "Destaque", "parte2": ""}); st.rerun()

            st.caption("Subtítulo  *(frase de apoio abaixo do título)*")
            for i, s in enumerate(st.session_state.t2_hero_subtitulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t2_hero_subtitulos[i]["valor"] = st.text_area(
                        "Sub", s["valor"], key=f"t2_hs_{i}", height=80, label_visibility="collapsed",
                        placeholder="Frase curta que explica o que você oferece")
                with c2:
                    if len(st.session_state.t2_hero_subtitulos) > 1 and _del_btn(f"t2_hs_del_{i}"):
                        st.session_state.t2_hero_subtitulos.pop(i); st.rerun()
            if _add_btn("t2_hs_add", "＋ Adicionar subtítulo"):
                st.session_state.t2_hero_subtitulos.append({"valor": "Novo subtítulo"}); st.rerun()

            st.caption("Estatísticas  *(Número | Descrição)*")
            for i, stat in enumerate(st.session_state.t2_hero_stats):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t2_hero_stats[i]["numero"] = st.text_input(
                        "Num", stat["numero"], key=f"t2_hstat_n_{i}", label_visibility="collapsed",
                        placeholder="Ex: 5.000+")
                with c2:
                    st.session_state.t2_hero_stats[i]["label"] = st.text_input(
                        "Lab", stat["label"], key=f"t2_hstat_l_{i}", label_visibility="collapsed",
                        placeholder="Ex: Alunos Ativos")
                with c3:
                    if len(st.session_state.t2_hero_stats) > 1 and _del_btn(f"t2_hstat_del_{i}"):
                        st.session_state.t2_hero_stats.pop(i); st.rerun()
            if _add_btn("t2_hstat_add", "＋ Adicionar estatística"):
                st.session_state.t2_hero_stats.append({"numero": "0", "label": "Novo dado"}); st.rerun()

            st.caption("Botão principal  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t2_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t2_hero_btns[i]["texto"] = st.text_input(
                        "Txt", btn["texto"], key=f"t2_hbtn_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t2_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t2_hbtn_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t2_hero_btns) > 1 and _del_btn(f"t2_hbtn_del_{i}"):
                        st.session_state.t2_hero_btns.pop(i); st.rerun()
            if _add_btn("t2_hbtn_add", "＋ Adicionar botão hero"):
                st.session_state.t2_hero_btns.append({"texto": "Saiba Mais", "url": ""}); st.rerun()

            st.caption("Emoji/Ícone do hero  *(bloco laranja à direita do título)*")
            for i, img in enumerate(st.session_state.t2_hero_images):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t2_hero_images[i]["emoji"] = st.text_input(
                        "Emoji", img["emoji"], key=f"t2_himg_{i}", label_visibility="collapsed",
                        help="Cole um emoji aqui, ex: 🏋️ 🏆 💪")
                with c2:
                    if len(st.session_state.t2_hero_images) > 1 and _del_btn(f"t2_himg_del_{i}"):
                        st.session_state.t2_hero_images.pop(i); st.rerun()
            if _add_btn("t2_himg_add", "＋ Adicionar emoji"):
                st.session_state.t2_hero_images.append({"emoji": "🏆"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. SERVIÇOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏋️ Serviços</div>', unsafe_allow_html=True)

            st.caption("Título da seção  *(Texto Normal | Destaque laranja)*")
            for i, t in enumerate(st.session_state.t2_serv_titulos):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t2_serv_titulos[i]["parte1"] = st.text_input(
                        "P1", t["parte1"], key=f"t2_st_p1_{i}", label_visibility="collapsed",
                        placeholder="Texto normal")
                with c2:
                    st.session_state.t2_serv_titulos[i]["destaque"] = st.text_input(
                        "Dest", t["destaque"], key=f"t2_st_dest_{i}", label_visibility="collapsed",
                        placeholder="Destaque")
                with c3:
                    if len(st.session_state.t2_serv_titulos) > 1 and _del_btn(f"t2_st_del_{i}"):
                        st.session_state.t2_serv_titulos.pop(i); st.rerun()
            if _add_btn("t2_st_add", "＋ Adicionar título"):
                st.session_state.t2_serv_titulos.append({"parte1": "Nossos", "destaque": "Serviços"}); st.rerun()

            st.caption("Subtítulo da seção")
            for i, desc in enumerate(st.session_state.t2_serv_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t2_serv_descs[i]["valor"] = st.text_area(
                        "Desc", desc["valor"], key=f"t2_sd_{i}", height=60, label_visibility="collapsed",
                        placeholder="Frase de apoio abaixo do título")
                with c2:
                    if len(st.session_state.t2_serv_descs) > 1 and _del_btn(f"t2_sd_del_{i}"):
                        st.session_state.t2_serv_descs.pop(i); st.rerun()
            if _add_btn("t2_sd_add", "＋ Adicionar subtítulo"):
                st.session_state.t2_serv_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Cards de serviço  *(clique para expandir e editar cada um)*")
            for i, card in enumerate(st.session_state.t2_serv_cards):
                with st.expander(f"Serviço {i+1}: {card['titulo']}"):
                    st.session_state.t2_serv_cards[i]["icone"] = st.text_input(
                        "Ícone/Emoji", card["icone"], key=f"t2_sc_i_{i}",
                        help="Cole um emoji, ex: 🏋️ 🧘 🥗")
                    st.session_state.t2_serv_cards[i]["titulo"] = st.text_input(
                        "Título", card["titulo"], key=f"t2_sc_t_{i}")
                    st.session_state.t2_serv_cards[i]["descricao"] = st.text_area(
                        "Descrição", card["descricao"], key=f"t2_sc_d_{i}", height=80,
                        placeholder="Descreva este serviço. Para negrito, itálico etc. use as Observações.")
                    if len(st.session_state.t2_serv_cards) > 1:
                        if st.button("🗑 Remover este serviço", key=f"t2_sc_del_{i}"):
                            st.session_state.t2_serv_cards.pop(i); st.rerun()
            if _add_btn("t2_sc_add", "＋ Adicionar card de serviço"):
                st.session_state.t2_serv_cards.append({"icone": "✨", "titulo": "Novo Serviço", "descricao": "Descrição aqui"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. DIFERENCIAIS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🌟 Diferenciais</div>', unsafe_allow_html=True)

            st.caption("Título da seção  *(Texto Normal | Destaque laranja)*")
            for i, t in enumerate(st.session_state.t2_feat_titulos):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t2_feat_titulos[i]["parte1"] = st.text_input(
                        "P1", t["parte1"], key=f"t2_ft_p1_{i}", label_visibility="collapsed",
                        placeholder="Texto normal")
                with c2:
                    st.session_state.t2_feat_titulos[i]["destaque"] = st.text_input(
                        "Dest", t["destaque"], key=f"t2_ft_dest_{i}", label_visibility="collapsed",
                        placeholder="Destaque")
                with c3:
                    if len(st.session_state.t2_feat_titulos) > 1 and _del_btn(f"t2_ft_del_{i}"):
                        st.session_state.t2_feat_titulos.pop(i); st.rerun()
            if _add_btn("t2_ft_add", "＋ Adicionar título"):
                st.session_state.t2_feat_titulos.append({"parte1": "Por que", "destaque": "Nós"}); st.rerun()

            st.caption("Subtítulo da seção")
            for i, desc in enumerate(st.session_state.t2_feat_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t2_feat_descs[i]["valor"] = st.text_area(
                        "Desc", desc["valor"], key=f"t2_fd_{i}", height=60, label_visibility="collapsed",
                        placeholder="Frase de apoio")
                with c2:
                    if len(st.session_state.t2_feat_descs) > 1 and _del_btn(f"t2_fd_del_{i}"):
                        st.session_state.t2_feat_descs.pop(i); st.rerun()
            if _add_btn("t2_fd_add", "＋ Adicionar subtítulo"):
                st.session_state.t2_feat_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Boxes de diferencial  *(clique para expandir e editar cada um)*")
            for i, box in enumerate(st.session_state.t2_feat_boxes):
                with st.expander(f"Diferencial {i+1}: {box['titulo']}"):
                    st.session_state.t2_feat_boxes[i]["titulo"] = st.text_input(
                        "Título", box["titulo"], key=f"t2_fb_t_{i}")
                    st.session_state.t2_feat_boxes[i]["descricao"] = st.text_area(
                        "Descrição", box["descricao"], key=f"t2_fb_d_{i}", height=80,
                        placeholder="Explique este diferencial. Para formatação especial, use as Observações.")
                    if len(st.session_state.t2_feat_boxes) > 1:
                        if st.button("🗑 Remover este diferencial", key=f"t2_fb_del_{i}"):
                            st.session_state.t2_feat_boxes.pop(i); st.rerun()
            if _add_btn("t2_fb_add", "＋ Adicionar diferencial"):
                st.session_state.t2_feat_boxes.append({"titulo": "Novo Diferencial", "descricao": "Explique aqui"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. PREÇOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💰 Planos e Preços</div>', unsafe_allow_html=True)

            st.caption("Título da seção  *(Texto Normal | Destaque laranja)*")
            for i, t in enumerate(st.session_state.t2_price_titulos):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t2_price_titulos[i]["parte1"] = st.text_input(
                        "P1", t["parte1"], key=f"t2_pt_p1_{i}", label_visibility="collapsed",
                        placeholder="Texto normal")
                with c2:
                    st.session_state.t2_price_titulos[i]["destaque"] = st.text_input(
                        "Dest", t["destaque"], key=f"t2_pt_dest_{i}", label_visibility="collapsed",
                        placeholder="Destaque")
                with c3:
                    if len(st.session_state.t2_price_titulos) > 1 and _del_btn(f"t2_pt_del_{i}"):
                        st.session_state.t2_price_titulos.pop(i); st.rerun()
            if _add_btn("t2_pt_add", "＋ Adicionar título"):
                st.session_state.t2_price_titulos.append({"parte1": "Planos e", "destaque": "Preços"}); st.rerun()

            st.caption("Subtítulo da seção")
            for i, desc in enumerate(st.session_state.t2_price_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t2_price_descs[i]["valor"] = st.text_area(
                        "Desc", desc["valor"], key=f"t2_pd_{i}", height=60, label_visibility="collapsed",
                        placeholder="Frase de apoio")
                with c2:
                    if len(st.session_state.t2_price_descs) > 1 and _del_btn(f"t2_pd_del_{i}"):
                        st.session_state.t2_price_descs.pop(i); st.rerun()
            if _add_btn("t2_pd_add", "＋ Adicionar subtítulo"):
                st.session_state.t2_price_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Cards de plano  *(clique para expandir e editar cada um)*")
            for i, card in enumerate(st.session_state.t2_price_cards):
                with st.expander(f"Plano: {card['titulo']}"):
                    st.session_state.t2_price_cards[i]["titulo"] = st.text_input(
                        "Nome do Plano", card["titulo"], key=f"t2_pc_t_{i}")
                    st.session_state.t2_price_cards[i]["preco"] = st.text_input(
                        "Preço", card["preco"], key=f"t2_pc_p_{i}",
                        placeholder="Ex: R$ 99")
                    st.session_state.t2_price_cards[i]["periodo"] = st.text_input(
                        "Período", card["periodo"], key=f"t2_pc_per_{i}",
                        placeholder="Ex: Por mês, Por ano")
                    st.session_state.t2_price_cards[i]["features"] = st.text_area(
                        "Vantagens (uma por linha)", card["features"], key=f"t2_pc_f_{i}", height=100,
                        placeholder="Acesso à academia\nAulas em grupo\nPersonal trainer")
                    st.session_state.t2_price_cards[i]["btn_txt"] = st.text_input(
                        "Texto do Botão", card["btn_txt"], key=f"t2_pc_bt_{i}")
                    st.session_state.t2_price_cards[i]["url"] = st.text_input(
                        "Link do Botão", card["url"], key=f"t2_pc_u_{i}",
                        placeholder="https:// ou seção de destino",
                        help="Pode ser seu WhatsApp, link de pagamento, ou qualquer URL.")
                    if len(st.session_state.t2_price_cards) > 1:
                        if st.button("🗑 Remover este plano", key=f"t2_pc_del_{i}"):
                            st.session_state.t2_price_cards.pop(i); st.rerun()
            if _add_btn("t2_pc_add", "＋ Adicionar plano"):
                st.session_state.t2_price_cards.append({"titulo": "Novo Plano", "preco": "R$ 0", "periodo": "mês", "features": "Vantagem 1", "btn_txt": "Assinar", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. DEPOIMENTOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💬 Depoimentos</div>', unsafe_allow_html=True)

            st.caption("Título da seção  *(Texto Normal | Destaque laranja)*")
            for i, t in enumerate(st.session_state.t2_test_titulos):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t2_test_titulos[i]["parte1"] = st.text_input(
                        "P1", t["parte1"], key=f"t2_tt_p1_{i}", label_visibility="collapsed",
                        placeholder="Texto normal")
                with c2:
                    st.session_state.t2_test_titulos[i]["destaque"] = st.text_input(
                        "Dest", t["destaque"], key=f"t2_tt_dest_{i}", label_visibility="collapsed",
                        placeholder="Destaque")
                with c3:
                    if len(st.session_state.t2_test_titulos) > 1 and _del_btn(f"t2_tt_del_{i}"):
                        st.session_state.t2_test_titulos.pop(i); st.rerun()
            if _add_btn("t2_tt_add", "＋ Adicionar título"):
                st.session_state.t2_test_titulos.append({"parte1": "Histórias de", "destaque": "Sucesso"}); st.rerun()

            st.caption("Subtítulo da seção")
            for i, desc in enumerate(st.session_state.t2_test_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t2_test_descs[i]["valor"] = st.text_area(
                        "Desc", desc["valor"], key=f"t2_td_{i}", height=60, label_visibility="collapsed",
                        placeholder="Frase de apoio")
                with c2:
                    if len(st.session_state.t2_test_descs) > 1 and _del_btn(f"t2_td_del_{i}"):
                        st.session_state.t2_test_descs.pop(i); st.rerun()
            if _add_btn("t2_td_add", "＋ Adicionar subtítulo"):
                st.session_state.t2_test_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Depoimentos  *(clique para expandir e editar cada um)*")
            for i, test in enumerate(st.session_state.t2_test_cards):
                with st.expander(f"Depoimento de {test['autor']}"):
                    st.session_state.t2_test_cards[i]["texto"] = st.text_area(
                        "Texto do depoimento", test["texto"], key=f"t2_tc_x_{i}", height=80,
                        placeholder="Cole aqui o texto do depoimento, sem aspas.")
                    st.session_state.t2_test_cards[i]["autor"] = st.text_input(
                        "Nome do autor", test["autor"], key=f"t2_tc_a_{i}",
                        placeholder="Ex: Maria Silva")
                    st.session_state.t2_test_cards[i]["cargo"] = st.text_input(
                        "Cargo ou descrição", test["cargo"], key=f"t2_tc_c_{i}",
                        placeholder="Ex: Aluna Premium, Cliente há 2 anos")
                    if len(st.session_state.t2_test_cards) > 1:
                        if st.button("🗑 Remover este depoimento", key=f"t2_tc_del_{i}"):
                            st.session_state.t2_test_cards.pop(i); st.rerun()
            if _add_btn("t2_tc_add", "＋ Adicionar depoimento"):
                st.session_state.t2_test_cards.append({"texto": "Excelente!", "autor": "Nome", "cargo": "Cliente"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. CTA FINAL
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📢 Chamada Final</div>', unsafe_allow_html=True)

            st.caption("Título  *(Texto Normal | Destaque laranja)*")
            for i, t in enumerate(st.session_state.t2_ctaf_titulos):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t2_ctaf_titulos[i]["parte1"] = st.text_input(
                        "P1", t["parte1"], key=f"t2_ctaft_p1_{i}", label_visibility="collapsed",
                        placeholder="Texto normal")
                with c2:
                    st.session_state.t2_ctaf_titulos[i]["destaque"] = st.text_input(
                        "Dest", t["destaque"], key=f"t2_ctaft_d_{i}", label_visibility="collapsed",
                        placeholder="Destaque")
                with c3:
                    if len(st.session_state.t2_ctaf_titulos) > 1 and _del_btn(f"t2_ctaft_del_{i}"):
                        st.session_state.t2_ctaf_titulos.pop(i); st.rerun()
            if _add_btn("t2_ctaft_add", "＋ Adicionar título"):
                st.session_state.t2_ctaf_titulos.append({"parte1": "Texto", "destaque": "Destaque"}); st.rerun()

            st.caption("Descrição")
            for i, desc in enumerate(st.session_state.t2_ctaf_descs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t2_ctaf_descs[i]["valor"] = st.text_area(
                        "Desc", desc["valor"], key=f"t2_ctafd_{i}", height=80, label_visibility="collapsed",
                        placeholder="Frase de encerramento e chamada para ação")
                with c2:
                    if len(st.session_state.t2_ctaf_descs) > 1 and _del_btn(f"t2_ctafd_del_{i}"):
                        st.session_state.t2_ctaf_descs.pop(i); st.rerun()
            if _add_btn("t2_ctafd_add", "＋ Adicionar descrição"):
                st.session_state.t2_ctaf_descs.append({"valor": "Nova descrição"}); st.rerun()

            st.caption("Botão  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t2_ctaf_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t2_ctaf_btns[i]["texto"] = st.text_input(
                        "Txt", btn["texto"], key=f"t2_ctafb_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t2_ctaf_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t2_ctafb_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t2_ctaf_btns) > 1 and _del_btn(f"t2_ctafb_del_{i}"):
                        st.session_state.t2_ctaf_btns.pop(i); st.rerun()
            if _add_btn("t2_ctafb_add", "＋ Adicionar botão"):
                st.session_state.t2_ctaf_btns.append({"texto": "Saiba Mais", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 9. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">👣 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Infos de contato  *(telefone, e-mail etc.)*")
            for i, info in enumerate(st.session_state.t2_footer_infos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t2_footer_infos[i]["valor"] = st.text_input(
                        "Contato", info["valor"], key=f"t2_fi_{i}", label_visibility="collapsed",
                        placeholder="Ex: Telefone: (11) 99999-9999 | Email: contato@suaempresa.com.br")
                with c2:
                    if len(st.session_state.t2_footer_infos) > 1 and _del_btn(f"t2_fi_del_{i}"):
                        st.session_state.t2_footer_infos.pop(i); st.rerun()
            if _add_btn("t2_fi_add", "＋ Adicionar info contato"):
                st.session_state.t2_footer_infos.append({"valor": "Nova informação"}); st.rerun()

            st.caption("Endereço")
            for i, addr in enumerate(st.session_state.t2_footer_addrs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t2_footer_addrs[i]["valor"] = st.text_input(
                        "Endereço", addr["valor"], key=f"t2_fa_{i}", label_visibility="collapsed",
                        placeholder="Ex: Rua das Flores, 100 - São Paulo, SP")
                with c2:
                    if len(st.session_state.t2_footer_addrs) > 1 and _del_btn(f"t2_fa_del_{i}"):
                        st.session_state.t2_footer_addrs.pop(i); st.rerun()
            if _add_btn("t2_fa_add", "＋ Adicionar endereço"):
                st.session_state.t2_footer_addrs.append({"valor": "Novo endereço"}); st.rerun()

            st.caption("Copyright")
            for i, copy in enumerate(st.session_state.t2_footer_copys):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t2_footer_copys[i]["valor"] = st.text_input(
                        "Copy", copy["valor"], key=f"t2_fc_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 Minha Empresa. Todos os direitos reservados.")
                with c2:
                    if len(st.session_state.t2_footer_copys) > 1 and _del_btn(f"t2_fc_del_{i}"):
                        st.session_state.t2_footer_copys.pop(i); st.rerun()
            if _add_btn("t2_fc_add", "＋ Adicionar linha"):
                st.session_state.t2_footer_copys.append({"valor": "© 2026"}); st.rerun()

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
                3. Cole essa URL no campo correspondente nas seções acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Banner / Hero: <strong>1920 × 800 px</strong><br>
                • Cards / miniaturas: <strong>600 × 400 px</strong><br>
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
            for i, obs in enumerate(st.session_state.t2_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t2_obs[i]["valor"] = st.text_area(
                        "Obs", obs["valor"], key=f"t2_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t2_obs) > 1 and _del_btn(f"t2_obs_del_{i}"):
                        st.session_state.t2_obs.pop(i); st.rerun()
            if _add_btn("t2_obs_add", "＋ Adicionar observação"):
                st.session_state.t2_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 12. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t2_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t2_email_cliente.strip() or "@" not in st.session_state.t2_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t2_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t2_send", type="primary",
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
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t2_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t2_nome_cliente}'*."
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
        page_icon="💪",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
    render()
