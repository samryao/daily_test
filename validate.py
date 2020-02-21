from id_validator import validator

# 校验身份证号
def vali_dator():
    id = input("输入身份证号: ")
    print(validator.is_valid(id))

vali_dator()
