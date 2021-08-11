

# text = "X-DSPAM-Confidence:    0.8475"
# textmod = text[24:32]
# print(float(textmod))

text = "X-DSPAM-Confidence:    0.8475"
textmod = text.find('.')

print(float(text[24:30]))