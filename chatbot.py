import openai
# Remplacez 'YOUR_API_KEY' par votre clé API OpenAI
openai.api_key = "YOUR_API_KEY"
def chatbot_gpt(prompt):
    response = openai.Completion.create(
        model="gpt-4-turbo",  # Modèle à utiliser
        prompt=prompt,
        max_tokens=150,
        temperature=0.7,
        top_p=1.0,)

    return response.choices[0].text.strip()

def main():
    print("TravelPal : Bonjour ! Posez-moi une question. Tapez 'au revoir' pour quitter.")
    while True:
        user_input = input("Vous : ")
        if user_input.lower() == "au revoir":
            print("TravelPal : Au revoir !")
            break
        response = chatbot_gpt(user_input)
        print(f"TravelPal : {response}")
if __name__ == "__main__":
    main()
