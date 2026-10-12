# Ejercicio: Confirmación de pedido pequeño

# Variables a utilizar en este ejercicio
# item_name	str	Entidad de dominio: artículo.
# unit_price_cents	int	Entidad de dominio: precio unitario.
# requested_quantity	int	Entidad de dominio: cantidad solicitada.
# total_amount_cents	int	Entidad de dominio: importe total.


from typing import Any, Dict, List, Optional, Tuple, Union

def confirmation_order(item_name: str, unit_price_cents: int, requested_quantity: int) -> Dict[str, Union[str, int]]:
    clear_item = item_name.strip()
    if not clear_item:
        raise ValueError("El nombre del artículo no puede estar vacío.")
    unit_price = unit_price_cents
    if unit_price <= 0:
        raise ValueError("El precio unitario no puede ser negativo.")
    if requested_quantity < 1 or requested_quantity > 20:
        raise ValueError("La cantidad solicitada debe estar entre 1 y 20.")
    total_amount_cents = unit_price_cents * requested_quantity
    return {
            "item_name": clear_item,
            "unit_price_cents": unit_price_cents,
            "requested_quantity": requested_quantity,
            "total_amount_cents": total_amount_cents
        }


print(confirmation_order("  Camiseta  ", 300, 3))  # Ejemplo de uso