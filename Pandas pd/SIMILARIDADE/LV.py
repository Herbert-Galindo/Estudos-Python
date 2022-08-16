import Levenshtein

ld = Levenshtein.distance('pso_visd_dh00072_bx1_bx2_0.00_6.96m_d.jpg', 'pso_visd_dh00072_bx1_bx2_6.96m_d.jpg')
lr = Levenshtein.ratio('pso_visd_dh00072_bx1_bx2_0.00_6.96m_d.jpg', 'pso_visd_dh00072_bx1_bx2_6.96m_d.jpg')
print(ld)
print(lr)

def longest_common_substring(s1, s2):
   m = [[0] * (1 + len(s2)) for i in range (1 + len(s1))]
   longest, x_longest = 0, 0
   for x in range(1, 1 + len(s1)):
       for y in range(1, 1 + len(s2)):
           if s1[x - 1] == s2[y - 1]:
               m[x][y] = m[x - 1][y - 1] + 1
               if m[x][y] > longest:
                   longest = m[x][y]
                   x_longest = x
           else:
               m[x][y] = 0
   return s1[x_longest - longest: x_longest]

def similarity(s1, s2):
    return 2. * len(longest_common_substring(s1, s2)) / (len(s1) + len(s2)) * 100

similarity('pso_visd_dh00072_bx10_bx20_30.20_69.6m_d.jpg','pso_visd_dh00072_bx1_bx2_6.96m_d.jpg')