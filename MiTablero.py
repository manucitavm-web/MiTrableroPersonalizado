import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
from io import BytesIO

st.title("🎨 Tablero + Contador de letras")

with st.sidebar:
    st.subheader("🧠 Entrada de texto")

    texto = st.text_input("Escribe una palabra o frase:")

    letras = 0
    palabras = 0

    if texto:
        # 🔹 Contador
        letras = len(texto.replace(" ", ""))
        palabras = len(texto.split())

        st.write(f"🔤 Letras (sin espacios): {letras}")
        st.write(f"📝 Palabras: {palabras}")

    st.subheader("🎛️ Configuración del tablero")

    canvas_width = st.slider("Ancho", 300, 700, 500, 50)
    canvas_height = st.slider("Alto", 200, 600, 300, 50)

    drawing_mode = st.selectbox(
        "Herramienta:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    stroke_width = st.slider("Grosor de línea", 1, 30, 15)
    stroke_color = st.color_picker("Color de trazo", "#FFFFFF")
    bg_color = st.color_picker("Color de fondo", "#000000")


# 🔹 Mostrar instrucción
if texto:
    st.info(f"✏️ Dibuja esto: '{texto}' (Tiene {letras} letras)")

# 🎨 Canvas
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",
)

# 🔹 Validar si dibujó algo
if canvas_result.json_data is not None:
    if len(canvas_result.json_data["objects"]) > 0:
        st.success("¡Dibujo realizado! 👍")

# 🔹 Descargar dibujo
if canvas_result.image_data is not None:
    img = Image.fromarray(canvas_result.image_data.astype('uint8'))
    buf = BytesIO()
    img.save(buf, format="PNG")

    st.download_button(
        label="📥 Descargar dibujo",
        data=buf.getvalue(),
        file_name="mi_dibujo.png",
        mime="image/png"
    )
