import streamlit as st
import pandas as pd

# Stel pagina config in
st.set_page_config(
    page_title="Chatbot Selectie Assistent",
    page_icon="🤖",
    layout="wide"
)

# Titel en introductie
st.title("🤖 Chatbot Selectie Assistent")
st.markdown("""
### Welke chatbot past het beste bij jouw taak?
Deze tool helpt je de ideale AI-assistent te kiezen op basis van wat je wilt doen.
""")

# Chatbot informatie database
chatbots = {
    "ChatGPT": {
        "sterkte": "Gebruiksvriendelijk, creatief, goed in nuance en menselijke interactie",
        "zwakte": "Niet altijd 100% nauwkeurig, soms te voorzichtig",
        "best_voor": ["Advies", "Verhalen", "Creatieve opdrachten", "Samenvatten", "Algemene gesprekken"],
        "prijs": "Gratis of €23/maand (Plus) / €229/maand (Team)",
        "kleur": "#74aa9c",
        "link": "https://chat.openai.com"
    },
    "Gemini": {
        "sterkte": "Enorm contextvenster, Google integratie, uitstekende beeldherkenning",
        "zwakte": "Soms overdreven voorzichtig, interface kan rommelig zijn",
        "best_voor": ["Grote documenten", "Google Apps", "Beeldanalyse", "Creatief schrijven met feiten"],
        "prijs": "Gratis of €22/maand (Advanced)",
        "kleur": "#4285f4",
        "link": "https://gemini.google.com"
    },
    "Deepseek": {
        "sterkte": "Uitzonderlijk in programmeren, wiskunde, logica, goedkope API",
        "zwakte": "Minder 'gezellig', minder visuele features",
        "best_voor": ["Coderen", "Debuggen", "Wiskunde", "Technische documentatie", "Logische puzzels"],
        "prijs": "Gratis of zeer goedkope API",
        "kleur": "#ff6b35",
        "link": "https://chat.deepseek.com"
    },
    "Perplexity": {
        "sterkte": "Real-time internet, bronvermelding, feitenchecks, onderzoek",
        "zwakte": "Droge tekststijl, minder creatief",
        "best_voor": ["Academisch onderzoek", "Nieuws", "Feitenchecks", "Web samenvattingen"],
        "prijs": "Gratis of €20/maand (Pro)",
        "kleur": "#6c5ce7",
        "link": "https://www.perplexity.ai"
    }
}

# Functie voor beslisboom logica
def bepaal_beste_chatbot(antwoorden):
    hoofddoel = antwoorden.get("hoofddoel")
    
    if hoofddoel == "A":  # Code en programmeren
        subcode = antwoorden.get("subcode")
        
        if subcode == "A1":  # Code schrijven
            taal = antwoorden.get("taal")
            if taal in ["A1b", "A1d"]:  # Data science of andere specifieke taal
                return "Deepseek", "Deepseek is uitzonderlijk goed in Python en complexe programmeerlogica."
            else:
                return "ChatGPT", "ChatGPT is goed in algemene web development en heeft brede kennis."
                
        elif subcode == "A2":  # Debuggen/uitleg
            debug_type = antwoorden.get("debug_type")
            if debug_type == "A2a":  # Foutmeldingen
                return "Deepseek", "Deepseek begrijpt technische foutmeldingen direct en accuraat."
            elif debug_type == "A2b":  # Complexe code uitleg
                return "ChatGPT", "ChatGPT kan complexe code in begrijpelijke taal uitleggen."
            else:  # Best practices
                return "Deepseek", "Deepseek volgt strikte codeerstandaarden en best practices."
                
        elif subcode == "A3":  # Optimalisatie
            opti_type = antwoorden.get("opti_type")
            if opti_type == "A3a":  # Performance
                return "Deepseek", "Deepseek is sterk in algoritmes en performance optimalisatie."
            elif opti_type == "A3b":  # Leesbaarheid
                return "ChatGPT", "ChatGPT maakt code netjes en goed becommentarieerd."
            else:  # Architectuur
                return "Deepseek", "Deepseek is goed in schaalbare architectuur en systeemdesign."
                
        elif subcode == "A4":  # IDE integratie
            return "Deepseek", "Deepseek heeft een goede API voor IDE integratie en is kostenefficiënt."
    
    elif hoofddoel == "B":  # Creatieve content
        return "ChatGPT", "ChatGPT is het beste in creatief schrijven, verhalen en menselijke taal."
    
    elif hoofddoel == "C":  # Documenten analyseren
        doc_type = antwoorden.get("doc_type")
        if doc_type == "C1":  # Lange documenten
            return "Gemini", "Gemini heeft het grootste contextvenster voor lange documenten."
        elif doc_type == "C2":  # Info extraheren
            return "Perplexity", "Perplexity is nauwkeurig in feiten extractie en bronvermelding."
        elif doc_type == "C3":  # OCR/beeldherkenning
            return "Gemini", "Gemini heeft uitstekende vision capabilities voor beeldanalyse."
        else:  # Vergelijken docs
            return "Gemini", "Gemini kan meerdere documenten tegelijk laden en vergelijken."
    
    elif hoofddoel == "D":  # Onderzoek & feitencheck
        return "Perplexity", "Perplexity heeft real-time internettoegang en geeft bronvermelding."
    
    elif hoofddoel == "E":  # Algemeen gesprek
        return "ChatGPT", "ChatGPT is het meest empathisch en natuurlijk in gesprekken."
    
    elif hoofddoel == "F":  # Wiskunde & data
        wisk_type = antwoorden.get("wisk_type")
        if wisk_type in ["F1", "F3"]:  # Complexe wiskunde/formules
            return "Deepseek", "Deepseek is uitzonderlijk sterk in wiskunde en logica."
        elif wisk_type == "F2":  # Data analyse
            return "ChatGPT", "ChatGPT met Data Analyst is goed voor statistiek."
        else:  # Grafieken begrijpen
            return "Gemini", "Gemini begrijpt visualisaties en grafieken uitstekend."
    
    return "ChatGPT", "All-round oplossing voor de meeste taken."

