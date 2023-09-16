def identify_card_type(prefix):
    card_prefixes = {
        "4": "Visa",
        "5": "Mastercard",
        "3": "American Express",
        "6": "Discover",
        "34": "American Express",
        "37": "American Express",
        "51": "Mastercard",
        "52": "Mastercard",
        "53": "Mastercard",
        "54": "Mastercard",
        "55": "Mastercard",
        "6011": "Discover",
        "3": "Diners Club",
        "1800": "Diners Club",
        "2014": "Diners Club",
        "3088": "Diners Club",
        "36": "Diners Club",
        "300": "Diners Club",
        "6011": "Discover",
        "622126": "Discover",
        "622925": "Discover",
        "601100": "Discover",
    }

    for card_prefix, card_type in card_prefixes.items():
        if prefix.startswith(card_prefix):
            return card_type

    return "Inconnu"

user_input = input("Veuillez entrer les cinq premiers chiffres de votre carte : ")
card_type = identify_card_type(user_input)
print(f"Type de carte : {card_type}")

input("Appuyez sur Entrée pour quitter...")