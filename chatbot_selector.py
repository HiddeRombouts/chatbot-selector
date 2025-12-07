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
st.markdown("### Welke chatbot past het beste bij jouw taak?")
st.markdown("Deze tool helpt je de ideale AI-assistent te kiezen op basis van wat je wilt doen.")

# Chatbot informatie database - UITGEBREID MET AFBEELDINGEN OPTIES
chatbots = {
    "ChatGPT": {
        "sterkte": "Gebruiksvriendelijk, creatief, goed in nuance en menselijke interactie, DALL-E 3 voor afbeeldingen",
        "zwakte": "Niet altijd 100% nauwkeurig, soms te voorzichtig, DALL-E heeft beperkingen voor bepaalde inhoud",
        "best_voor": ["Advies", "Verhalen", "Creatieve opdrachten", "Samenvatten", "Algemene gesprekken", "DALL-E 3 afbeeldingen"],
        "prijs": "Gratis of €23/maand (Plus) / €229/maand (Team)",
        "afbeeldingen": "✅ DALL-E 3 (Plus abonnement nodig)",
        "kleur": "#74aa9c",
        "link": "https://chat.openai.com",
        "img_guide": "Gebruik DALL-E 3 in ChatGPT Plus voor realistische en creatieve afbeeldingen",
        "img_tools": ["DALL-E 3", "GPT-4o Vision"]
    },
    "Gemini": {
        "sterkte": "Enorm contextvenster, Google integratie, uitstekende beeldherkenning, ImageFX voor afbeeldingen",
        "zwakte": "Soms overdreven voorzichtig, interface kan rommelig zijn, beperkte beeldgeneratie",
        "best_voor": ["Grote documenten", "Google Apps", "Beeldanalyse", "Creatief schrijven met feiten", "Google ImageFX"],
        "prijs": "Gratis of €22/maand (Advanced)",
        "afbeeldingen": "✅ ImageFX (experimenteel) & Vertex AI",
        "kleur": "#4285f4",
        "link": "https://gemini.google.com",
        "img_guide": "ImageFX in AI Studio voor experimentele beeldgeneratie, of Vertex AI voor professioneel gebruik",
        "img_tools": ["ImageFX", "Vertex AI", "Imagen 3"]
    },
    "Deepseek": {
        "sterkte": "Uitzonderlijk in programmeren, wiskunde, logica, goedkope API",
        "zwakte": "Minder 'gezellig', minder visuele features, GEEN ingebouwde beeldgeneratie",
        "best_voor": ["Coderen", "Debuggen", "Wiskunde", "Technische documentatie", "Logische puzzels"],
        "prijs": "Gratis of zeer goedkope API",
        "afbeeldingen": "❌ Geen ingebouwde beeldgeneratie",
        "kleur": "#ff6b35",
        "link": "https://chat.deepseek.com",
        "img_guide": "Deepseek heeft geen beeldgeneratie. Gebruik in combinatie met DALL-E, Midjourney of Stable Diffusion",
        "img_tools": ["Geen"]
    },
    "Perplexity": {
        "sterkte": "Real-time internet, bronvermelding, feitenchecks, onderzoek, Pro versie met beeldgeneratie",
        "zwakte": "Droge tekststijl, minder creatief, beeldgeneratie alleen in Pro versie",
        "best_voor": ["Academisch onderzoek", "Nieuws", "Feitenchecks", "Web samenvattingen", "Onderzoek + afbeeldingen"],
        "prijs": "Gratis of €20/maand (Pro)",
        "afbeeldingen": "✅ Pro versie (meerdere modellen)",
        "kleur": "#6c5ce7",
        "link": "https://www.perplexity.ai",
        "img_guide": "Perplexity Pro kan schakelen tussen modellen die beeldgeneratie ondersteunen",
        "img_tools": ["GPT-4o", "Claude 3.5", "DALL-E via integratie"]
    },
    "Midjourney": {
        "sterkte": "Beste kwaliteit beeldgeneratie, artistieke stijlen, zeer creatief, sterke community",
        "zwakte": "Alleen via Discord, geen chat interface, moeilijk te leren, duur",
        "best_voor": ["Artistieke afbeeldingen", "Concept art", "Fotorealistische beelden", "Design"],
        "prijs": "$10-$120/maand",
        "afbeeldingen": "✅ Gespecialiseerd in beeldgeneratie",
        "kleur": "#1e1e1e",
        "link": "https://www.midjourney.com",
        "img_guide": "Gebruik via Discord, bekende voor hoge kwaliteit artistieke afbeeldingen",
        "img_tools": ["Midjourney V6", "Niji (anime)"]
    },
    "Leonardo.AI": {
        "sterkte": "Zeer controleerbare beeldgeneratie, veel aanpasbare modellen, gratis tier beschikbaar",
        "zwakte": "Minder bekend, kwaliteit soms inconsistent",
        "best_voor": ["Gratis beeldgeneratie", "Aangepaste modellen", "Consistentie tussen beelden"],
        "prijs": "Gratis (beperkt) of $10-$48/maand",
        "afbeeldingen": "✅ Gespecialiseerd in beeldgeneratie",
        "kleur": "#ff6b00",
        "link": "https://leonardo.ai",
        "img_guide": "Goed voor gratis gebruik en controle over beeldstijlen/models",
        "img_tools": ["Meerdere Stable Diffusion modellen"]
    }
}

