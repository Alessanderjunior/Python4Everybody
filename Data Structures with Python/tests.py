data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])

# text = "X-DSPAM-Confidence:    0.8475"
# textmod = text[24:32]
# print(float(textmod))

text = "X-DSPAM-Confidence:    0.8475"
textmod = text.find('.')

print(float(text[24:30]))