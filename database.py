import sqlite3

def init_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            image1 TEXT,
            image2 TEXT
        )
    ''')
    # Insert sample products (replace image URLs with real ones if available)
    sample_products = [
        (1, "Laptop Pro", "High-performance laptop with 16GB RAM", 999.99, "https://lucek.com.mx/products/placa-con-mecanismo-bp07-m-p", "https://lucek.com.mx/products/placa-con-mecanismo-bp07-m-p"),
        (2, "Wireless Mouse", "Ergonomic mouse with long battery life", 29.99, "https://lucek.com.mx/collections/cbb-cristal-blanco/products/placa-con-1-interruptor-de-escalera-de-3-modulos-bp01-3-cbb", "https://lucek.com.mx/collections/cbb-cristal-blanco/products/placa-con-1-interruptor-de-escalera-de-3-modulos-bp01-3-cbb"),
    ]
    cursor.executemany('INSERT OR REPLACE INTO products (id, name, description, price, image1, image2) VALUES (?, ?, ?, ?, ?, ?)', sample_products)
    conn.commit()
    conn.close()

def get_product(product_id):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    product = cursor.fetchone()
    conn.close()
    return product

if __name__ == "__main__":
    init_db()