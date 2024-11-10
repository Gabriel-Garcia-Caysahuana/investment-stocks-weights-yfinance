import streamlit as st
st.set_page_config(
    page_title="Análisis de Inversión Bursátil",  # Título que aparecerá en la pestaña
    page_icon="📈"  # Puedes usar emojis o un enlace a un ícono personalizado
)
st.title("Apoya el Proyecto")

st.write("""
    Si encuentras útil esta aplicación y deseas contribuir para su mantenimiento y desarrollo,
    puedes realizar una donación. Tu apoyo nos ayuda a seguir mejorando y ofreciendo nuevas
    funcionalidades para el análisis de inversiones bursátiles.
    
    ¡Gracias por tu generosidad!
""")

# Botón de donación (usando PayPal como ejemplo, puedes modificarlo para Ko-fi o Buy Me a Coffee)
donation_html = """
<div style="text-align: center;">
    <form action="https://www.paypal.com/donate" method="post" target="_blank">
        <input type="hidden" name="hosted_button_id" value="9LU6XZNK9DTPJ">
        <input type="image" src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif" border="0" name="submit" alt="Donate with PayPal">
        <img alt="" border="0" src="https://www.paypal.com/en_US/i/scr/pixel.gif" width="1" height="1">
    </form>
</div>
"""

st.markdown(donation_html, unsafe_allow_html=True)


st.sidebar.title("Acerca de")
st.sidebar.info("""
👨‍💻 **Desarrollado por:** Gabriel García Caysahuana 
                
📧 **Contacto:** Proximamente
                
🌐 **GitHub:** [GabrielGarcía](https://github.com/Gabriel-Garcia-Caysahuana)  
                
🔗 **LinkedIn:** [Gabriel García Caysahuana](https://www.linkedin.com/in/gabriel-garcia-caysahuana/)

Esta aplicación fue desarrollada para ayudar a los inversionistas a analizar 
y optimizar su portafolio de acciones. Si tienes alguna pregunta o sugerencia,
¡no dudes en ponerte en contacto!
""")