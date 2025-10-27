from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    event = request.form['event']
    tickets = request.form['tickets']
    seat_type = request.form['seatType']
    return f"""
    <body style='font-family:Arial;background:#f5f6fa;display:flex;justify-content:center;align-items:center;height:100vh;'>
        <div style='background:white;padding:30px;border-radius:10px;box-shadow:0 0 10px #ccc;text-align:center;width:350px;'>
            <h2 style='color:#2f3640;'>🎟️ Booking Confirmed!</h2>
            <p><b>Name:</b> {name}</p>
            <p><b>Event:</b> {event}</p>
            <p><b>Tickets:</b> {tickets}</p>
            <p><b>Seat Type:</b> {seat_type}</p>
            <a href='/' style='text-decoration:none;color:white;background:#00a8ff;padding:10px 20px;border-radius:5px;'>Back to Home</a>
        </div>
    </body>
    """

if __name__ == '__main__':
    app.run(debug=True)