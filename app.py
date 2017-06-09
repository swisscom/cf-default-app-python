import os
from flask import Flask, request, render_template

# Bootstrap the app
app = Flask(__name__)

# Set the port dynamically with a default of 3000 for local development
port = int(os.getenv('PORT', '3000'))

# Our base route which renders an HTML template
@app.route('/')
def index():
    return render_template('index.html', env_vars=os.environ, req_headers=request.headers, req_params=request.args)

# Start the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
