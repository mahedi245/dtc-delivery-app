import sys
import re
with open('D:/Zahir/DeliveryApp/templates/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

fallback_html = """
                                        <!-- পুরনো ডেটা যদি আগের ফরম্যাটে থাকে (Mobile) -->
                                        {% if not order['door_wood'] and not order['frame_wood'] and not order['other_items'] %}
                                        <div class="p-2 mb-2 rounded bg-light border">
                                            <strong>{{ order['product_name'] or '-' }}</strong>
                                            <div class="small text-dark mt-1">
                                                {% if order['wood_type'] %}<span class="badge bg-secondary">{{ order['wood_type'] }}</span>{% endif %}
                                                {% if order['size'] %}<span class="badge bg-secondary">{{ order['size'] }}</span>{% endif %}
                                                {% if order['quantity'] %}<span class="badge bg-dark ms-1">{{ order['quantity'] }}</span>{% endif %}
                                            </div>
                                        </div>
                                        {% endif %}
"""

old_part = """                                        {% if order['other_items'] %}
                                        <div class="small text-secondary mb-1">
                                            <span class="badge bg-info text-dark">🪑 অন্যান্য</span> {{ order['other_items'] }}
                                        </div>
                                        {% endif %}"""

text = text.replace(old_part, old_part + fallback_html)

with open('D:/Zahir/DeliveryApp/templates/index.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Updated index.html with fallback')
