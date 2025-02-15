d={101:"John Doe", 102:"Jane Smith", 103:"Peter Johnson"}
s_d=dict(sorted(d.items(),key=lambda x:x[1]))
print(s_d)