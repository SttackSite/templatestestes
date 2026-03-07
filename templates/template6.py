import streamlit as st
import json
import urllib.request

# ─────────────────────────────────────────────────────────────────────────────
# CONFIGURAÇÕES FIXAS
# ─────────────────────────────────────────────────────────────────────────────
TEMPLATE_IMAGE_URL = "https://raw.githubusercontent.com/SttackSite/templatestestes/main/img6.png"
TEMPLATE_NAME      = "Template 6 — Alta Precisão (Bautz Style)"
TEMPLATE_ID        = "template_6"
RESEND_API_KEY     = st.secrets.get("RESEND_KEY", "")
DESTINO_EMAIL      = "sttacksite@gmail.com"


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init():
    defaults = {
        # ── IDENTIFICAÇÃO ────────────────────────────────────────────────────
        "t6_nome_cliente":  "",
        "t6_email_cliente": "",
        "t6_nome_site":     "",

        # ── CORES ───────────────────────────────────────────────────────────
        "t6_cores": [
            {"nome": "Cor de Destaque (Azul Técnico)", "valor": "#0047bb"},
            {"nome": "Cor de Fundo (Gray Soft)",       "valor": "#f5f5f7"},
            {"nome": "Cor do Texto (Deep Black)",      "valor": "#1a1a1a"},
        ],


        # ── HERO ────────────────────────────────────────────────────────────
        "t6_hero_mono":       [{"valor": "Codeless Architecture v2.0"}],
        "t6_hero_titulos":    [{"valor": "SITES DE ALTA PRECISÃO."}],
        "t6_hero_subtitulos": [{"valor": "Desenvolva a sua presença digital com a eficiência de um processo industrial. Templates otimizados para velocidade, conversão e autonomia total."}],
        "t6_hero_btns":       [{"texto": "CONFIGURAR AGORA", "url": "seção Catálogo de Componentes"}],

        # ── CATÁLOGO ────────────────────────────────────────────────────────
        "t6_cat_mono":    [{"valor": "// CATÁLOGO DE COMPONENTES"}],
        "t6_cat_titulos": [{"valor": "MODELOS DISPONÍVEIS"}],
        "t6_cat_items": [
            {"nome": "STRUCTURAL MINIMAL", "ref": "BTZ-01", "img": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?w=600", "desc": "Estrutura modular com 100% de pontuação no Core Web Vitals.", "btn_txt": "INSPECIONAR BTZ-01", "url": "https://wa.me/5511999999999"},
            {"nome": "DYNAMIC FLOW",       "ref": "BTZ-02", "img": "https://images.unsplash.com/photo-1497366754035-f200968a6e72?w=600", "desc": "Estrutura modular com 100% de pontuação no Core Web Vitals.", "btn_txt": "INSPECIONAR BTZ-02", "url": "https://wa.me/5511999999999"},
            {"nome": "CORPORATE CORE",     "ref": "BTZ-03", "img": "https://images.unsplash.com/photo-1497215728101-856f4ea42174?w=600", "desc": "Estrutura modular com 100% de pontuação no Core Web Vitals.", "btn_txt": "INSPECIONAR BTZ-03", "url": "https://wa.me/5511999999999"},
        ],

        # ── PROVA SOCIAL ────────────────────────────────────────────────────
        "t6_trust_label": [{"valor": "TRUSTED BY INDUSTRY LEADERS:"}],
        "t6_logos": [
            {"valor": "MATTEL"},
            {"valor": "SIEMENS"},
            {"valor": "BMW"},
            {"valor": "BASF"},
        ],

        # ── APLICAÇÕES ──────────────────────────────────────────────────────
        "t6_apps_titulo": [{"valor": "APLICAÇÕES DO SISTEMA"}],
        "t6_apps": [
            {"num": "01", "label": "AUTONOMIA",     "titulo": "Crie e customize em minutos sem depender de terceiros ou agências lentas."},
            {"num": "02", "label": "RENTABILIDADE", "titulo": "Venda sites profissionais com margem de lucro industrial para o mercado B2B."},
            {"num": "03", "label": "PERFORMANCE",   "titulo": "Aumente a conversão dos seus produtos com layouts validados por testes de stress."},
        ],

        # ── WORKFLOW ────────────────────────────────────────────────────────
        "t6_flow_titulo": [{"valor": "FLUXO DE IMPLEMENTAÇÃO"}],
        "t6_flow": [
            {"num": "01", "titulo": "AQUISIÇÃO DO MÓDULO", "desc": "Acesso imediato ao repositório de códigos fonte após a validação."},
            {"num": "02", "titulo": "ASSEMBLY (MONTAGEM)", "desc": "Substitua textos e imagens seguindo o nosso manual de diretrizes visuais."},
            {"num": "03", "titulo": "DEPLOYMENT",          "desc": "Conecte o seu domínio e publique o site em servidores de alta velocidade."},
            {"num": "04", "titulo": "OPERAÇÃO",            "desc": "Seu site está pronto para gerar resultados com manutenção zero."},
        ],

        # ── PLANOS ──────────────────────────────────────────────────────────
        "t6_planos_titulo": [{"valor": "PLANOS DE ACESSO"}],
        "t6_planos": [
            {"nome": "BASIC UNIT", "valor": "R$ 97",  "features": "1 Template Modular\nManual de Montagem",                           "btn_txt": "ADQUIRIR BASIC",      "url": "https://wa.me/5511999999999", "destaque": False},
            {"nome": "FULL STACK", "valor": "R$ 197", "features": "Todos os Templates\nSuporte Técnico Direto\nUpdates de Engenharia", "btn_txt": "ADQUIRIR FULL",       "url": "https://wa.me/5511999999999", "destaque": True},
            {"nome": "ENTERPRISE", "valor": "R$ 497", "features": "Licença Comercial\nWhitelabel Ready\nConsultoria de Deploy",       "btn_txt": "ADQUIRIR ENTERPRISE", "url": "https://wa.me/5511999999999", "destaque": False},
        ],

        # ── FAQ ─────────────────────────────────────────────────────────────
        "t6_faqs": [
            {"pergunta": "O CÓDIGO É OTIMIZADO PARA SEO?",   "resposta": "Sim, todos os modelos seguem a semântica correta de HTML5 para máxima indexação."},
            {"pergunta": "POSSO ALTERAR AS CORES E FONTES?",  "resposta": "Absolutamente. O sistema é modular e permite alterações rápidas no ficheiro de estilos."},
        ],

        # ── FOOTER ──────────────────────────────────────────────────────────
        "t6_footer_left":   [{"valor": "SITE PRO / ENGINEERING DIVISION"}],
        "t6_footer_center": [{"valor": "© 2026 ALL RIGHTS RESERVED"}],
        "t6_footer_right":  [{"valor": "BUILD_V.4.0.1"}],

        # ── OBSERVAÇÕES ─────────────────────────────────────────────────────
        "t6_obs": [{"valor": ""}],
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
            "nome":      st.session_state.t6_nome_cliente,
            "email":     st.session_state.t6_email_cliente,
            "nome_site": st.session_state.t6_nome_site,
            "url_final": f"https://sttacksite.streamlit.app/?c={st.session_state.t6_nome_site}",
        },
        "cores": st.session_state.t6_cores,
        "navbar": {
            "logo":  st.session_state.t6_navbar_logo,
            "links": st.session_state.t6_navbar_links,
            "cta":   st.session_state.t6_navbar_cta,
        },
        "hero": {
            "mono":       st.session_state.t6_hero_mono,
            "titulos":    st.session_state.t6_hero_titulos,
            "subtitulos": st.session_state.t6_hero_subtitulos,
            "botoes":     st.session_state.t6_hero_btns,
        },
        "catalogo": {
            "mono":    st.session_state.t6_cat_mono,
            "titulos": st.session_state.t6_cat_titulos,
            "itens":   st.session_state.t6_cat_items,
        },
        "prova_social": {
            "label": st.session_state.t6_trust_label,
            "logos": st.session_state.t6_logos,
        },
        "aplicacoes": {
            "titulo": st.session_state.t6_apps_titulo,
            "cards":  st.session_state.t6_apps,
        },
        "workflow": {
            "titulo": st.session_state.t6_flow_titulo,
            "passos": st.session_state.t6_flow,
        },
        "planos": {
            "titulo": st.session_state.t6_planos_titulo,
            "itens":  st.session_state.t6_planos,
        },
        "faq":    st.session_state.t6_faqs,
        "footer": {
            "esquerda": st.session_state.t6_footer_left,
            "centro":   st.session_state.t6_footer_center,
            "direita":  st.session_state.t6_footer_right,
        },
        "observacoes": st.session_state.t6_obs,
    }

