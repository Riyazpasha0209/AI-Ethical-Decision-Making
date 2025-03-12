from flask import Flask, render_template, request
from google import genai

app = Flask(__name__)

# Configure Google Gemini AI
client = genai.Client(api_key="Gemini_api_key")

@app.route("/", methods=["GET", "POST"])
def index():
    ai_response = None

    if request.method == "POST":
        # Get input values
        q1 = request.form.get("q1", "").strip()
        q2 = request.form.get("q2", "").strip()
        q3 = request.form.get("q3", "").strip()
        q4 = request.form.get("q4", "").strip()

        combined_response = f"As an ethical decision-making AI assistant, analyze the following business decision:\n Question: {q1}  \nContext: {q2}  \nStakeholders_involved: {q3.join(', ')}  \nPotential_Impact: {q4} \nPlease provide a comprehensive ethical analysis and recommendation, considering: \n1. Ethical principles involved \n2. Potential consequences for all stakeholders \n3. Risk assessment \n4. Specific recommendations for proceeding \n5. Mitigation strategies \nFormat the response in a clear, professional manner. Give response in 3-4 lines precisely"


        response = client.models.generate_content(
        model="gemini-2.0-flash", contents=combined_response
        )

        # Extract AI response
        ai_response = response.text if response and hasattr(response, "text") else "No response from AI."

        return render_template("index.html", combined_response=combined_response, ai_response=ai_response)

    return render_template("index.html", combined_response=None, ai_response=None)

if __name__ == "__main__":
    app.run(debug=True)
