def out(h, s) :
    print(h, sorted(list(s)))

s1 = set(input('String 1 : '))
s2 = set(input('String 2 : '))
u = set('qwertyuioplkjhgfdsazxcvbnm')

out('Set 1 :', s1)
out('Set 2 :', s2)
out('a:', s1|s2)
out('b:', s1&s2)
out('c:', s1-s2)
out('d:', s2-s1)
out('e:', u-s1-s2)