# Functie voor beslisboom logica - UITGEBREID MET AFBEELDINGEN
def bepaal_beste_chatbot(antwoorden):
    hoofddoel = antwoorden.get("hoofddoel")
    
    # SPECIALE CASE: Afbeeldingen genereren
    if hoofddoel == "G":  # Nieuwe optie voor afbeeldingen
        img_type = antwoorden.get("img_type")
        
        if img_type == "G1":  # Artistiek/creatief
            return "Midjourney", "Midjourney is de beste voor artistieke en creatieve afbeeldingen van hoge kwaliteit."
        elif img_type == "G2":  # Fotorealistisch
            return "Midjourney", "Midjourney V6 is uitstekend voor fotorealistische beelden."
        elif img_type == "G3":  # Gratis optie
            return "Leonardo.AI", "Leonardo.AI heeft een goede gratis tier voor beeldgeneratie."
        elif img_type == "G4":  # Binnen chat interface
            return "ChatGPT", "ChatGPT met DALL-E 3 integreert beeldgeneratie in de chat interface."
        elif img_type == "G5":  # Technische/diagrammen
            return "ChatGPT", "ChatGPT kan diagrammen en technische afbeeldingen goed genereren."
        else:  # Algemene afbeeldingen
            return "Midjourney", "Midjourney is de industrie standaard voor AI beeldgeneratie."
    
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
        creative_type = antwoorden.get("creative_type", "B1")
        if creative_type == "B5":  # Creatief MET afbeeldingen
            return "ChatGPT", "ChatGPT combineert creatief schrijven met DALL-E 3 beeldgeneratie."
        else:
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
                st.markdown(f"**Afbeeldingen:** {info['afbeeldingen']}")
                st.markdown(f"**Prijs:** {info['prijs']}")
                st.markdown(f"[Open {naam}]({info['link']})")
    else:
        info = chatbots[selected_chatbot]
        st.markdown(f"### {selected_chatbot}")
        st.markdown(f"**Sterkte:** {info['sterkte']}")
        st.markdown(f"**Zwakte:** {info['zwakte']}")
        st.markdown(f"**Afbeeldingen:** {info['afbeeldingen']}")
        st.markdown(f"**Best voor:**")
        for item in info['best_voor']:
            st.markdown(f"- {item}")
        st.markdown(f"**Prijs:** {info['prijs']}")
        st.markdown(f"[Open {selected_chatbot}]({info['link']})")