# Sidebar voor navigatie
with st.sidebar:
    st.header("📊 Chatbot Vergelijking")
    
    # Toon chatbot info in sidebar
    selected_chatbot = st.selectbox(
        "Bekijk chatbot details:",
        ["Alle chatbots"] + list(chatbots.keys())
    )
    
    if selected_chatbot == "Alle chatbots":
        for naam, info in chatbots.items():
            with st.expander(f"🤖 {naam}"):
                st.markdown(f"**Sterkte:** {info['sterkte']}")
                st.markdown(f"**Zwakte:** {info['zwakte']}")
                st.markdown(f"**Best voor:** {', '.join(info['best_voor'])}")
                st.markdown(f"**Prijs:** {info['prijs']}")
                st.markdown(f"[Open {naam}]({info['link']})")
    else:
        info = chatbots[selected_chatbot]
        st.markdown(f"### {selected_chatbot}")
        st.markdown(f"**Sterkte:** {info['sterkte']}")
        st.markdown(f"**Zwakte:** {info['zwakte']}")
        st.markdown(f"**Best voor:**")
        for item in info['best_voor']:
            st.markdown(f"- {item}")
        st.markdown(f"**Prijs:** {info['prijs']}")
        st.markdown(f"[Open {selected_chatbot}]({info['link']})")

# Hoofdinhoud - Stap 1: Hoofddoel
st.header("Stap 1: Wat is je hoofddoel?")
hoofddoel = st.radio(
    "Selecteer je hoofdtaak:",
    [
        "A) Code en programmeren",
        "B) Creatieve content (tekst, ideeën, scripts)",
        "C) Documenten/tekst analyseren", 
        "D) Onderzoek & feitencheck",
        "E) Algemeen gesprek / advies",
        "F) Wiskunde & data-analyse"
    ],
    key="hoofddoel"
)

antwoorden = {"hoofddoel": hoofddoel[0]}

# Stap 2: Vervolgvragen gebaseerd op hoofddoel
if hoofddoel.startswith("A"):  # Code
    st.header("Stap 2: Wat voor code-hulp nodig?")
    subcode = st.radio(
        "Selecteer type code-hulp:",
        [
            "A1) Code schrijven vanaf scratch",
            "A2) Bestaande code debuggen/uitleg",
            "A3) Code optimalisatie/refactoring",
            "A4) IDE-integratie / autocomplete"
        ],
        key="subcode"
    )
    antwoorden["subcode"] = subcode[0:2]
    
    if subcode.startswith("A1"):  # Code schrijven
        st.subheader("Stap 3: Programmeertaal/framework?")
        taal = st.radio(
            "Welke programmeertaal/framework?",
            [
                "A1a) Web development (HTML/CSS/JS)",
                "A1b) Data science (Python/R)",
                "A1c) Mobile apps",
                "A1d) Andere specifieke taal"
            ],
            key="taal"
        )
        antwoorden["taal"] = taal[0:3]
        
    elif subcode.startswith("A2"):  # Debuggen
        st.subheader("Stap 3: Wat precies?")
        debug_type = st.radio(
            "Type debug/uitleg:",
            [
                "A2a) Foutmeldingen begrijpen",
                "A2b) Complexe code uitleggen",
                "A2c) Best practices adviseren"
            ],
            key="debug_type"
        )
        antwoorden["debug_type"] = debug_type[0:3]
        
    elif subcode.startswith("A3"):  # Optimalisatie
        st.subheader("Stap 3: Type optimalisatie?")
        opti_type = st.radio(
            "Focus van optimalisatie:",
            [
                "A3a) Performance/snelheid",
                "A3b) Code leesbaarheid",
                "A3c) Schaalbaarheid/architectuur"
            ],
            key="opti_type"
        )
        antwoorden["opti_type"] = opti_type[0:3]

