import streamlit as st
from PIL import Image, ImageEnhance
from io import BytesIO

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="AI Image Enhancer",
    page_icon="🪄",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- CUSTOM CSS (Dark Theme with Gradient Background) ---
st.markdown("""
    <style>
        body {
            background: linear-gradient(120deg, #1e1e2f, #2b2b40);
            color: #f5f5f5;
        }
        .stApp {
            background: linear-gradient(120deg, #1e1e2f, #2b2b40);
        }
        .stSlider label, .stDownloadButton, .stFileUploader label {
            color: #f5f5f5 !important;
            font-weight: 600;
        }
        .stDownloadButton button {
            background-color: #00b894;
            color: white;
            font-size: 16px;
            border-radius: 8px;
        }
        .stDownloadButton button:hover {
            background-color: #019875;
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER ---
st.title("🪄 AI Image Enhancer")
st.caption("Enhance your photos with simple sliders — brightness, contrast, sharpness, and color adjustment.")

# --- SIDEBAR SETTINGS ---
st.sidebar.header("🎛️ Enhancement Controls")

brightness = st.sidebar.slider("🌞 Brightness", 0.5, 3.0, 1.0)
contrast = st.sidebar.slider("🌗 Contrast", 0.5, 3.0, 1.0)
sharpness = st.sidebar.slider("✨ Sharpness", 0.5, 3.0, 1.0)
color = st.sidebar.slider("🎨 Color", 0.5, 3.0, 1.0)

# --- FILE UPLOADER ---
uploaded_file = st.file_uploader("📤 Upload an image file", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Open image
    img = Image.open(uploaded_file).convert("RGB")

    # Apply enhancements
    enhanced_img = ImageEnhance.Brightness(img).enhance(brightness)
    enhanced_img = ImageEnhance.Contrast(enhanced_img).enhance(contrast)
    enhanced_img = ImageEnhance.Sharpness(enhanced_img).enhance(sharpness)
    enhanced_img = ImageEnhance.Color(enhanced_img).enhance(color)

    # --- DISPLAY SIDE-BY-SIDE ---
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🖼️ Original")
        st.image(img, use_container_width=True)
    with col2:
        st.subheader("🚀 Enhanced")
        st.image(enhanced_img, use_container_width=True)

    # --- DOWNLOAD BUTTON ---
    buf = BytesIO()
    enhanced_img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.markdown("---")
    st.subheader("📥 Download Your Enhanced Image")
    st.download_button(
        label="Download Enhanced Image 🪄",
        data=byte_im,
        file_name="enhanced_image.png",
        mime="image/png",
    )
else:
    st.info("👆 Upload an image to start enhancing.")

# --- FOOTER ---
st.markdown(
    "<hr><center>✨ Built with ❤️ using Streamlit & Pillow ✨</center>",
    unsafe_allow_html=True,
)
