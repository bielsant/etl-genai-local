import random

def gerar_beneficio(cartao):
    beneficios = {
        "Gold": [
            "cashback em compras",
            "limite diferenciado",
            "promoções exclusivas"
        ],
        "Platinum": [
            "acesso a salas VIP",
            "milhas aéreas",
            "seguro viagem"
        ],
        "Black": [
            "concierge 24h",
            "benefícios premium internacionais",
            "alto limite"
        ],
        "Silver": [
            "controle pelo app",
            "segurança nas transações",
            "facilidade no dia a dia"
        ]
    }

    return random.choice(beneficios.get(cartao, ["benefícios exclusivos"]))


def gerar_mensagem(nome, cartao):
    beneficio = gerar_beneficio(cartao)

    return f"Olá {nome}, seu cartão {cartao} oferece {beneficio}. Aproveite!"


def transform_data(df):
    print("[TRANSFORM] Gerando mensagens...")

    df["mensagem"] = df.apply(
        lambda row: gerar_mensagem(row["nome"], row["cartao"]),
        axis=1
    )

    return df