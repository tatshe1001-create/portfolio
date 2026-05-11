"""
Tatjana Shevchik – Portfolio
Starten mit: streamlit run app.py
Abhängigkeiten: pip install streamlit
"""

import streamlit as st

st.set_page_config(
    page_title="Tatjana Shevchik · Portfolio",
    page_icon="🔬",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Mono', monospace !important;
}

.port-name {
    font-family: 'DM Serif Display', serif !important;
    font-size: 2.8rem;
    font-weight: 400;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: #111;
    margin-bottom: 0.2rem;
}
.port-name em { color: #555; font-style: italic; }

.port-tagline {
    font-size: 14px;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #444;
    margin-bottom: 1.5rem;
    font-weight: 400;
}

.section-label {
    font-size: 12px;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #111;
    font-weight: 500;
    margin-top: 2rem;
    margin-bottom: 0.75rem;
    border-left: 3px solid #111;
    padding-left: 10px;
}

.bio-text {
    font-size: 16px;
    line-height: 1.9;
    color: #222;
    font-weight: 400;
}
.bio-text strong { color: #111; font-weight: 500; }

.stat-row { display: flex; gap: 12px; margin: 1.5rem 0; }
.stat-box {
    flex: 1;
    background: #111;
    border-radius: 12px;
    padding: 18px 12px;
    text-align: center;
}
.stat-num {
    font-family: 'DM Serif Display', serif;
    font-size: 1.9rem;
    font-weight: 400;
    color: #fff;
    display: block;
}
.stat-lab {
    font-size: 11px;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #aaa;
    font-weight: 400;
    margin-top: 4px;
    display: block;
}

.port-divider { height: 1px; background: #ddd; margin: 1.75rem 0; }

.link-row {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 14px 16px;
    background: #f5f5f3;
    border-radius: 10px;
    margin-bottom: 10px;
    font-size: 15px;
    color: #111;
    font-weight: 400;
    border: 1px solid #ddd;
}
.link-row a { color: #111; text-decoration: none; font-weight: 500; }
.link-row a:hover { text-decoration: underline; }

.proj-card {
    border: 1.5px solid #ddd;
    border-radius: 14px;
    padding: 20px 22px;
    margin-bottom: 16px;
    background: #fff;
}
.proj-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.3rem;
    font-weight: 400;
    color: #111;
    margin-bottom: 5px;
}
.proj-meta {
    font-size: 13px;
    color: #555;
    letter-spacing: 0.05em;
    margin-bottom: 12px;
    font-weight: 400;
}
.proj-body {
    font-size: 15px;
    line-height: 1.85;
    color: #222;
    font-weight: 400;
    margin-bottom: 14px;
}
.proj-body strong { color: #111; font-weight: 500; }

.tag-row { display: flex; flex-wrap: wrap; gap: 7px; }
.tag {
    font-size: 12px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    padding: 5px 12px;
    border-radius: 6px;
    border: 1.5px solid #ccc;
    color: #333;
    font-weight: 400;
    background: #fafaf8;
}

.stButton > button {
    font-family: 'DM Mono', monospace !important;
    font-size: 14px !important;
    font-weight: 500 !important;
    border-radius: 9px !important;
    border: 1.5px solid #999 !important;
    background: #f5f5f3 !important;
    color: #111 !important;
    padding: 9px 20px !important;
    transition: all 0.15s !important;
    width: 100%;
}
.stButton > button:hover {
    background: #111 !important;
    border-color: #111 !important;
    color: #fff !important;
}

.stack-section { margin-bottom: 1.75rem; }

.port-footer {
    font-size: 13px;
    color: #666;
    text-align: center;
    padding-top: 1.5rem;
    border-top: 1px solid #ddd;
    margin-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ── HEADER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="port-name">Tatjana <em>Shevchik</em></div>
<div class="port-tagline">Data Science · ML · LLM · Ulm</div>
""", unsafe_allow_html=True)

st.markdown("<div class='port-divider'></div>", unsafe_allow_html=True)

# ── BIO ──────────────────────────────────────────────────────────────────────
st.markdown("""
<p class="bio-text">
    <strong>Ich frage zuerst: Geht das nicht auch einfacher?</strong><br>
    Mathematische Biometrie (B.Sc., Uni Ulm) trifft auf LLM-Integration,
    echte Neugier und den Drang, Prozesse zu automatisieren — egal ob Modell,
    Pipeline oder Workflow. Aktuell Praktikantin @ DASU Ulm,
    eigene KI-Pipeline seit 2026 live im Kundeneinsatz.
</p>
""", unsafe_allow_html=True)

# ── STATS ────────────────────────────────────────────────────────────────────
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
        <span class="stat-num">94,6 %</span>
        <span class="stat-lab">FNN-Accuracy</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='port-divider'></div>", unsafe_allow_html=True)

# ── KONTAKT ──────────────────────────────────────────────────────────────────
st.markdown("<div class='section-label'>Kontakt & Profile</div>", unsafe_allow_html=True)
st.markdown("""
<div class="link-row">🔗 &nbsp;
    <a href="https://linkedin.com/in/tatjana-shevchik" target="_blank">
        linkedin.com/in/tatjana-shevchik
    </a>
</div>
<div class="link-row">✉️ &nbsp;
    <a href="mailto:tatshev@outlook.de">tatshev@outlook.de</a>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='port-divider'></div>", unsafe_allow_html=True)

# ── PROJEKTE ─────────────────────────────────────────────────────────────────
st.markdown("<div class='section-label'>Projekte</div>", unsafe_allow_html=True)

st.markdown("""
<div class="proj-card">
    <div class="proj-title">KI Information Extraction – Köhler Auktionshaus</div>
    <div class="proj-meta">DASU Ulm &nbsp;·&nbsp; 2026 &nbsp;·&nbsp; produktiver Kundeneinsatz</div>
    <div class="proj-body">
        <strong>End-to-End-Pipeline</strong> zur automatisierten Extraktion von
        Metadaten aus Briefmarken, Briefen und Attesten. Mehrere LLM-APIs
        (Mistral, Gemini) evaluiert und integriert — Ergebnis: messbar höhere
        Precision &amp; Recall. Inklusive interaktivem
        <strong>KI-Demo-Exponat</strong> für Messen und Kundenpräsentationen.
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
        st.markdown("🔗 [http://80.151.131.52:10046/](http://80.151.131.52:10046/)")
with col2:
    if st.button("↗  Projektseite DASU", key="dasu"):
        st.markdown("🔗 [dasu.digital/project/koehler-auktionshaus](https://www.dasu.digital/project/koehler-auktionshaus/)")

st.markdown("""
<div class="proj-card" style="margin-top:16px;">
    <div class="proj-title">ML-gestützte Bildanalyse – Rift Valley Fever</div>
    <div class="proj-meta">Universität Ulm &nbsp;·&nbsp; Bachelor-Thesis &nbsp;·&nbsp; Note 1,0 &nbsp;·&nbsp; Sept. 2025</div>
    <div class="proj-body">
        Machine-Learning-Framework zur Analyse von Fluoreszenzmikroskopiedaten
        für die Antikörperdetektion des Rift-Valley-Fiebers.
        Vollständige Pipeline: <strong>Bildsegmentierung</strong> (Watershed) →
        <strong>Feature Extraction</strong> (Geometrie, Textur, Momente) →
        <strong>Klassifikation</strong> (Gaussian Naive Bayes &amp; Feedforward Neural Network).<br>
        Datensatz: 369 Bilder &nbsp;·&nbsp; ~850.000 klassifizierte Zellen &nbsp;·&nbsp; FNN-Accuracy 94,6&nbsp;%.
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

# ── TECH STACK ───────────────────────────────────────────────────────────────
st.markdown("<div class='section-label'>Tech Stack</div>", unsafe_allow_html=True)
st.markdown("""
<div class="tag-row stack-section">
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

# ── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="port-footer">Tatjana Shevchik · Ulm 2026 · Erstellt mit Streamlit</div>
""", unsafe_allow_html=True)
