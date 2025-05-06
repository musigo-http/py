import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Infos d'authentification
adresse_email = "mateo@musigo.duckdns.org"
mot_de_passe_app = "P@ssW0rd!2023"

# Construction du mail
destinataire = "mateo.ahmed-tayeb@musigo.duckdns.org"
sujet = "Objet du mail"
corps = "Ceci est un mail envoyé automatiquement depuis un script Python 😎"

message = MIMEMultipart()
message["From"] = adresse_email
message["To"] = destinataire
message["Subject"] = sujet

# Attacher le texte brut
message.attach(MIMEText(corps, "plain"))

# Connexion au serveur SMTP Postfix (auto-hébergé)
with smtplib.SMTP("musigo.duckdns.org", 25) as serveur:
    serveur.ehlo()
    serveur.starttls()  # Passage en TLS
    serveur.login(adresse_email, mot_de_passe_app)
    serveur.sendmail(adresse_email, destinataire, message.as_string())

print("✅ Email envoyé avec succès.")
