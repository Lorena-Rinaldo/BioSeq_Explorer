
def calcular_gc(dna):
    if not isinstance(dna, str) or dna == "":
        return None

    for base in dna:
        if base not in "ATCG":
            return None

    quantidade_gc = dna.count("G") + dna.count("C")
    total = len(dna)

    percentual = (quantidade_gc / total) * 100

    return percentual


if __name__ == "__main__":
    exemplos = [
        ("ATGC", 50.0),
        ("GGCC", 100.0),
        ("ATAT", 0.0),
        ("ATGX", None),
        ("", None),
    ]

    for sequencia, esperado in exemplos:
        resultado = calcular_gc(sequencia)
        print(f"{sequencia!r}: {resultado} (esperado: {esperado})")
        assert resultado == esperado

    print("Todos os testes passaram!")
