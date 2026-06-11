import pandas as pd

data = {
    'review': [
        'aplikasi bagus banget belanja jadi mudah',
        'pengiriman lama sekali kecewa',
        'murah dan banyak diskon',
        'sering error aplikasinya pas mau bayar',
        'barang sampai dengan selamat kualitas oke',
        'penjual tidak amanah jangan beli di sini',
        'suka banget sama gratis ongkirnya',
        'cs tidak membantu sama sekali'
    ],
    'label': [1, 0, 1, 0, 1, 0, 1, 0] # 1 positif, 0 negatif
}

df = pd.DataFrame(data)
df.to_csv('review_shopee.csv', index=False)
print("File review_shopee.csv berhasil dibuat!")