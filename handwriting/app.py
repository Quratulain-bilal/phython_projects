from PIL import Image, ImageDraw, ImageFont
import textwrap

def handwriting(text):
    img = Image.new("RGB", (800, 600), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("ImperialScript-Regular.ttf", 40)
    wrapped_text = textwrap.fill(text, width=40)
    lines = wrapped_text.split("\n")
    y = (600 - len(lines) * 50) // 2
    for line in lines:
        x = (800 - draw.textbbox((0, 0), line, font=font)[2]) // 2
        draw.text((x, y), line, font=font, fill="black")
        y += 50
    img.save("handwriting.png")
    img.show()

handwriting("""Artificial Intelligence (AI) – The Future of Innovation

AI enables machines to think and learn like humans. From Siri to self-driving cars, AI transforms industries. It speeds up processes in healthcare, finance, and education. AI-powered chatbots provide instant support. Machine learning predicts trends, but AI raises ethical concerns. As AI evolves, it shapes the future of technology. 🚀""")