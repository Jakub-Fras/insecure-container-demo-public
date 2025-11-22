"""
Intentionally vulnerable demo app for demonstration and testing purposes.

This is a small Flask app with deliberately bad practices:
- Hardcoded secret key
- Debug mode enabled by default
- Unsafe YAML loading
- Old dependency versions (defined in requirements.txt)
"""

from flask import Flask, request
import yaml
import os

app = Flask(__name__)

# Hardcoded secret (bad practice)
app.config["SECRET_KEY"] = "super-secret-hardcoded-key"

@app.route("/")
def index():
    return "Intentionally vulnerable demo app"

# Vulnerable endpoint (unsafe YAML loading)
@app.route("/yaml", methods=["POST"])
def yaml_load():
    # This is intentionally unsafe (yaml.load instead of safe_load)
    data = yaml.load(request.data, Loader=yaml.FullLoader)
    return {"loaded": str(data)}

if __name__ == "__main__":
    # Debug mode defaulting to ON (bad for production)
    debug_mode = os.environ.get("FLASK_DEBUG", "1")
    app.run(host="0.0.0.0", port=8080, debug=debug_mode == "1")
