import instaloader

# Initialize Instaloader
L = instaloader.Instaloader()

# Replace with an actual Instagram post shortcode
shortcode = "DHi04cio3Lu"  # Example shortcode from a post URL

try:
    post = instaloader.Post.from_shortcode(L.context, shortcode)

    post_details = {
        "Post ID": post.mediaid,
        "Caption": post.caption,
        "Likes": post.likes,
        "Comments": post.comments,
        "Owner": post.owner_username,
        "Media Type": "Video" if post.is_video else "Image",
        "Media URL": post.video_url if post.is_video else post.url
    }

    print(post_details)

except Exception as e:
    print("Error:", e)
