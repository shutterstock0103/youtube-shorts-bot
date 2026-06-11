from content_selector import choose_content
from generate_quote import get_quote
from generate_relax_text import get_relax_text

mode = choose_content()

if mode == "motivation":
    quote = get_quote()
    print("Motivational Short")
    print(quote)

else:
    text = get_relax_text()
    print("Relaxing Short")
    print(text)
