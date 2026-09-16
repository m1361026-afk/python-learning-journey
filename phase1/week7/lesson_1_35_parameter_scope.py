total = 100
def add_money(total):
    total += 50
    print(f"Inside function: {total}")
    return total

updated_total = add_money(total)
print(f"Outside original total: {total}")
print(f"Returned total: {updated_total}")