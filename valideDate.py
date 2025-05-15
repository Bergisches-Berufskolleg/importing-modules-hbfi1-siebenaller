from leapYear import isLeapYear


def validateDate(tag, monat, jahr):
    if not (isinstance(tag, int) and isinstance(monat, int) and isinstance(jahr, int)):
        return False
    if jahr < 1 or monat < 1 or monat > 12 or tag < 1:
        return False
    tage_im_monat = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if monat == 2 and isLeapYear(jahr):
        max_tag = 29
    else:
        max_tag = tage_im_monat[monat]
    if tag > max_tag:
        return False
    return True

def main():
    tag   = int(input("Gib ein Tag ein: "))
    monat = int(input("Gib ein Monat ein: "))
    jahr  = int(input("Gib ein Jahr ein: "))
    print(validateDate(tag, monat, jahr))

if __name__ == "__main__":
    main()