def _enviar_resend(payload: dict) -> bool:
    try:
        body_html = f"<pre style='font-family:monospace;font-size:13px'>{json.dumps(payload, ensure_ascii=False, indent=2)}</pre>"
        data = json.dumps({
            "from":    "editor@sttacksite.com.br",
            "to":      [DESTINO_EMAIL],
            "subject": f"[Novo Pedido] {TEMPLATE_NAME} — {payload['identificacao']['nome']}",
            "html":    body_html,
        }).encode("utf-8")
        req = urllib.request.Request(
            "https://api.resend.com/emails",
            data=data,
            headers={
                "Authorization": f"Bearer {RESEND_API_KEY}",
                "Content-Type":  "application/json",
            },
            method="POST",
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            return resp.status in (200, 201)
    except Exception:
        return False


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

            st.session_state.t6_nome_cliente = st.text_input(
                "Seu nome completo",
                value=st.session_state.t6_nome_cliente,
                key="t6_nome_cliente_inp",
                placeholder="Ex: João Silva",
                help="Seu nome para identificarmos seu pedido.")

            st.session_state.t6_email_cliente = st.text_input(
                "Seu e-mail (mesmo e-mail de cadastro na Eduzz)",
                value=st.session_state.t6_email_cliente,
                key="t6_email_cliente_inp",
                placeholder="Ex: joao@email.com",
                help="Use o mesmo e-mail com o qual você comprou na Eduzz.")

            st.markdown("""
            <div class="info-box" style="margin-top:8px">
                🌐 <strong>Nome do seu site:</strong> seu site ficará disponível em<br>
                <code>https://sttacksite.streamlit.app/?c=<strong>seunome</strong></code><br>
                Digite abaixo o que você quer no lugar de <strong>seunome</strong>
                (sem espaços, sem acentos — ex: joaosilva, bautz2026, meusite).
            </div>
            """, unsafe_allow_html=True)

            st.session_state.t6_nome_site = st.text_input(
                "Nome desejado para a URL do site",
                value=st.session_state.t6_nome_site,
                key="t6_nome_site_inp",
                placeholder="Ex: bautz2026  →  sttacksite.streamlit.app/?c=bautz2026",
                help="Apenas letras minúsculas, números e hífens. Sem espaços.")

            # ══════════════════════════════════════════════════════════════════
            # 1. CORES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🎨 Cores Industriais</div>', unsafe_allow_html=True)
            st.caption("Clique na bolinha colorida para escolher a cor de cada elemento.")
            for i, cor in enumerate(st.session_state.t6_cores):
                c1, c2, c3 = st.columns([5, 2, 1])
                with c1:
                    st.session_state.t6_cores[i]["nome"] = st.text_input(
                        "Nome", cor["nome"], key=f"t6_cor_n_{i}", label_visibility="collapsed",
                        placeholder="Onde essa cor é usada")
                with c2:
                    st.session_state.t6_cores[i]["valor"] = st.color_picker(
                        "Cor", cor["valor"], key=f"t6_cor_v_{i}", label_visibility="collapsed")
                with c3:
                    if len(st.session_state.t6_cores) > 1 and _del_btn(f"t6_cor_del_{i}"):
                        st.session_state.t6_cores.pop(i); st.rerun()
            if _add_btn("t6_cor_add", "＋ Adicionar cor"):
                st.session_state.t6_cores.append({"nome": "Indique onde usar", "valor": "#FFFFFF"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 2. NAVBAR
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔝 Navegação (Navbar)</div>', unsafe_allow_html=True)

            st.caption("Logo / Nome da marca")
            for i, item in enumerate(st.session_state.t6_navbar_logo):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_navbar_logo[i]["valor"] = st.text_input(
                        "Logo", item["valor"], key=f"t6_logo_{i}", label_visibility="collapsed",
                        placeholder="Ex: MINHA EMPRESA")
                with c2:
                    if len(st.session_state.t6_navbar_logo) > 1 and _del_btn(f"t6_logo_del_{i}"):
                        st.session_state.t6_navbar_logo.pop(i); st.rerun()
            if _add_btn("t6_logo_add", "＋ Adicionar logo"):
                st.session_state.t6_navbar_logo.append({"valor": "NOVA MARCA"}); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                🔗 <strong>URLs e destinos dos botões:</strong> você pode colocar seu WhatsApp
                (<code>https://wa.me/55119XXXXXXXX</code>), Instagram, qualquer link — ou simplesmente
                descrever para qual seção o botão deve levar (ex: <em>seção de contato ao final da página</em>).
            </div>
            """, unsafe_allow_html=True)

            st.caption("Links do menu  *(Texto | Destino ou URL)*")
            for i, link in enumerate(st.session_state.t6_navbar_links):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t6_navbar_links[i]["texto"] = st.text_input(
                        "Texto", link["texto"], key=f"t6_nl_txt_{i}", label_visibility="collapsed",
                        placeholder="Texto do link")
                with c2:
                    st.session_state.t6_navbar_links[i]["url"] = st.text_input(
                        "Destino", link["url"], key=f"t6_nl_url_{i}", label_visibility="collapsed",
                        placeholder="Seção ou https://...")
                with c3:
                    if len(st.session_state.t6_navbar_links) > 1 and _del_btn(f"t6_nl_del_{i}"):
                        st.session_state.t6_navbar_links.pop(i); st.rerun()
            if _add_btn("t6_nl_add", "＋ Adicionar link ao menu"):
                st.session_state.t6_navbar_links.append({"texto": "Link", "url": "seção de destino"}); st.rerun()

            st.caption("Botão CTA da Navbar  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t6_navbar_cta):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t6_navbar_cta[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t6_ncta_txt_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t6_navbar_cta[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t6_ncta_url_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t6_navbar_cta) > 1 and _del_btn(f"t6_ncta_del_{i}"):
                        st.session_state.t6_navbar_cta.pop(i); st.rerun()
            if _add_btn("t6_ncta_add", "＋ Adicionar botão CTA"):
                st.session_state.t6_navbar_cta.append({"texto": "NOVO CTA", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 3. HERO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🏗️ Hero (Seção Principal)</div>', unsafe_allow_html=True)

            st.caption("Label Mono  *(texto pequeno técnico acima do título)*")
            for i, m in enumerate(st.session_state.t6_hero_mono):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_hero_mono[i]["valor"] = st.text_input(
                        "Mono Label", m["valor"], key=f"t6_h_m_{i}", label_visibility="collapsed",
                        placeholder="Ex: Codeless Architecture v2.0")
                with c2:
                    if len(st.session_state.t6_hero_mono) > 1 and _del_btn(f"t6_h_m_del_{i}"):
                        st.session_state.t6_hero_mono.pop(i); st.rerun()
            if _add_btn("t6_h_m_add", "＋ Adicionar label mono"):
                st.session_state.t6_hero_mono.append({"valor": "Novo Label"}); st.rerun()

            st.caption("Título  *(para quebrar linha, descreva nas Observações)*")
            for i, t in enumerate(st.session_state.t6_hero_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_hero_titulos[i]["valor"] = st.text_area(
                        "Título", t["valor"], key=f"t6_h_t_{i}", height=70,
                        label_visibility="collapsed",
                        placeholder="Título principal em maiúsculas")
                with c2:
                    if len(st.session_state.t6_hero_titulos) > 1 and _del_btn(f"t6_h_t_del_{i}"):
                        st.session_state.t6_hero_titulos.pop(i); st.rerun()
            if _add_btn("t6_h_t_add", "＋ Adicionar título"):
                st.session_state.t6_hero_titulos.append({"valor": "NOVO TÍTULO"}); st.rerun()

            st.caption("Subtítulo  *(frase descritiva abaixo do título)*")
            for i, s in enumerate(st.session_state.t6_hero_subtitulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_hero_subtitulos[i]["valor"] = st.text_area(
                        "Subtítulo", s["valor"], key=f"t6_h_s_{i}", height=80,
                        label_visibility="collapsed",
                        placeholder="Frase que explica o que você oferece")
                with c2:
                    if len(st.session_state.t6_hero_subtitulos) > 1 and _del_btn(f"t6_h_s_del_{i}"):
                        st.session_state.t6_hero_subtitulos.pop(i); st.rerun()
            if _add_btn("t6_h_s_add", "＋ Adicionar subtítulo"):
                st.session_state.t6_hero_subtitulos.append({"valor": "Novo subtítulo"}); st.rerun()

            st.caption("Botões do Hero  *(Texto | URL ou destino)*")
            for i, btn in enumerate(st.session_state.t6_hero_btns):
                c1, c2, c3 = st.columns([4, 4, 1])
                with c1:
                    st.session_state.t6_hero_btns[i]["texto"] = st.text_input(
                        "Texto", btn["texto"], key=f"t6_h_btn_t_{i}", label_visibility="collapsed",
                        placeholder="Texto do botão")
                with c2:
                    st.session_state.t6_hero_btns[i]["url"] = st.text_input(
                        "URL", btn["url"], key=f"t6_h_btn_u_{i}", label_visibility="collapsed",
                        placeholder="https:// ou seção")
                with c3:
                    if len(st.session_state.t6_hero_btns) > 1 and _del_btn(f"t6_h_btn_del_{i}"):
                        st.session_state.t6_hero_btns.pop(i); st.rerun()
            if _add_btn("t6_h_btn_add", "＋ Adicionar botão ao hero"):
                st.session_state.t6_hero_btns.append({"texto": "NOVO BOTÃO", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 4. CATÁLOGO
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">📦 Catálogo de Componentes</div>', unsafe_allow_html=True)

            st.caption("Label Mono da seção")
            for i, m in enumerate(st.session_state.t6_cat_mono):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_cat_mono[i]["valor"] = st.text_input(
                        "Mono", m["valor"], key=f"t6_cat_m_{i}", label_visibility="collapsed",
                        placeholder="Ex: // CATÁLOGO DE COMPONENTES")
                with c2:
                    if len(st.session_state.t6_cat_mono) > 1 and _del_btn(f"t6_cat_m_del_{i}"):
                        st.session_state.t6_cat_mono.pop(i); st.rerun()

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t6_cat_titulos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_cat_titulos[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t6_cat_t_{i}", label_visibility="collapsed",
                        placeholder="Ex: MODELOS DISPONÍVEIS")
                with c2:
                    if len(st.session_state.t6_cat_titulos) > 1 and _del_btn(f"t6_cat_t_del_{i}"):
                        st.session_state.t6_cat_titulos.pop(i); st.rerun()

            st.markdown("""
            <div class="info-box" style="margin:4px 0 8px">
                📸 <strong>Imagens dos cards:</strong> cole a URL de uma imagem do
                <a href="https://imgur.com" target="_blank">imgur.com</a> no campo URL da Imagem.
                Tamanho recomendado: <strong>600 × 400 px</strong>.
            </div>
            """, unsafe_allow_html=True)

            st.caption("Itens do catálogo  *(clique para expandir e editar cada um)*")
            for i, item in enumerate(st.session_state.t6_cat_items):
                with st.expander(f"Modelo {i+1}: {item['nome']}"):
                    st.session_state.t6_cat_items[i]["nome"] = st.text_input(
                        "Nome do Modelo", item["nome"], key=f"t6_ci_n_{i}",
                        placeholder="Nome em maiúsculas")
                    st.session_state.t6_cat_items[i]["ref"] = st.text_input(
                        "REF (Código de referência)", item["ref"], key=f"t6_ci_r_{i}",
                        placeholder="Ex: BTZ-01")
                    st.session_state.t6_cat_items[i]["img"] = st.text_input(
                        "URL da Imagem", item["img"], key=f"t6_ci_i_{i}",
                        placeholder="https://i.imgur.com/... ou deixe vazio",
                        help="Cole a URL da imagem do imgur.com")
                    st.session_state.t6_cat_items[i]["desc"] = st.text_area(
                        "Descrição", item["desc"], key=f"t6_ci_d_{i}", height=70,
                        placeholder="Descreva este modelo brevemente")
                    st.session_state.t6_cat_items[i]["btn_txt"] = st.text_input(
                        "Texto do Botão", item["btn_txt"], key=f"t6_ci_bt_{i}")
                    st.session_state.t6_cat_items[i]["url"] = st.text_input(
                        "URL do Botão", item["url"], key=f"t6_ci_u_{i}",
                        placeholder="https:// ou seção de destino")
                    if len(st.session_state.t6_cat_items) > 1:
                        if st.button("🗑 Remover este modelo", key=f"t6_ci_del_{i}"):
                            st.session_state.t6_cat_items.pop(i); st.rerun()
            if _add_btn("t6_ci_add", "＋ Adicionar modelo ao catálogo"):
                st.session_state.t6_cat_items.append({
                    "nome": "NOVO MODELO", "ref": "BTZ-00", "img": "",
                    "desc": "Descrição do modelo.", "btn_txt": "INSPECIONAR BTZ-00", "url": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 5. PROVA SOCIAL
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🤝 Prova Social (Marcas de Confiança)</div>', unsafe_allow_html=True)

            st.caption("Label da faixa  *(texto que aparece antes das marcas)*")
            for i, item in enumerate(st.session_state.t6_trust_label):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_trust_label[i]["valor"] = st.text_input(
                        "Label", item["valor"], key=f"t6_tl_{i}", label_visibility="collapsed",
                        placeholder="Ex: TRUSTED BY INDUSTRY LEADERS:")
                with c2:
                    if len(st.session_state.t6_trust_label) > 1 and _del_btn(f"t6_tl_del_{i}"):
                        st.session_state.t6_trust_label.pop(i); st.rerun()

            st.caption("Marcas / nomes de clientes  *(exibidos em texto)*")
            for i, logo in enumerate(st.session_state.t6_logos):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_logos[i]["valor"] = st.text_input(
                        "Marca", logo["valor"], key=f"t6_l_v_{i}", label_visibility="collapsed",
                        placeholder="Ex: NOME DA EMPRESA")
                with c2:
                    if len(st.session_state.t6_logos) > 1 and _del_btn(f"t6_l_del_{i}"):
                        st.session_state.t6_logos.pop(i); st.rerun()
            if _add_btn("t6_l_add", "＋ Adicionar marca"):
                st.session_state.t6_logos.append({"valor": "NOVA MARCA"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 6. APLICAÇÕES
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🛠️ Aplicações do Sistema</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t6_apps_titulo):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_apps_titulo[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t6_at_{i}", label_visibility="collapsed",
                        placeholder="Ex: APLICAÇÕES DO SISTEMA")
                with c2:
                    if len(st.session_state.t6_apps_titulo) > 1 and _del_btn(f"t6_at_del_{i}"):
                        st.session_state.t6_apps_titulo.pop(i); st.rerun()

            st.caption("Cards  *(clique para expandir e editar cada um)*")
            for i, app in enumerate(st.session_state.t6_apps):
                with st.expander(f"Card {app['num']}: {app['label']}"):
                    st.session_state.t6_apps[i]["num"] = st.text_input(
                        "Número", app["num"], key=f"t6_a_n_{i}",
                        placeholder="Ex: 01, 02, 03")
                    st.session_state.t6_apps[i]["label"] = st.text_input(
                        "Rótulo", app["label"], key=f"t6_a_l_{i}",
                        placeholder="Ex: AUTONOMIA")
                    st.session_state.t6_apps[i]["titulo"] = st.text_area(
                        "Descrição", app["titulo"], key=f"t6_a_t_{i}", height=70,
                        placeholder="Descreva esta aplicação ou benefício")
                    if len(st.session_state.t6_apps) > 1:
                        if st.button("🗑 Remover este card", key=f"t6_a_del_{i}"):
                            st.session_state.t6_apps.pop(i); st.rerun()
            if _add_btn("t6_a_add", "＋ Adicionar card de aplicação"):
                st.session_state.t6_apps.append({"num": "04", "label": "NOVO", "titulo": "Descrição da aplicação."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 7. WORKFLOW
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">⚙️ Fluxo de Implementação</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t6_flow_titulo):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_flow_titulo[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t6_ft_{i}", label_visibility="collapsed",
                        placeholder="Ex: FLUXO DE IMPLEMENTAÇÃO")
                with c2:
                    if len(st.session_state.t6_flow_titulo) > 1 and _del_btn(f"t6_ft_del_{i}"):
                        st.session_state.t6_flow_titulo.pop(i); st.rerun()

            st.caption("Passos  *(clique para expandir e editar cada um)*")
            for i, flow in enumerate(st.session_state.t6_flow):
                with st.expander(f"Passo {flow['num']}: {flow['titulo']}"):
                    st.session_state.t6_flow[i]["num"] = st.text_input(
                        "Número", flow["num"], key=f"t6_f_n_{i}",
                        placeholder="Ex: 01, 02...")
                    st.session_state.t6_flow[i]["titulo"] = st.text_input(
                        "Título", flow["titulo"], key=f"t6_f_t_{i}")
                    st.session_state.t6_flow[i]["desc"] = st.text_area(
                        "Descrição", flow["desc"], key=f"t6_f_d_{i}", height=70,
                        placeholder="Explique o que acontece neste passo")
                    if len(st.session_state.t6_flow) > 1:
                        if st.button("🗑 Remover este passo", key=f"t6_f_del_{i}"):
                            st.session_state.t6_flow.pop(i); st.rerun()
            if _add_btn("t6_f_add", "＋ Adicionar passo ao workflow"):
                st.session_state.t6_flow.append({"num": "05", "titulo": "NOVO PASSO", "desc": "Descrição do passo."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 8. PLANOS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">💰 Planos de Acesso</div>', unsafe_allow_html=True)

            st.caption("Título da seção")
            for i, t in enumerate(st.session_state.t6_planos_titulo):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_planos_titulo[i]["valor"] = st.text_input(
                        "Título", t["valor"], key=f"t6_pt_{i}", label_visibility="collapsed",
                        placeholder="Ex: PLANOS DE ACESSO")
                with c2:
                    if len(st.session_state.t6_planos_titulo) > 1 and _del_btn(f"t6_pt_del_{i}"):
                        st.session_state.t6_planos_titulo.pop(i); st.rerun()

            st.caption("Planos  *(clique para expandir e editar cada um)*")
            for i, plano in enumerate(st.session_state.t6_planos):
                with st.expander(f"Plano: {plano['nome']}"):
                    st.session_state.t6_planos[i]["nome"] = st.text_input(
                        "Nome do Plano", plano["nome"], key=f"t6_p_n_{i}")
                    st.session_state.t6_planos[i]["valor"] = st.text_input(
                        "Preço", plano["valor"], key=f"t6_p_v_{i}",
                        placeholder="Ex: R$ 197")
                    st.session_state.t6_planos[i]["features"] = st.text_area(
                        "Vantagens (uma por linha)", plano["features"], key=f"t6_p_f_{i}", height=100,
                        placeholder="Feature 1\nFeature 2\nFeature 3")
                    st.session_state.t6_planos[i]["btn_txt"] = st.text_input(
                        "Texto do Botão", plano["btn_txt"], key=f"t6_p_bt_{i}")
                    st.session_state.t6_planos[i]["url"] = st.text_input(
                        "URL do Botão", plano["url"], key=f"t6_p_u_{i}",
                        placeholder="https:// ou seção de destino",
                        help="Pode ser link de pagamento, WhatsApp etc.")
                    st.session_state.t6_planos[i]["destaque"] = st.checkbox(
                        "Destaque (fundo escuro — plano recomendado)", value=plano["destaque"], key=f"t6_p_d_{i}")
                    if len(st.session_state.t6_planos) > 1:
                        if st.button("🗑 Remover este plano", key=f"t6_p_del_{i}"):
                            st.session_state.t6_planos.pop(i); st.rerun()
            if _add_btn("t6_p_add", "＋ Adicionar plano"):
                st.session_state.t6_planos.append({
                    "nome": "NOVO PLANO", "valor": "R$ 0", "features": "Feature 1\nFeature 2",
                    "btn_txt": "ADQUIRIR", "url": "", "destaque": False}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 9. FAQ
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">❓ FAQ</div>', unsafe_allow_html=True)
            st.caption("Perguntas e Respostas  *(clique para expandir e editar cada uma)*")
            for i, faq in enumerate(st.session_state.t6_faqs):
                with st.expander(f"FAQ {i+1}: {faq['pergunta'][:45]}..."):
                    st.session_state.t6_faqs[i]["pergunta"] = st.text_input(
                        "Pergunta", faq["pergunta"], key=f"t6_faq_p_{i}",
                        placeholder="ESCREVA A PERGUNTA EM MAIÚSCULAS")
                    st.session_state.t6_faqs[i]["resposta"] = st.text_area(
                        "Resposta", faq["resposta"], key=f"t6_faq_r_{i}", height=80,
                        placeholder="Escreva a resposta de forma clara e objetiva")
                    if len(st.session_state.t6_faqs) > 1:
                        if st.button("🗑 Remover esta pergunta", key=f"t6_faq_del_{i}"):
                            st.session_state.t6_faqs.pop(i); st.rerun()
            if _add_btn("t6_faq_add", "＋ Adicionar pergunta ao FAQ"):
                st.session_state.t6_faqs.append({"pergunta": "NOVA PERGUNTA?", "resposta": "Resposta aqui."}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 10. FOOTER
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🔻 Rodapé</div>', unsafe_allow_html=True)

            st.caption("Texto esquerdo  *(ex: nome da empresa / divisão)*")
            for i, f in enumerate(st.session_state.t6_footer_left):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_footer_left[i]["valor"] = st.text_input(
                        "Footer Esquerda", f["valor"], key=f"t6_fl_{i}", label_visibility="collapsed",
                        placeholder="Ex: MINHA EMPRESA / DIVISION")
                with c2:
                    if len(st.session_state.t6_footer_left) > 1 and _del_btn(f"t6_fl_del_{i}"):
                        st.session_state.t6_footer_left.pop(i); st.rerun()
            if _add_btn("t6_fl_add", "＋ Adicionar texto esquerdo"):
                st.session_state.t6_footer_left.append({"valor": "Novo texto"}); st.rerun()

            st.caption("Texto central  *(ex: © 2026 ALL RIGHTS RESERVED)*")
            for i, f in enumerate(st.session_state.t6_footer_center):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_footer_center[i]["valor"] = st.text_input(
                        "Footer Centro", f["valor"], key=f"t6_fc_{i}", label_visibility="collapsed",
                        placeholder="Ex: © 2026 ALL RIGHTS RESERVED")
                with c2:
                    if len(st.session_state.t6_footer_center) > 1 and _del_btn(f"t6_fc_del_{i}"):
                        st.session_state.t6_footer_center.pop(i); st.rerun()
            if _add_btn("t6_fc_add", "＋ Adicionar texto central"):
                st.session_state.t6_footer_center.append({"valor": "Novo texto"}); st.rerun()

            st.caption("Texto direito  *(ex: versão do build ou slogan técnico)*")
            for i, f in enumerate(st.session_state.t6_footer_right):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_footer_right[i]["valor"] = st.text_input(
                        "Footer Direita", f["valor"], key=f"t6_fr_{i}", label_visibility="collapsed",
                        placeholder="Ex: BUILD_V.4.0.1")
                with c2:
                    if len(st.session_state.t6_footer_right) > 1 and _del_btn(f"t6_fr_del_{i}"):
                        st.session_state.t6_footer_right.pop(i); st.rerun()
            if _add_btn("t6_fr_add", "＋ Adicionar texto direito"):
                st.session_state.t6_footer_right.append({"valor": "Novo texto"}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 11. IMAGENS
            # ══════════════════════════════════════════════════════════════════
            st.markdown('<div class="section-label">🖼️ Imagens</div>', unsafe_allow_html=True)
            st.markdown("""
            <div class="info-box">
                📸 <strong>Como adicionar imagens ao seu site:</strong><br><br>
                1. Acesse <a href="https://imgur.com" target="_blank"><strong>imgur.com</strong></a>
                   (gratuito, sem cadastro) e faça o upload da sua imagem.<br>
                2. Clique com o botão direito na imagem → <em>Copiar endereço da imagem</em> — a URL termina em
                   <code>.jpg</code>, <code>.png</code> ou <code>.webp</code>.<br>
                3. Cole essa URL no campo <em>URL da Imagem</em> dentro de cada card do Catálogo acima.<br><br>
                📐 <strong>Tamanhos recomendados:</strong><br>
                • Cards do Catálogo: <strong>600 × 400 px</strong><br>
                • Banner / Hero: <strong>1920 × 800 px</strong><br>
                • Logo: <strong>200 × 60 px</strong> (fundo transparente, formato PNG)<br><br>
                ❌ <strong>Não conseguiu subir a imagem?</strong> Envie para
                <strong>sttacksite@gmail.com</strong> com o assunto <em>"Imagem — [nome do seu site]"</em>.
            </div>
            """, unsafe_allow_html=True)

            # ══════════════════════════════════════════════════════════════════
            # 12. OBSERVAÇÕES
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
            for i, item in enumerate(st.session_state.t6_obs):
                c1, c2 = st.columns([9, 1])
                with c1:
                    st.session_state.t6_obs[i]["valor"] = st.text_area(
                        "Obs", item["valor"], key=f"t6_obs_{i}", height=90,
                        placeholder="Descreva aqui qualquer ajuste, ideia ou pedido especial...",
                        label_visibility="collapsed")
                with c2:
                    if len(st.session_state.t6_obs) > 1 and _del_btn(f"t6_obs_del_{i}"):
                        st.session_state.t6_obs.pop(i); st.rerun()
            if _add_btn("t6_obs_add", "＋ Adicionar observação"):
                st.session_state.t6_obs.append({"valor": ""}); st.rerun()

            # ══════════════════════════════════════════════════════════════════
            # 13. REVISÃO + ENVIO
            # ══════════════════════════════════════════════════════════════════
            st.markdown("---")

            with st.expander("👁 Revisar dados antes de enviar"):
                st.json(_build_json())

            erros = []
            if not st.session_state.t6_nome_cliente.strip():
                erros.append("• Preencha seu **nome completo**.")
            if not st.session_state.t6_email_cliente.strip() or "@" not in st.session_state.t6_email_cliente:
                erros.append("• Preencha um **e-mail válido** (mesmo da Eduzz).")
            if not st.session_state.t6_nome_site.strip():
                erros.append("• Preencha o **nome desejado para a URL** do site.")

            if erros:
                st.warning("⚠️ Antes de enviar, corrija os itens abaixo:\n\n" + "\n".join(erros))

            if st.button("✅ Finalizar e Enviar para a Equipe", key="t6_send", type="primary",
                         disabled=len(erros) > 0):
                payload = _build_json()
                sucesso = _enviar_resend(payload)
                if sucesso:
                    st.success(
                        "🎉 **Pedido enviado com sucesso!**\n\n"
                        "Nossa equipe já recebeu suas informações e entrará em contato assim que o site "
                        "estiver em produção. Caso surja alguma dúvida, falaremos com você pelo e-mail "
                        f"informado. 😊\n\n"
                        f"Seu site será publicado em: **https://sttacksite.streamlit.app/?c={st.session_state.t6_nome_site}**"
                    )
                    st.balloons()
                else:
                    st.warning(
                        "⚠️ Houve um problema ao enviar automaticamente. "
                        "Copie o JSON abaixo e envie para **sttacksite@gmail.com** com o assunto "
                        f"*'Pedido — {st.session_state.t6_nome_cliente}'*."
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
