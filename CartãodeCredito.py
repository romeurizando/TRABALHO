import getpass

def get_payment_info():
    payment_data = {}

    payment_method = input("Escolha o método de pagamento (Cartão de Crédito ou Pix): ").strip().lower()

    if payment_method == "cartão de crédito":
        payment_data["Número do Cartão"] = input("Número do Cartão: ").strip()
        payment_data["Nome Impresso no Cartão"] = input("Nome Impresso no Cartão: ").strip()
        payment_data["Validade"] = input("Validade (MM/AA): ").strip()
        payment_data["CVV"] = getpass.getpass("CVV: ").strip()
    elif payment_method == "pix":
        payment_data["Chave Pix"] = input("Chave Pix: ").strip()
    else:
        print("Método de pagamento não reconhecido.")
        return None

    return payment_data

def main():
    payment_info = get_payment_info()
    if payment_info:
        print("Dados armazenados com sucesso.")
        print(payment_info)
if __name__ == "__main__":
    main()