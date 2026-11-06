
def contar_nucleotideos(dna):
    if not isinstance(dna, str) or not dna:
        return None

    for base in dna:
        if base not in "ATCG":
            return None

    contagem = {
        "A": dna.count("A"),
        "T": dna.count("T"),
        "C": dna.count("C"),
        "G": dna.count("G")
    }

    return contagem


if __name__ == "__main__":
    exemplos = [
        ("ATGCCGTA", {"A": 2, "T": 2, "C": 2, "G": 2}),
        ("AAAA", {"A": 4, "T": 0, "C": 0, "G": 0}),
        ("ATGX", None),
        ("", None)
    ]

    for sequencia, esperado in exemplos:
        resultado = contar_nucleotideos(sequencia)
        print(f"{sequencia!r}: {resultado}")
        assert resultado == esperado

    print("Todos os testes passaram!")
