# -*- coding: utf-8 -*-
import lib.Rabbit as rabbit

text =  "ေဝလ သီခ်င္းမ်ားစုစည္းမွဳ႕ ၁"
unicode_text = rabbit.uni2zg(text)
zawgyi_text = rabbit.zg2uni(text)
print(type(text))
print(unicode_text)
print(zawgyi_text)

