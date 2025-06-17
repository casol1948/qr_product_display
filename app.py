<<<<<<< HEAD
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, Render!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
=======
from flask import Flask, render_template_string
from database import get_product

app = Flask(__name__)

# HTML template for product page
PRODUCT_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>{{ product[1] }}</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; margin: 20px; }
        .product { max-width: 600px; margin: auto; }
        img { max-width: 200px; margin: 10px; }
    </style>
</head>
<body>
    <div class="product">
        <h1>{{ product[1] }}</h1>
        <p>{{ product[2] }}</p>
        <h2>Price: ${{ product[3] }}</h2>
        {% if product[4] %}
            <img src="{{ product[4] }}" alt="Product Image 1">
        {% endif %}
        {% if product[5] %}
            <img src="{{ product[5] }}" alt="Product Image 2">
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/product/<int:product_id>')
def show_product(product_id):
    product = get_product(product_id)
    if product:
        return render_template_string(PRODUCT_TEMPLATE, product=product)
    return "Product not found", 404

if __name__ == "__main__":
    app.run(debug=True)
>>>>>>> 9c4ea3772b6c8ddaf9ab126621ba611c8e04a3ea
