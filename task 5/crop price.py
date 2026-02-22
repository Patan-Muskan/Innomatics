def premium_crop_filter(price):
    premium = []
    for p in price:
        if p > 2000:
            premium.append(p)
    print("Premium Crop Prices:", premium)
premium_crop_filter([1500, 2500, 1800, 3200])