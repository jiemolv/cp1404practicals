# 创建颜色名称与十六进制代码的常量字典
COLORS = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF",
    "BLUEVIOLET": "#8A2BE2"
}

for colour_name, colour_code in COLORS.items():
    print(f"{colour_name.upper()} is {colour_code}")

while True:
    colour_name = input("Enter colour name:").upper()

    if colour_name == "":
        break

    try:
        colour_code = COLORS[colour_name]
        print(f"{colour_name.upper()} is {colour_code}")
    except KeyError:
        print("Invalid color name")