def cookie():
    cad = float(input('How much money in CAD do you have?\n'))
    usd = cad * 0.81
    cookies = usd // 0.50
    usd_change = usd - cookies * 0.50
    cad_change = usd_change / 0.81
    h, f, t, T, F, o, q, d, n, p = change_usd(usd_change)
    hu, fif, tw, te, fi, on, qu, di, ni, pe = change_cad(cad_change)
    print(f'You can buy {cookies} cookies.\n Your change after this purchase would be ${usd_change:.2f} or C${cad_change:.2f}\n')
    print(f'In USD, your change is {h:.f} hundreds, {f:.0f} fifties, {t:.0f} twenties, {T:.0f} tens, {F:.0f} fives, {o:.0f} ones, {q:.0f} quarters, {d:.0f} dimes, {n:.0f} nickels, and {p:.0f} pennies')
    print(f'In CAD, your change is {hu:.0f} hundreds, {fif:.0f} fifties, {tw:.0f} twenties, {te:.0f} tens, {fi:.0f} fives, {on:.0f} ones, {qu:.0f} quarters, {di:.0f} dimes, {ni:.0f} nickels, and {pe:.0f} pennies')

def change_usd(usd_change):    
    hundred = usd_change // 100
    fifty = (usd_change - hundred * 100) // 50
    twenty = (usd_change - hundred * 100 - fifty * 50) // 20
    ten = (usd_change - hundred * 100 - fifty * 50 - twenty * 20) // 10
    five  = (usd_change - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10) // 5
    one = (usd_change - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10) // 1
    quarter = (usd_change - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10 - one * 1) // 0.25
    dime = (usd_change - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10 - one * 1 - quarter * 0.25) // 0.1
    nickel = (usd_change - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10 - one * 1 - quarter * 0.25 - dime * 0.1) // 0.05
    penny = (usd_change - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10 - one * 1 - quarter * 0.25 - dime * 0.1 - nickel * 0.05) // 0.01
    return hundred, fifty, twenty, ten, five, one, quarter, dime, nickel, penny
    
def change_cad(cad_change):
    hundred = cad_change // 100
    fifty = (cad_change - hundred * 100) // 50
    twenty = (cad_change - hundred * 100 - fifty * 50) // 20
    ten = (cad_change - hundred * 100 - fifty * 50 - twenty * 20) // 10
    five  = (cad_change - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10) // 5
    one = (cad_change - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10) // 1
    quarter = (cad_change - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10 - one * 1) // 0.25
    dime = (cad_change - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10 - one * 1 - quarter * 0.25) // 0.1
    nickel = (cad_change - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10 - one * 1 - quarter * 0.25 - dime * 0.1) // 0.05
    penny = (cad_change - hundred * 100 - fifty * 50 - twenty * 20 - ten * 10 - one * 1 - quarter * 0.25 - dime * 0.1 - nickel * 0.05) // 0.01
    return hundred, fifty, twenty, ten, five, one, quarter, dime, nickel, penny