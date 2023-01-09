def colorcode(hex):
    rgb=[]
    for i in (0,2,4):
        decimal = int(hex[i:i+2],16)
        rgb.append(decimal)
    return tuple(rgb)
print(colorcode('FF0000'))