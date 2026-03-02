import streamlit as st

st.set_page_config(page_title="Template 2 - Personalização", layout="wide")

st.title("🎨 Personalização do Template 2")

st.markdown("Preencha as informações abaixo para personalizar seu site.")

# =========================================================
# 1. IDENTIDADE VISUAL
# =========================================================

st.header("🔷 1. Identidade Visual")

cor_principal = st.text_input(
    "Onde aplicar a cor principal?",
    placeholder="Ex.: botões, títulos, fundo da seção principal"
)

st.caption("Informe claramente onde a cor deve ser aplicada. Caso não especifique, aplicaremos apenas nos botões principais.")

cor_secundaria = st.text_input(
    "Onde aplicar a cor secundária?",
    placeholder="Ex.: fundo do rodapé, cards de serviço"
)

st.caption("Utilize para detalhes ou áreas de contraste. Evite repetir a aplicação da cor principal.")

# =========================================================
# 2. BOTÕES
# =========================================================

st.header("🔷 2. Botões da Página")

texto_botao = st.text_input(
    "Texto do botão",
    placeholder="Ex.: Fale Conosco, Solicitar Orçamento"
)

destino_botao = st.text_input(
    "Para onde o botão leva?",
    placeholder="Ex.: contato, sobre, serviços"
)

st.caption("Informe o nome exato da seção. O botão fará rolagem automática até essa área. Para link externo, informe a URL completa (https://...).")

# =========================================================
# 3. SEÇÕES DA PÁGINA
# =========================================================

st.header("🔷 3. Seções da Página")

nome_secao = st.text_input(
    "Nome da seção",
    placeholder="Ex.: Sobre Nós"
)

conteudo_secao = st.text_area(
    "Conteúdo da seção",
    placeholder="Descreva o conteúdo desta seção"
)

st.caption("Seja objetivo e direto. Caso não envie conteúdo, a seção poderá não ser exibida.")

# =========================================================
# 4. CONTATO
# =========================================================

st.header("🔷 4. Contato")

whatsapp = st.text_input(
    "Número de WhatsApp (apenas números com DDD)",
    placeholder="11999999999"
)

st.caption("Inserir apenas números. O botão abrirá conversa automática.")

email = st.text_input(
    "E-mail profissional",
    placeholder="contato@empresa.com"
)

# =========================================================
# 5. OBSERVAÇÕES GERAIS
# =========================================================

st.header("🔷 5. Observações Gerais")

observacoes = st.text_area(
    "Alguma instrução adicional?",
    placeholder="Descreva aqui qualquer ajuste específico que deseja no site"
)

st.caption("Use este campo para solicitações fora do padrão.")

# =========================================================
# BOTÃO FINAL
# =========================================================

if st.button("🚀 Enviar Personalização"):
    st.success("Personalização enviada com sucesso!")
    st.write("Em breve iniciaremos a configuração do seu site.")
