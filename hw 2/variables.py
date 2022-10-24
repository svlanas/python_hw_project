# Спосіб 1
var1 = 10
var2 = 20
var3 = var1
var1 = var2
var2 = var3
print('змінна 1 =', var1, '; змінна 2 =', var2)

# Спосіб 2
var12 = 10
var22 = 20
var12, var22 = var22, var12
print('змінна 12 =', var12, '; змінна 22 =', var22)

# Спосіб 3
var13 = 10
var23 = 20
var13 = var13 + var23
var23 = var13 - var23
var13 = var13 - var23
print('змінна 13 =', var12, '; змінна 23 =', var22)
