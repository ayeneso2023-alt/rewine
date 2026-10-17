#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ReWine Multilingual Website Generator
Generates Marketing (index*.html), Support (soporte*.html), and Privacy (privacidad*.html)
pages across all 7 supported languages:
ES (Español), EN (English), FR (Français), IT (Italiano), PT (Português), RU (Русский), ZH (中文 - 简体).
"""

import os

LANGUAGES = [
    {"code": "es", "flag": "🇪🇸", "label": "ES", "name": "Español"},
    {"code": "en", "flag": "🇬🇧", "label": "EN", "name": "English"},
    {"code": "fr", "flag": "🇫🇷", "label": "FR", "name": "Français"},
    {"code": "it", "flag": "🇮🇹", "label": "IT", "name": "Italiano"},
    {"code": "pt", "flag": "🇵🇹", "label": "PT", "name": "Português"},
    {"code": "ru", "flag": "🇷🇺", "label": "RU", "name": "Русский"},
    {"code": "zh", "flag": "🇨🇳", "label": "ZH", "name": "中文 (简体)"},
]

def get_page_filename(page_type, lang_code):
    suffix = "" if lang_code == "es" else f"-{lang_code}"
    return f"{page_type}{suffix}.html"

def render_lang_switcher(current_page_type, current_lang_code):
    items = []
    for lang in LANGUAGES:
        target_file = get_page_filename(current_page_type, lang["code"])
        is_active = ' class="active"' if lang["code"] == current_lang_code else ''
        items.append(f'<a href="{target_file}"{is_active}>{lang["flag"]} {lang["label"]}</a>')
    return "\n        ".join(items)

def render_nav(current_page_type, current_lang_code, nav_texts):
    index_file = get_page_filename("index", current_lang_code)
    soporte_file = get_page_filename("soporte", current_lang_code)
    privacidad_file = get_page_filename("privacidad", current_lang_code)

    act_index = ' class="active"' if current_page_type == "index" else ''
    act_soporte = ' class="active"' if current_page_type == "soporte" else ''
    act_privacidad = ' class="active"' if current_page_type == "privacidad" else ''

    lang_switcher_html = render_lang_switcher(current_page_type, current_lang_code)

    return f"""  <nav class="navbar">
    <div class="container nav-wrap">
      <a href="{index_file}" class="nav-brand">
        <img src="assets/logo.png" alt="ReWine Logo" class="nav-logo">
        <span class="nav-title">ReWine</span>
      </a>
      <ul class="nav-links">
        <li><a href="{index_file}"{act_index}>{nav_texts['home']}</a></li>
        <li><a href="{soporte_file}"{act_soporte}>{nav_texts['support']}</a></li>
        <li><a href="{privacidad_file}"{act_privacidad}>{nav_texts['privacy']}</a></li>
      </ul>
      <div class="lang-switcher">
        {lang_switcher_html}
      </div>
      <div>
        <a href="#" class="btn-cta">App Store</a>
      </div>
    </div>
  </nav>"""

def render_footer(current_lang_code, footer_texts):
    index_file = get_page_filename("index", current_lang_code)
    soporte_file = get_page_filename("soporte", current_lang_code)
    privacidad_file = get_page_filename("privacidad", current_lang_code)

    return f"""  <footer>
    <div class="container">
      <div class="responsible-drinking-box">
        <span class="responsible-drinking-badge">{footer_texts['badge']}</span>
        <p class="responsible-drinking-text">{footer_texts['text']}</p>
      </div>
      <p>&copy; 2026 ReWine by JACOOR. {footer_texts['rights']}</p>
      <p style="margin-top: 8px;">
        <a href="{index_file}">{footer_texts['home']}</a> &bull;
        <a href="{soporte_file}">{footer_texts['support']}</a> &bull;
        <a href="{privacidad_file}">{footer_texts['privacy']}</a>
      </p>
    </div>
  </footer>"""

# Shared UI translations
UI_STRINGS = {
    "es": {
        "home": "Inicio",
        "support": "Soporte & FAQ",
        "privacy": "Privacidad",
        "guide_cta": "Ver Guía y Soporte",
        "badge": "🔞 +18 AÑOS • CONSUMO RESPONSABLE",
        "text": "ReWine es una herramienta de registro técnico y apreciación sensorial destinada exclusivamente a personas mayores de edad (+18). Promovemos la cultura del vino y el consumo responsable y moderado. El abuso de bebidas alcohólicas es perjudicial para la salud.",
        "rights": "Todos los derechos reservados."
    },
    "en": {
        "home": "Home",
        "support": "Support & FAQ",
        "privacy": "Privacy",
        "guide_cta": "View Guide & Support",
        "badge": "🔞 18+ YEARS • RESPONSIBLE DRINKING",
        "text": "ReWine is a technical tasting notebook and sensory appreciation tool designed exclusively for adults of legal drinking age (+18). We actively advocate for wine education and responsible, moderate enjoyment. Alcohol abuse is harmful to your health.",
        "rights": "All rights reserved."
    },
    "fr": {
        "home": "Accueil",
        "support": "Support & FAQ",
        "privacy": "Confidentialité",
        "guide_cta": "Guide & Assistance",
        "badge": "🔞 +18 ANS • CONSOMMATION RESPONSABLE",
        "text": "ReWine est un carnet de dégustation technique et d'évaluation sensorielle destiné exclusivement aux personnes majeures (+18 ans). Nous encourageons la culture du vin et une consommation responsable et modérée. L'abus d'alcool est dangereux pour la santé.",
        "rights": "Tous droits réservés."
    },
    "it": {
        "home": "Inizio",
        "support": "Supporto & FAQ",
        "privacy": "Privacy",
        "guide_cta": "Guida & Supporto",
        "badge": "🔞 +18 ANNI • BERE RESPONSABILE",
        "text": "ReWine è uno strumento di degustazione tecnica e apprezzamento sensoriale destinato esclusivamente ai maggiori di 18 anni. Promuoviamo la cultura del vino e un consumo consapevole e moderato. L'abuso di bevande alcoliche è dannoso per la salute.",
        "rights": "Tutti i diritti riservati."
    },
    "pt": {
        "home": "Início",
        "support": "Suporte & FAQ",
        "privacy": "Privacidade",
        "guide_cta": "Ver Guia & Suporte",
        "badge": "🔞 +18 ANOS • CONSUMO RESPONSÁVEL",
        "text": "ReWine é um caderno técnico de provas e apreciação sensorial destinado exclusivamente a maiores de idade (+18 anos). Promovemos a cultura do vinho e o consumo responsável e moderado. O consumo excessivo de álcool é prejudicial à saúde.",
        "rights": "Todos os direitos reservados."
    },
    "ru": {
        "home": "Главная",
        "support": "Поддержка и FAQ",
        "privacy": "Конфиденциальность",
        "guide_cta": "Руководство и помощь",
        "badge": "🔞 18+ • ОТВЕТСТВЕННОЕ УПОТРЕБЛЕНИЕ",
        "text": "ReWine — профессиональный дегустационный дневник и инструмент сенсорной оценки, предназначенный исключительно для совершеннолетних пользователей (18+). Мы поддерживаем культуру вина и ответственное, умеренное потребление. Чрезмерное употребление алкоголя вредит здоровью.",
        "rights": "Все права защищены."
    },
    "zh": {
        "home": "首页",
        "support": "技术支持与常见问题",
        "privacy": "隐私政策",
        "guide_cta": "查看指南与支持",
        "badge": "🔞 年满18岁 • 理性鉴赏与负责任饮酒",
        "text": "ReWine 是一款专为法定成年人（18周岁及以上）打造的专业品酒记录与感官品评工具。我们倡导葡萄酒文化与适量、健康的理性品鉴。过量饮酒有害健康。",
        "rights": "保留所有权利。"
    }
}

# MARKETING DATA
MARKETING_DATA = {
    "es": {
        "title": "ReWine — Cuaderno Profesional de Catas de Vino & Ficha Sommelier",
        "meta_desc": "ReWine es tu cuaderno profesional de catas de vino. 7 idiomas, nivel de sommelier con progresión interactiva, estadísticas de Top Países, 400+ DOs mundiales, rueda de aromas con clasificación enológica, dictado por voz y PDF editorial.",
        "hero_badge": "Cuaderno Enológico Internacional • 7 Idiomas",
        "hero_title": "El Arte de la Cata en tu Bolsillo con <span>ReWine</span>",
        "hero_sub": "La herramienta definitiva para amantes del vino y sumilleres. Registra catas completas con ubicación GPS automática, dictado por voz, nivel de sommelier interactivo, catálogo de más de 400 D.O. e IGPs mundiales, rueda de aromas profesional y fichas en PDF editorial con fotos sin deformación.",
        "features": [
            ("🌍", "Totalmente Multilingüe (7 Idiomas)", "Disponible en <strong>Español, English, Français, Italiano, Português, Русский y 中文 (简体)</strong>. Selector inicial y cambio instantáneo en cualquier pantalla con terminología sommelier WSET y ampelografía adaptada."),
            ("🏆", "Nivel Sommelier & Progresión Gamificada", "5 niveles de maestría: <strong>Principiante, Aficionado, Medio, Superior y Master of Wine</strong>. Toca el recuadro para abrir la hoja de ruta interactiva con tus medallas, porcentaje de avance, tips sommelier y los requisitos exactos que te faltan para subir de nivel."),
            ("📊", "Top Países & Estadísticas de Bodega", "Analiza tu colección con el ranking de <strong>Top Países</strong> de procedencia con banderas nacionales en alta definición, recuento de botellas, porcentaje de bodega y nota media acumulada."),
            ("🍷", "Filtros y Clasificación Oficial (7 Dimensiones)", "Filtra y ordena tu cuaderno según las 7 dimensiones técnicas de cata: Tipo de producto, Carácter/Efervescencia, Color cromático, Añada, D.O./Región, País y <strong>Variedad de uva normalizada</strong> (sin duplicados ni porcentajes residuales)."),
            ("🌸", "Rueda & Glosario de Aromas Oficial", "14 familias aromáticas organizadas con rigor enológico en <strong>Aromas Primarios</strong> (varietales y terruño), <strong>Secundarios</strong> (fermentación y lías) y <strong>Terciarios</strong> (crianza, roble, soleras y guarda). Descriptores directos y limpios."),
            ("🎙️", "Dictado por Voz Inteligente (On-Device)", "Graba observaciones visuales, olfativas y gustativas al instante hablando con total libertad. Reconocimiento de voz nativo en tu dispositivo con <strong>privacidad 100% garantizada</strong> (sin servidores externos ni almacenamiento de grabaciones)."),
            ("🍇", "Catálogo Mundial: 400+ D.O. e IGPs & 64+ Uvas", "Más de 400 Denominaciones de Origen de todo el mundo con banderas y nombres traducidos (incluyendo Hungría y Líbano), y más de 64 uvas viníferas nobles con nombres autóctonos adaptados al idioma activo."),
            ("📍", "Lugar de Cata por GPS & Nombre del Catador", "Registra el lugar de tu cata con tres modalidades: <strong>GPS Automático</strong> en un toque (resuelve bodega o restaurante sin rastreo en segundo plano), escritura manual o en blanco. Personaliza el nombre del sumiller o evaluador."),
            ("📄", "Fichas en PDF con Fotos en Proporción Exacta", "Exporta fichas de cata completas en formato A4 con maquetación vintage en el idioma activo. Las fotografías se encuadran matemáticamente <strong>conservando el 100% de su relación de aspecto original</strong> con marcos dorados de lujo."),
            ("🔒", "100% Privado, Seguro, Offline y Sin Publicidad", "Diseñado para operar en salas de barricas y bodegas sin cobertura. Sin cuentas obligatorias, sin rastreadores invasivos y con copia de seguridad cifrada en tu cuenta privada de iCloud.")
        ]
    },
    "en": {
        "title": "ReWine — Professional Wine Tasting Journal & Sommelier Sheet",
        "meta_desc": "ReWine is your professional wine tasting notebook. 7 languages, gamified sommelier levels, Top Countries statistics, 400+ world appellations, aroma wheel with oenological classification, voice dictation, and editorial PDF export.",
        "hero_badge": "International Enological Journal • 7 Languages",
        "hero_title": "The Art of Wine Tasting in Your Pocket with <span>ReWine</span>",
        "hero_sub": "The ultimate companion for wine lovers and sommeliers. Record complete tastings with auto GPS location, voice dictation, interactive sommelier progression, 400+ world appellations & PGIs catalog, professional aroma wheel, and parchment A4 PDF exports with perfectly proportioned photos.",
        "features": [
            ("🌍", "Fully Multilingual (7 Languages)", "Available in <strong>English, Spanish, French, Italian, Portuguese, Russian, and Simplified Chinese</strong>. Choose your language at launch or switch dynamically anytime with certified WSET sommelier terminology."),
            ("🏆", "Sommelier Level & Gamified Progression", "5 professional mastery tiers: <strong>Beginner, Enthusiast, Intermediate, Advanced, and Master of Wine</strong>. Tap the card to open an interactive roadmap with crests, progress percentage, sommelier tips, and missing milestones."),
            ("📊", "Top Countries & Cellar Analytics", "Analyze your tasting journey with the <strong>Top Countries</strong> ranking featuring high-definition national flags, bottle count, cellar share percentage, and average scores."),
            ("🍷", "Official Tasting Filters (7 Dimensions)", "Filter and sort your journal across 7 official dimensions: Product type, Character/Effervescence, Color, Vintage, Appellation/PGI, Country, and <strong>Normalized grape varieties</strong> (deduplicated, without percentages)."),
            ("🌸", "Official Aroma Wheel & Sensory Glossary", "14 aroma families classified with oenological precision into <strong>Primary Aromas</strong> (varietal & terroir), <strong>Secondary</strong> (fermentation & lees), and <strong>Tertiary</strong> (oak, soleras & aging). Clean, direct descriptors."),
            ("🎙️", "Smart Voice Dictation (On-Device)", "Dictate visual, olfactory, and palate notes hands-free. Powered by native on-device Apple Speech Recognition ensuring <strong>100% privacy</strong> without sending audio to third-party servers."),
            ("🍇", "World Catalog: 400+ Appellations & 64+ Grapes", "Over 400 world appellations & PGIs with localized names and flags (including Hungary and Lebanon), plus 64+ noble grape varieties with regional synonyms adaptively translated."),
            ("📍", "GPS Tasting Location & Sommelier Signature", "Three modes to log the tasting venue: <strong>Auto GPS</strong> with one tap (resolves winery or restaurant locally without background tracking), manual typing, or leave blank. Customize the evaluator/sommelier name."),
            ("📄", "Editorial PDF Sheets with Proportional Photos", "Instant A4 PDF export in the currently active language. Vintage parchment layout with photos of the glass, label, cork, or bottle in <strong>exact original aspect ratio</strong> with luxury gold borders."),
            ("🔒", "100% Private, Secure, Offline & Ad-Free", "Engineered to work seamlessly in underground cellars and remote vineyards. No mandatory accounts, no invasive trackers, and encrypted backup in your private iCloud account.")
        ]
    },
    "fr": {
        "title": "ReWine — Carnet Professionnel de Dégustation de Vin & Fiche Sommelier",
        "meta_desc": "ReWine est votre carnet professionnel de dégustation. 7 langues, niveaux de sommelier avec progression interactive, statistiques Meilleurs Pays, 400+ AOP mondiales, roue des arômes oenologique, dictée vocale et export PDF.",
        "hero_badge": "Carnet Œnologique International • 7 Langues",
        "hero_title": "L'Art de la Dégustation en Poche avec <span>ReWine</span>",
        "hero_sub": "L'outil ultime des passionnés et sommeliers. Enregistrez des dégustations complètes avec localisation GPS, dictée vocale, progression sommelier interactive, catalogue de 400+ AOP mondiales, roue des arômes professionnelle et fiches PDF avec photos aux proportions exactes.",
        "features": [
            ("🌍", "Totalement Multilingue (7 Langues)", "Disponible en <strong>Français, Anglais, Espagnol, Italien, Portugais, Russe et Chinois (Simplifié)</strong>. Sélecteur initial et changement instantané avec terminologie oenologique WSET certifiée."),
            ("🏆", "Niveau Sommelier & Progression Gamifiée", "5 rangs de maîtrise : <strong>Débutant, Passionné, Intermédiaire, Supérieur et Master of Wine</strong>. Touchez la carte pour ouvrir une feuille de route interactive avec trophées, pourcentage, conseils et conditions requises pour monter en niveau."),
            ("📊", "Meilleurs Pays & Statistiques de Cave", "Analysez vos dégustations avec le classement des <strong>Meilleurs Pays</strong> d'origine, drapeaux nationaux HD, nombre de bouteilles, part de cave et note moyenne."),
            ("🍷", "Filtres & Classification Officielle (7 Dimensions)", "Filtrez et triez selon les 7 dimensions techniques : Type de produit, Caractère/Effervescence, Couleur, Millésime, AOP/IGP, Pays et <strong>Cépage normalisé</strong> (sans doublons ni pourcentages)."),
            ("🌸", "Roue & Glossaire des Arômes Officiels", "14 familles aromatiques classées en <strong>Arômes Primaires</strong> (variétal et terroir), <strong>Secondaires</strong> (fermentation et lies) et <strong>Tertiaires</strong> (élevage, fût, solera et garde). Descriptifs épurés et directs."),
            ("🎙️", "Dictée Vocale Intelligente (Sur l'Appareil)", "Enregistrez vos impressions visuelles, olfactives et gustatives à la voix. Reconnaissance vocale Apple locale avec <strong>confidentialité 100% garantie</strong> (aucun enregistrement audio envoyé sur des serveurs tiers)."),
            ("🍇", "Catalogue Mondial : 400+ AOP/IGP & 64+ Cépages", "Plus de 400 appellations du monde avec drapeaux et traductions (incluant la Hongrie et le Liban), et plus de 64 cépages nobles avec dénominations autochtones adaptées."),
            ("📍", "Lieu par GPS & Signature du Sommelier", "Trois modes pour enregistrer le lieu : <strong>GPS Automatique</strong> en un clic (résolution locale de domaine ou restaurant sans pistage), saisie manuelle ou laisser vide. Nom du dégustateur personnalisable."),
            ("📄", "Fiches PDF Éditoriales avec Photos Proportionnées", "Exportation instantanée de fiches de dégustation A4 en parchemin vintage. Les photographies s'ajustent en <strong>conservant 100% de leur format d'origine</strong> avec de somptueux cadres dorés."),
            ("🔒", "100% Privé, Sécurisé, Hors Ligne et Sans Pub", "Conçu pour fonctionner dans les caves souterraines sans réseau. Sans compte obligatoire, sans traceurs invasifs et avec sauvegarde chiffrée sur votre compte privé iCloud.")
        ]
    },
    "it": {
        "title": "ReWine — Taccuino Professionale di Degustazione Vini & Scheda Sommelier",
        "meta_desc": "ReWine è il tuo taccuino professionale di degustazione. 7 lingue, livelli sommelier con progressione interattiva, statistiche Top Paesi, 400+ DOC mondiali, ruota degli aromi enologica, dettatura vocale ed export PDF.",
        "hero_badge": "Taccuino Enologico Internazionale • 7 Lingue",
        "hero_title": "L'Arte della Degustazione in Tasca con <span>ReWine</span>",
        "hero_sub": "Lo strumento definitivo per appassionati e sommelier. Registra degustazioni complete con GPS automatico, dettatura vocale, progressione sommelier interattiva, catalogo di 400+ DOC/IGP mondiali, ruota degli aromi professionale e schede PDF con foto in proporzione perfetta.",
        "features": [
            ("🌍", "Completamente Multilingue (7 Lingue)", "Disponibile in <strong>Italiano, Inglese, Spagnolo, Francese, Portoghese, Russo e Cinese (Semplificato)</strong>. Scelta iniziale e cambio dinamico istantaneo con terminologia sommelier WSET."),
            ("🏆", "Livello Sommelier & Progressione Gamificata", "5 livelli di maestria: <strong>Principiante, Appassionato, Intermedio, Superiore e Master of Wine</strong>. Tocca la scheda per visualizzare il percorso interattivo con medaglie, percentuale, consigli e requisiti per salire di livello."),
            ("📊", "Top Paesi & Statistiche di Cantina", "Analizza la tua collezione con la classifica dei <strong>Top Paesi</strong> di provenienza con bandiere nazionali HD, conteggio bottiglie, quota percentuale e punteggio medio."),
            ("🍷", "Filtri e Classificazione Ufficiale (7 Dimensioni)", "Filtra e ordina secondo le 7 dimensioni tecniche: Tipo di prodotto, Carattere/Effervescenza, Colore, Annata, Denominazione/IGP, Paese e <strong>Varietà d'uva normalizzata</strong> (senza duplicati né percentuali)."),
            ("🌸", "Ruota & Glossario degli Aromi Ufficiali", "14 famiglie aromatiche suddivise con rigore enologico in <strong>Aromi Primari</strong> (varietali e terroir), <strong>Secondari</strong> (fermentazione e fecce) e <strong>Terziari</strong> (invecchiamento in botte, soleras e bottiglia)."),
            ("🎙️", "Dettatura Vocale Intelligente (On-Device)", "Registra note visive, olfattive e gustative parlando liberamente. Riconoscimento vocale Apple on-device con <strong>privacy al 100%</strong> (nessun audio inviato a server esterni)."),
            ("🍇", "Catalogo Mondiale: 400+ Denominazioni & 64+ Vitigni", "Oltre 400 denominazioni d'origine mondiali con bandiere e nomi tradotti (inclusi Ungheria e Libano) e oltre 64 vitigni nobili con sinonimi autoctoni adattati alla lingua attiva."),
            ("📍", "Luogo di Degustazione GPS & Firma Sommelier", "Tre modalità per registrare il luogo: <strong>GPS Automatico</strong> in un tocco (cantina o ristorante senza tracciamento in background), testo manuale o vuoto. Firma personalizzabile del sommelier."),
            ("📄", "Schede PDF Editoriali con Foto Proporzionate", "Esportazione istantanea in PDF A4 in carta pergamena vintage. Le foto mantengono il <strong>100% delle proporzioni originali</strong> senza alcuna deformazione, incorniciate in oro."),
            ("🔒", "100% Privato, Sicuro, Offline e Senza Pubblicità", "Funziona perfettamente in cantine sotterranee e vigneti senza segnale. Nessun account obbligatorio, nessun tracciamento invasivo e backup cifrato sul tuo iCloud personale.")
        ]
    },
    "pt": {
        "title": "ReWine — Caderno Profissional de Prova de Vinhos & Ficha Sommelier",
        "meta_desc": "ReWine é o seu caderno profissional de provas de vinhos. 7 idiomas, níveis de sommelier com progressão interativa, estatísticas Principais Países, 400+ D.O. mundiais, roda de aromas enológica, ditado por voz e PDF editorial.",
        "hero_badge": "Caderno Enológico Internacional • 7 Idiomas",
        "hero_title": "A Arte da Prova no seu Bolso com <span>ReWine</span>",
        "hero_sub": "A ferramenta definitiva para apreciadores e sommeliers. Registe provas completas com GPS automático, ditado por voz, progressão sommelier interativa, catálogo de 400+ D.O. e IGPs mundiais, roda de aromas profissional e fichas em PDF editorial com fotos sem deformação.",
        "features": [
            ("🌍", "Totalmente Multilingue (7 Idiomas)", "Disponível em <strong>Português, Inglês, Espanhol, Francês, Italiano, Russo e Chinês (Simplificado)</strong>. Seletor inicial e troca instantânea com terminologia enológica WSET certificada."),
            ("🏆", "Nível Sommelier & Progressão Gamificada", "5 níveis de mestria: <strong>Principiante, Entusiasta, Médio, Superior e Master of Wine</strong>. Toque no cartão para abrir o roteiro interativo com medalhas, percentagem de avanço, dicas sommelier e metas para subir de nível."),
            ("📊", "Principais Países & Estatísticas de Adega", "Analise a sua coleção com o ranking dos <strong>Principais Países</strong> com bandeiras nacionais HD, contagem de garrafas, percentagem da adega e pontuação média acumulada."),
            ("🍷", "Filtros e Classificação Oficial (7 Dimensões)", "Filtre e organize o seu caderno através das 7 dimensões oficiais: Tipo de produto, Caráter/Efervescência, Cor, Safra, D.O./IGP, País e <strong>Casta de uva normalizada</strong> (sem duplicatas nem percentagens)."),
            ("🌸", "Roda & Glossário de Aromas Oficiais", "14 famílias aromáticas estruturadas em <strong>Aromas Primários</strong> (varietais e terroir), <strong>Secundários</strong> (fermentação e borras) e <strong>Terciários</strong> (estágio em carvalho, soleras e guarda). Descritores diretos e elegantes."),
            ("🎙️", "Ditado por Voz Inteligente (No Dispositivo)", "Registe observações visuais, olfativas e gustativas falando com naturalidade. Reconhecimento vocal nativo Apple com <strong>100% de privacidade</strong> (sem envio de áudio para servidores externos)."),
            ("🍇", "Catálogo Mundial: 400+ D.O./IGPs & 64+ Castas", "Mais de 400 Denominações de Origem de todo o mundo com bandeiras e traduções (incluindo Hungria e Líbano), e mais de 64 castas nobres com nomes autóctones adaptados."),
            ("📍", "Local por GPS & Assinatura do Sommelier", "Três opções para o local: <strong>GPS Automático</strong> com um toque (adega ou restaurante sem rastreamento em segundo plano), escrita manual ou em branco. Nome personalizado do provador/sommelier."),
            ("📄", "Fichas em PDF com Fotos na Proporção Exata", "Exportação instantânea de fichas em PDF A4 com design pergaminho vintage. As fotografias são renderizadas <strong>preservando 100% da proporção original</strong> com molduras douradas."),
            ("🔒", "100% Privado, Seguro, Offline e Sem Publicidade", "Funciona perfeitamente em caves subterrâneas e vinhas sem rede. Sem criação obrigatória de contas, sem rastreadores invasivos e com cópia de segurança encriptada no iCloud.")
        ]
    },
    "ru": {
        "title": "ReWine — Профессиональный Винный Дневник & Карта Сомелье",
        "meta_desc": "ReWine — ваш профессиональный дегустационный блокнот. 7 языков, уровни сомелье с интерактивным прогрессом, рейтинг Топ Стран, 400+ апелласьонов мира, винное колесо ароматов, голосовая диктовка и экспорт в PDF.",
        "hero_badge": "Международный Винный Дневник • 7 Языков",
        "hero_title": "Искусство Дегустации в Вашем Кармане с <span>ReWine</span>",
        "hero_sub": "Идеальный инструмент для любителей вина и сомелье. Фиксируйте полные дегустации с авто-GPS, голосовой диктовкой, интерактивным повышением ранга сомелье, каталогом 400+ апелласьонов мира, профессиональным колесом ароматов и PDF-отчетами с идеальными пропорциями фотографий.",
        "features": [
            ("🌍", "Полная Мультиязычность (7 Языков)", "Доступно на <strong>Русском, Английском, Испанском, Французском, Итальянском, Португальском и Китайском (Упрощенном)</strong>. Выбор языка при старте и мгновенное переключение с сертифицированной терминологией WSET."),
            ("🏆", "Ранг Сомелье & Геймификация Прогресса", "5 уровней мастерства: <strong>Начинающий, Любитель, Средний, Высший и Master of Wine</strong>. Нажмите на карточку, чтобы открыть интерактивный экран с трофеями, процентом прогресса, советами сомелье и точным списком условий для перехода на новый уровень."),
            ("📊", "Топ Стран & Аналитика Винного Погреба", "Анализируйте свои дегустации с рейтингом <strong>Топ Стран</strong> происхождения с флагами высокого разрешения, количеством бутылок, процентной долей коллекции и средней оценкой."),
            ("🍷", "Фильтры и Официальная Классификация (7 Категорий)", "Сортируйте и фильтруйте дневник по 7 техническим категориям: Тип продукта, Игристость/Характер, Цвет, Год урожая, Апелласьон/IGP, Страна и <strong>Нормализованный сорт винограда</strong> (без дубликатов и процентов)."),
            ("🌸", "Колесо & Глоссарий Винных Ароматов", "14 ароматических семейств с профессиональным разделением на <strong>Первичные</strong> (сорт и терруар), <strong>Вторичные</strong> (брожение и дрожжевой осадок) и <strong>Третичные</strong> (выдержка в дубе, солера и бутылочное старение)."),
            ("🎙️", "Умная Голосовая Диктовка (На Устройстве)", "Диктуйте визуальные, ароматические и вкусовые заметки голосом. Нативное распознавание речи Apple прямо на устройстве гарантирует <strong>100% конфиденциальность</strong> (аудио не передается на внешние серверы)."),
            ("🍇", "Мировой Каталог: 400+ Апелласьонов & 64+ Сорта", "Более 400 апелласьонов мира с флагами и локализованными названиями (включая Венгрию и Ливан) и свыше 64 благородных сортов винограда с автохтонными синонимами."),
            ("📍", "GPS Место Дегустации & Имя Сомелье", "Три режима указания места: <strong>Авто-GPS</strong> в одно касание (определение винодельни или ресторана без фоновой слежки), ручной ввод или пропуск. Указание имени дегустатора."),
            ("📄", "Полиграфические PDF-Листы с Пропорциями Фото", "Мгновенный экспорт дегустационных листов А4 на винтажном пергаменте на активном языке. Фотографии бокала, этикетки, пробки или бутылки <strong>сохраняют 100% исходных пропорций</strong> в золотых рамках."),
            ("🔒", "100% Приватно, Надежно, Офлайн и Без Рекламы", "Создано для использования в подвалах и на отдаленных виноградниках без связи. Без обязательной регистрации, без слежки и с резервным копированием в ваш личный iCloud.")
        ]
    },
    "zh": {
        "title": "ReWine — 专业葡萄酒品鉴笔记本 & 侍酒师品评档案",
        "meta_desc": "ReWine 是您的随身专业葡萄酒品鉴笔记本。支持7国语言，具备五级侍酒师进阶成长体系、顶级产酒国大数据统计、400+全球法定产区、分级风味轮盘、本地语音口述及高端PDF报告导出。",
        "hero_badge": "国际化专业品酒笔记本 • 7国语言支持",
        "hero_title": "指尖上的专业品酒艺术，尽在 <span>ReWine</span>",
        "hero_sub": "葡萄酒爱好者与职业侍酒师的终极利器。支持一键式自动GPS酒庄定位、本地智能语音口述录入、互动式侍酒师进阶面板、收录全球400+法定产区与64+酿酒葡萄品种，提供三级官方香气轮盘及高保真无损照片PDF排版导出。",
        "features": [
            ("🌍", "全方位多语言支持（7种语言）", "支持 <strong>中文（简体）、英语、西班牙语、法语、意大利语、葡萄牙语和俄语</strong>。首次启动即提供语言选择，随时动态秒级切换，严格采用WSET/OIV标准侍酒与葡萄品种术语。"),
            ("🏆", "侍酒师段位体系 & 互动成长面板", "5大专业进阶段位：<strong>初学者、葡萄酒爱好者、中级品酒师、高级侍酒师与葡萄酒大师（Master of Wine）</strong>。点击卡片开启互动式进阶面板，查看荣誉徽章、达成进度百分比、侍酒师心得及晋升目标。"),
            ("📊", "顶级产酒国排行榜 & 酒窖大数据", "通过 <strong>顶级产酒国（Top Countries）</strong> 排行榜深入洞察您的品评历程，配备高清国旗标识、收录酒款数、酒窖占比及累计平均分。"),
            ("🍷", "多重筛选与官方品酒分类（7大技术维度）", "根据官方品鉴技术标准的7个维度精准检索：产品类型、气泡与酒体性格、酒色、年份、法定产区、出产国以及 <strong>标准化葡萄品种</strong>（自动消除重复与百分比后缀干扰）。"),
            ("🌸", "官方三级风味轮盘与感官词汇库", "14大香气家族严格区分为：<strong>一类香气</strong>（品种与风土原生果香、花香）、<strong>二类香气</strong>（发酵与酒泥陈酿酵母香）及 <strong>三类香气</strong>（橡木桶、索莱拉系统与老熟陈年陈香）。精炼纯正。"),
            ("🎙️", "智能本地语音口述（设备端运行）", "通过麦克风流畅口述记录视觉、嗅觉与口感评述。依托Apple本地设备端语音识别技术，<strong>100%隐私保障</strong>（绝不向第三方服务器传输或保留任何录音数据）。"),
            ("🍇", "全球产区图谱：400+法定产区 & 64+酿酒葡萄", "收录全球400多个知名产区（包含匈牙利托卡伊与黎巴嫩贝卡谷地等）及64种以上主流酿酒葡萄，并根据所选语言自适应显示本土传统名称。"),
            ("📍", "GPS品酒地点定位 & 侍酒师署名", "三种地点记录模式：<strong>一键自动GPS</strong>（本地解析酒庄或餐厅，绝无后台轨迹追踪）、手动输入或留空。自由设定评审品酒师签名。"),
            ("📄", "高保真PDF品酒报告（照片无损比例）", "一键生成当前激活语言版本的A4尺寸复古羊皮纸排版报告。酒杯、酒标、木塞与酒瓶照片 <strong>100%保留原始构图宽高比</strong>，辅以华贵烫金边框。"),
            ("🔒", "100%纯本地私密、离线可用、无广告", "专为地下酒窖与无信号葡萄园设计，完全支持离线操作。无需强制注册，零追踪，无广告干扰，支持Apple个人iCloud端到端加密备份。")
        ]
    }
}

# SUPPORT FAQ DATA
SUPPORT_DATA = {
    "es": {
        "title": "Soporte Técnico & Contacto — ReWine",
        "meta_desc": "Centro de soporte oficial de ReWine. Preguntas frecuentes sobre nivel de sommelier, idiomas, dictado por voz, filtros, 400+ DOs, PDF y contacto.",
        "h1": "Soporte Técnico de ReWine",
        "subtitle": "Centro de ayuda oficial, preguntas frecuentes y guía de novedades enológicas.",
        "faqs": [
            ("¿Cómo funciona el Nivel del Sommelier y qué requisitos tiene cada nivel?",
             "El sistema gamificado de ReWine evalúa tu trayectoria sensorial en <strong>5 niveles progresivos</strong>:<br>"
             "• <strong>Principiante:</strong> A partir de 1 vino catado.<br>"
             "• <strong>Aficionado:</strong> 20+ vinos, 4+ Denominaciones de Origen y 3+ países catados.<br>"
             "• <strong>Medio:</strong> 50+ vinos, 7+ Denominaciones de Origen y 5+ países catados.<br>"
             "• <strong>Superior:</strong> 100+ vinos, 15+ Denominaciones de Origen, 7+ países y 2+ tipos de producto.<br>"
             "• <strong>Master of Wine:</strong> 200+ vinos, 30+ Denominaciones de Origen, 12+ países y 3+ tipos de producto.<br>"
             "Al pulsar la tarjeta del Nivel Sommelier en la pestaña «Estadísticas», se abre una hoja de progresión interactiva con medallas, porcentaje de avance, consejos enológicos y el detalle exacto de qué requisitos te faltan para subir de nivel."),

            ("¿Cómo funciona el dictado por voz para registrar notas sensoriales?",
             "En las observaciones de la fase visual, olfativa y gustativa encontrarás un botón con icono de micrófono. Al pulsarlo, puedes hablar con naturalidad y ReWine transcribirá tu voz a texto en tiempo real. La transcripción se procesa <strong>100% de forma local en tu dispositivo</strong> gracias al framework Speech nativo de iOS. ReWine nunca envía tus grabaciones a servidores externos ni almacena tus archivos de audio, garantizando tu total privacidad."),

            ("¿En qué se diferencian los aromas primarios, secundarios y terciarios en la rueda?",
             "La rueda y glosario de ReWine sigue la clasificación sensorial oficial de la sumillería internacional:<br>"
             "• <strong>Aromas Primarios:</strong> Proceden directamente de la uva y el terruño (frutas cítricas, blancas, de hueso, tropicales, rojas, negras, flores, notas vegetales y balsámicas).<br>"
             "• <strong>Aromas Secundarios:</strong> Se originan durante la fermentación alcohólica, maloláctica y la crianza sobre lías (lácticos, mantequilla, panadería y brioche).<br>"
             "• <strong>Aromas Terciarios:</strong> Nacen durante el envejecimiento en barricas de roble, la reducción en botella y soleras (especias, vainilla, madera, tostados, frutos secos y notas minerales de evolución)."),

            ("¿Cómo funcionan los filtros avanzados y la normalización de variedades?",
             "En la vista de «Mi Cuaderno» puedes filtrar por las 7 dimensiones técnicas oficiales: 1) Tipo de producto, 2) Carácter/Efervescencia, 3) Color cromático, 4) Añada/Cosecha, 5) Denominación de Origen o IGP, 6) País y 7) Variedades de uva. El filtro de variedades <strong>normaliza automáticamente los nombres</strong>: por ejemplo, si tienes vinos con 'Tempranillo 5%' o 'Tempranillo 10%', el filtro los agrupa de forma limpia bajo 'Tempranillo', eliminando duplicados y sufijos innecesarios."),

            ("¿Qué denominaciones de origen incluye el catálogo mundial?",
             "El catálogo de ReWine cuenta con <strong>más de 400 Denominaciones de Origen, IGPs y apelaciones oficiales</strong> de todo el mundo. Incluye todas las regiones de España, Francia, Italia, Portugal, Alemania, Estados Unidos, Argentina, Chile, Sudáfrica, Australia, Nueva Zelanda, y recientemente ampliado con Hungría (Tokaj, Eger, Villány, etc.) y Líbano (Bekaa Valley, Batroun, Jezzine, etc.), con sus respectivas banderas nacionales y nombres adaptados a cada idioma."),

            ("¿Cómo se exportan las fichas en PDF y cómo se tratan las fotografías?",
             "Desde cualquier ficha técnica o detalle de cata, pulsa «Exportar a PDF». ReWine compone un documento A4 de estética editorial vintage en papel pergamino con bordes dorados, generado íntegramente en el idioma activo. Las fotografías adjuntas se redimensionan mediante cálculo proporcional exacto, <strong>respetando el 100% de su relación de aspecto original</strong> sin recortes ni distorsiones."),

            ("¿Cómo funciona el registro de ubicación por GPS y qué privacidad ofrece?",
             "En la sección técnica de cada cata puedes elegir entre: <strong>GPS Automático</strong> (resuelve el nombre de la bodega, restaurante o municipio mediante los servicios de localización locales de Apple sin guardar historial de rutas), <strong>Escribir a mano</strong> o <strong>Dejar en blanco</strong>. Tus coordenadas nunca se transmiten a servidores de terceros."),

            ("¿Cómo se cambia el idioma de la aplicación?",
             "ReWine está traducida al 100% en 7 idiomas (Español, Inglés, Francés, Italiano, Portugués, Ruso y Chino Simplificado). Al abrir la app por primera vez puedes elegir tu idioma preferido, y puedes cambiarlo en cualquier momento tocando la píldora con bandera situada en la barra de herramientas superior de «Mi Cuaderno»."),

            ("¿Puedo usar la aplicación sin conexión a internet?",
             "Sí, con total autonomía. ReWine está diseñada con arquitectura local offline para su uso en salas de catas subterráneas, viñedos o ferias sin cobertura. Si tienes activada la copia de seguridad de iCloud en tu iPhone o iPad, tus datos y fotos se respaldan de forma cifrada en tu cuenta privada de Apple.")
        ],
        "contact_title": "Contacto Directo con el Desarrollador",
        "contact_desc": "¿Tienes alguna consulta, sugerencia de mejora o necesitas asistencia técnica? Contáctanos directamente y te responderemos a la mayor brevedad:",
        "compat": "Compatibilidad: iOS 17.0 o superior (iPhone y iPad).",
        "dev": "Desarrollador: JACOOR."
    },
    "en": {
        "title": "Technical Support & Contact — ReWine",
        "meta_desc": "Official ReWine Support Center. FAQs regarding sommelier levels, languages, voice dictation, filters, 400+ appellations, PDF export, and contact.",
        "h1": "ReWine Technical Support",
        "subtitle": "Official help center, frequently asked questions, and enological features guide.",
        "faqs": [
            ("How does the Sommelier Level work and what are the requirements for each tier?",
             "ReWine's gamified progression evaluates your wine journey across <strong>5 mastery tiers</strong>:<br>"
             "• <strong>Beginner:</strong> Starting from 1 tasted wine.<br>"
             "• <strong>Enthusiast:</strong> 20+ wines, 4+ Appellations/PGIs, and 3+ countries tasted.<br>"
             "• <strong>Intermediate:</strong> 50+ wines, 7+ Appellations/PGIs, and 5+ countries tasted.<br>"
             "• <strong>Advanced:</strong> 100+ wines, 15+ Appellations/PGIs, 7+ countries, and 2+ product types.<br>"
             "• <strong>Master of Wine:</strong> 200+ wines, 30+ Appellations/PGIs, 12+ countries, and 3+ product types.<br>"
             "Tapping the Sommelier Level card in the «Statistics» tab opens an interactive sheet with crests, progress percentage, expert tips, and exact milestones needed to reach the next tier."),

            ("How does voice dictation work for tasting notes and is it private?",
             "In the visual, olfactory, and palate observation fields, you will find a microphone icon. Tap it and speak naturally; ReWine will transcribe your impressions in real time. Dictation is processed <strong>100% locally on your device</strong> using Apple's native Speech framework. ReWine never stores audio recordings or sends voice data to external servers, guaranteeing total privacy."),

            ("What is the difference between primary, secondary, and tertiary aromas on the wheel?",
             "ReWine's aroma wheel strictly adheres to international sommelier standards:<br>"
             "• <strong>Primary Aromas:</strong> Derived directly from the grape variety and terroir (citrus, stone fruit, tropical fruit, berries, floral, herbal, and balsamic notes).<br>"
             "• <strong>Secondary Aromas:</strong> Developed during alcoholic/malolactic fermentation and lees contact (dairy, fresh butter, pastry, and brioche).<br>"
             "• <strong>Tertiary Aromas:</strong> Created during oak barrel aging, solera aging, and bottle maturation (spices, vanilla, toasted wood, dried fruits, leather, and evolution minerals)."),

            ("How do advanced filters and grape variety normalization work?",
             "In «My Journal», filter by 7 official technical dimensions: 1) Product Type, 2) Character/Effervescence, 3) Color, 4) Vintage, 5) Appellation/PGI, 6) Country, and 7) Grape Varieties. The variety filter <strong>automatically normalizes names</strong>: for instance, wines listed as 'Tempranillo 5%' or 'Tempranillo 10%' are grouped cleanly under 'Tempranillo', eliminating duplicates and percentage noise."),

            ("What wine regions are included in the world catalog?",
             "The ReWine catalog encompasses <strong>over 400 official Appellations, PGIs, and wine regions</strong> worldwide. It includes comprehensive coverage of Spain, France, Italy, Portugal, Germany, the USA, Argentina, Chile, South Africa, Australia, New Zealand, plus recently added Hungary (Tokaj, Eger, Villány, etc.) and Lebanon (Bekaa Valley, Batroun, Jezzine, etc.), with flags and localized names."),

            ("How are PDF sheets exported and how are photos rendered?",
             "From any tasting entry, tap «Export to PDF». ReWine generates an A4 vintage parchment editorial sheet with luxury gold borders in the currently active language. Attached photographs are scaled using exact aspect ratio calculations, <strong>preserving 100% of their original proportions</strong> without cropping or distortion."),

            ("How does GPS location logging work and how is privacy handled?",
             "In the technical section of each tasting, choose between: <strong>Auto GPS</strong> (resolves winery, restaurant, or city name locally using Apple's location framework without tracking background routes), <strong>Manual Typing</strong>, or <strong>Leave Blank</strong>. Coordinates are never sent to third-party servers."),

            ("How do I change the app's language?",
             "ReWine is 100% localized into 7 languages (English, Spanish, French, Italian, Portuguese, Russian, and Simplified Chinese). Select your language during onboarding or change it anytime by tapping the flag pill button in the top navigation bar of «My Journal»."),

            ("Can I use ReWine without an internet connection?",
             "Yes, completely offline. ReWine is built on a local-first architecture for underground cellars, barrel rooms, or remote vineyards. If iCloud backup is enabled on your iPhone or iPad, your tastings and photos are backed up securely and encrypted in your personal Apple iCloud storage.")
        ],
        "contact_title": "Direct Developer Contact",
        "contact_desc": "Have a question, feature suggestion, or need technical assistance? Contact us directly and we will respond promptly:",
        "compat": "Compatibility: iOS 17.0 or higher (iPhone and iPad).",
        "dev": "Developer: JACOOR."
    },
    "fr": {
        "title": "Support Technique & Contact — ReWine",
        "meta_desc": "Centre d'assistance officiel ReWine. FAQ sur les niveaux de sommelier, langues, dictée vocale, filtres, 400+ AOP, export PDF et contact.",
        "h1": "Support Technique ReWine",
        "subtitle": "Centre d'aide officiel, questions fréquentes et guide des nouveautés œnologiques.",
        "faqs": [
            ("Comment fonctionne le Niveau de Sommelier et quels sont les critères de chaque rang ?",
             "Le système de progression de ReWine évalue votre parcours de dégustation selon <strong>5 rangs de maîtrise</strong> :<br>"
             "• <strong>Débutant :</strong> Dès 1 vin dégusté.<br>"
             "• <strong>Passionné :</strong> 20+ vins, 4+ Appellations/IGP et 3+ pays dégustés.<br>"
             "• <strong>Intermédiaire :</strong> 50+ vins, 7+ Appellations/IGP et 5+ pays dégustés.<br>"
             "• <strong>Supérieur :</strong> 100+ vins, 15+ Appellations/IGP, 7+ pays et 2+ types de produits.<br>"
             "• <strong>Master of Wine :</strong> 200+ vins, 30+ Appellations/IGP, 12+ pays et 3+ types de produits.<br>"
             "Touchez la carte Niveau Sommelier dans l'onglet «Statistiques» pour ouvrir la feuille de route interactive avec trophées, pourcentage de progression, conseils de sommelier et jalons manquants."),

            ("Comment fonctionne la dictée vocale pour noter les impressions sensorielles ?",
             "Dans les champs d'observations visuelles, olfactives et gustatives, touchez l'icône de microphone pour parler naturellement. ReWine transcrit votre voix en temps réel. La transcription est traitée <strong>100% localement sur votre appareil</strong> via le framework Speech natif d'Apple. Aucun fichier audio n'est conservé ni transmis à des serveurs tiers."),

            ("Quelle est la différence entre arômes primaires, secondaires et tertiaires ?",
             "La roue des arômes de ReWine respecte la méthode officielle de dégustation :<br>"
             "• <strong>Arômes Primaires :</strong> Issus du cépage et du terroir (agrumes, fruits blancs, fruits à noyau, fruits exotiques, fruits rouges, noirs, fleurs et notes végétales).<br>"
             "• <strong>Arômes Secondaires :</strong> Produits par les fermentations alcoolique et malolactique et l'élevage sur lies (notes lactiques, beurre, brioche).<br>"
             "• <strong>Arômes Tertiaires :</strong> Développés lors du vieillissement en fût de chêne, solera et garde en bouteille (épices, vanille, boisé, fruits secs et minéraux de garde)."),

            ("Comment fonctionnent les filtres avancés et la normalisation des cépages ?",
             "Dans «Mon Carnet», filtrez selon les 7 dimensions officielles : Type de produit, Effervescence, Couleur, Millésime, AOP/IGP, Pays et Cépage. Le filtre des cépages <strong>normalise automatiquement les dénominations</strong> (ex. 'Tempranillo 5%' ou '10%' sont regroupés sous 'Tempranillo' sans doublons ni pourcentages)."),

            ("Quelles régions viticoles sont intégrées dans le catalogue mondial ?",
             "ReWine regroupe <strong>plus de 400 Appellations d'Origine et IGP mondiales</strong>. Toutes les régions de France, Espagne, Italie, Portugal, Allemagne, États-Unis, Argentine, Chili, Afrique du Sud, Australie, Nouvelle-Zélande, ainsi que la Hongrie (Tokaj, Eger, etc.) et le Liban (Bekaa, Batroun, etc.) avec leurs drapeaux nationaux."),

            ("Comment exporter les fiches en PDF et quel est le rendu des photos ?",
             "Depuis n'importe quelle fiche, appuyez sur «Exporter en PDF». ReWine génère un document éditorial A4 vintage sur papier parchemin avec liseré doré dans la langue active. Les photos <strong>conservent 100% de leur ratio d'aspect original</strong> sans rognage."),

            ("Comment fonctionne le lieu de dégustation par GPS et qu'en est-il de la confidentialité ?",
             "Choisissez entre : <strong>GPS Automatique</strong> (détection locale du domaine ou restaurant via Apple sans suivi d'itinéraire), <strong>Saisie manuelle</strong> ou <strong>Laisser vide</strong>. Aucune coordonnée n'est transmise à l'extérieur."),

            ("Comment changer la langue de l'application ?",
             "ReWine est traduite intégralement en 7 langues. Vous pouvez choisir votre langue au lancement ou la changer à tout moment en touchant la pilule avec le drapeau dans l'en-tête de «Mon Carnet»."),

            ("L'application fonctionne-t-elle sans connexion Internet ?",
             "Oui, parfaitement hors ligne. Idéal pour les caves souterraines et vignobles isolés. Vos données sont synchronisées de façon chiffrée avec votre compte privé iCloud.")
        ],
        "contact_title": "Contact Direct avec le Développeur",
        "contact_desc": "Une question, une suggestion ou besoin d'assistance ? Écrivez-nous directement :",
        "compat": "Compatibilité : iOS 17.0 ou supérieur (iPhone et iPad).",
        "dev": "Développeur : JACOOR."
    },
    "it": {
        "title": "Supporto Tecnico & Contatto — ReWine",
        "meta_desc": "Centro di supporto ufficiale ReWine. Domande frequenti su livelli sommelier, lingue, dettatura vocale, filtri, 400+ DOC, export PDF e contatti.",
        "h1": "Supporto Tecnico ReWine",
        "subtitle": "Centro di assistenza ufficiale, domande frequenti e guida alle funzionalità enologiche.",
        "faqs": [
            ("Come funziona il Livello Sommelier e quali requisiti richiede ciascun livello?",
             "La progressione di ReWine valuta il tuo percorso di degustazione su <strong>5 livelli di maestria</strong>:<br>"
             "• <strong>Principiante:</strong> A partire da 1 vino degustato.<br>"
             "• <strong>Appassionato:</strong> 20+ vini, 4+ Denominazioni/IGP e 3+ paesi.<br>"
             "• <strong>Intermedio:</strong> 50+ vini, 7+ Denominazioni/IGP e 5+ paesi.<br>"
             "• <strong>Superiore:</strong> 100+ vini, 15+ Denominazioni/IGP, 7+ paesi e 2+ tipi di prodotto.<br>"
             "• <strong>Master of Wine:</strong> 200+ vini, 30+ Denominazioni/IGP, 12+ paesi e 3+ tipi di prodotto.<br>"
             "Toccando il riquadro Livello Sommelier in «Statistiche» si apre la schermata interattiva con medaglie, percentuale di completamento, consigli e requisiti mancanti per avanzare."),

            ("Come funziona la dettatura vocale per le note di degustazione ed è privata?",
             "Nelle sezioni delle osservazioni visive, olfattive e gustative puoi toccare l'icona del microfono e dettare liberamente le tue sensazioni. La trascrizione avviene <strong>al 100% localmente sul tuo dispositivo</strong> tramite il framework Apple Speech. ReWine non invia registrazioni audio a server esterni né archivia la tua voce."),

            ("Qual è la differenza tra aromi primari, secondari e terziari nella ruota?",
             "La ruota di ReWine adotta la classificazione enologica internazionale:<br>"
             "• <strong>Aromi Primari:</strong> Originati dall'uva e dal terroir (agrumi, frutti bianchi, drupacee, frutti tropicali, frutti rossi e neri, note floreali ed erbacee).<br>"
             "• <strong>Aromi Secondari:</strong> Nati dalla fermentazione e dall'affinamento sui lieviti (lattici, burro, panetteria, brioche).<br>"
             "• <strong>Aromi Terziari:</strong> Sviluppati durante la maturazione in botte di rovere, soleras e bottiglia (spezie, vaniglia, tostatura, frutta secca, cuoio e note minerali evolute)."),

            ("Come funzionano i filtri avanzati e la normalizzazione dei vitigni?",
             "In «Mio Taccuino» puoi filtrare per 7 dimensioni tecniche: Tipo di prodotto, Effervescenza, Colore, Annata, Denominazione/IGP, Paese e Vitigni. Il filtro <strong>normalizza automaticamente i vitigni</strong> raggruppando varianti come 'Tempranillo 5%' sotto un unico 'Tempranillo'."),

            ("Quali denominazioni sono incluse nel catalogo mondiale?",
             "ReWine include <strong>oltre 400 Denominazioni d'Origine e IGP mondiali</strong>. Copertura completa di Italia, Francia, Spagna, Portogallo, Germania, Stati Uniti, Argentina, Cile, Sudafrica, Australia, Nuova Zelanda, Ungheria e Libano con bandiere e nomi tradotti."),

            ("Come vengono esportate le schede in PDF e come sono visualizzate le foto?",
             "Toccando «Esporta in PDF», ReWine crea una scheda A4 vintage su carta pergamena con cornici dorate nella lingua attiva. Le fotografie <strong>mantengono il 100% delle proporzioni originali</strong> senza alcuna alterazione visiva."),

            ("Come funziona il rilevamento GPS del luogo di degustazione?",
             "Disponibili tre opzioni: <strong>GPS Automatico</strong> (geocodifica locale di cantina o ristorante tramite Apple senza tracciamento di percorsi), <strong>Manuale</strong> o <strong>Vuoto</strong>. Nessuna coordinata viene trasferita all'esterno."),

            ("Come si cambia la lingua dell'applicazione?",
             "ReWine è tradotta al 100% in 7 lingue. Puoi impostare la lingua al primo avvio o modificarla toccando la pillola della bandiera in alto in «Mio Taccuino»."),

            ("Posso usare l'app senza connessione a internet?",
             "Sì, ReWine funziona interamente offline. I tuoi dati e fotografie sono al sicuro e sincronizzati in modo crittografato tramite il tuo account privato iCloud.")
        ],
        "contact_title": "Contatto Diretto con lo Sviluppatore",
        "contact_desc": "Hai domande, suggerimenti o necessiti di supporto tecnico? Scrivici direttamente:",
        "compat": "Compatibilità: iOS 17.0 o superiore (iPhone e iPad).",
        "dev": "Sviluppatore: JACOOR."
    },
    "pt": {
        "title": "Suporte Técnico & Contacto — ReWine",
        "meta_desc": "Centro de suporte oficial ReWine. Perguntas frequentes sobre níveis de sommelier, idiomas, ditado por voz, filtros, 400+ D.O., exportação em PDF e contactos.",
        "h1": "Suporte Técnico ReWine",
        "subtitle": "Centro de ajuda oficial, perguntas frequentes e guia de novidades enológicas.",
        "faqs": [
            ("Como funciona o Nível de Sommelier e quais os requisitos de cada patamar?",
             "A progressão do ReWine avalia a sua experiência em <strong>5 níveis profissionais</strong>:<br>"
             "• <strong>Principiante:</strong> A partir de 1 vinho provado.<br>"
             "• <strong>Entusiasta:</strong> 20+ vinhos, 4+ Denominações/IGP e 3+ países.<br>"
             "• <strong>Médio:</strong> 50+ vinhos, 7+ Denominações/IGP e 5+ países.<br>"
             "• <strong>Superior:</strong> 100+ vinhos, 15+ Denominações/IGP, 7+ países e 2+ tipos de produto.<br>"
             "• <strong>Master of Wine:</strong> 200+ vinhos, 30+ Denominações/IGP, 12+ países e 3+ tipos de produto.<br>"
             "Toque no cartão Nível Sommelier no separador «Estatísticas» para abrir a folha de rota interativa com medalhas, percentagem, conselhos e os requisitos necessários para subir de nível."),

            ("Como funciona o ditado por voz para registar impressões sensoriais?",
             "Nos campos de observações visuais, olfativas e gustativas, toque no ícone do microfone para ditar as suas notas. A transcrição ocorre <strong>100% localmente no seu dispositivo</strong> através do framework Apple Speech. O ReWine não envia áudio para servidores externos nem armazena as suas gravações."),

            ("Qual a diferença entre aromas primários, secundários e terciários na roda?",
             "A roda de aromas do ReWine segue o rigor internacional da escanção:<br>"
             "• <strong>Aromas Primários:</strong> Provenientes da casta e do terroir (citrinos, fruta branca, caroço, tropical, frutos vermelhos, pretos, notas florais e vegetais).<br>"
             "• <strong>Aromas Secundários:</strong> Resultantes da fermentação alcoólica, maloláctica e borras finas (manteiga, panificação, brioche).<br>"
             "• <strong>Aromas Terciários:</strong> Adquiridos durante o estágio em barrica de carvalho, soleras e envelhecimento em garrafa (especiarias, baunilha, tosta, frutos secos e evolução)."),

            ("Como funcionam os filtros avançados e a normalização de castas?",
             "Em «Meu Caderno», filtre por 7 dimensões técnicas oficiais: Tipo de produto, Efervescência, Cor, Safra, D.O./IGP, País e Castas. O filtro <strong>normaliza automaticamente as castas</strong>, agrupando variações como 'Tempranillo 5%' sob 'Tempranillo'."),

            ("Que regiões estão incluídas no catálogo mundial?",
             "O catálogo do ReWine inclui <strong>mais de 400 Denominações de Origem e IGPs</strong> de todo o mundo: Portugal (Douro, Alentejo, Dão, Vinho Verde, etc.), Espanha, França, Itália, Alemanha, EUA, Argentina, Chile, África do Sul, Austrália, Hungria e Líbano com bandeiras e nomes traduzidos."),

            ("Como se exportam as fichas em PDF e como surgem as fotografias?",
             "Toque em «Exportar para PDF» para gerar uma ficha A4 em pergaminho vintage com molduras douradas no idioma ativo. As fotografias <strong>mantêm 100% da sua proporção original</strong> sem qualquer corte."),

            ("Como funciona o registo de localização por GPS?",
             "Disponibiliza três opções: <strong>GPS Automático</strong> (resolução local da adega ou restaurante através da Apple sem rastreamento de rotas), <strong>Manual</strong> ou <strong>Em branco</strong>. Nenhuma coordenada é transmitida a terceiros."),

            ("Como altero o idioma da aplicação?",
             "O ReWine está traduzido em 7 idiomas. Escolha o seu idioma preferido no arranque ou altere-o a qualquer momento tocando na bandeira no topo de «Meu Caderno»."),

            ("Posso utilizar a aplicação sem ligação à Internet?",
             "Sim, funciona totalmente offline. Ideal para caves subterrâneas e vinhedos isolados. Os seus dados são guardados de forma segura e encriptada no seu iCloud pessoal.")
        ],
        "contact_title": "Contacto Direto com o Programador",
        "contact_desc": "Tem alguma dúvida, sugestão ou necessita de assistência técnica? Contacte-nos diretamente:",
        "compat": "Compatibilidade: iOS 17.0 ou superior (iPhone e iPad).",
        "dev": "Programador: JACOOR."
    },
    "ru": {
        "title": "Техническая Поддержка & Контакты — ReWine",
        "meta_desc": "Официальный центр поддержки ReWine. Ответы на частые вопросы об уровнях сомелье, языках, голосовом вводе, фильтрах, 400+ апелласьонах, PDF и контактах.",
        "h1": "Техническая Поддержка ReWine",
        "subtitle": "Официальный центр помощи, частые вопросы и руководство по винным функциям.",
        "faqs": [
            ("Как работает система уровней сомелье и каковы требования для каждого ранга?",
             "Геймифицированная система ReWine оценивает ваш дегустационный путь по <strong>5 уровням мастерства</strong>:<br>"
             "• <strong>Начинающий:</strong> Начиная с 1 продегустированного вина.<br>"
             "• <strong>Любитель:</strong> 20+ вин, 4+ апелласьона/IGP и 3+ страны.<br>"
             "• <strong>Средний:</strong> 50+ вин, 7+ апелласьонов/IGP и 5+ стран.<br>"
             "• <strong>Высший:</strong> 100+ вин, 15+ апелласьонов/IGP, 7+ стран и 2+ типа продукта.<br>"
             "• <strong>Master of Wine:</strong> 200+ вин, 30+ апелласьонов/IGP, 12+ стран и 3+ типа продукта.<br>"
             "Нажатие на карточку уровня во вкладке «Статистика» открывает интерактивный экран с трофеями, процентом прогресса, советами сомелье и точным списком условий для повышения ранга."),

            ("Как работает голосовая диктовка дегустационных заметок и насколько это безопасно?",
             "В полях визуальных, обонятельных и вкусовых заметок нажмите на значок микрофона и говорите в обычном темпе. Распознавание речи происходит <strong>на 100% локально на вашем устройстве</strong> с помощью нативного фреймворка Apple Speech. ReWine не отправляет аудио на внешние серверы и не сохраняет записи голоса."),

            ("В чем различие первичных, вторичных и третичных ароматов в колесе ароматов?",
             "Колесо ароматов ReWine основано на стандартах международной школы сомелье:<br>"
             "• <strong>Первичные ароматы:</strong> Исходят от самого винограда и терруара (цитрусовые, белые фрукты, косточковые, тропические, красные и черные ягоды, цветы, травы).<br>"
             "• <strong>Вторичные ароматы:</strong> Возникают в процессе брожения и выдержки на осадке (сливочные ноты, масло, выпечка, бриошь).<br>"
             "• <strong>Третичные ароматы:</strong> Формируются при выдержке в дубовых бочках, солерах и при бутылочной выдержке (пряности, ваниль, древесина, орехи, кожа, минералы зрелости)."),

            ("Как работают расширенные фильтры и нормализация сортов винограда?",
             "В «Моем Дневнике» фильтруйте по 7 официальным категориям: Тип продукта, Игристость, Цвет, Год урожая, Апелласьон/IGP, Страна и Сорта винограда. Фильтр <strong>автоматически нормализует сорта</strong>: записи вроде 'Tempranillo 5%' объединяются в чистый 'Tempranillo' без повторов."),

            ("Какие винные регионы включены в мировой каталог?",
             "Каталог ReWine насчитывает <strong>более 400 официальных апелласьонов и защищенных географических указаний</strong> со всего мира: Испания, Франция, Италия, Португалия, Германия, США, Аргентина, Чили, ЮАР, Австралия, Новая Зеландия, Венгрия и Ливан с флагами и переведенными названиями."),

            ("Как экспортируются дегустационные листы в PDF и как отображаются фотографии?",
             "Нажмите «Экспорт в PDF» для генерации листа формата А4 на винтажном пергаменте с золотым обрамлением на выбранном языке. Фотографии масштабируются с <strong>100% сохранением исходных пропорций</strong> без искажений."),

            ("Как работает фиксация места дегустации по GPS?",
             "Доступны три варианта: <strong>Авто-GPS</strong> (локальное определение винодельни или ресторана через службы Apple без отслеживания маршрутов), <strong>Ручной ввод</strong> или <strong>Оставить пустым</strong>. Координаты не передаются третьим сторонам."),

            ("Как изменить язык приложения?",
             "ReWine полностью переведено на 7 языков. Выберите язык при первом запуске или смените его в любой момент, нажав на плашку с флагом в верхней панели «Моего Дневника»."),

            ("Работает ли приложение без подключения к интернету?",
             "Да, полностью автономно. Отлично подходит для винных погребов и удаленных виноградников. Ваши данные надежно и конфиденциально синхронизируются через личный аккаунт iCloud.")
        ],
        "contact_title": "Прямой Контакт с Разработчиком",
        "contact_desc": "Есть вопросы, предложения или требуется техническая помощь? Напишите нам напрямую:",
        "compat": "Совместимость: iOS 17.0 или новее (iPhone и iPad).",
        "dev": "Разработчик: JACOOR."
    },
    "zh": {
        "title": "技术支持与客户服务 — ReWine",
        "meta_desc": "ReWine 官方支持中心。侍酒师段位进阶、多语言切换、本地语音口述、7大维度筛选、400+全球法定产区、PDF导出及开发者联络方式。",
        "h1": "ReWine 技术支持中心",
        "subtitle": "官方帮助中心、常见问题解答与品酒新特性深度指引。",
        "faqs": [
            ("侍酒师段位进阶体系是如何运作的？各级别晋升条件是什么？",
             "ReWine 进阶体系通过 <strong>5个段位</strong> 科学量化您的品鉴积累：<br>"
             "• <strong>初学者（Principiante）：</strong> 记录 1 款葡萄酒即可解锁。<br>"
             "• <strong>品酒爱好者（Aficionado）：</strong> 累计品评 20+ 款酒、覆盖 4+ 个法定产区及 3+ 个出产国。<br>"
             "• <strong>中级品酒师（Medio）：</strong> 累计品评 50+ 款酒、覆盖 7+ 个法定产区及 5+ 个出产国。<br>"
             "• <strong>高级侍酒师（Superior）：</strong> 累计品评 100+ 款酒、覆盖 15+ 个法定产区、7+ 个出产国及 2+ 种产品大类。<br>"
             "• <strong>葡萄酒大师（Master of Wine）：</strong> 累计品评 200+ 款酒、覆盖 30+ 个法定产区、12+ 个出产国及 3+ 种产品大类。<br>"
             "在「品酒统计」页面轻触侍酒师段位卡片，即可呼出交互式进阶面板，直观查看荣誉勋章、达成进度百分比、侍酒师金句及晋升下一级所需的具体指标。"),

            ("语音口述录入品酒笔记是如何工作的？是否能保证隐私？",
             "在外观、嗅觉与口感观察框中轻触麦克风图标，即可自由口述品酒感受，文字将实时录入。语音识别依托Apple系统原生Speech框架 <strong>100%在您的设备端本地运算</strong>。ReWine 绝不上传录音至外部云端服务器，亦不保留任何音频文件，彻底守护您的隐私。"),

            ("风味轮盘中的一类、二类与三类香气有何区别？",
             "ReWine 严格遵循国际专业侍酒师（WSET/OIV）的感官分类体系：<br>"
             "• <strong>一类香气（Primary）：</strong> 源自葡萄品种与产区风土的原生果香、花香与植物气息（柑橘、白果、核果、热带水果、红黑浆果、花香与草本）。<br>"
             "• <strong>二类香气（Secondary）：</strong> 酒精发酵、苹果酸-乳酸发酵及酒泥接触产生的风味（乳脂、黄油、烘焙与奶油面包）。<br>"
             "• <strong>三类香气（Tertiary）：</strong> 橡木桶陈酿、索莱拉陈年与瓶中熟化形成的复杂风味（辛香料、香草、烤木、坚果、皮革及陈年矿物感）。"),

            ("多维高级筛选与葡萄品种标准化是如何实现的？",
             "在「我的笔记本」中支持按7大维度精准筛选：产品类型、气泡性格、酒色、年份、法定产区、出产国与葡萄品种。品种筛选器 <strong>自动标准化聚合</strong>：例如含有“Tempranillo 5%”或“Tempranillo 10%”的记录将自动归并在纯净的“Tempranillo”词条下，无任何冗余重复。"),

            ("全球产区图谱收录了哪些产区？",
             "收录了全球 <strong>400多个官方知名法定产区与IGP地理标志</strong>。全面覆盖西班牙、法国、意大利、葡萄牙、德国、美国、阿根廷、智利、南非、澳大利亚、新西兰，并全新纳入匈牙利（托卡伊、埃格尔等）与黎巴嫩（贝卡谷地、巴特伦等），全部配备国旗标识及多语言名称。"),

            ("PDF品酒报告是如何生成的？照片比例是否会失真？",
             "轻触「导出为PDF」，系统将即时以当前所选语言生成A4规格的复古羊皮纸排版报告。酒标、杯中酒或木塞照片均经过高精度几何运算，<strong>100%保留原始摄影宽高比</strong>，配以精致烫金边框，杜绝任何形变。"),

            ("GPS品酒地点定位模式及隐私说明：",
             "提供三种模式：<strong>自动GPS</strong>（调用Apple本地定位服务解析酒庄或餐厅名称，不记录任何行动轨迹）、<strong>手动输入</strong> 或 <strong>留空</strong>。所有地理信息绝不传输给任何第三方。"),

            ("如何切换应用程序语言？",
             "ReWine 完整支持7种主流语言。在首次启动时可自由选择，日常使用中也可随时轻触「我的笔记本」顶部导航栏的国旗胶囊按钮动态切换。"),

            ("在无网络环境下能否正常使用？",
             "完全支持纯离线运作。特别适用于地下酒窖、防空洞酒库或偏远葡萄园。若您开启了Apple iCloud备份，您的数据和照片将通过端到端加密安全存储于您的私人云端。")
        ],
        "contact_title": "直接联络开发者",
        "contact_desc": "如果您有任何功能建议、技术疑问或商务咨询，欢迎直接与我们取得联系：",
        "compat": "系统兼容性：iOS 17.0 或更高版本（支持 iPhone 与 iPad）。",
        "dev": "开发者：JACOOR。"
    }
}

# PRIVACY POLICY DATA
PRIVACY_DATA = {
    "es": {
        "title": "Política de Privacidad — ReWine",
        "meta_desc": "Política de Privacidad oficial de ReWine. Privacidad absoluta: almacenamiento 100% local, reconocimiento de voz on-device, sin rastreo y control total.",
        "h1": "Política de Privacidad",
        "updated": "Última actualización: 18 de octubre de 2026",
        "sections": [
            ("1. Compromiso Fundamental de Privacidad",
             "<p>En <strong>ReWine</strong> (desarrollada por JACOOR), la privacidad y la confidencialidad de tus datos constituyen nuestra máxima prioridad. Diseñamos la aplicación bajo el principio de <em>Privacidad por Diseño</em> (Privacy by Design), garantizando que tu experiencia enológica permanezca siempre bajo tu control exclusivo.</p>"),

            ("2. Cero Recopilación de Datos Personales",
             "<p><strong>ReWine NO recopila, transmite, vende ni comparte ningún tipo de dato personal con terceros.</strong></p>"
             "<ul>"
             "<li>No recopilamos correos electrónicos, nombres reales, números telefónicos ni perfiles de usuario.</li>"
             "<li>No recopilamos identificadores de publicidad (IDFA) ni identificadores únicos de dispositivo (IDFV).</li>"
             "<li>No integramos SDKs de analítica invasiva, rastreadores de comportamiento ni redes de publicidad (Tracking = NO).</li>"
             "<li>No rastreamos tu ubicación en segundo plano ni almacenamos historiales de desplazamiento.</li>"
             "</ul>"),

            ("3. Almacenamiento Estrictamente Local",
             "<p>Toda la información registrada en ReWine se almacena de forma única y exclusiva en la memoria interna de tu dispositivo (Sandbox local de iOS / iPadOS):</p>"
             "<ul>"
             "<li><strong>Fichas Técnicas de Cata:</strong> Nombre del vino, bodega, tipo de producto, efervescencia, color, añada, variedades de uva, lugar de la cata, nombre del catador o sommelier, observaciones sensoriales, nivel sommelier y puntuaciones quedan guardados localmente.</li>"
             "<li><strong>Fotografías Enológicas:</strong> Las imágenes capturadas de botellas, etiquetas, copas, tapones o maridajes se comprimen y conservan en el directorio privado de la app, manteniendo el 100% de sus proporciones originales.</li>"
             "<li><strong>Copia de Seguridad en iCloud:</strong> Si tienes habilitada la copia de seguridad de iCloud en tu iPhone o iPad, tus datos se respaldan de manera cifrada en tu cuenta personal de Apple, sin acceso para ReWine ni para terceros.</li>"
             "</ul>"),

            ("4. Uso Transparente de Permisos del Dispositivo",
             "<p>ReWine únicamente solicita permisos del sistema cuando son estrictamente necesarios para prestar las funcionalidades solicitadas por el usuario:</p>"
             "<ul>"
             "<li><strong>Ubicación Durante el Uso (NSLocationWhenInUseUsageDescription):</strong> Permiso opcional utilizado única y exclusivamente cuando el usuario pulsa la opción «GPS Automático» para registrar el lugar, bodega o restaurante donde se efectúa la cata. La ubicación se resuelve en el propio dispositivo mediante el servicio de geocodificación de Apple. ReWine nunca transmite coordenadas a servidores propios o externos, no rastrea en segundo plano y ofrece siempre las alternativas de introducir el lugar manualmente o dejarlo en blanco.</li>"
             "<li><strong>Micrófono y Reconocimiento de Voz (NSMicrophoneUsageDescription & NSSpeechRecognitionUsageDescription):</strong> Utilizados de forma puntual y exclusiva cuando pulsas el icono de micrófono para dictar por voz tus impresiones sensoriales (visuales, olfativas o gustativas). El reconocimiento de voz se procesa <strong>100% en local en el propio dispositivo</strong> mediante el framework nativo de Apple. ReWine <strong>NUNCA almacena archivos de audio</strong>, no graba en segundo plano ni envía tus grabaciones a servidores externos.</li>"
             "<li><strong>Cámara (NSCameraUsageDescription):</strong> Se solicita exclusivamente para permitirte tomar fotografías de botellas, etiquetas, copas o maridajes en el momento de la cata. Las capturas se procesan y almacenan de forma local.</li>"
             "<li><strong>Galería de Fotos (NSPhotoLibraryUsageDescription):</strong> Se solicita únicamente para que puedas adjuntar imágenes existentes desde el carrete de tu dispositivo a tus fichas de cata.</li>"
             "</ul>"),

            ("5. Documentos Exportados en PDF y Compartición",
             "<p>Las fichas de cata maquetadas en PDF se generan íntegramente mediante el motor gráfico de iOS en tu propio dispositivo. Se componen con diseño vintage en el idioma activo, respetando la relación de aspecto de tus fotografías y mostrando el nombre del catador y lugar de la cata. Los documentos solo se transfieren cuando decides compartirlos voluntariamente a través del menú nativo de iOS (AirDrop, Correo, Mensajes o impresión AirPrint).</p>"),

            ("6. Menores de Edad y Clasificación",
             "<p>ReWine es una herramienta de registro técnico, cultural y sensorial orientada a aficionados y profesionales de la sumillería y enología. Cumple estrictamente con las directrices de Apple App Store y no comercializa, distribuye ni promociona la venta directa de bebidas alcohólicas.</p>"
             "<p><strong>Aviso de Mayoría de Edad y Consumo Responsable:</strong> La aplicación cuenta con una clasificación oficial <strong>17+</strong> en Apple App Store. ReWine está destinada exclusivamente a personas que hayan alcanzado la mayoría de edad legal para el consumo de alcohol (+18 años en España y la Unión Europea). Promovemos activamente el consumo moderado y la cultura enológica responsable. El consumo excesivo de alcohol es perjudicial para la salud.</p>"),

            ("7. Contacto Directo",
             "<p>Si tienes cualquier duda, consulta o sugerencia sobre nuestra política de privacidad, puedes comunicarte directamente con nosotros:</p>"
             "<p><strong>Correo Electrónico de Asistencia:</strong> <a href=\"mailto:ayeneso2023@gmail.com\" style=\"color: var(--accent-magenta); font-weight: 600;\">ayeneso2023@gmail.com</a><br>"
             "<strong>Desarrollador:</strong> JACOOR</p>")
        ]
    },
    "en": {
        "title": "Privacy Policy — ReWine",
        "meta_desc": "Official ReWine Privacy Policy. Absolute privacy: 100% local storage, on-device voice recognition, no tracking, and total user data control.",
        "h1": "Privacy Policy",
        "updated": "Last updated: October 18, 2026",
        "sections": [
            ("1. Fundamental Commitment to Privacy",
             "<p>At <strong>ReWine</strong> (developed by JACOOR), your privacy and data confidentiality are our highest priority. We engineered the app following the principle of <em>Privacy by Design</em>, ensuring that your wine tasting journey remains entirely under your personal control.</p>"),

            ("2. Zero Personal Data Collection",
             "<p><strong>ReWine DOES NOT collect, transmit, sell, or share any personal data with third parties.</strong></p>"
             "<ul>"
             "<li>We do not collect email addresses, names, phone numbers, or account profiles.</li>"
             "<li>We do not collect Advertising Identifiers (IDFA) or Vendor Identifiers (IDFV).</li>"
             "<li>We do not integrate invasive analytics SDKs, behavioral trackers, or ad networks (Tracking = NO).</li>"
             "<li>We never track your background location or maintain movement histories.</li>"
             "</ul>"),

            ("3. Strictly Local Storage",
             "<p>All information entered into ReWine is stored exclusively on your device's internal storage (iOS / iPadOS local app sandbox):</p>"
             "<ul>"
             "<li><strong>Technical Tasting Sheets:</strong> Wine name, winery, product type, effervescence, color, vintage, grape varieties, venue, sommelier name, sensory impressions, sommelier level, and scores are stored locally.</li>"
             "<li><strong>Wine Photography:</strong> Captured photos of bottles, labels, glasses, corks, or pairings are compressed and saved in the app's private documents directory, preserving 100% of their original aspect ratio.</li>"
             "<li><strong>iCloud Backup:</strong> If iCloud backup is active on your device, your data is securely and encrypted backed up to your personal Apple account without access by ReWine or third parties.</li>"
             "</ul>"),

            ("4. Transparent Device Permissions",
             "<p>ReWine only requests system permissions when strictly necessary to fulfill user-initiated actions:</p>"
             "<ul>"
             "<li><strong>Location When In Use (NSLocationWhenInUseUsageDescription):</strong> An optional permission used exclusively when you tap «Auto GPS» to identify the winery, restaurant, or municipality of your tasting. Geocoding is resolved locally on the device using Apple services. Coordinates are never sent to external servers, background tracking is not used, and manual or blank options are always available.</li>"
             "<li><strong>Microphone & Speech Recognition (NSMicrophoneUsageDescription & NSSpeechRecognitionUsageDescription):</strong> Requested solely when you tap the microphone button to dictate sensory tasting notes (visual, olfactory, or palate). Speech recognition runs <strong>100% locally on your device</strong> via Apple's native framework. ReWine <strong>NEVER stores audio files</strong>, does not record in the background, and never transmits voice recordings to external servers.</li>"
             "<li><strong>Camera (NSCameraUsageDescription):</strong> Requested solely to allow you to take photos of wine bottles, labels, glasses, or pairings during tastings. Photos are processed and saved locally.</li>"
             "<li><strong>Photo Library (NSPhotoLibraryUsageDescription):</strong> Requested solely to let you attach existing photos from your camera roll to tasting records.</li>"
             "</ul>"),

            ("5. Exported PDF Documents and Sharing",
             "<p>Tasting sheets formatted as PDFs are generated entirely on your device using iOS rendering engines. They feature vintage parchment styling in the active language, preserving original photo aspect ratios and sommelier signatures. Files are only shared when you explicitly initiate an action via iOS sharing menus (AirDrop, Mail, Messages, or AirPrint).</p>"),

            ("6. Age Rating & Responsible Drinking",
             "<p>ReWine is a technical, educational, and sensory notebook intended for wine enthusiasts and certified sommeliers. It strictly complies with Apple App Store guidelines and does not sell, distribute, or promote alcoholic beverage purchases.</p>"
             "<p><strong>Age Advisory & Responsible Enjoyment:</strong> The application holds an official <strong>17+</strong> rating on the Apple App Store. ReWine is intended exclusively for individuals of legal drinking age (+18 in most jurisdictions). We actively champion moderation and wine culture. Excessive alcohol consumption is harmful to health.</p>"),

            ("7. Direct Contact",
             "<p>If you have any questions or feedback regarding our privacy policy, please contact us directly:</p>"
             "<p><strong>Support Email:</strong> <a href=\"mailto:ayeneso2023@gmail.com\" style=\"color: var(--accent-magenta); font-weight: 600;\">ayeneso2023@gmail.com</a><br>"
             "<strong>Developer:</strong> JACOOR</p>")
        ]
    },
    "fr": {
        "title": "Politique de Confidentialité — ReWine",
        "meta_desc": "Politique de confidentialité officielle de ReWine. Confidentialité absolue : stockage 100% local, dictée vocale locale, sans traceur et contrôle total.",
        "h1": "Politique de Confidentialité",
        "updated": "Dernière mise à jour : 18 octobre 2026",
        "sections": [
            ("1. Engagement Fondamental de Confidentialité",
             "<p>Chez <strong>ReWine</strong> (développé par JACOOR), la confidentialité de vos données est notre priorité absolue. Nous concevons l'application selon le principe de <em>Privacy by Design</em>, garantissant que vos dégustations restent sous votre contrôle exclusif.</p>"),

            ("2. Zéro Collecte de Données Personnelles",
             "<p><strong>ReWine NE collecte, NE transmet, NE vend et NE partage aucune donnée personnelle avec des tiers.</strong></p>"
             "<ul>"
             "<li>Aucune collecte d'e-mails, de noms, de numéros de téléphone ni de profils.</li>"
             "<li>Aucune collecte d'identifiants publicitaires (IDFA) ni d'identifiants appareil (IDFV).</li>"
             "<li>Aucun SDK d'analyse invasive, ni outil de pistage ni réseau publicitaire (Tracking = NON).</li>"
             "<li>Aucun suivi d'emplacement en arrière-plan ni historique de déplacements.</li>"
             "</ul>"),

            ("3. Stockage Strictement Local",
             "<p>Toutes les données saisies dans ReWine sont stockées exclusivement dans la mémoire interne de votre appareil (Sandbox iOS / iPadOS) :</p>"
             "<ul>"
             "<li><strong>Fiches Techniques :</strong> Nom du vin, domaine, type de produit, effervescence, couleur, millésime, cépages, lieu, nom du sommelier, notes sensorielles, niveau sommelier et scores sont conservés localement.</li>"
             "<li><strong>Photos Œnologiques :</strong> Les clichés de bouteilles, étiquettes, verres ou bouchons sont conservés dans le répertoire privé de l'app, en préservant 100% de leur ratio d'aspect original.</li>"
             "<li><strong>Sauvegarde iCloud :</strong> Si la sauvegarde iCloud est activée, vos données sont sauvegardées de manière chiffrée sur votre compte Apple personnel sans accès par ReWine.</li>"
             "</ul>"),

            ("4. Utilisation Transparente des Autorisations",
             "<p>ReWine ne sollicite des autorisations système que lorsque cela est strictement nécessaire :</p>"
             "<ul>"
             "<li><strong>Localisation Pendant l'Utilisation (NSLocationWhenInUseUsageDescription) :</strong> Utilisée exclusivement lorsque vous touchez «GPS Automatique» pour identifier le domaine ou le restaurant. La géocodification est résolue localement via Apple. Les coordonnées ne sont jamais transmises à des tiers.</li>"
             "<li><strong>Microphone & Reconnaissance Vocale (NSMicrophoneUsageDescription & NSSpeechRecognitionUsageDescription) :</strong> Sollicités uniquement lorsque vous touchez le micro pour dicter vos notes. Le traitement s'effectue <strong>100% localement sur votre appareil</strong> via le framework Apple. ReWine <strong>NE conserve AUCUN fichier audio</strong> et n'enregistre jamais en arrière-plan.</li>"
             "<li><strong>Appareil Photo (NSCameraUsageDescription) :</strong> Utilisé pour prendre des photos de bouteilles, verres ou étiquettes lors de la dégustation.</li>"
             "<li><strong>Bibliothèque Photos (NSPhotoLibraryUsageDescription) :</strong> Utilisée pour importer des photos existantes de votre galerie.</li>"
             "</ul>"),

            ("5. Documents PDF et Partage Volontaire",
             "<p>Les fiches de dégustation en PDF sont générées sur votre appareil avec un design parchemin vintage dans la langue active. Les fichiers ne sont transmis que lorsque vous choisissez délibérément de les partager via les options natives d'iOS (AirDrop, Mail, Messages, etc.).</p>"),

            ("6. Classification d'Âge & Consommation Responsable",
             "<p>ReWine est un carnet technique et culturel destiné aux passionnés et professionnels. L'application respecte les directives de l'App Store et ne commercialise aucun alcool.</p>"
             "<p><strong>Avertissement Légal :</strong> Classée <strong>17+</strong> sur l'App Store, ReWine s'adresse exclusivement aux personnes majeures (+18 ans). Nous encourageons la modération. L'abus d'alcool est dangereux pour la santé.</p>"),

            ("7. Contact Direct",
             "<p>Pour toute question concernant notre politique de confidentialité :</p>"
             "<p><strong>E-mail d'Assistance :</strong> <a href=\"mailto:ayeneso2023@gmail.com\" style=\"color: var(--accent-magenta); font-weight: 600;\">ayeneso2023@gmail.com</a><br>"
             "<strong>Développeur :</strong> JACOOR</p>")
        ]
    },
    "it": {
        "title": "Informativa sulla Privacy — ReWine",
        "meta_desc": "Informativa sulla privacy ufficiale di ReWine. Privacy assoluta: archiviazione 100% locale, riconoscimento vocale on-device, nessun tracciamento e controllo totale.",
        "h1": "Informativa sulla Privacy",
        "updated": "Ultimo aggiornamento: 18 ottobre 2026",
        "sections": [
            ("1. Impegno Fondamentale per la Privacy",
             "<p>In <strong>ReWine</strong> (sviluppata da JACOOR), la riservatezza dei tuoi dati è la nostra priorità assoluta. Applichiamo il principio di <em>Privacy by Design</em> affinché la tua esperienza enologica rimanga interamente sotto il tuo controllo.</p>"),

            ("2. Zero Raccolta di Dati Personali",
             "<p><strong>ReWine NON raccoglie, trasmette, vende né condivide alcun dato personale con terze parti.</strong></p>"
             "<ul>"
             "<li>Non raccogliamo indirizzi e-mail, nomi, numeri telefonici né profili utente.</li>"
             "<li>Non raccogliamo ID pubblicitari (IDFA) né ID dispositivo (IDFV).</li>"
             "<li>Non integriamo SDK di analisi invasiva né reti pubblicitarie (Tracking = NO).</li>"
             "<li>Non monitoriamo la posizione in background né memorizziamo percorsi.</li>"
             "</ul>"),

            ("3. Archiviazione Rigorosamente Locale",
             "<p>Tutte le informazioni registrate in ReWine risiedono unicamente nella memoria interna del tuo dispositivo (Sandbox locale iOS / iPadOS):</p>"
             "<ul>"
             "<li><strong>Schede di Degustazione:</strong> Nome del vino, cantina, tipo di prodotto, effervescenza, colore, annata, vitigni, luogo, sommelier, note sensoriali, livello sommelier e voti sono conservati localmente.</li>"
             "<li><strong>Fotografie Enologiche:</strong> Le immagini di bottiglie, etichette o calici sono salvate nella cartella privata dell'app, preservando il 100% delle proporzioni originali.</li>"
             "<li><strong>Backup su iCloud:</strong> Con il backup iCloud attivo, i tuoi dati sono salvati in forma crittografata sul tuo account personale Apple.</li>"
             "</ul>"),

            ("4. Uso Trasparente delle Autorizzazioni",
             "<p>ReWine richiede permessi di sistema solo quando strettamente necessari:</p>"
             "<ul>"
             "<li><strong>Posizione Durante l'Uso (NSLocationWhenInUseUsageDescription):</strong> Utilizzata unicamente con l'opzione «GPS Automatico» per rilevare la cantina o il ristorante. La geocodifica avviene sul dispositivo tramite Apple senza invio di coordinate all'esterno.</li>"
             "<li><strong>Microfono & Riconoscimento Vocale (NSMicrophoneUsageDescription & NSSpeechRecognitionUsageDescription):</strong> Utilizzati esclusivamente per la dettatura vocale delle note sensoriali. L'elaborazione avviene <strong>al 100% localmente sul dispositivo</strong> tramite il framework Apple. ReWine <strong>NON conserva file audio</strong> né registra in background.</li>"
             "<li><strong>Fotocamera (NSCameraUsageDescription):</strong> Per scattare foto a bottiglie, calici ed etichette durante la degustazione.</li>"
             "<li><strong>Libreria Foto (NSPhotoLibraryUsageDescription):</strong> Per allegare immagini esistenti dalla galleria.</li>"
             "</ul>"),

            ("5. Documenti PDF Esportati e Condivisione",
             "<p>Le schede PDF vengono composte sul dispositivo con stile pergamena vintage nella lingua attiva. Vengono condivise solo su tua esplicita iniziativa tramite il menu nativo di iOS.</p>"),

            ("6. Classificazione per Età & Consumo Responsabile",
             "<p>ReWine è uno strumento tecnico e culturale destinato ad appassionati e professionisti. Conforme alle linee guida di App Store, non commercializza bevande alcoliche.</p>"
             "<p><strong>Avviso di Età:</strong> Classificazione <strong>17+</strong> su App Store. Destinata esclusivamente a maggiorenni (+18 anni). Promuoviamo un consumo moderato e responsabile.</p>"),

            ("7. Contatto Diretto",
             "<p>Per qualsiasi domanda sulla nostra informativa sulla privacy:</p>"
             "<p><strong>Email di Assistenza:</strong> <a href=\"mailto:ayeneso2023@gmail.com\" style=\"color: var(--accent-magenta); font-weight: 600;\">ayeneso2023@gmail.com</a><br>"
             "<strong>Sviluppatore:</strong> JACOOR</p>")
        ]
    },
    "pt": {
        "title": "Política de Privacidade — ReWine",
        "meta_desc": "Política de Privacidade oficial do ReWine. Privacidade absoluta: armazenamento 100% local, reconhecimento vocal no dispositivo, sem rastreamento e controlo total.",
        "h1": "Política de Privacidade",
        "updated": "Última atualização: 18 de outubro de 2026",
        "sections": [
            ("1. Compromisso Fundamental de Privacidade",
             "<p>No <strong>ReWine</strong> (desenvolvido por JACOOR), a privacidade e confidencialidade dos seus dados são a nossa máxima prioridade. Adotamos o princípio de <em>Privacy by Design</em> para garantir que a sua experiência enológica permaneça sob o seu controlo exclusivo.</p>"),

            ("2. Zero Recolha de Dados Pessoais",
             "<p><strong>O ReWine NÃO recolhe, transmite, vende nem partilha quaisquer dados pessoais com terceiros.</strong></p>"
             "<ul>"
             "<li>Não recolhemos e-mails, nomes reais, contactos nem perfis de utilizador.</li>"
             "<li>Não recolhemos identificadores publicitários (IDFA) nem de dispositivo (IDFV).</li>"
             "<li>Não integramos SDKs analíticos invasivos nem redes de anúncios (Tracking = NÃO).</li>"
             "<li>Não monitorizamos a localização em segundo plano nem guardamos históricos de deslocação.</li>"
             "</ul>"),

            ("3. Armazenamento Estritamente Local",
             "<p>Toda a informação registada no ReWine reside unicamente na memória interna do seu dispositivo (Sandbox local iOS / iPadOS):</p>"
             "<ul>"
             "<li><strong>Fichas Técnicas de Prova:</strong> Nome do vinho, produtor, tipo de produto, efervescência, cor, safra, castas, local, sommelier, observações sensoriais, nível sommelier e pontuações são guardados localmente.</li>"
             "<li><strong>Fotografias Enológicas:</strong> As fotos de garrafas, rótulos ou taças são guardadas no diretório privado da app, mantendo 100% da sua proporção original.</li>"
             "<li><strong>Cópia de Segurança no iCloud:</strong> Se tiver o backup do iCloud ativo, os seus dados são salvaguardados de forma encriptada na sua conta pessoal Apple.</li>"
             "</ul>"),

            ("4. Uso Transparente de Permissões",
             "<p>O ReWine solicita permissões apenas quando estritamente necessárias:</p>"
             "<ul>"
             "<li><strong>Localização Durante a Utilização (NSLocationWhenInUseUsageDescription):</strong> Utilizada exclusivamente com a opção «GPS Automático» para identificar a adega ou restaurante. A geocodificação é resolvida localmente através da Apple. Nenhuma coordenada é transmitida a servidores externos.</li>"
             "<li><strong>Microfone & Reconhecimento Vocal (NSMicrophoneUsageDescription & NSSpeechRecognitionUsageDescription):</strong> Utilizados pontualmente para ditar notas sensoriais por voz. O processamento ocorre <strong>100% localmente no dispositivo</strong> através do framework nativo Apple. O ReWine <strong>NÃO guarda ficheiros de áudio</strong> nem grava em segundo plano.</li>"
             "<li><strong>Câmara (NSCameraUsageDescription):</strong> Para captar fotografias de garrafas, rótulos ou taças durante a prova.</li>"
             "<li><strong>Fototeca (NSPhotoLibraryUsageDescription):</strong> Para associar imagens já existentes na sua galeria.</li>"
             "</ul>"),

            ("5. Fichas em PDF e Partilha Voluntária",
             "<p>Os documentos PDF são compostos no dispositivo com estilo vintage no idioma ativo, preservando a proporção original das fotos. São partilhados exclusivamente por iniciativa voluntária do utilizador através do menu nativo do iOS.</p>"),

            ("6. Classificação Etária & Consumo Responsável",
             "<p>O ReWine é uma ferramenta técnica e cultural destinada a entusiastas e profissionais. Cumpre rigorosamente as diretrizes da App Store e não comercializa bebidas alcoólicas.</p>"
             "<p><strong>Aviso de Maioridade:</strong> Classificação <strong>17+</strong> na App Store. Destinado exclusivamente a maiores de idade (+18 anos). Promovemos o consumo responsável e moderado.</p>"),

            ("7. Contacto Direto",
             "<p>Para qualquer esclarecimento sobre a nossa política de privacidade:</p>"
             "<p><strong>E-mail de Apoio:</strong> <a href=\"mailto:ayeneso2023@gmail.com\" style=\"color: var(--accent-magenta); font-weight: 600;\">ayeneso2023@gmail.com</a><br>"
             "<strong>Programador:</strong> JACOOR</p>")
        ]
    },
    "ru": {
        "title": "Политика Конфиденциальности — ReWine",
        "meta_desc": "Официальная политика конфиденциальности ReWine. Абсолютная приватность: 100% локальное хранение, локальное распознавание речи, без слежки и рекламы.",
        "h1": "Политика Конфиденциальности",
        "updated": "Последнее обновление: 18 октября 2026 г.",
        "sections": [
            ("1. Фундаментальный Принцип Приватности",
             "<p>В приложении <strong>ReWine</strong> (разработчик JACOOR) конфиденциальность ваших данных является главным приоритетом. Мы следуем принципу <em>Privacy by Design</em>, гарантируя, что ваш дегустационный опыт находится под вашим полным контролем.</p>"),

            ("2. Нулевой Сбор Персональных Данных",
             "<p><strong>ReWine НЕ собирает, НЕ передает, НЕ продает и НЕ предоставляет персональные данные третьим лицам.</strong></p>"
             "<ul>"
             "<li>Мы не собираем адреса электронной почты, имена, телефоны или учетные записи.</li>"
             "<li>Мы не собираем рекламные идентификаторы (IDFA) или идентификаторы поставщика (IDFV).</li>"
             "<li>Мы не используем навязчивые аналитические SDK или рекламные трекеры (Tracking = НЕТ).</li>"
             "<li>Мы не отслеживаем геопозицию в фоновом режиме и не храним историю перемещений.</li>"
             "</ul>"),

            ("3. Строго Локальное Хранение",
             "<p>Вся информация в ReWine хранится исключительно во внутренней памяти вашего устройства (локальная песочница iOS / iPadOS):</p>"
             "<ul>"
             "<li><strong>Дегустационные Заметки:</strong> Название вина, винодельня, тип продукта, игристость, цвет, год, сорта винограда, место, имя сомелье, сенсорные оценки, уровень сомелье и баллы сохраняются локально.</li>"
             "<li><strong>Винные Фотографии:</strong> Снимки бутылок, этикеток или бокалов сохраняются в приватной директории приложения со 100% сохранением исходных пропорций.</li>"
             "<li><strong>Резервное Копирование iCloud:</strong> При включенном резервном копировании iCloud данные шифруются и хранятся в вашей личной учетной записи Apple.</li>"
             "</ul>"),

            ("4. Прозрачное Использование Разрешений",
             "<p>ReWine запрашивает системные разрешения только в случаях, когда это необходимо для работы выбранных пользователем функций:</p>"
             "<ul>"
             "<li><strong>Геопозиция При Использовании (NSLocationWhenInUseUsageDescription):</strong> Используется исключительно при нажатии «Авто-GPS» для определения названия винодельни или ресторана. Геокодирование выполняется локально службами Apple без передачи координат на внешние серверы.</li>"
             "<li><strong>Микрофон и Распознавание Речи (NSMicrophoneUsageDescription & NSSpeechRecognitionUsageDescription):</strong> Запрашиваются только при нажатии на значок микрофона для голосовой диктовки заметок. Распознавание выполняется <strong>на 100% локально на устройстве</strong> через Apple Speech. ReWine <strong>НЕ сохраняет аудиофайлы</strong> и не ведет фоновую запись.</li>"
             "<li><strong>Камера (NSCameraUsageDescription):</strong> Для создания фотографий бутылок, этикеток и бокалов во время дегустации.</li>"
             "<li><strong>Медиатека Фото (NSPhotoLibraryUsageDescription):</strong> Для прикрепления ранее сделанных снимков из галереи.</li>"
             "</ul>"),

            ("5. Документы PDF и Экспорт",
             "<p>Дегустационные листы PDF генерируются непосредственно на вашем устройстве с винтажным пергаментным оформлением на активном языке. Документы передаются исключительно по вашей команде через стандартное системное меню iOS (AirDrop, Почта, Сообщения и т.д.).</p>"),

            ("6. Возрастной Рейтинг и Ответственное Потребление",
             "<p>ReWine — технический и культурный инструмент для ценителей вина и профессионалов. Приложение строго соблюдает правила Apple App Store и не занимается продажей или рекламой алкогольной продукции.</p>"
             "<p><strong>Возрастное Предупреждение:</strong> Рейтинг <strong>17+</strong> в Apple App Store. Приложение предназначено исключительно для совершеннолетних пользователей (18+). Мы выступаем за умеренное и ответственное потребление. Чрезмерное употребление алкоголя вредит здоровью.</p>"),

            ("7. Прямой Контакт",
             "<p>По всем вопросам, связанным с политикой конфиденциальности:</p>"
             "<p><strong>Электронная Почта Поддержки:</strong> <a href=\"mailto:ayeneso2023@gmail.com\" style=\"color: var(--accent-magenta); font-weight: 600;\">ayeneso2023@gmail.com</a><br>"
             "<strong>Разработчик:</strong> JACOOR</p>")
        ]
    },
    "zh": {
        "title": "隐私政策 — ReWine",
        "meta_desc": "ReWine 官方隐私政策。极致隐私保护：100%本地存储、设备端本地语音口述处理、零数据追踪、全面保障用户数据自主权。",
        "h1": "隐私政策",
        "updated": "最近更新日期：2026年10月18日",
        "sections": [
            ("1. 核心隐私承诺",
             "<p>在 <strong>ReWine</strong>（由 JACOOR 独立开发），您的个人隐私与数据安全是我们的最高准则。我们始终秉承 <em>“从源头保障隐私”（Privacy by Design）</em> 的核心设计理念，确保您的葡萄酒品鉴旅程与感官记录完全由您自主掌控。</p>"),

            ("2. 零个人数据收集原则",
             "<p><strong>ReWine 绝不收集、传输、出售或与任何第三方共享您的任何个人数据。</strong></p>"
             "<ul>"
             "<li>我们不收集您的电子邮箱、真实姓名、电话号码或任何身份注册凭证。</li>"
             "<li>我们不收集广告标识符（IDFA）或设备唯一标识符（IDFV）。</li>"
             "<li>我们不集成任何侵入式行为统计SDK、第三方跟踪器或广告变现网络（Tracking = 否）。</li>"
             "<li>我们绝不在后台追踪您的地理位置，亦不保存任何行踪轨迹。</li>"
             "</ul>"),

            ("3. 严格本地化存储架构",
             "<p>您在 ReWine 中记录的所有数据均唯一且排他地保存在您设备的本地沙盒中（iOS / iPadOS 本地存储）：</p>"
             "<ul>"
             "<li><strong>品酒档案：</strong> 葡萄酒名称、酒庄、产品类别、起泡性格、颜色、年份、葡萄品种、品鉴地点、侍酒师署名、感官笔记、侍酒师段位与评分均在本地加密保存。</li>"
             "<li><strong>品评照片：</strong> 拍摄的酒瓶、酒标、酒杯、软木塞或配餐照片均保存在应用程序的受保护私有目录中，100%保留原始几何宽高比。</li>"
             "<li><strong>iCloud 云端备份：</strong> 若您在设备上启用了 Apple iCloud 备份，您的数据将在您个人的 Apple 账户中端到端加密备份，ReWine 及任何第三方均无权访问。</li>"
             "</ul>"),

            ("4. 系统权限使用规范",
             "<p>ReWine 仅在您主动发起特定操作时请求必要的系统权限：</p>"
             "<ul>"
             "<li><strong>使用期间位置权限（NSLocationWhenInUseUsageDescription）：</strong> 仅在您轻触「自动GPS」选项时使用，用于在本地解析当前品酒所在的酒庄、餐厅或产区名称。地理编码完全通过 Apple 原生服务在本地处理，绝不向外部服务器传输经纬度。</li>"
             "<li><strong>麦克风与语音识别（NSMicrophoneUsageDescription & NSSpeechRecognitionUsageDescription）：</strong> 仅在您轻触麦克风按钮口述外观、香气或口感观察时单次调用。语音识别 <strong>100%在您的设备端本地运行</strong>。ReWine <strong>绝不存储任何音频文件</strong>，不在后台运行录音，亦绝不向外部云端传输您的声音。</li>"
             "<li><strong>相机权限（NSCameraUsageDescription）：</strong> 仅用于在品鉴现场即时拍摄葡萄酒瓶、酒标或酒杯照片。</li>"
             "<li><strong>照片图库权限（NSPhotoLibraryUsageDescription）：</strong> 仅用于允许您从设备相册中选取并关联既有照片至品酒档案。</li>"
             "</ul>"),

            ("5. PDF 报告生成与主动分享",
             "<p>PDF 格式的品酒档案完全依托 iOS 图形渲染引擎在本地生成，采用典雅复古羊皮纸排版并适配当前选定语言。所有文档仅在您通过系统分享菜单（AirDrop、邮件、信息或 AirPrint 打印）主动触发时才会导出或传输。</p>"),

            ("6. 年龄评级与理性品鉴倡议",
             "<p>ReWine 是一款专为葡萄酒爱好者与职业侍酒师设计的专业技术记录与文化鉴赏工具。严格遵循 Apple App Store 审核准则，不开展任何酒精饮料的销售、分销或推广业务。</p>"
             "<p><strong>法定年龄提醒与健康倡议：</strong> 本应用在 App Store 的官方分级为 <strong>17+</strong>。ReWine 专为达到法定饮酒年龄（中国及绝大多数国家/地区为18周岁及以上）的成年人设计。我们积极倡导适量品鉴与健康理性的葡萄酒文化。过量饮酒有害健康。</p>"),

            ("7. 开发者联系方式",
             "<p>如果您对本隐私政策有任何疑问、建议或需要技术支持，请随时直接联络我们：</p>"
             "<p><strong>客服与技术支持邮箱：</strong> <a href=\"mailto:ayeneso2023@gmail.com\" style=\"color: var(--accent-magenta); font-weight: 600;\">ayeneso2023@gmail.com</a><br>"
             "<strong>开发者：</strong> JACOOR</p>")
        ]
    }
}

def generate_index_html(lang):
    code = lang["code"]
    ui = UI_STRINGS[code]
    data = MARKETING_DATA[code]

    nav_html = render_nav("index", code, ui)
    footer_html = render_footer(code, ui)

    cards_html = []
    for icon, title, desc in data["features"]:
        cards_html.append(f"""      <div class="feature-card">
        <div class="card-icon">{icon}</div>
        <h3>{title}</h3>
        <p>{desc}</p>
      </div>""")
    cards_str = "\n\n".join(cards_html)

    soporte_file = get_page_filename("soporte", code)

    html = f"""<!DOCTYPE html>
