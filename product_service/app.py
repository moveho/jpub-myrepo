from flask import Flask, request, jsonify
import pymysql
import os

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host=os.environ.get("DBHOST", "db_service"),
        user=os.environ.get("DBUSER", "root"),
        password=os.environ.get("DBPWD", "pw"),
        db=os.environ.get("DATABASE", "products"),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route("/addproduct", methods=["POST"])
def add_product():
    data = request.get_json()
    required_fields = ["prd_name", "category", "origin_country", "warehouse_location", "price", "stock"]

    if not all(field in data for field in required_fields):
        return jsonify({"message": "Missing fields"}), 400

    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("""
            INSERT INTO products (prd_name, category, origin_country, warehouse_location, price, stock)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            data["prd_name"], data["category"], data["origin_country"],
            data["warehouse_location"], data["price"], data["stock"]
        ))
        conn.commit()
    conn.close()
    return jsonify({"message": "Product added"}), 201

@app.route("/getproduct/<int:prd_id>", methods=["GET"])
def get_product_by_id(prd_id):
    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT prd_id, prd_name, category, origin_country, warehouse_location, price, stock, created_at FROM products WHERE prd_id = %s", (prd_id,))
        product = cursor.fetchone()
    conn.close()

    if product:
        return jsonify(product), 200
    else:
        return jsonify({"message": "Product not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

