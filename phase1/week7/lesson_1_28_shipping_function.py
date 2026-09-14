def check_shipping(total):
    if total >= 7000:
        return "Free shipping"
    else:
        return "Shipping fee required"

free_shipping_result = check_shipping(8240)
threshold_result = check_shipping(7000)
shipping_fee_result = check_shipping(6999)

print(free_shipping_result)
print(threshold_result)
print(shipping_fee_result)