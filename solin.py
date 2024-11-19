import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Replace this with your Bot Token from BotFather
BOT_TOKEN = "7127840868:AAH54q2zfYTtrprepgI7kGdtSOM-4mr5uRM"
bot = telebot.TeleBot("7127840868:AAH54q2zfYTtrprepgI7kGdtSOM-4mr5uRM")

# Predefined responses for topics
RESPONSES = {
    "html": "HTML (HyperText Markup Language) is the standard markup language for creating web pages. How can I assist you with HTML?",
    "css": "CSS (Cascading Style Sheets) is used to style HTML elements. How can I help with CSS?",
    "python": "Python is a versatile programming language, and Tkinter is its built-in library for creating GUIs. What do you want to know about Python or Tkinter?",
    "what is flexbox": 
        "CSS Flexbox is a layout model that allows you to design responsive web pages easily. "
        "It enables you to align and distribute space among items in a container, even when their sizes are unknown or dynamic.",
    "what is grid":  "CSS Grid is a powerful layout system for creating two-dimensional layouts. "
        "It allows you to divide a page into rows and columns and place items within the grid. It's especially useful for complex web layouts.",
    "what is gap": "The gap property in CSS is used to specify the space between items in a container, typically in a flexbox or grid layout."
            "It is a shorthand for defining the spacing between rows and columns in a grid or between flex items.",
    
}

# Helper function to determine the topic
def determine_topic(message):
    text = message.text.lower()
    if "html" in text:
        return "html"
    elif "css" in text:
        return "css"
    elif "python" in text or "tkinter" in text:
        return "python"
    elif "what is flexbpox" in text:
        return "what is flexbox"
    elif "what is grid" in text:
        return "what is grid"
    elif "what is gap" in text:
        return "what is gap"
    return None

# Start command handler
@bot.message_handler(commands=["start"])
def start(message):
    # Create a reply markup with buttons
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    html_button = KeyboardButton("HTML")
    css_button = KeyboardButton("CSS")
    python_button = KeyboardButton("Python")
    markup.add(html_button, css_button, python_button)

    # Send welcome message with buttons
    bot.send_message(
        message.chat.id,
        "Welcome! Select a topic to ask about:\n- HTML\n- CSS\n- Python (Tkinter)",
        reply_markup=markup,
    )

# Message handler for topic selection
@bot.message_handler(func=lambda message: message.text in ["HTML", "CSS", "Python","what is flexbox","what is grid","what is gap"])
def handle_topic_selection(message):
    topic = message.text.lower()
    bot.send_message(message.chat.id, RESPONSES[topic])

# Fallback message handler for questions
@bot.message_handler(func=lambda message: True)
def handle_question(message):
    topic = determine_topic(message)
    if topic:
        bot.send_message(message.chat.id, RESPONSES[topic])
    else:
        bot.send_message(
            message.chat.id,
            "I'm sorry, I can currently only help with HTML, CSS, and Python questions. Please ask about one of these topics!"
        )

# Start polling
if __name__ == "__main__":
    print("Bot is running...")
    bot.polling()