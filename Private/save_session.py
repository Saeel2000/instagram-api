import instaloader

# Initialize Instaloader
L = instaloader.Instaloader()

# Replace with your Instagram credentials
USERNAME = "your_instagram_username"
PASSWORD = "your_instagram_password"

# Login and save session
L.login(USERNAME, PASSWORD)
L.save_session_to_file()
print("✅ Instagram session saved successfully!")
