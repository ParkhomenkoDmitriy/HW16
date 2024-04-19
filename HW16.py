byte_string = b'r\xc3\xa9sum\xc3\xa9'
decoded_string = byte_string.decode()
print(decoded_string)
latin1_byte_string = decoded_string.encode('latin1')
print(latin1_byte_string)
final_string = latin1_byte_string.decode('latin1')
print(final_string)
