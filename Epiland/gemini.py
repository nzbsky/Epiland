import json
import os

from google import genai
from dotenv import load_dotenv


load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

VALID_INTENTS = [

    "BOOK_PARTY",
    "SHOW_ENTERTAINMENTS",
    "SHOW_PRICES",
    "SHOW_INFO",
    "SHOW_PLAN",
    "MANAGER_HELP",
    "UNKNOWN"

]


SYSTEM_PROMPT = """
Ти AI router для Telegram-бота дитячого парку.

Ти НЕ звичайний чат-бот.

Твоє завдання:
визначити intent користувача.

Ти відповідаєш ТІЛЬКИ JSON.

Формат:

{
  "intent": "BOOK_PARTY",
  "reply": "Допоможу організувати свято 🎉"
}

Можливі intents:

BOOK_PARTY
SHOW_ENTERTAINMENTS
SHOW_PRICES
SHOW_INFO
SHOW_PLAN
MANAGER_HELP
UNKNOWN

Правила:

- Якщо користувач хоче організувати день народження → BOOK_PARTY
- Якщо хоче атракціони або розваги → SHOW_ENTERTAINMENTS
- Якщо питає ціни або тарифи → SHOW_PRICES
- Якщо питає адресу, контакти, графік → SHOW_INFO
- Якщо хоче спланувати відпочинок → SHOW_PLAN
- Якщо хоче поговорити з менеджером → MANAGER_HELP
- Якщо intent незрозумілий → UNKNOWN

reply має бути:
- короткий
- дружній
- українською
- максимум 1 речення
"""

def ask_gemini(
    text,
    current_step=None,
    user_state=None
):

    try:

        prompt = f"""
CURRENT STEP:
{current_step}

USER STATE:
{json.dumps(user_state, ensure_ascii=False)}

USER MESSAGE:
{text}
"""



        response = client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt,

            config={
                "system_instruction": SYSTEM_PROMPT,
                "response_mime_type": "application/json",
                "temperature": 0.2
            }
        )


        raw_text = response.text.strip()

        print("\n========== GEMINI ==========")
        print(raw_text)
        print("============================\n")


        data = json.loads(raw_text)

        if data.get("intent") not in VALID_INTENTS:
            data["intent"] = "UNKNOWN"

        if not data.get("reply"):

            data["reply"] = (
                "😔 Не зовсім зрозумів тебе"
            )


        return data

    except json.JSONDecodeError as e:

        print(f"\nJSON ERROR: {e}\n")

        return {

            "intent": "UNKNOWN",

            "reply": (
                "😔 Не зовсім зрозумів тебе.\n"
                "Спробуй кнопки нижче 👇"
            )

        }


    except Exception as e:

        print(f"\nGEMINI ERROR: {e}\n")

        return {

            "intent": "UNKNOWN",

            "reply": (
                "⚠️ Тимчасова помилка AI.\n"
                "Спробуй ще раз трохи пізніше"
            )

        }