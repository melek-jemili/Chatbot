import openai
import os
from datetime import datetime

# Configuration de l'API OpenAI
# Remplacez "VOTRE_CLE_API" par votre véritable clé API OpenAI
openai.api_key = "VOTRE_CLE_API"

# Contexte initial pour le chatbot
CONTEXTE_INITIAL = """Tu es un assistant touristique français expert. Tu dois :
- Donner des informations précises sur les attractions touristiques
- Suggérer des activités selon les intérêts du visiteur
- Fournir des conseils pratiques sur les transports et l'hébergement
- Rester poli et professionnel
- Répondre en français
- Garder des réponses concises mais informatives"""

def obtenir_reponse_openai(message, historique=[]):
    """
    Obtient une réponse via l'API OpenAI en utilisant l'historique de la conversation
    """
    try:
        # Préparation des messages avec le contexte et l'historique
        messages = [
            {"role": "system", "content": CONTEXTE_INITIAL}
        ]
        
        # Ajout de l'historique des conversations
        for h in historique[-5:]:  # Garder seulement les 5 derniers échanges
            messages.append({"role": "user", "content": h["user"]})
            messages.append({"role": "assistant", "content": h["assistant"]})
            
        # Ajout du message actuel
        messages.append({"role": "user", "content": message})

        # Appel à l'API OpenAI
        response = openai.chat.completions.create(
            model="gpt-4-turbo",
            messages=messages,
            max_tokens=150,
            temperature=0.7
        )
        
        return response.choices[0].message.content

    except Exception as e:
        return f"Désolé, une erreur s'est produite : {str(e)}"

def sauvegarder_conversation(historique):
    """
    Sauvegarde l'historique de la conversation dans un fichier
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    with open(f"conversation_{timestamp}.txt", "w", encoding="utf-8") as f:
        for echange in historique:
            f.write(f"Utilisateur: {echange['user']}\n")
            f.write(f"TravelPal: {echange['TravelPal']}\n\n")

def chatbot_touristique():
    """
    Fonction principale du chatbot
    """
    print("TravelPal Touristique: Bonjour ! Je suis votre guide virtuel. Comment puis-je vous aider ?")
    print("(Tapez 'au revoir' pour quitter)")
    
    historique = []
    
    while True:
        # Obtenir l'entrée de l'utilisateur
        message = input("Vous: ").strip()
        
        # Vérifier si l'utilisateur veut quitter
        if message.lower() == "au revoir":
            print("TravelPal: Au revoir ! J'espère avoir pu vous aider dans vos projets de voyage !")
            sauvegarder_conversation(historique)
            break
        
        # Obtenir la réponse via OpenAI
        reponse = obtenir_reponse_openai(message, historique)
        
        # Sauvegarder l'échange dans l'historique
        historique.append({
            "user": message,
            "TravelPal": reponse
        })
        
        # Afficher la réponse
        print("TravelPal:", reponse)

if __name__ == "__main__":
    chatbot_touristique()
