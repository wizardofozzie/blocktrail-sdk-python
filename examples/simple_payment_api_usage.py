import blocktrail

client = blocktrail.APIClient("MYKEY", "MYSECRET", testnet=True)

(wallet, backup_private_key) = client.create_new_wallet("testwallet", "testpassword")

wallet = client.init_wallet("testwallet", "testpassword")

print wallet.new_adress()
print wallet.new_adress()
print wallet.new_adress()

print wallet.pay([
    ("mtKuzf8QxJuziTxUyH81KtVhNUN9ps4aKJ", 1.0),
    ("2NGU9xir2geepbHznsuXt17HDfEqHoGWnaB", 0.1),
])
