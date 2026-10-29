import re

with open('DeliveryApp/templates/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_part = re.search(r'<!-- ১\. মোবাইল ভিউ: কার্ড লেআউট.*?<!-- ২\. ডেস্কটপ ভিউ', html, re.DOTALL)
if old_part:
    with open('new_code.html', 'r', encoding='utf-8') as f2:
        new_text = f2.read()
    
    html = html.replace(old_part.group(0), new_text + '\n<!-- ২. ডেস্কটপ ভিউ')
    with open('DeliveryApp/templates/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("SUCCESS")
else:
    print("NOT FOUND")
