class MinhaClasse:
    def __enter__(self):
        print("Entrei kkkk")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saii kkk :o")


with MinhaClasse() as kk:
    print("Entou aqui dentro")