import qrcode
from database import get_product

def generate_qr_codes(base_url):
    for product_id in range(1, 3):  # Adjust range based on number of products
        product = get_product(product_id)
        if product:
            qr_url = f"{base_url}/product/{product_id}"
            qr = qrcode.QRCode(version=1, box_size=10, border=4)
            qr.add_data(qr_url)
            qr.make(fit=True)
            img = qr.make_image(fill='black', back_color='white')
            img.save(f"qr_product_{product_id}.png")
            print(f"Generated QR code for {product[1]}: qr_product_{product_id}.png")

if __name__ == "__main__":
    # Use local URL for testing
    base_url = "http://localhost:5000"
    generate_qr_codes(base_url)