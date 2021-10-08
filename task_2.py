def sec_to_hours(seconds):
    a=str(seconds//3600)
    b=str((seconds%3600)//60)
    c=str((seconds%3600)%60)
    d=["{}:{}:{}".format(a, b, c)]
    return d


print(sec_to_hours(1000))


print(sec_to_hours(30*60*24+105))
