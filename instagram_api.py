from fastapi import FastAPI, HTTPException
import instaloader

app = FastAPI()

# Initialize Instaloader
L = instaloader.Instaloader()

@app.get("/instagram/{shortcode}")
def get_instagram_post(shortcode: str):
    try:
        post = instaloader.Post.from_shortcode(L.context, shortcode)

        return {
            "Post ID": post.mediaid,
            "Caption": post.caption,
            "Likes": post.likes,
            "Comments": post.comments,
            "Owner": post.owner_username,
            "Media Type": "Video" if post.is_video else "Image",
            "Media URL": post.video_url if post.is_video else post.url
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

