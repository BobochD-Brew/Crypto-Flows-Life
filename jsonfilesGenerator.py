for k in range(512):
    f = open(str(k)+".json", "w")
    f.write("""
    {
        "name": "Crypto Flow Life #"""+str(k)+"""",
        "description": "Crypto Life #"""+str(k)+""" \\nby @bobochdbrew",
        "animation_url": "https://bobochd-brew.github.io/Crypto-Flows-Life-Htmls/"""+str(k)+""".html",
        "image": "https://bobochd-brew.github.io/Crypto-Flows-Life-Pngs/"""+str(k)+""".png",
        "creator": "Boboch D. Brew"}
    """)
    f.close()
