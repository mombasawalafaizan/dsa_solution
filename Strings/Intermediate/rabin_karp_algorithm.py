def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    d = 256 # Considering ASCII values
    p = 0   # Hash value for pattern
    t = 0   # Hash value for current substring from text
    h = 1
    for i in range(M-1):
        h = (h*d)%q
    
    for i in range(M):
        p = (d*p + ord(pat[i]))%q
        t = (d*t + ord(txt[i]))%q
    
    for i in range(N-M+1):
        if p==t:
            j = 0
            while j < M:
                if txt[i+j] != pat[j]:
                    break
                else:
                    j+=1
            if j == M:
                print('Pattern found at index:', i)
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q
            if t < 0:
                t = t+q

txt = 'GEEKS FOR GEEKS'
pat = 'GEEK'
q = 101 # A prime number
search(pat, txt, q)