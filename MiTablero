import streamlit as st
from streamlit_drawable_canvas import st_canvas
from deep_translator import GoogleTranslator

st.title("Tablero para dibujo + Traductor")

with st.sidebar:
    st.subheader("Propiedades del Tablero")

    # 🔹 NUEVA SECCIÓN: Traductor
    st.subheader("Traductor Español → Inglés")
    palabra = st.text_input("Escribe una palabra en español:")

    traduccion = ""
    if palabra:
        traduccion = GoogleTranslator(source='es', target='en').translate(palabra)
        st.success(f"Inglés: {traduccion}")

    # Canvas dimensions
    st.subheader("Dimensiones del Tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)

    # Drawing mode selector
    drawing_mode = st.selectbox(
        "Herramienta de Dibujo:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    # Stroke width slider
    stroke_width = st.slider("Selecciona el ancho de línea", 1, 30, 15)

    # Stroke color picker
    stroke_color = st.color_picker("Color de trazo", "#FFFFFF")

    # Background color
    bg_color = st.color_picker("Color de fondo", "#000000")


# 🔹 Mensaje en pantalla principal
if palabra:
    st.info(f"Dibuja esto: {traduccion}")

# Canvas
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

# 🔹 Extra: validar que sí dibujó algo
if canvas_result.json_data is not None:
    if len(canvas_result.json_data["objects"]) > 0:
        st.success("¡Dibujo realizado! 👍")
