with open('input.txt','r') as file:
    data = file.read().strip()

sections = data.split('\n')
total = 0
for s in sections:
    s1,s2 = s.split(',')
    s1_start, s1_end = map(int,s1.split('-'))
    s2_start,s2_end = map(int,s2.split('-'))
    if (s1_start <= s2.start and s2_end <= s1_end) or (s2_start <= s1.start and s1_end <= s2_end):
        total += 1
print(total)