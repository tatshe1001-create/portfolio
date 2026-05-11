"""
Tatjana Shevchik – Portfolio & QR-Generator
Starten mit: streamlit run app.py
Abhängigkeiten: pip install streamlit qrcode[pil] Pillow
"""

import streamlit as st
import qrcode
from PIL import Image
import io

# ── Seitenkonfiguration ──────────────────────────────────────────────────────
st.set_page_config(
    page_title="Tatjana Shevchik · Portfolio",
    page_icon="🔬",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Globale Schriften & Reset */
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@300;400&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Mono', monospace !important;
}

/* Header-Name */
.port-name {
    font-family: 'DM Serif Display', serif !important;
    font-size: 2.4rem;
    font-weight: 400;
    letter-spacing: -0.02em;
    line-height: 1.1;
    margin-bottom: 0.15rem;
}
.port-name em { color: #888; font-style: italic; }

/* Section-Label */
.section-label {
    font-size: 10px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #999;
    margin-bottom: 0.4rem;
    margin-top: 1.6rem;
    font-family: 'DM Mono', monospace;
}

/* Bio-Text */
.bio-text {
    font-size: 14px;
    line-height: 1.75;
    color: #666;
    font-weight: 300;
    font-family: 'DM Mono', monospace;
}
.bio-text strong { color: #222; font-weight: 400; }

/* Stat-Kacheln */
.stat-row { display: flex; gap: 10px; margin: 1.2rem 0 1.6rem; }
.stat-box {
    flex: 1;
    background: #f7f7f5;
    border-radius: 10px;
    padding: 14px 10px;
    text-align: center;
}
.stat-num {
    font-family: 'DM Serif Display', serif;
    font-size: 1.6rem;
    font-weight: 400;
    color: #111;
    display: block;
}
.stat-lab {
    font-size: 10px;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #999;
    font-weight: 300;
}

/* Projekt-Karte */
.proj-card {
    border: 1px solid #e8e8e4;
    border-radius: 14px;
    padding: 18px 20px;
    margin-bottom: 14px;
    background: #fff;
}
.proj-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.1rem;
    font-weight: 400;
    color: #111;
    margin-bottom: 4px;
}
.proj-meta {
    font-size: 11px;
    color: #aaa;
    letter-spacing: 0.06em;
    margin-bottom: 10px;
    font-weight: 300;
}
.proj-body {
    font-size: 13px;
    line-height: 1.75;
    color: #666;
    font-weight: 300;
    margin-bottom: 12px;
}
.proj-body strong { color: #222; font-weight: 400; }
.tag-row { display: flex; flex-wrap: wrap; gap: 6px; }
.tag {
    font-size: 10px;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    padding: 3px 9px;
    border-radius: 5px;
    border: 1px solid #e8e8e4;
    color: #888;
    font-weight: 400;
}

/* Link-Zeilen */
.link-row {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 12px 14px;
    background: #f7f7f5;
    border-radius: 10px;
    margin-bottom: 8px;
    font-size: 13px;
    color: #444;
    font-weight: 300;
}
.link-row a { color: #444; text-decoration: none; }
.link-row a:hover { color: #111; }

/* Streamlit Button überschreiben */
.stButton > button {
    font-family: 'DM Mono', monospace !important;
    font-size: 12px !important;
    font-weight: 400 !important;
    border-radius: 8px !important;
    border: 1px solid #e0e0dc !important;
    background: transparent !important;
    color: #555 !important;
    padding: 6px 16px !important;
    transition: all 0.15s !important;
    letter-spacing: 0.04em;
}
.stButton > button:hover {
    background: #f7f7f5 !important;
    border-color: #bbb !important;
    color: #111 !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 4px;
    border-bottom: 1px solid #e8e8e4;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'DM Mono', monospace !important;
    font-size: 12px !important;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: #999 !important;
    padding: 6px 14px !important;
}
.stTabs [aria-selected="true"] {
    color: #111 !important;
    border-bottom: 2px solid #111 !important;
    background: transparent !important;
}

/* Divider */
.port-divider {
    height: 1px;
    background: #e8e8e4;
    margin: 1.6rem 0;
}

/* Footer */
.port-footer {
    font-size: 11px;
    color: #bbb;
    text-align: center;
    padding-top: 1.5rem;
    border-top: 1px solid #e8e8e4;
    font-weight: 300;
    letter-spacing: 0.06em;
}

/* QR-Sektion */
.qr-card {
    border: 1px solid #e8e8e4;
    border-radius: 14px;
    padding: 20px;
    background: #fff;
    margin-top: 1rem;
}
.qr-label {
    font-size: 11px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #aaa;
    margin-bottom: 4px;
}
</style>
""", unsafe_allow_html=True)


# ── Hilfsfunktion: QR-Code ────────────────────────────────────────────────────
def make_qr(url: str, size: int = 6) -> Image.Image:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=size,
        border=3,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#111111", back_color="#ffffff")
    return img.convert("RGB")


def qr_to_bytes(img: Image.Image) -> bytes:
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()


# ── TABS ──────────────────────────────────────────────────────────────────────
tab_portfolio, tab_qr = st.tabs(["◈  Portfolio", "⊞  QR-Generator"])


# ════════════════════════════════════════════════════════════════════════════════
# TAB 1: PORTFOLIO
# ════════════════════════════════════════════════════════════════════════════════
with tab_portfolio:

    # Header
    st.markdown("""
    <div class="port-name">Tatjana <em>Shevchik</em></div>
    <div class="section-label">Data Science · ML · LLM · Ulm</div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='port-divider'></div>", unsafe_allow_html=True)

    # Bio
    st.markdown("""
    <p class="bio-text">
        <strong>Ich frage zuerst: Geht das nicht auch einfacher?</strong><br>
        Mathematische Biometrie (B.Sc., Uni Ulm) trifft auf LLM-Integration,
        echte Neugier und den Drang, Prozesse zu automatisieren — egal ob Modell,
        Pipeline oder Workflow. Aktuell Praktikantin @ DASU Ulm,
        eigene KI-Pipeline seit 2026 live im Kundeneinsatz.
    </p>
    """, unsafe_allow_html=True)

    # Stats
    st.markdown("""
    <div class="stat-row">
        <div class="stat-box">
            <span class="stat-num">1,0</span>
            <span class="stat-lab">Bachelorarbeit</span>
        </div>
        <div class="stat-box">
            <span class="stat-num">850k</span>
            <span class="stat-lab">Zellen klassifiziert</span>
        </div>
        <div class="stat-box">
            <span class="stat-num">94,6&nbsp;%</span>
            <span class="stat-lab">FNN-Accuracy</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='port-divider'></div>", unsafe_allow_html=True)

    # Kontakt
    st.markdown("<div class='section-label'>Kontakt & Profile</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="link-row">
        <span>🔗</span>
        <a href="https://linkedin.com/in/tatjana-shevchik" target="_blank">
            linkedin.com/in/tatjana-shevchik
        </a>
    </div>
    <div class="link-row">
        <span>✉️</span>
        <a href="mailto:tatshev@outlook.de">tatshev@outlook.de</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='port-divider'></div>", unsafe_allow_html=True)

    # ── Projekte ──────────────────────────────────────────────────────────────
    st.markdown("<div class='section-label'>Projekte</div>", unsafe_allow_html=True)

    # Projekt 1 – DASU
    st.markdown("""
    <div class="proj-card">
        <div class="proj-title">KI Information Extraction – Köhler Auktionshaus</div>
        <div class="proj-meta">DASU Ulm · 2026 · produktiver Kundeneinsatz</div>
        <div class="proj-body">
            <strong>End-to-End-Pipeline</strong> zur automatisierten Extraktion von
            Metadaten aus Briefmarken, Briefen und Attesten. Mehrere LLM-APIs (Mistral, Gemini)
            evaluiert und integriert — Ergebnis: messbar höhere Precision & Recall.
            Inklusive interaktivem <strong>KI-Demo-Exponat</strong> für Messen und
            Kundenpräsentationen.
        </div>
        <div class="tag-row">
            <span class="tag">Python</span>
            <span class="tag">LLM APIs</span>
            <span class="tag">Prompt Engineering</span>
            <span class="tag">Mistral</span>
            <span class="tag">Gemini</span>
            <span class="tag">Git</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶  Live-Demo öffnen", key="demo"):
            st.markdown("[http://80.151.131.52:10046/](http://80.151.131.52:10046/)")
    with col2:
        if st.button("↗  Projektseite DASU", key="dasu"):
            st.markdown("[dasu.digital/project/koehler-auktionshaus](https://www.dasu.digital/project/koehler-auktionshaus/)")

    # Projekt 2 – Bachelorarbeit
    st.markdown("""
    <div class="proj-card" style="margin-top:14px;">
        <div class="proj-title">ML-gestützte Bildanalyse – Rift Valley Fever</div>
        <div class="proj-meta">Universität Ulm · Bachelor-Thesis · Note 1,0 · Sept. 2025</div>
        <div class="proj-body">
            Machine-Learning-Framework zur Analyse von Fluoreszenz­mikroskopie­daten
            für die Antikörperdetektion des Rift-Valley-Fiebers.
            Vollständige Pipeline: <strong>Bildsegmentierung</strong> (Watershed) →
            <strong>Feature Extraction</strong> (Geometrie, Textur, Momente) →
            <strong>Klassifikation</strong> (Gaussian Naive Bayes & Feedforward Neural Network).<br>
            Datensatz: 369 Bilder · ~850.000 klassifizierte Zellen · FNN-Accuracy 94,6 %.
        </div>
        <div class="tag-row">
            <span class="tag">Python</span>
            <span class="tag">scikit-learn</span>
            <span class="tag">scikit-image</span>
            <span class="tag">Neural Network</span>
            <span class="tag">Naive Bayes</span>
            <span class="tag">Biomedizin</span>
            <span class="tag">Watershed</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='port-divider'></div>", unsafe_allow_html=True)

    # Tech Stack
    st.markdown("<div class='section-label'>Tech Stack</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="tag-row" style="margin-bottom: 1.6rem;">
        <span class="tag">Python</span>
        <span class="tag">R</span>
        <span class="tag">SQL</span>
        <span class="tag">Pandas</span>
        <span class="tag">NumPy</span>
        <span class="tag">scikit-learn</span>
        <span class="tag">Matplotlib</span>
        <span class="tag">Mistral</span>
        <span class="tag">Gemini</span>
        <span class="tag">ChatGPT</span>
        <span class="tag">Claude</span>
        <span class="tag">Git</span>
        <span class="tag">Jupyter</span>
        <span class="tag">SPSS</span>
        <span class="tag">Typo3</span>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="port-footer">Tatjana Shevchik · Ulm 2026 · Erstellt mit Streamlit</div>
    """, unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════════
# TAB 2: QR-GENERATOR
# ════════════════════════════════════════════════════════════════════════════════
with tab_qr:

    st.markdown("<div class='section-label'>QR-Code erstellen</div>", unsafe_allow_html=True)
    st.markdown("""
    <p class="bio-text" style="margin-bottom:1.2rem;">
        Gib eine URL ein — z.&thinsp;B. die Adresse dieser Portfolio-Seite —
        und lade den QR-Code direkt herunter.
    </p>
    """, unsafe_allow_html=True)

    # Vordefinierte Schnelllinks
    st.markdown("<div class='qr-label'>Schnellauswahl</div>", unsafe_allow_html=True)
    quick_links = {
        "Diese Portfolio-Seite": "https://DEINE-URL.streamlit.app",
        "LinkedIn":              "https://linkedin.com/in/tatjana-shevchik",
        "KI-Demo (DASU)":        "http://80.151.131.52:10046/",
        "DASU Projektseite":     "https://www.dasu.digital/project/koehler-auktionshaus/",
        "Eigene URL eingeben":   "",
    }

    choice = st.selectbox(
        label="",
        options=list(quick_links.keys()),
        label_visibility="collapsed",
    )

    if choice == "Eigene URL eingeben":
        url_input = st.text_input(
            "URL",
            placeholder="https://...",
            label_visibility="collapsed",
        )
    else:
        url_input = quick_links[choice]
        st.markdown(f"""
        <div class="link-row" style="margin-bottom:0.5rem;">
            <span>🔗</span> <span style="font-size:13px;">{url_input}</span>
        </div>
        """, unsafe_allow_html=True)

    # QR-Größe
    qr_size = st.slider("Größe (Box-Pixel)", min_value=4, max_value=12, value=7, step=1)

    # Generieren
    if url_input and url_input.strip():
        img = make_qr(url_input.strip(), size=qr_size)
        img_bytes = qr_to_bytes(img)

        col_qr, col_info = st.columns([1, 1.4])
        with col_qr:
            st.image(img, caption="", use_container_width=True)
        with col_info:
            st.markdown(f"""
            <div class="qr-card">
                <div class="qr-label">URL</div>
                <p style="font-size:12px; color:#555; word-break:break-all; margin:4px 0 14px;">
                    {url_input.strip()}
                </p>
                <div class="qr-label">Format</div>
                <p style="font-size:12px; color:#555; margin:4px 0 14px;">PNG · schwarz / weiß</p>
                <div class="qr-label">Fehlerkorrektur</div>
                <p style="font-size:12px; color:#555; margin:4px 0;">Stufe H (30 % wiederherstellbar)</p>
            </div>
            """, unsafe_allow_html=True)

        # Download-Button
        st.download_button(
            label="⬇  QR-Code als PNG herunterladen",
            data=img_bytes,
            file_name="qr_tatjana_portfolio.png",
            mime="image/png",
            use_container_width=True,
        )

        st.info(
            "💡 Tipp: Sobald deine Streamlit-App deployed ist, wähle "
            "**'Eigene URL eingeben'** und füge die öffentliche App-URL ein — "
            "dann kannst du diesen QR-Code direkt in deinen Lebenslauf einbauen.",
            icon=None,
        )
    else:
        st.markdown("""
        <div style="text-align:center; padding:3rem 0; color:#ccc; font-size:13px;">
            ← URL eingeben oder auswählen
        </div>
        """, unsafe_allow_html=True)