<html lang="{code}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{data['title']}</title>
  <meta name="description" content="{data['meta_desc']}">
  <link rel="stylesheet" href="style.css">
  <link rel="icon" type="image/png" href="assets/logo.png">
</head>
<body>
{nav_html}

  <header class="hero">
    <div class="container">
      <div class="badge">{data['hero_badge']}</div>
      <h1>{data['hero_title']}</h1>
      <p class="hero-subtitle">{data['hero_sub']}</p>
      <div>
        <a href="{soporte_file}" class="btn-cta" style="font-size: 16px; padding: 14px 32px;">{ui['guide_cta']}</a>
      </div>
    </div>
  </header>

  <section class="container">
    <div class="features-grid">
{cards_str}
    </div>
  </section>

{footer_html}
</body>
</html>
"""
    return html

def generate_soporte_html(lang):
    code = lang["code"]
    ui = UI_STRINGS[code]
    data = SUPPORT_DATA[code]

    nav_html = render_nav("soporte", code, ui)
    footer_html = render_footer(code, ui)

    faq_items = []
    for q, a in data["faqs"]:
        faq_items.append(f"""      <div class="faq-item">
        <h4>{q}</h4>
        <p>{a}</p>
      </div>""")
    faqs_str = "\n\n".join(faq_items)

    html = f"""<!DOCTYPE html>
