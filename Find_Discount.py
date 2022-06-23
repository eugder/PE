def dis(price, discount):
    end_price = price*((100-discount)/100)
    return round(end_price, 2)

print (dis(89.27, 20))