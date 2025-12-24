from flask import Flask, request

app = Flask(__name__)

# Simple function with if-else
def careerGuidance(interest):
    if interest == "science":
        return "You can choose Engineering, Medical or Research field."
    elif interest == "commerce":
        return "You can choose CA, BBA, MBA or Banking field."
    elif interest == "arts":
        return "You can choose Law, Journalism, Design or Teaching."
    else:
        return "Please select a valid interest."

# Home page route
@app.route("/")
def home():
    return """
    <h1>Career Guidance for Students</h1>
    <p>Select your interest:</p>
    <form action="/result" method="post">
        <select name="interest">
            <option value="science">Science</option>
            <option value="commerce">Commerce</option>
            <option value="arts">Arts</option>
        </select>
        <br><br>
        <input type="submit" value="Get Career Suggestion">
    </form>
    """

# Result page route
@app.route("/result", methods=["POST"])
def result():
    interest = request.form["interest"]
    suggestion = careerGuidance(interest)  # Corrected function name

    return f"""
    <h2>Your Interest: {interest}</h2>
    <h3>Career Suggestion:</h3>
    <p>{suggestion}</p>
    <a href="/">Go Back</a>
    """

# Run the server
if __name__ == "__main__":
    app.run(debug=True)
