from flask import Flask, render_template, request, redirect, session, url_for, flash
import requests
import os

app = Flask(__name__)
app.secret_key = 'frontend_secret'

AUTH_URL = "http://auth_service:5001"
PRODUCT_URL = "http://product_service:5002"

@app.route("/")
def home():
    return render_template("addproduct.html", user=session.get("user"))

@app.route("/about")
def about():
    return render_template("about.html", user=session.get("user"))

@app.route("/addproduct", methods=["POST"])
def add_product():
    if not session.get("user"):
        flash("로그인 후 이용 가능합니다.")
        return redirect(url_for("login"))

    data = {
        "prd_name": request.form["prd_name"],
        "category": request.form["category"],
        "origin_country": request.form["origin_country"],
        "warehouse_location": request.form["warehouse_location"],
        "price": request.form["price"],
        "stock": request.form["stock"]
    }

    res = requests.post(f"{PRODUCT_URL}/addproduct", json=data)
    if res.status_code == 201:
        return render_template("addproductoutput.html", name=data['prd_name'], user=session.get("user"))
    return res.text, res.status_code

@app.route("/getproduct")
def get_product():
    return render_template("getproduct.html", user=session.get("user"))

@app.route("/fetchproduct", methods=["POST"])
def fetch_product():
    prd_id = request.form["prd_id"]
    res = requests.get(f"{PRODUCT_URL}/getproduct/{prd_id}")
    if res.status_code == 200:
        raw = res.json()
        data = {
            "id": raw["prd_id"],
            "name": raw["prd_name"],
            "category": raw["category"],
            "country": raw["origin_country"],
            "location": raw["warehouse_location"],
            "price": raw["price"],
            "stock": raw["stock"],
            "created": raw["created_at"]
        }
        return render_template("getproductoutput.html", **data, user=session.get("user"))
    else:
        return "상품을 찾을 수 없습니다", 404


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        res = requests.post(f"{AUTH_URL}/register", json={"username": username, "password": password})
        if res.status_code == 201:
            return redirect(url_for("login"))
        else:
            return res.text, res.status_code
    return render_template("register.html", user=session.get("user"))
2
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        res = requests.post(f"{AUTH_URL}/login", json={"username": username, "password": password})
        if res.status_code == 200:
            session["user"] = username
            return redirect("/")
        else:
            flash("로그인 정보가 올바르지 않습니다.")
            return redirect(url_for("login"))
    return render_template("login.html", user=session.get("user"))

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

