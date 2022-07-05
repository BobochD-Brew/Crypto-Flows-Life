for k in range(512):
    f = open(str(k)+".json", "w")
    f.write("""
    {
        "name": "Flow Life #"""+str(k)+"""",
        "description": "Flow Life #"""+str(k)+""" \\n by @bobochdbrew",
        "animation_url": "https://bobochd-brew.github.io/Crypto-Flows-Life-Htmls/"""+str(k)+""".html",
        "image": "https://bobochd-brew.github.io/Crypto-Flows-Life-Pngs/"""+str(k)+""".png",
        "creator": "Boboch D. Brew",
        "attributes": [
                { "trait_type": "Cells", "value": \""""+str(sum(map(lambda x: int(x),bin(k)[2:])))+"""\" }
            ]
    }
    """)
    f.close()
