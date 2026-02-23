import streamlit as st
import importlib

# O set_page_config DEVE ficar apenas aqui no main.py
st.set_page_config(layout="wide", page_title="Sttack Templates Hub", page_icon="🚀")

def main():
    # 1. Captura o parâmetro da URL (ex: ?t=26)
    query_params = st.query_params
    template_id = query_params.get("t", "home")

    # 2. Lógica de Navegação
    if template_id == "home":
        st.title("🚀 Bem-vindo ao Sttack Templates")
        st.markdown("""
        ### Como acessar seus templates:
        Adicione `?t=NÚMERO` ao final da URL do seu navegador.
        
        **Exemplo:**
        - Para o Template 26: `https://seusite.streamlit.app/?t=26`
        """)
        st.info("Certifique-se de que os arquivos estão nomeados como 'Template26.py' no seu GitHub.")
        
    else:
        try:
            # Tenta carregar o arquivo (ex: Template26.py)
            module_name = f"Template{template_id}"
            template_module = importlib.import_module(module_name)
            
            # Chama a função render() que está dentro do arquivo do template
            template_module.render()
            
        except ModuleNotFoundError:
            st.error(f"❌ Erro: O arquivo 'Template{template_id}.py' não foi encontrado no repositório.")
            if st.button("Voltar ao Início"):
                st.query_params.clear()
        except Exception as e:
            st.error(f"⚠️ Ocorreu um erro ao carregar o template: {e}")

if __name__ == "__main__":
    main()
