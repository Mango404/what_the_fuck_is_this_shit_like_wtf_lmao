a = 10
total = 0
price = float(input())
for s in a:
    Petya = int(input('Enter tovarish Petya`s yavloki`s count'))
    Masha = int(input('Enter tovarish Masha`s yabloki`s count'))
    PetyaCost = float(input('Enter tovarish Petya`s yabloki`s price'))
    MashaCost = float(input('Enter tovarish Masha`s yabloki`s price'))
    summ1 = Petya * PetyaCost - price * Petya
    summ2 = Masha * MashaCost - price * Masha
    if summ1 > 300:
        nolog = summ1 // 5
        Petyasumm = summ1 - nolog
    if summ2 > 300:
        nolog1 = summ2 // 5
        Mashasumm = summ2 - nolog1
    summ = Petyasumm + Mashasumm
    print(summ, 'denyag podnyali tovarishi Petya i Masha.')
    print('U tovarisha Petra', Petyasumm, 'denyag. U tovarisha Mashi', Mashasumm, 'denyag.')
total_summ = summ * 10
print(total_summ, 'zarabotaly Petya i Masha za 10 let')