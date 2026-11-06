
def complementar_dna(dna):
    if not isinstance(dna, str) or dna == "":
        return None

    pares = {"A": "T", "T": "A", "C": "G", "G": "C"}
    complementar = ""

    for base in dna:
        if base not in pares:
            return None
        complementar += pares[base]

    return complementar


if __name__ == "__main__":
    exemplos = [
        ("ATGCCGTA", "TACGGCAT"),
        ("AAAA", "TTTT"),
        ("GGCC", "CCGG"),
        ("ATGX", None),
        ("", None),
    ]

    for sequencia, esperado in exemplos:
        resultado = complementar_dna(sequencia)
        print(f"{sequencia!r}: {resultado} (esperado: {esperado})")
        assert resultado == esperado

    print("Todos os testes passaram!")
