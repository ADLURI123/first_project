from django.http import HttpResponse
def print_pattern(request) :
    a="Moon flowers bloom only at night, closing during the day."
    n=len(a)
    s=""
    v = {'a':0,'e':0,'i':0,'o':0,'u':0}
    for i in range(n):
        for j in v.keys():
            if(a[i]==j):
                v[j]=v[j]+1
    for i in v.keys():
        if(v[i]>0):
            s=s+i
    return HttpResponse(s)