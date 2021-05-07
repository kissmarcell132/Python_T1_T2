def main() -> None:
    __test__ = input('Írjon be egy t betűt ha egy téglatest felszínét és térfogatát szeretné kiszámolni, viszont ha egy henger felszínét és térfogatát szeretné kiszámolni írjon be egy h betűt: ')
    felszín: float = 0
    térfogat: float = 0
    pí = 3.14
    if __test__ == "t":
        a_oldal = float(input('Kérem adja meg a téglatest a oldalának az értékét: '))
        bo_ldal = float(input('Kérem adja meg a téglatest b oldalának az értékét: '))
        c_oldal = float(input('Kérem adja meg a téglatest c oldalának az értékét: '))
        felszín = felszín +(2 * (a_oldal * bo_ldal + a_oldal * c_oldal + bo_ldal * c_oldal))
        térfogat = térfogat + (a_oldal * bo_ldal * c_oldal)
        print(f'A választott test felszíne: {felszín}')
        print(f'A választott test térfogata: {térfogat}')
    elif __test__ == "h":
        sugár = float(input('Kérem adja meg a henger sugarának az értékét: '))
        magasság = float(input('Kérem adja meg a henger magasságának az értékét: '))
        felszín = felszín + 2 * sugár ** 2 * pí + 2 * sugár * pí * magasság
        térfogat = sugár ** 2 * pí * magasság
        print(f'A választott test felszíne: {felszín}')
        print(f'A választott test térfogata: {térfogat}')
    else:
        print('Kérem a "t" és "h" betűk közül válasszon!')


if __name__ == "__main__":
    main()
