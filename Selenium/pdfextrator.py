import tabula as ta

df = ta.read_pdf("AlphaPriceList.pdf")
ta.read_pdf("AlphaPriceList.pdf", multiple_tables=True)
ta.convert_into("AlphaPriceList.pdf", "pricelist.xlsx", output_format="xlsx")

