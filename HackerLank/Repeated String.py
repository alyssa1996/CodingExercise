def repeatedString(s, n):
    if len(s)==1:
        if s[0]=='a':
            return n
        else:
            return 0
    else:
        count=s.count('a')*(n//len(s))
        if n%len(s)==0:
            return count
        else:
            count+=s[:n%len(s)].count('a')
            return count