<html lang="{code}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{data['title']}</title>
  <meta name="description" content="{data['meta_desc']}">
  <link rel="stylesheet" href="style.css">
  <link rel="icon" type="image/png" href="assets/logo.png">
</head>
<body>
{nav_html}

  <main class="container">
    <div class="legal-content">
      <h1 style="font-size: 36px; margin-bottom: 8px; color: #FFFFFF;">{data['h1']}</h1>
      <p style="color: var(--accent-gold); font-weight: 600; margin-bottom: 30px;">{data['subtitle']}</p>

      <h2>{ 'Preguntas Frecuentes (FAQ)' if code == 'es' else ('Frequently Asked Questions (FAQ)' if code == 'en' else ('Foire Aux Questions (FAQ)' if code == 'fr' else ('Domande Frequenti (FAQ)' if code == 'it' else ('Perguntas Frequentes (FAQ)' if code == 'pt' else ('Часто задаваемые вопросы (FAQ)' if code == 'ru' else '常见问题解答 (FAQ)'))))) }</h2>

{faqs_str}

      <h2>{data['contact_title']}</h2>
      <p>{data['contact_desc']}</p>
      <p>
        <strong>Email:</strong> <a href="mailto:ayeneso2023@gmail.com" style="color: var(--accent-magenta); font-weight: 600;">ayeneso2023@gmail.com</a><br>
        <strong>{data['compat']}</strong><br>
        <strong>{data['dev']}</strong>
      </p>
    </div>
  </main>

