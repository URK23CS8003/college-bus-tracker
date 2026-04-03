from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime

app = Flask(__name__)

buses = {
    "B01": {"route": "Route 1 - Main Gate to Hostel A", "driver": "Ravi Kumar", "status": "On Time", "last_updated": "08:00 AM", "stops": ["Main Gate", "Library", "Engineering Block", "Hostel A"]},
    "B02": {"route": "Route 2 - Railway Station to College", "driver": "Suresh M", "status": "Delayed", "last_updated": "08:15 AM", "stops": ["Railway Station", "Bus Stand", "Market", "College"]},
    "B03": {"route": "Route 3 - City Center to Campus", "driver": "Karthik R", "status": "On Time", "last_updated": "08:05 AM", "stops": ["City Center", "Park", "Hospital", "Campus"]},
    "B04": {"route": "Route 4 - North Zone to College", "driver": "Muthu S", "status": "Not Started", "last_updated": "07:50 AM", "stops": ["North Zone", "Temple", "School", "College"]},
    "B05": {"route": "Route 5 - South Zone to Campus", "driver": "Arjun P", "status": "On Time", "last_updated": "08:10 AM", "stops": ["South Zone", "Mall", "Hospital", "Campus"]},
}

announcements = [
    {"id": 1, "message": "Bus B02 delayed by 15 minutes due to traffic near Railway Station.", "time": "08:15 AM"},
    {"id": 2, "message": "All buses will follow alternate route tomorrow due to college event.", "time": "07:45 AM"},
]

@app.route("/")
def index():
    return render_template("index.html", buses=buses, announcements=announcements)

@app.route("/admin")
def admin():
    return render_template("admin.html", buses=buses, announcements=announcements)

@app.route("/admin/update", methods=["POST"])
def update_status():
    bus_id = request.form.get("bus_id")
    status = request.form.get("status")
    if bus_id in buses and status:
        buses[bus_id]["status"] = status
        buses[bus_id]["last_updated"] = datetime.now().strftime("%I:%M %p")
    return redirect(url_for("admin"))

@app.route("/admin/announce", methods=["POST"])
def add_announcement():
    message = request.form.get("message")
    if message:
        new_id = max([a["id"] for a in announcements], default=0) + 1
        announcements.insert(0, {
            "id": new_id,
            "message": message,
            "time": datetime.now().strftime("%I:%M %p")
        })
    return redirect(url_for("admin"))

@app.route("/api/buses")
def api_buses():
    return jsonify(buses)

@app.route("/api/buses/<bus_id>")
def api_bus(bus_id):
    if bus_id in buses:
        return jsonify(buses[bus_id])
    return jsonify({"error": "Bus not found"}), 404

@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
