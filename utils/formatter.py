def format_newsletter(summaries):
    html = "<h2>🗞️ Your Daily AI-Powered Newsletter</h2><ul>"
    for item in summaries:
        html += f"<li><strong>{item['title']}</strong><br>"
        html += f"{item['summary']}<br>"
        html += f"<a href='{item['link']}'>Read more</a></li><br><br>"
    html += "</ul>"
    return html
