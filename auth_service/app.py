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

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"message": "Username and password required"}), 400

    conn = get_db_connection()
    with conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            conn.commit()
        except pymysql.MySQLError as e:
            return jsonify({"message": "Registration failed", "error": str(e)}), 500
    conn.close()
    return jsonify({"message": "User registered"}), 201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    conn = get_db_connection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

