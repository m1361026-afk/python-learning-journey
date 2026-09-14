def calculate_subtotal(price, quantity):
    subtotal = price * quantity
    return subtotal

keyboard_subtotal = calculate_subtotal(1200, 1)
mouse_subtotal  = calculate_subtotal(650, 2)
usb_cable_subtotal  = calculate_subtotal(180, 3)

print(f"Keyboard subtotal: {keyboard_subtotal}")
print(f"Mouse subtotal: {mouse_subtotal }")
print(f"USB Cable subtotal: {usb_cable_subtotal }")
