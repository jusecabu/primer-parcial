## Requerimientos funcionales

- [ ] El sistema debe de poder registrar un nuevo estilo de naves en caso tal que se autorice y ademas debe tener los otros 4 estilos de naves
- [ ] El sistema debe verificar que un estilo no tenga dos naves __X__ sobre un mismo eje __O__
- [ ] El sistema debe dejar iniciar la cotización
- [ ] El sistema debe dejar registrar cada ventana en la cotización actual
- [ ] El sistema debe dejar ingresar el alto y ancho de toda la ventana
- [ ] El sistema debe verificar que el alto y ancho sea mayor a $8cm \times 8cm$
- [ ] El sistema debe calcular el tamaño de cada nave con el ancho y el alto
- [ ] El sistema debe calcular cuantas chapas tendrá la ventana dependiendo de cuantas naves __X__ tenga
- [ ] El sistema debe dejar elegir el acabado del aluminio de la nave pulido, lacado brillante, lacado mate y anodizado
- [ ] El sistema debe dejar elegir el tipo de vidrio transparente, bronce, azul y adicional se desea agregar un esmerilado al vidrio
- [ ] El sistema debe calcular el precio por ventana y el total en la cotización

## Requerimientos no funcionales

- [ ] El sistema cumple con mostrar un menu textual
_ [ ] El sistema cumple con mostrar cada opresión con texto
- [ ] El sistema cumple con adicionar un descuento después de comprar mas de 100 ventanas

## Detalles adicionales

### Estilos de nave preestablecidos

'O' indica que es una nave estática y 'X' indica que es una nave que se desliza. Los estilos preestablecidos de las naves serian los siguientes:

- O
- XO
- OXO
- OXXO

### Tabla de precios

- Tabla de los acabado de aluminio

  | Acabado          | $precio \times metro$ |
  |------------------|----------------------:|
  | Pulido           |           $ 50,700.00 |
  | Lacado brillante |           $ 54,200.00 |
  | Lacado mate      |           $ 53,600.00 |
  | Anodizado        |           $ 57,300.00 |

- Tablas de precio de los vidrios

  | Tipo de vidrio        | $precio \times cm^2$ |
  |-----------------------|---------------------:|
  | Transparente          |               $ 8.25 |
  | Bronce                |               $ 9.15 |
  | Azul                  |              $ 12.75 |
  | Adicional: Esmerilado |               $ 5.20 |