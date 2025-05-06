import time
from bs4 import BeautifulSoup
import requests
import json

with open("donnee.json", "r") as fichierjson:
    jsonread = json.load(fichierjson)

i = nombre_firstnames = sum(1 for lead in jsonread if lead.get("firstname"))-1
#i = 11
donnees = []
donneesjson = []
while(i != 0):
    #for loop in range(2):
    ######################################
    ###########SECTION 1##################
    ######################################
    firstnames = [lead["firstname"] for lead in jsonread][i]

    lastname = [lead["lastname"] for lead in jsonread][i]

    shortBio = [lead["shortBio"] for lead in jsonread][i]

    jobTitle = [lead["jobTitle"] for lead in jsonread][i]
    
    companyName = [lead["companyName"] for lead in jsonread][i]

    nombre_firstnames = sum(1 for lead in jsonread if lead.get("firstname"))
    print(i)

    url = 'https://ile-reunion.org/gpt3/resultat'
    data = {
            'D1': 'Option sortie audio',
            'exemple-prompt': 'Exemples de prompt',
            'xscreen': '1280',
            'yscreen': '800',
            'question': f"""
            Tu es Paul, consultant indépendant. Tu rédiges une note de connexion LinkedIn, adressée à {firstnames} {lastname}, CEO ou Co-founder chez {companyName}. Tu as lu attentivement sa bio : {shortBio}. Tu utilises la méthode Challenger Sales avec un regard critique et non commercial.  🎯 Tu cherches à provoquer un micro-déclic, en une seule phrase. Ton rôle : suggérer qu’il existe un geste professionnel que {firstnames} continue d’exécuter, sans jamais avoir décidé de le faire — un reste de réflexe opérationnel jamais interrogé.  Tu relies ton message à un des cas d’usage suivants issus de la BDD : 1. Relances internes (Slack/email) encore faites manuellement, 2. Préparation de réponses à appels d’offres, 3. Compilation manuelle d’avancement projet, 4. Structuration de la connaissance produit, 5. Diffusion interne de reporting stratégique non automatisée.  Tu écris un texte non générique, au style littéraire et improbable, comme un fragment de journal d’observation. Tu évites toute formule vue ou attendue.  ⚠️ Format strict : ≤ 300 caractères (espaces compris), vouvoiement, 1 phrase, aucune signature, aucun lien, aucune majuscule de politesse. Une curiosité sèche et intrigante.   🛑 Le ton ne doit en aucun cas être donneur de leçon. Vous écrivez d’égal à égal, sans posture de supériorité, sans jugement implicite. Vous observez, vous suggérez, vous respectez l’intelligence opérationnelle du dirigeant.  🎯 Le ton du message doit rester simple, direct, sans complexité inutile. Il ne doit jamais donner l'impression de faire la leçon. Vous vous adressez à un dirigeant en égal, avec respect et lucidité. La forme peut être élégante, mais jamais alambiquée. Préférez les phrases sobres, les images claires, et les tensions feutrées.  📎 Chaque message doit impérativement commencer par “Bonjour {firstnames},” sans formule commerciale ni flatterie.  🎯 Priorité : utilisez des cas d’usage relatifs aux tâches internes ou transverses : reporting, validation, coordination, documentation, structuration d’information, automatisation interne. N’utilisez pas de cas orientés client sauf si cela ressort explicitement de la bio ou du poste.  📤 Sortie attendue : uniquement le contenu du message. Pas de balise, pas de préfixe 'Objet:' ou 'Message:', pas de signature ni lien.  🔍 Chaque message doit être entièrement centré sur le contexte professionnel réel du destinataire. Aucune formulation générique n’est admise. Le texte doit faire directement référence à son environnement opérationnel, à son secteur, à ses processus internes ou à ses responsabilités telles qu’exprimées dans sa bio. Évitez les termes vagues comme 'dirigeant', 'certains formats', 'habitudes'. Ancrez chaque phrase dans le quotidien réel et spécifique de la personne ciblée.
            """
        }

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Language': 'fr-FR',
            'Referer': 'https://ile-reunion.org/gpt3/',
        }

    response = requests.post(url, data=data, headers=headers)
    print(response.text)
    if response.status_code == 200:
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        for center in soup.find_all("center"):
                center.decompose()

        div_message = soup.find("div", class_="affichage")

        if div_message:
            for br in div_message.find_all("br"):
                br.replace_with("\n")

            texte_final = div_message.get_text(separator="\n", strip=True)

            lignes = texte_final.split("\n")
            
            lignes = [ligne for ligne in lignes if "Résultat :" not in ligne and "Posez une autre question" not in ligne and "Requêtes" not in ligne]

            texte_final_filtré = "\n".join(lignes)

            with open("mail.txt", "a", encoding="utf-8") as f:
                f.write(texte_final_filtré + "\n\n")
        else:
            print("Div avec class 'affichage' non trouvée")

    else:
        print(f"Erreur lors de la requête : {response.status_code}")

    texte_final_filtré_linkedin1 = texte_final_filtré
    #personne = {
    #    "contenu": texte_final_filtré
    #}
    #donneesjson.append(personne)

    ######################################
    ###########SECTION 2##################
    ######################################
    firstnames = [lead["firstname"] for lead in jsonread][i]

    lastname = [lead["lastname"] for lead in jsonread][i]

    shortBio = [lead["shortBio"] for lead in jsonread][i]

    jobTitle = [lead["jobTitle"] for lead in jsonread][i]
    
    companyName = [lead["companyName"] for lead in jsonread][i]

    nombre_firstnames = sum(1 for lead in jsonread if lead.get("firstnames"))

    url = 'https://ile-reunion.org/gpt3/resultat'
    data = {
            'D1': 'Option sortie audio',
            'exemple-prompt': 'Exemples de prompt',
            'xscreen': '1280',
            'yscreen': '800',
            'question': f"""
            Tu es Paul. Consultant indépendant. Tu écris un message post-connexion LinkedIn à {firstnames}, CEO ou Co-founder chez {companyName}, après acceptation. Tu appliques la méthode Challenger Sales mais sans script, sans flatterie, sans automatisme. Tu ne remercies pas — tu ouvres une brèche.  🎯 Ton objectif est de troubler légèrement une certitude opérationnelle. Ce message est bref, sec, mais stratégiquement dissonant.  Tu relies ton propos à un des cas d’usage suivants, extraits de la BDD Arkel : 1. Suivi ou relance de projet encore opérés à la main, 2. Synthèses de réunion ou arbitrages partagés tapés manuellement, 3. Mise à jour des outils de pilotage produits sans automatisation, 4. Structuration ou diffusion de KPI techniques à la main, 5. Réponses à des sollicitations internes faites sans levier.  Tu poses une seule question en vouvoiement, qui sous-entend que quelque chose dans l’organisation de {companyName} n’est plus soutenable intellectuellement.  ⚠️ Sortie attendue : 1 à 2 phrases max. Aucun merci, aucun lien, aucun emoji. Juste une tension polie qui attend une réaction.  Tu t’inspires systématiquement de la bio {shortBio} pour adapter le langage, les exemples, et la structure du message au profil réel du destinataire.  🛑 Le ton ne doit en aucun cas être donneur de leçon. Vous écrivez d’égal à égal, sans posture de supériorité, sans jugement implicite. Vous observez, vous suggérez, vous respectez l’intelligence opérationnelle du dirigeant.  🎯 Le ton du message doit rester simple, direct, sans complexité inutile. Il ne doit jamais donner l'impression de faire la leçon. Vous vous adressez à un dirigeant en égal, avec respect et lucidité. La forme peut être élégante, mais jamais alambiquée. Préférez les phrases sobres, les images claires, et les tensions feutrées.  📎 Chaque message doit impérativement commencer par “Bonjour {firstnames},” sans formule commerciale ni flatterie.  🎯 Priorité : utilisez des cas d’usage relatifs aux tâches internes ou transverses : reporting, validation, coordination, documentation, structuration d’information, automatisation interne. N’utilisez pas de cas orientés client sauf si cela ressort explicitement de la bio ou du poste.  📤 Sortie attendue : uniquement le contenu du message. Pas de balise, pas de préfixe 'Objet:' ou 'Message:', pas de signature ni lien.  🔍 Chaque message doit être entièrement centré sur le contexte professionnel réel du destinataire. Aucune formulation générique n’est admise. Le texte doit faire directement référence à son environnement opérationnel, à son secteur, à ses processus internes ou à ses responsabilités telles qu’exprimées dans sa bio. Évitez les termes vagues comme 'dirigeant', 'certains formats', 'habitudes'. Ancrez chaque phrase dans le quotidien réel et spécifique de la personne ciblée.
            """
        }

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Language': 'fr-FR',
            'Referer': 'https://ile-reunion.org/gpt3/',
        }

    response = requests.post(url, data=data, headers=headers)
    print(response.text)
    if response.status_code == 200:
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        for center in soup.find_all("center"):
                center.decompose()

        for center in soup.find_all("center"):
                center.decompose()

        div_message = soup.find("div", class_="affichage")

        if div_message:
            for br in div_message.find_all("br"):
                br.replace_with("\n")

            texte_final = div_message.get_text(separator="\n", strip=True)

            lignes = texte_final.split("\n")
            
            lignes = [ligne for ligne in lignes if "Résultat :" not in ligne and "Posez une autre question" not in ligne and "Requêtes" not in ligne]

            texte_final_filtré = "\n".join(lignes)

            with open("mail.txt", "a", encoding="utf-8") as f:
                f.write(texte_final_filtré + "\n\n")
        else:
            print("Div avec class 'affichage' non trouvée")

    else:
        print(f"Erreur lors de la requête : {response.status_code}")

    texte_final_filtré_linkedin2 = texte_final_filtré
    personne = {
        "contenuLinkedIn1": texte_final_filtré_linkedin1,
        "contenuLinkedIn2": texte_final_filtré_linkedin2
    }
    donneesjson.append(personne)
    #for loop in range(3):
    #############################
    ##############SECTION 1######
    #############################
    firstnames = [lead["firstname"] for lead in jsonread][i]

    lastname = [lead["lastname"] for lead in jsonread][i]

    shortBio = [lead["shortBio"] for lead in jsonread][i]

    jobTitle = [lead["jobTitle"] for lead in jsonread][i]
    
    companyName = [lead["companyName"] for lead in jsonread][i]

    nombre_firstnames = sum(1 for lead in jsonread if lead.get("firstnames"))

    url = 'https://ile-reunion.org/gpt3/resultat'
    data = {
            'D1': 'Option sortie audio',
            'exemple-prompt': 'Exemples de prompt',
            'xscreen': '1280',
            'yscreen': '800',
            'question': f"""
            Tu es Paul. Consultant indépendant. Tu n’es pas là pour proposer une solution. Tu es là pour exposer une évidence que personne n’a encore osé formuler.  Tu écris un email d’accroche, adressé à un CEO ou Co-founder, {firstnames}, chez {companyName}, dont tu as lu attentivement la bio : {shortBio}. Tu pratiques la méthode Challenger Sales, mais tu le fais avec une plume presque littéraire. Tu n’informes pas : tu questionnes. Tu n’analyses pas : tu suggères.  🎯 Tu identifies une friction que tout le monde a fini par normaliser. Tu l’écris comme une faille élégante. Tu ne vends rien, tu ne proposes rien, tu tends une tension.  Tu relies ton message à l’un des 5 cas d’usage suivants (issus de la BDD) : 1. Automatisation du suivi post-réunion (relances, synthèses), 2. Réponses récurrentes aux demandes clients ou partenaires, 3. Tableaux de pilotage et rapports de performance automatisés, 4. Coordination des tâches récurrentes par intelligence contextuelle, 5. Consolidation automatisée d’indicateurs clés transverses.  Le style est volontairement imprévisible. Il ne doit jamais ressembler à un mail marketing. Chaque mot doit sembler écrit par un humain qui doute avec clarté. Tu termines par une question qui ne cherche pas de call, mais qui exige une prise de position intérieure.  ⚠️ Format attendu : email brut, vouvoiement strict, ton analytique, aucun lien ni signature, terminé par une question ouverte stratégique.   🛑 Le ton ne doit en aucun cas être donneur de leçon. Vous écrivez d’égal à égal, sans posture de supériorité, sans jugement implicite. Vous observez, vous suggérez, vous respectez l’intelligence opérationnelle du dirigeant.  🎯 Le ton du message doit rester simple, direct, sans complexité inutile. Il ne doit jamais donner l'impression de faire la leçon. Vous vous adressez à un dirigeant en égal, avec respect et lucidité. La forme peut être élégante, mais jamais alambiquée. Préférez les phrases sobres, les images claires, et les tensions feutrées.  📎 Chaque message doit impérativement commencer par “Bonjour {firstnames},” sans formule commerciale ni flatterie.  🎯 Priorité : utilisez des cas d’usage relatifs aux tâches internes ou transverses : reporting, validation, coordination, documentation, structuration d’information, automatisation interne. N’utilisez pas de cas orientés client sauf si cela ressort explicitement de la bio ou du poste.  📤 Sortie attendue : uniquement le contenu du message. Pas de balise, pas de préfixe 'Objet:' ou 'Message:', pas de signature ni lien.  🔍 Chaque message doit être entièrement centré sur le contexte professionnel réel du destinataire. Aucune formulation générique n’est admise. Le texte doit faire directement référence à son environnement opérationnel, à son secteur, à ses processus internes ou à ses responsabilités telles qu’exprimées dans sa bio. Évitez les termes vagues comme 'dirigeant', 'certains formats', 'habitudes'. Ancrez chaque phrase dans le quotidien réel et spécifique de la personne ciblée.
            """
        }

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Language': 'fr-FR',
            'Referer': 'https://ile-reunion.org/gpt3/',
        }

    response = requests.post(url, data=data, headers=headers)
    print(response.text)
    if response.status_code == 200:
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        for center in soup.find_all("center"):
                center.decompose()

        div_message = soup.find("div", class_="affichage")

        if div_message:
            for br in div_message.find_all("br"):
                br.replace_with("\n")

            texte_final = div_message.get_text(separator="\n", strip=True)

            lignes = texte_final.split("\n")
            
            lignes = [ligne for ligne in lignes if "Résultat :" not in ligne and "Posez une autre question" not in ligne and "Requêtes" not in ligne]

            texte_final_filtré = "\n".join(lignes)

            with open("mail.txt", "a", encoding="utf-8") as f:
                f.write(texte_final_filtré + "\n\n")
        else:
            print("Div avec class 'affichage' non trouvée")

    else:
        print(f"Erreur lors de la requête : {response.status_code}")



    url = 'https://ile-reunion.org/gpt3/resultat'
    data = {
            'D1': 'Option sortie audio',
            'exemple-prompt': 'Exemples de prompt',#faire le prompt
            'xscreen': '1280',#####################
            'yscreen': '800',########OBJET#########
            'question': f"""
            Tu es Paul, consultant indépendant spécialisé dans la suppression des frictions opérationnelles invisibles chez les dirigeants de PME. Tu ne proposes pas un outil. Tu proposes une clarification. Et tu ne commences jamais par vanter un bénéfice, mais par pointer un angle mort.  Tu es convaincu qu’un dirigeant ne gagne pas de temps en ajoutant une solution, mais en arrêtant ce qu’il n’aurait jamais dû faire lui-même.  Tu rédiges un objet d’email d’introduction, envoyé à {firstnames} {lastname}, {jobTitle} chez {companyName}, dont tu as étudié la posture dans la bio suivante : {shortBio}.  🎯 Ton objectif est de créer une tension légère mais stratégique. Le lecteur doit pressentir que ce message parlera de quelque chose qu’il a intégré à son quotidien, mais qui pourrait être désintégré sans douleur. Pas de promesse. Pas de verbe d’action. Un diagnostic silencieux, dans le ton.  Tu connectes l’objet à un des 5 cas d’usage suivants : 1. Suivis ou relances internes (mail ou Slack) encore gérés manuellement, 2. Comptes rendus de réunions encore structurés à la main, 3. Tableaux de bord financiers mis à jour dans Excel, 4. Réponses opérationnelles client encore envoyées manuellement, 5. Création de documents simples (contrats types, étiquettes, fiches produits) à la main.  ⚠️ Sortie attendue : un objet clair, sobre, structurant, entre 8 et 12 mots, sans ponctuation excessive, sans balises ni mentions.   🛑 Le ton ne doit en aucun cas être donneur de leçon. Vous écrivez d’égal à égal, sans posture de supériorité, sans jugement implicite. Vous observez, vous suggérez, vous respectez l’intelligence opérationnelle du dirigeant.  🎯 Le ton du message doit rester simple, direct, sans complexité inutile. Il ne doit jamais donner l'impression de faire la leçon. Vous vous adressez à un dirigeant en égal, avec respect et lucidité. La forme peut être élégante, mais jamais alambiquée. Préférez les phrases sobres, les images claires, et les tensions feutrées.  📎 Chaque message doit impérativement commencer par “Bonjour {firstnames},” sans formule commerciale ni flatterie.  🎯 Priorité : utilisez des cas d’usage relatifs aux tâches internes ou transverses : reporting, validation, coordination, documentation, structuration d’information, automatisation interne. N’utilisez pas de cas orientés client sauf si cela ressort explicitement de la bio ou du poste.  📤 Sortie attendue : uniquement le contenu du message. Pas de balise, pas de préfixe 'Objet:' ou 'Message:', pas de signature ni lien.  🔍 Chaque message doit être entièrement centré sur le contexte professionnel réel du destinataire. Aucune formulation générique n’est admise. Le texte doit faire directement référence à son environnement opérationnel, à son secteur, à ses processus internes ou à ses responsabilités telles qu’exprimées dans sa bio. Évitez les termes vagues comme 'dirigeant', 'certains formats', 'habitudes'. Ancrez chaque phrase dans le quotidien réel et spécifique de la personne ciblée.
            """
        }

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Language': 'fr-FR',
            'Referer': 'https://ile-reunion.org/gpt3/',
        }

    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        for center in soup.find_all("center"):
                center.decompose()

        texte_brut = soup.get_text(separator=' ', strip=True)

        p_resultat = soup.find('p', text=lambda x: x and 'Résultat :' in x)
        if p_resultat:
            suivant = p_resultat.find_next_sibling(text=True)
            if suivant:
                texte_suivant = suivant.strip()
                print(texte_suivant)
                with open("objet.txt", "a") as synthesewrite:
                    synthesewrite.write(texte_suivant)

            else:
                print("Texte suivant non trouvé")
        else:
            print("Balise <p> avec 'Résultat :' non trouvée")

    else:
        print(f"Erreur lors de la requête : {response.status_code}")
    texte_final_filtré1 = texte_final_filtré
    #personne = {
    #    "objet": texte_suivant,
    #    "contenu": texte_final_filtré
    #}
    #donnees.append(personne)
    #############################
    ##############SECTION 2######
    #############################
    firstnames = [lead["firstname"] for lead in jsonread][i]

    lastname = [lead["lastname"] for lead in jsonread][i]

    shortBio = [lead["shortBio"] for lead in jsonread][i]

    jobTitle = [lead["jobTitle"] for lead in jsonread][i]
    
    companyName = [lead["companyName"] for lead in jsonread][i]

    nombre_firstnames = sum(1 for lead in jsonread if lead.get("firstnames"))

    url = 'https://ile-reunion.org/gpt3/resultat'
    data = {
            'D1': 'Option sortie audio',
            'exemple-prompt': 'Exemples de prompt',
            'xscreen': '1280',
            'yscreen': '800',
            'question': f"""
            Tu es Paul. Consultant indépendant. Tu interviens lorsqu’un dirigeant pense que certaines tâches sont stratégiques alors qu’elles sont seulement devenues normales par manque d’alternative. Tu rédiges un email autonome, à {firstnames}, CEO ou Co-founder chez {companyName}, en t’inspirant de sa bio {shortBio}.  🎯 Tu ne fais pas de relance. Tu changes d’angle. Tu ouvres un nouveau couloir stratégique en partant d’une tâche jugée non déléguable — mais dont la répétition trahit la nature automatisable.  Tu relies ton message à un des cas d’usage suivants (issus de la BDD) : 1. Génération automatisée de trames de compte rendu projet ou client, 2. Production de contenus récurrents liés à la qualité ou conformité, 3. Organisation et classification automatisée de documents techniques, 4. Rédaction de réponses à sollicitations internes répétitives, 5. Préparation de synthèses produit pour partenaires externes.  Le message est vouvoié, écrit dans un style littéraire mais chirurgical, et se conclut sur une question ouverte qui vise à faire émerger un renoncement possible plutôt qu’un nouveau processus.  ⚠️ Sortie attendue : email brut, aucun lien, aucune promesse, aucune signature. Un texte ciselé comme un doute silencieux.   🛑 Le ton ne doit en aucun cas être donneur de leçon. Vous écrivez d’égal à égal, sans posture de supériorité, sans jugement implicite. Vous observez, vous suggérez, vous respectez l’intelligence opérationnelle du dirigeant.  🎯 Le ton du message doit rester simple, direct, sans complexité inutile. Il ne doit jamais donner l'impression de faire la leçon. Vous vous adressez à un dirigeant en égal, avec respect et lucidité. La forme peut être élégante, mais jamais alambiquée. Préférez les phrases sobres, les images claires, et les tensions feutrées.  📎 Chaque message doit impérativement commencer par “Bonjour {firstnames},” sans formule commerciale ni flatterie.  🎯 Priorité : utilisez des cas d’usage relatifs aux tâches internes ou transverses : reporting, validation, coordination, documentation, structuration d’information, automatisation interne. N’utilisez pas de cas orientés client sauf si cela ressort explicitement de la bio ou du poste.  📤 Sortie attendue : uniquement le contenu du message. Pas de balise, pas de préfixe 'Objet:' ou 'Message:', pas de signature ni lien.  🔍 Chaque message doit être entièrement centré sur le contexte professionnel réel du destinataire. Aucune formulation générique n’est admise. Le texte doit faire directement référence à son environnement opérationnel, à son secteur, à ses processus internes ou à ses responsabilités telles qu’exprimées dans sa bio. Évitez les termes vagues comme 'dirigeant', 'certains formats', 'habitudes'. Ancrez chaque phrase dans le quotidien réel et spécifique de la personne ciblée.
            """
        }

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Language': 'fr-FR',
            'Referer': 'https://ile-reunion.org/gpt3/',
        }

    response = requests.post(url, data=data, headers=headers)
    print(response.text)
    if response.status_code == 200:
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        for center in soup.find_all("center"):
                center.decompose()

        div_message = soup.find("div", class_="affichage")

        if div_message:
            for br in div_message.find_all("br"):
                br.replace_with("\n")

            texte_final = div_message.get_text(separator="\n", strip=True)

            lignes = texte_final.split("\n")
            
            lignes = [ligne for ligne in lignes if "Résultat :" not in ligne and "Posez une autre question" not in ligne and "Requêtes" not in ligne]

            texte_final_filtré = "\n".join(lignes)

            with open("mail.txt", "a", encoding="utf-8") as f:
                f.write(texte_final_filtré + "\n\n")
        else:
            print("Div avec class 'affichage' non trouvée")

    else:
        print(f"Erreur lors de la requête : {response.status_code}")


    #personne = {
    #    "objet": texte_suivant,
    #    "contenu": texte_final_filtré
    #}
    #donnees.append(personne)
    texte_final_filtré2 = texte_final_filtré
    #############################
    ##############SECTION 3######
    #############################
    firstnames = [lead["firstname"] for lead in jsonread][i]

    lastname = [lead["lastname"] for lead in jsonread][i]

    shortBio = [lead["shortBio"] for lead in jsonread][i]

    jobTitle = [lead["jobTitle"] for lead in jsonread][i]
    
    companyName = [lead["companyName"] for lead in jsonread][i]

    nombre_firstnames = sum(1 for lead in jsonread if lead.get("firstnames"))

    url = 'https://ile-reunion.org/gpt3/resultat'
    data = {
            'D1': 'Option sortie audio',
            'exemple-prompt': 'Exemples de prompt',
            'xscreen': '1280',
            'yscreen': '800',
            'question': f"""
            Tu es Paul. Consultant indépendant. Tu rédiges un dernier message, non pour relancer, mais pour partager un constat vécu, issu de missions concrètes en PME. Tu ne conclus pas. Tu observes, tu racontes, tu ne demandes rien — mais tu laisses une tension.  🎯 Objectif : montrer que ce ne sont pas les grandes structures qui transforment le plus radicalement, mais les dirigeants de PME qui ont encore les mains dans les systèmes. Parce qu’ils savent ce que ça coûte, et ce que ça mobilise.   Tu fais passer l’idée que l’automatisation n’est jamais totale, que l’intelligence reste humaine en boucle (human-in-the-loop), et que le rôle du dirigeant est de reprendre le contrôle, pas de l’abandonner.  Tu t’adresses à {firstnames} {lastname}, CEO ou Co-founder chez {companyName}, dont tu as lu attentivement la bio : {shortBio}.  Tu relies ton message à des cas d’usage réels issus de la BDD, parmi : 1. Génération automatisée de fiches produits ou documents externes récurrents,   2. Synthèse projet automatisée, revue par un décideur (human-in-the-loop),   3. Suppression des validations intermédiaires non critiques,   4. Rédaction automatisée de briefs internes, relus ponctuellement,   5. Construction d’un référentiel documentaire dynamique, maintenu par itération humaine.  Tu adoptes un style littéraire improbable, très éloigné d’un email de relance. Tu racontes une scène. Un souvenir. Un mouvement. Pas une promesse.   Le message se termine sur une question ouverte, sans jamais tendre la main.  ⚠️ Sortie attendue : email brut, style littéraire improbable, aucune formule de clôture, aucune proposition. Juste un constat, un silence, une tension.   🛑 Le ton ne doit en aucun cas être donneur de leçon. Vous écrivez d’égal à égal, sans posture de supériorité, sans jugement implicite. Vous observez, vous suggérez, vous respectez l’intelligence opérationnelle du dirigeant.  🎯 Le ton du message doit rester simple, direct, sans complexité inutile. Il ne doit jamais donner l'impression de faire la leçon. Vous vous adressez à un dirigeant en égal, avec respect et lucidité. La forme peut être élégante, mais jamais alambiquée. Préférez les phrases sobres, les images claires, et les tensions feutrées.  📎 Chaque message doit impérativement commencer par “Bonjour {firstnames},” sans formule commerciale ni flatterie.  🎯 Priorité : utilisez des cas d’usage relatifs aux tâches internes ou transverses : reporting, validation, coordination, documentation, structuration d’information, automatisation interne. N’utilisez pas de cas orientés client sauf si cela ressort explicitement de la bio ou du poste.  📤 Sortie attendue : uniquement le contenu du message. Pas de balise, pas de préfixe 'Objet:' ou 'Message:', pas de signature ni lien.  🔍 Chaque message doit être entièrement centré sur le contexte professionnel réel du destinataire. Aucune formulation générique n’est admise. Le texte doit faire directement référence à son environnement opérationnel, à son secteur, à ses processus internes ou à ses responsabilités telles qu’exprimées dans sa bio. Évitez les termes vagues comme 'dirigeant', 'certains formats', 'habitudes'. Ancrez chaque phrase dans le quotidien réel et spécifique de la personne ciblée.
            """
        }

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Language': 'fr-FR',
            'Referer': 'https://ile-reunion.org/gpt3/',
        }

    response = requests.post(url, data=data, headers=headers)
    print(response.text)
    if response.status_code == 200:
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        for center in soup.find_all("center"):
                center.decompose()

        div_message = soup.find("div", class_="affichage")

        if div_message:
            for br in div_message.find_all("br"):
                br.replace_with("\n")

            texte_final = div_message.get_text(separator="\n", strip=True)

            lignes = texte_final.split("\n")
            
            lignes = [ligne for ligne in lignes if "Résultat :" not in ligne and "Posez une autre question" not in ligne and "Requêtes" not in ligne]

            texte_final_filtré = "\n".join(lignes)

            with open("mail.txt", "a", encoding="utf-8") as f:
                f.write(texte_final_filtré + "\n\n")
        else:
            print("Div avec class 'affichage' non trouvée")

    else:
        print(f"Erreur lors de la requête : {response.status_code}")



    url = 'https://ile-reunion.org/gpt3/resultat'
    data = {
            'D1': 'Option sortie audio',
            'exemple-prompt': 'Exemples de prompt',#faire le prompt
            'xscreen': '1280',
            'yscreen': '800',
            'question': f"Tu es Paul, consultant IA chez Arkel. Tu t’adresses à {firstnames} {lastname}, {jobTitle} chez {companyName}. Tu t’appuies sur sa bio : {shortBio}. Tu rédiges un objet d’email intrigant, épuré, évocateur, qui ouvre un fil stratégique sans vendre. L’objet suggère que {firstnames} continue peut-être à faire quelque chose qui ne devrait plus être fait manuellement. Ton style est sobre, presque littéraire. Pas de teasing forcé, pas de majuscules inutiles, jamais de “🚀”, “+30%”, ou “votre business”. ⚠️ Sortie attendue : objet seul, sans guillemets ni balises. Rien autour. {texte_final_filtré}"
        }

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.100 Safari/537.36',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Accept-Language': 'fr-FR',
            'Referer': 'https://ile-reunion.org/gpt3/',
        }

    response = requests.post(url, data=data, headers=headers)

    if response.status_code == 200:
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')

        for center in soup.find_all("center"):
                center.decompose()

        texte_brut = soup.get_text(separator=' ', strip=True)

        p_resultat = soup.find('p', text=lambda x: x and 'Résultat :' in x)
        if p_resultat:
            suivant = p_resultat.find_next_sibling(text=True)
            if suivant:
                texte_suivant = suivant.strip()
                print(texte_suivant)
                with open("objet.txt", "a") as synthesewrite:
                    synthesewrite.write(texte_suivant)

            else:
                print("Texte suivant non trouvé")
        else:
            print("Balise <p> avec 'Résultat :' non trouvée")

    else:
        print(f"Erreur lors de la requête : {response.status_code}")
    texte_final_filtré3 = texte_final_filtré
    personne = {
        "objet": texte_suivant,
        "contenuMailAccroche": texte_final_filtré1,
        "contenuMailAlternatif": texte_final_filtré2,
        "contenuMailFinal": texte_final_filtré3
    }
    donnees.append(personne)
    i-=1
with open("donnees_mail_generees.json", "w", encoding="utf-8") as f:
    json.dump(donnees, f, indent=4, ensure_ascii=False)
with open("donnees_linkedin_generees.json", "w", encoding="utf-8") as f:
    json.dump(donneesjson, f, indent=4, ensure_ascii=False)
