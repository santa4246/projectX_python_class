CONST_MATERIAL_WEIGHT = {
    '유리' : 2.4,
    '알루미늄' : 2.7,
    '탄소강' : 7.85
}
PI = 3.14159
MARS_GRAVITY_RATIO = 0.38

def main():
    global material, diameter, thickness, area, weight
    try:
        diameter = input_diameter()
        material = input_material()
        thickness, area, weight = sphere_area(diameter, material)
    except Exception as err :
        print("error: {0}".format(err))

def input_diameter():
    while True:
        try:
            diameter = input('지름을 입력하세요. \n')
            diameter = float(diameter)

            if float(diameter) == 0:
                print("0은 입력할 수 없습니다. 다시 입력하세요.")
                continue
            if float(diameter) < 0:
                print("음수는 입력할 수 없습니다. 다시 입력하세요.")
                continue
            
            break

        except ValueError:
            print("숫자만 입력이 가능합니다. 다시 입력하세요.")

    return diameter

def input_material():
    material_list = ['유리', '알루미늄', '탄소강']
    while True:
        material = input('재질을 입력하세요. \n')

        for value in material_list:
            if material == value:
                return material
            
        print("유리, 알루미늄, 탄소강 중 하나만 입력 가능합니다. 다시 입력하세요.")

        continue


def sphere_area(diameter, material, thickness=1):
    radius = diameter / 2
    area = 2 * PI * radius ** 2
    print(f"반구체의 전체 면적은 약 {area:.3f} 제곱미터입니다.")
    weight = sphere_weight(material, thickness, area)

    return thickness, area, weight

def sphere_weight(material, thickness, area):
    return (area * thickness * CONST_MATERIAL_WEIGHT[material] * MARS_GRAVITY_RATIO) / 1000


if __name__ == "__main__":
    main()

print(f"재질 ⇒ {material}, 지름 ⇒ {diameter}, 두께 ⇒ {thickness}, 면적 ⇒ {area:.3f}, 무게 ⇒ {weight:.3f} kg")
