import os
from flask import Flask, request, session, redirect, url_for, render_template
from flask_bcrypt import Bcrypt

def generate_secret_key(length):
    return os.urandom(length)

app = Flask(__name__, template_folder='app/templates', static_folder='app/static')
bcrypt = Bcrypt(app)
app.secret_key = generate_secret_key(length=64)  # Using a longer key length
# Fetch the username and password from environment variables
app_username = os.environ.get("APP_USERNAME")
app_password = os.environ.get("APP_PASSWORD")

# Ensure the password is hashed
hashed_password = bcrypt.generate_password_hash(app_password).decode('utf-8')

# Use the fetched username as the key, and the hashed password as the value
users = {app_username: hashed_password}

@app.route('/')
def home():
    if 'username' not in session:
        return redirect(url_for('login'))

    # Initialize orders in session if not already present
    if 'orders' not in session:
        initial_orders = []
        session['orders'] = initial_orders
        session['orders_display'] = [order for order in initial_orders if order['status'] == 'Pending']
        session['total_completed'] = 0  # Initialize total completed

    return render_template('home.html', orders=session['orders'])
    
@app.route('/add_order', methods=['POST'])
def add_order():
    if 'username' in session:
        # Extract the order value from the form
        order_value = request.form.get('order_value')

        # Create a new order and add it to the session
        new_id = max(order['id'] for order in session['orders']) + 1 if session['orders'] else 1
        new_order = {"id": new_id, "status": "Pending", "value": f"£{float(order_value):.2f}"}
        session['orders'].append(new_order)
        session.modified = True
    return redirect(url_for('home'))

@app.route('/complete_order/<int:order_id>', methods=['POST'])
def complete_order(order_id):
    if 'username' in session:
        # Move the completed order to a separate list in the session
        if 'completed_orders' not in session:
            session['completed_orders'] = []

        for order in session['orders']:
            if order['id'] == order_id:
                order['status'] = 'Completed'
                session['completed_orders'].append(order)
                break

        # Remove the order from the active orders list
        session['orders'] = [order for order in session['orders'] if order['id'] != order_id]

        # Recalculate the total of completed orders
        total_completed = sum(float(order['value'].strip('£')) for order in session['completed_orders'])
        session['total_completed'] = f"£{total_completed:.2f}"
        session.modified = True
    return redirect(url_for('home'))

@app.route('/cancel_order/<int:order_id>', methods=['POST'])
def cancel_order(order_id):
    if 'username' in session:
        session['orders'] = [order for order in session['orders'] if order['id'] != order_id]
        session.modified = True  # Inform Flask that the session has been modified
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate username and password
        user_hashed_password = users.get(username)
        if user_hashed_password and bcrypt.check_password_hash(user_hashed_password, password):
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
