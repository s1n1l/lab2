"""11. Дано три змінні: X, Y, Z. Якщо їх значення впорядковані за спаданням, то подвоїти їх; в іншому
випадку замінити значення кожної змінної на протилежне"""


x = int(input())
y = int(input())
z = int(input())

def tri(x, y, z,):
     if (x > y) and (y > z):
         x = x*2; y = y*2; z= z*2;
         return (x, y, z)
     else:
         a = (-x); b = (-y); c = (-z);
         return (a, b, c)

print (tri(x, y, z))