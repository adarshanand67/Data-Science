from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])
print(Color(red=255, green=0, blue=0))

color = Color(red=255, green=150, blue=200)
# red
print(color.red)

print(f"Red value: {color.red}, Green value: {color.green}, Blue value: {color.blue}")

print(f"Red value: {color[0]}, Green value: {color[1]}, Blue value: {color[2]}")
