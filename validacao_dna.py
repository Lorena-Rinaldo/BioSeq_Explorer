
def validar_dna(dna):
    if not isinstance(dna, str) or dna == "":
        return False

    for base in dna:
        if base not in "ATCG":
            return False

    return True


if __name__ == "__main__":
    exemplos = [
        ("ATGCCCTA", True),
        ("ATGXCCTA", False),
        ("", False),
        ("ATGU", False),
        ("ATG123", False),
    ]

    for sequencia, esperado in exemplos:
        obtido = validar_dna(sequencia)
        print(f"{sequencia!r}: {obtido} (esperado: {esperado})")
        assert obtido == esperado

    print("Todos os testes passaram!")
  