elif hoofddoel.startswith("C"):  # Documenten
    st.header("Stap 2: Type documentanalyse?")
    doc_type = st.radio(
        "Selecteer type analyse:",
        [
            "C1) Lange documenten samenvatten (10+ pagina's)",
            "C2) Specifieke info extraheren uit tekst",
            "C3) PDF/afbeelding tekst herkennen (OCR)",
            "C4) Vergelijken van meerdere documenten"
        ],
        key="doc_type"
    )
    antwoorden["doc_type"] = doc_type[0:2]

elif hoofddoel.startswith("F"):  # Wiskunde
    st.header("Stap 2: Type berekening/analyse?")
    wisk_type = st.radio(
        "Selecteer type wiskunde:",
        [
            "F1) Complexe wiskundige problemen",
            "F2) Data analyse / statistiek",
            "F3) Formules/vergelijkingen oplossen",
            "F4) Grafieken/visualisaties begrijpen"
        ],
        key="wisk_type"
    )
    antwoorden["wisk_type"] = wisk_type[0:2]

# Toon resultaat
if st.button("🔍 Bepaal beste chatbot", type="primary"):
    chatbot_naam, reden = bepaal_beste_chatbot(antwoorden)
    
    # Toon resultaat in mooie box
    chatbot_info = chatbots[chatbot_naam]
    
    st.markdown("---")
    st.header("🎯 Aanbevolen Chatbot")
    
    # Maak een gekleurde header
    col1, col2 = st.columns([1, 3])
    with col1:
        st.markdown(f"<h1 style='color: {chatbot_info['kleur']};'>🤖</h1>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<h2 style='color: {chatbot_info['kleur']};'>{chatbot_naam}</h2>", unsafe_allow_html=True)
    
    # Toon reden en details
    st.success(f"**Waarom {chatbot_naam}?** {reden}")
    
    col3, col4 = st.columns(2)
    with col3:
        st.markdown("**Sterkte punten:**")
        st.info(chatbot_info['sterkte'])
        
        st.markdown("**Best voor:**")
        for item in chatbot_info['best_voor']:
            st.markdown(f"✅ {item}")
            
    with col4:
        st.markdown("**Zwakke punten:**")
        st.warning(chatbot_info['zwakte'])
        
        st.markdown("**Prijs:**")
        st.code(chatbot_info['prijs'])
    
    # Snelkoppelingen
    st.markdown("### 🚀 Snel actie ondernemen")
    st.markdown(f"**[Open direct {chatbot_naam}]({chatbot_info['link']})**")
    
    # Alternatieve opties
    st.markdown("### 🔄 Alternatieve opties")
    alternatieven = [c for c in chatbots.keys() if c != chatbot_naam]
    
    cols = st.columns(len(alternatieven))
    for idx, alt in enumerate(alternatieven):
        with cols[idx]:
            st.markdown(f"**{alt}**")
            st.markdown(f"*{chatbots[alt]['sterkte'].split(',')[0]}*")
            st.markdown(f"[Open {alt}]({chatbots[alt]['link']})")

# Voorbeelden sectie
with st.expander("📋 Voorbeeld outputs bekijken"):
    st.subheader("Voorbeeld 1: Python code schrijven")
    st.code("""
Hoofddoel: A) Code en programmeren
Subdoel: A1) Code schrijven vanaf scratch
Taal: A1b) Data science (Python/R)

🎯 Aanbevolen Chatbot: Deepseek
✅ Waarom? Deepseek is uitzonderlijk goed in Python en complexe programmeerlogica.
    """)
    
    st.subheader("Voorbeeld 2: Onderzoek doen")
    st.code("""
Hoofddoel: D) Onderzoek & feitencheck

🎯 Aanbevolen Chatbot: Perplexity
✅ Waarom? Perplexity heeft real-time internettoegang en geeft bronvermelding.
    """)
    
    st.subheader("Voorbeeld 3: Creatief verhaal schrijven")
    st.code("""
Hoofddoel: B) Creatieve content

🎯 Aanbevolen Chatbot: ChatGPT
✅ Waarom? ChatGPT is het beste in creatief schrijven, verhalen en menselijke taal.
    """)

# Installatie instructies
with st.expander("🚀 Hoe deze app te draaien"):
    st.markdown("""
### Installatie stappen:

1. **Installeer Python** (versie 3.8 of hoger)

2. **Installeer Streamlit:**
```bash
pip install streamlit pandas
