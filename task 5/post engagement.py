def analyze_engagement(likes_list):
    total_likes = 0
    for likes in likes_list:
        total_likes += likes
    if total_likes > 1000:
        status = "Viral Post"
    else:
        status = "Normal Engagement"
    print("Total Likes:", total_likes)
    print("Post Status:", status)
likes = [200, 300, 150, 400]
analyze_engagement(likes)