import colorgram

colors = colorgram.extract('/home/kajal/Documents/Python-Revision/Liabraries/Turtle/image.png', 38)
# print(colors)
l = []
for i in colors:
    r = i.rgb.r
    g = i.rgb.g
    b = i.rgb.b
    l.append((r, g, b))
# print(l)