{footer_html}
</body>
</html>
"""
    return html

def generate_privacidad_html(lang):
    code = lang["code"]
    ui = UI_STRINGS[code]
    data = PRIVACY_DATA[code]

    nav_html = render_nav("privacidad", code, ui)
    footer_html = render_footer(code, ui)

    sections_html = []
    for heading, body in data["sections"]:
        sections_html.append(f"""      <h2>{heading}</h2>
      {body}""")
    sections_str = "\n\n".join(sections_html)

    html = f"""<!DOCTYPE html>
<html lang="{code}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{data['title']}</title>
  <meta name="description" content="{data['meta_desc']}">
  <link rel="stylesheet" href="style.css">
  <link rel="icon" type="image/png" href="assets/logo.png">
</head>
<body>
{nav_html}

  <main class="container">
    <div class="legal-content">
      <h1 style="font-size: 36px; margin-bottom: 8px; color: #FFFFFF;">{data['h1']}</h1>
      <p style="color: var(--accent-gold); font-weight: 600; margin-bottom: 24px;">{data['updated']}</p>

{sections_str}
    </div>
  </main>

{footer_html}
</body>
</html>
"""
    return html

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    generated_count = 0

    for lang in LANGUAGES:
        code = lang["code"]

        # 1. Marketing
        idx_filename = get_page_filename("index", code)
        idx_path = os.path.join(base_dir, idx_filename)
        with open(idx_path, "w", encoding="utf-8") as f:
            f.write(generate_index_html(lang))
        print(f"Generated: {idx_filename}")
        generated_count += 1

        # 2. Support
        sop_filename = get_page_filename("soporte", code)
        sop_path = os.path.join(base_dir, sop_filename)
        with open(sop_path, "w", encoding="utf-8") as f:
            f.write(generate_soporte_html(lang))
        print(f"Generated: {sop_filename}")
        generated_count += 1

        # 3. Privacy
        priv_filename = get_page_filename("privacidad", code)
        priv_path = os.path.join(base_dir, priv_filename)
        with open(priv_path, "w", encoding="utf-8") as f:
            f.write(generate_privacidad_html(lang))
        print(f"Generated: {priv_filename}")
        generated_count += 1

    print(f"\nSuccessfully generated {generated_count} pages across 7 languages!")

if __name__ == "__main__":
    main()
