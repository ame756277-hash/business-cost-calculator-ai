# business-cost-calculator-ai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json

    raw = float(data.get("raw", 0))
    packaging = float(data.get("packaging", 0))
    transport = float(data.get("transport", 0))
    other = float(data.get("other", 0))
    hours = float(data.get("hours", 0))
    rate = float(data.get("rate", 0))
    profit_percent = float(data.get("profit", 0))

    labor_cost = hours * rate
    total_cost = raw + packaging + transport + other + labor_cost

    profit = total_cost * (profit_percent / 100)
    selling_price = total_cost + profit

    safe_ad_budget = selling_price * 0.2

    return jsonify({
        "total_cost": round(total_cost, 2),
        "selling_price": round(selling_price, 2),
        "profit": round(profit, 2),
        "safe_ad_budget": round(safe_ad_budget, 2)
    })

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get("message", "").lower()

    if "price" in message or "দাম" in message:
        reply = "আপনার খরচ অনুযায়ী সঠিক দাম নির্ধারণে আমি সাহায্য করতে পারি। আগে হিসাব দিন।"
    elif "loss" in message or "লস" in message:
        reply = "লস এড়াতে আপনার খরচ কমানো বা দাম স্ট্র্যাটেজি পরিবর্তন করা দরকার।"
    elif "ad" in message or "ads" in message:
        reply = "Facebook ads budget সাধারণত profit এর ২০% এর মধ্যে রাখা ভালো।"
    else:
        reply = "আমি আপনার Business AI Assistant। আপনার প্রশ্ন বিস্তারিত লিখুন।"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
  
