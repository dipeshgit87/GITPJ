count = 0
P_n = '+977+11'
F_r = ''
for i in range(len(P_n)):
    if P_n[i] == '+':
        count = count + 1
        if count == 2:
            continue
    F_r = F_r + P_n[i]