# Hoofdinhoud - Stap 1: Hoofddoel (UITGEBREID)
st.header("Stap 1: Wat is je hoofddoel?")
hoofddoel = st.radio(
    "Selecteer je hoofdtaak:",
    [
        "A) Code en programmeren",
        "B) Creatieve content (tekst, ideeën, scripts)",
        "C) Documenten/tekst analyseren", 
        "D) Onderzoek & feitencheck",
        "E) Algemeen gesprek / advies",
        "F) Wiskunde & data-analyse",
        "G) Afbeeldingen genereren 🎨"  # NIEUWE OPTIE
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

elif hoofddoel.startswith("B"):  # Creatieve content (UITGEBREID)
    st.header("Stap 2: Wat voor creatieve content?")
    creative_type = st.radio(
        "Selecteer type creatieve content:",
        [
            "B1) Verhalen/scripts schrijven",
            "B2) Marketing teksten/branding",
            "B3) Ideeën brainstormen",
            "B4) Gedichten/artistieke tekst",
            "B5) Creatieve content MET afbeeldingen 🎨"  # NIEUWE OPTIE
        ],
        key="creative_type"
    )
    antwoorden["creative_type"] = creative_type[0:2]

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

elif hoofddoel.startswith("G"):  # NIEUWE OPTIE: Afbeeldingen genereren
    st.header("🎨 Stap 2: Wat voor afbeeldingen wil je genereren?")
    img_type = st.radio(
        "Selecteer type afbeelding:",
        [
            "G1) Artistieke/creatieve afbeeldingen",
            "G2) Fotorealistische beelden",
            "G3) Gratis optie (budget)",
            "G4) Binnen chat interface (geïntegreerd)",
            "G5) Technische afbeeldingen/diagrammen",
            "G6) Algemene afbeeldingen"
        ],
        key="img_type"
    )
    antwoorden["img_type"] = img_type[0:2]

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
        
        # Toon afbeeldingen info specifiek
        st.markdown("**Afbeeldingen genereren:**")
        if chatbot_info['afbeeldingen'].startswith("✅"):
            st.success(chatbot_info['afbeeldingen'])
            if 'img_guide' in chatbot_info:
                st.caption(chatbot_info['img_guide'])
        else:
            st.error(chatbot_info['afbeeldingen'])
        
        st.markdown("**Prijs:**")
        st.code(chatbot_info['prijs'])
    
    # Snelkoppelingen
    st.markdown("### 🚀 Snel actie ondernemen")
    st.markdown(f"**[Open direct {chatbot_naam}]({chatbot_info['link']})**")
    
    # Toon afbeeldingen-specifieke tips als relevant
    if hoofddoel.startswith("G") or (hoofddoel.startswith("B") and antwoorden.get("creative_type") == "B5"):
        with st.expander("💡 Tips voor afbeeldingen genereren"):
            if chatbot_naam == "Midjourney":
                st.markdown("""
                **Midjourney Tips:**
                - Gebruik `/imagine` command in Discord
                - Voeg style keywords toe zoals `--v 6.0` voor versie 6
                - Gebruik `--ar 16:9` voor landscape of `--ar 9:16` voor portrait
                - Experimenteer met `--style raw` voor meer controle
                """)
            elif chatbot_naam == "ChatGPT":
                st.markdown("""
                **ChatGPT DALL-E Tips:**
                - Wees specifiek in je beschrijvingen
                - Gebruik DALL-E 3 voor beste kwaliteit
                - Vraag om aanpassingen in dezelfde chat
                - Combineer met tekst voor complete content
                """)
            elif chatbot_naam == "Leonardo.AI":
                st.markdown("""
                **Leonardo.AI Tips:**
                - Maak gebruik van de gratis dagelijkse tokens
                - Experimenteer met verschillende modellen
                - Gebruik Alchemy voor betere kwaliteit
                - Pas Image Guidance aan voor meer controle
                """)
    
    # Alternatieve opties
    st.markdown("### 🔄 Alternatieve opties")
    
    # Voor afbeeldingen, toon specifiek alternatieven
    if hoofddoel.startswith("G"):
        image_chatbots = {k: v for k, v in chatbots.items() if v['afbeeldingen'].startswith("✅")}
        alternatieven = [c for c in image_chatbots.keys() if c != chatbot_naam]
    else:
        alternatieven = [c for c in chatbots.keys() if c != chatbot_naam]
    
    if alternatieven:
        cols = st.columns(len(alternatieven))
        for idx, alt in enumerate(alternatieven):
            with cols[idx]:
                st.markdown(f"**{alt}**")
                st.markdown(f"*{chatbots[alt]['sterkte'].split(',')[0]}*")
                if chatbots[alt]['afbeeldingen'].startswith("✅"):
                    st.markdown(f"🎨 {chatbots[alt]['afbeeldingen'].replace('✅ ', '')}")
                st.markdown(f"[Open {alt}]({chatbots[alt]['link']})")

# Voorbeelden sectie
with st.expander("📋 Voorbeeld outputs bekijken"):
    st.subheader("Voorbeeld 1: Python code schrijven")
    st.code("Hoofddoel: A) Code en programmeren\nSubdoel: A1) Code schrijven vanaf scratch\nTaal: A1b) Data science (Python/R)\n\n🎯 Aanbevolen Chatbot: Deepseek\n✅ Waarom? Deepseek is uitzonderlijk goed in Python en complexe programmeerlogica.")
    
    st.subheader("Voorbeeld 2: Fotorealistische afbeeldingen")
    st.code("Hoofddoel: G) Afbeeldingen genereren\nSubdoel: G2) Fotorealistische beelden\n\n🎯 Aanbevolen Chatbot: Midjourney\n✅ Waarom? Midjourney V6 is uitstekend voor fotorealistische beelden.")
    
    st.subheader("Voorbeeld 3: Creatief schrijven met afbeeldingen")
    st.code("Hoofddoel: B) Creatieve content\nSubdoel: B5) Creatieve content MET afbeeldingen\n\n🎯 Aanbevolen Chatbot: ChatGPT\n✅ Waarom? ChatGPT combineert creatief schrijven met DALL-E 3 beeldgeneratie.")
    
    st.subheader("Voorbeeld 4: Gratis afbeeldingen genereren")
    st.code("Hoofddoel: G) Afbeeldingen genereren\nSubdoel: G3) Gratis optie (budget)\n\n🎯 Aanbevolen Chatbot: Leonardo.AI\n✅ Waarom? Leonardo.AI heeft een goede gratis tier voor beeldgeneratie.")

# Afbeeldingen vergelijking sectie
with st.expander("🎨 Afbeeldingen Genereren Tools Overzicht"):
    st.subheader("Vergelijking AI Beeldgeneratie Tools")
    
    # Maak een tabel voor beeldgeneratie
    img_data = []
    for naam, info in chatbots.items():
        if info['afbeeldingen'].startswith("✅"):
            img_data.append({
                "Tool": naam,
                "Afbeeldingen": info['afbeeldingen'].replace("✅ ", ""),
                "Prijs": info['prijs'],
                "Best voor": ", ".join(info['best_voor'][:3]),
                "Link": info['link']
            })
    
    if img_data:
        df = pd.DataFrame(img_data)
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        st.markdown("**🎯 Snelle keuze gids:**")
        st.markdown("""
        - **Beste kwaliteit:** Midjourney
        - **Beste geïntegreerd in chat:** ChatGPT (DALL-E 3)
        - **Beste gratis optie:** Leonardo.AI
        - **Beste voor onderzoek:** Perplexity Pro
        - **Beste Google ecosysteem:** Gemini (ImageFX)
        """)
    else:
        st.info("Geen chatbots met beeldgeneratie gevonden.")



# Voeg wat CSS toe voor betere styling
st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        padding: 10px 24px;
    }
    .stRadio > label {
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    .stRadio > label:hover {
        background-color: #f0f2f6;
    }
    h1, h2, h3 {
        color: #1e3a8a;
    }
    div[data-testid="stExpander"] {
        background-color: #042b5e;
        border-radius: 10px;
        padding: 10px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>🤖 Chatbot Selectie Assistent v2.0 | Nu met afbeeldingen generatie opties 🎨</p>
</div>
""", unsafe_allow_html=True)
