

from flask import Flask, render_template, request, flash, redirect, url_for
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secret-key"

# 🔥 MongoDB bağlantısı
# client = MongoClient("mongodb+srv://ahmdag2041_db_user:HTQoEzTE2wQ7DgCG@cluster0.fqqqhoz.mongodb.net/")




client = MongoClient(
    "mongodb+srv://ahmdag2041_db_user:HTQoEzTE2wQ7DgCG@cluster0.fqqqhoz.mongodb.net/dbname?retryWrites=true&w=majority&tlsAllowInvalidCertificates=true"
)


db = client["sutasarruf"]                # → Veritabanı (ilk kayıt gelince oluşur)
collection = db["iletisim_mesajlari"]    # → Koleksiyon (ilk kayıt gelince oluşur)

@app.route("/evde-su-tasarrufu-nasil-yapilir")
def evde_su_tasarrufu():
    return render_template("evde-su-tasarrufu.html")



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # 🔥 MongoDB'ye kaydet
        collection.insert_one({
            "name": name,
            "email": email,
            "message": message,
            "time": datetime.now()
        })

        flash("Mesajınız başarıyla gönderildi!", "success")
        return redirect(url_for("index"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)






from flask import Response

@app.route("/sitemap.xml")
def sitemap():
    sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://sutasarrufrehberi.com/</loc>
    <lastmod>2025-01-01</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
"""
    return Response(sitemap_xml, mimetype="application/xml")










# from flask import Flask, render_template, request, flash, redirect, url_for

# app = Flask(__name__)
# app.secret_key = "secret-key"

# @app.route("/", methods=["GET", "POST"])
# def index():
#     if request.method == "POST":
#         name = request.form.get("name")
#         email = request.form.get("email")
#         message = request.form.get("message")
#         print(f"Form Gönderildi: {name}, {email}, {message}")
#         flash("Mesajınız başarıyla gönderildi!", "success")
#         return redirect(url_for("index"))
#     return render_template("index.html")

# if __name__ == "__main__":
#     app.run(debug=True)
