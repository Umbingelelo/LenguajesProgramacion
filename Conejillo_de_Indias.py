import re

a="SELECT Telefono FROM Estudiantes WHERE Nombre = ’ Clemente Aguilar ’;"
b="SELECT Edad , Nota FROM Estudiantes INNER JOIN Notas WHERE Estudiantes . Rol = Notas . Rol "
c="SELECT Nombre , Nota FROM Notas ORDER BY Nota DESC"
d="SELECT Nota FROM Notas"
e="SELECT * FROM Estudiantes ;"