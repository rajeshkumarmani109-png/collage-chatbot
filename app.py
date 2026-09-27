from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    message = data.get("message", "").lower().strip()

    # --------------------------------
    # 1. COURSES
    # --------------------------------
    if (
        "course" in message
        or "courses" in message
        or "program" in message
        or "programmes" in message
    ):
        reply = (
            "Noorul Islam Centre for Higher Education (NICHE) offers "
            "various Undergraduate, Postgraduate and Research programmes. "
            "The programmes include B.E./B.Tech, M.E./M.Tech, MBA, "
            "MCA, M.Sc, M.A, B.Sc, BBA, B.Com, BCA, BASLP and Ph.D programmes. "
            "For the latest course list, please check the official NICHE website."
        )

    # --------------------------------
    # 2. FEES
    # --------------------------------
    elif (
        "fee" in message
        or "fees" in message
        or "fees details" in message
        or "course fee" in message
    ):
        reply = (
            "Course fees at NICHE vary depending on the programme. "
            "For the exact and current fee structure, please contact the "
            "NICHE admission office at +91 89433 52456 or +91 99461 30462."
        )

    # --------------------------------
    # 3. COLLEGE TIMING
    # --------------------------------
    elif (
        "timing" in message
        or "timings" in message
        or "college time" in message
        or "working hours" in message
    ):
        reply = (
            "The college office working hours are generally "
            "Monday to Saturday, 9:00 AM to 5:00 PM. "
            "For specific department timings, please contact the college."
        )

    # --------------------------------
    # 4. ADMISSION PROCESS
    # --------------------------------
    elif (
        "admission" in message
        or "admission process" in message
        or "how to join" in message
        or "apply" in message
    ):
        reply = (
            "NICHE admissions are currently open for the 2026-2027 academic year. "
            "Students can apply through the official NICHE admission portal. "
            "For admission assistance, contact +91 89433 52456 or "
            "+91 99461 30462."
        )

    # --------------------------------
    # 5. HOSTEL
    # --------------------------------
    elif (
        "hostel" in message
        or "accommodation" in message
        or "hostel facility" in message
    ):
        reply = (
            "NICHE provides hostel facilities for students. "
            "For hostel availability, fees and accommodation details, "
            "please contact the college administration."
        )

    # --------------------------------
    # 6. PLACEMENT
    # --------------------------------
    elif (
        "placement" in message
        or "placements" in message
        or "job" in message
        or "career" in message
    ):
        reply = (
            "NICHE has a Placement Cell that supports students with "
            "placement and career-related activities. "
            "For current placement details, companies and statistics, "
            "please contact the Placement Cell."
        )

    # --------------------------------
    # 7. LOCATION
    # --------------------------------
    elif (
        "where" in message
        or "location" in message
        or "address" in message
        or "where is the college" in message
    ):
        reply = (
            "Noorul Islam Centre for Higher Education (NICHE) "
            "is located at Kumaracoil, Thuckalay, "
            "Kanyakumari District, Tamil Nadu - 629180, India."
        )

    # --------------------------------
    # 8. CONTACT NUMBER
    # --------------------------------
    elif (
        "contact" in message
        or "contact number" in message
        or "phone" in message
        or "telephone" in message
        or "mobile number" in message
    ):
        reply = (
            "NICHE contact details:\n\n"
            "Main Office: +91 4651 250 566\n"
            "Alternate: +91 94868 56101\n\n"
            "Admission Help Line:\n"
            "+91 89433 52456\n"
            "+91 99461 30462\n\n"
            "Email: info@niuniv.com"
        )

    # --------------------------------
    # GREETING
    # --------------------------------
    elif (
        "hello" in message
        or "hi" in message
        or "hai" in message
        or "hey" in message
    ):
        reply = (
            "Hello! 👋 Welcome to the Noorul Islam Centre for Higher Education "
            "(NICHE) Enquiry Chatbot.\n\n"
            "How can I help you?\n"
            "You can ask about courses, fees, admission, hostel, "
            "placement, college timing, location or contact details."
        )

    # --------------------------------
    # THANK YOU
    # --------------------------------
    elif (
        "thank you" in message
        or "thanks" in message
        or "thank" in message
    ):
        reply = (
            "You're welcome! 😊 "
            "Feel free to ask me anything about NICHE."
        )

    # --------------------------------
    # UNKNOWN QUESTION
    # --------------------------------
    else:
        reply = (
            "Sorry, I couldn't understand your question. 😕\n\n"
            "You can ask me about:\n"
            "1. Courses\n"
            "2. Fees\n"
            "3. College Timing\n"
            "4. Admission Process\n"
            "5. Hostel\n"
            "6. Placement\n"
            "7. College Location\n"
            "8. Contact Number"
        )

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)