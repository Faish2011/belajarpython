# from barcode import EAN13
# number = '012345678910'

# my_code = EAN13 (number)
# my_code.save ("barcode")


# from barcode import EAN13
# from barcode.writer import ImageWriter

# number = '012345678910'

# my_code = EAN13 (number, writer = ImageWriter ())
# my_code.save ("barcode")


from barcode import EAN13, Code39, Code128, JAN
from barcode.writer import ImageWriter


number1 = '490123456789'
number2 = 'BOOK123'
number3 = 'SN-9876543210'
number4 = '45191763'
my_code1 = EAN13 (number1, writer = ImageWriter ())
my_code2 = Code39 (number2, writer = ImageWriter ())
my_code3 = Code128 (number3, writer = ImageWriter ())


my_code1.save ("barcode_EAN13")
my_code2.save ("barcode_code39")
my_code3.save ("barcode_code128")

















