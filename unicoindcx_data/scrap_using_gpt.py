import re
import json
import openai


def save_to_json(structured_data, file_path="faq.json"):
    with open(file_path, "w") as json_file:
        json.dump(structured_data, json_file, indent=4)
    print(f"FAQ Data Saved to JSOn {file_path}")


# Example raw text input
raw_text = """
Client Terms & Conditions
Last Updated: 31st July 2023

These Terms and Conditions (hereinafter referred to as “Terms” or “Terms of Use”) is entered between you (hereinafter referred to as “you” or “your”) and Unicoin Digital Capital Exchange (UDCX) (hereinafter referred as “Unicoin”) that applies to the Client’s use of any and all Services, products and content provided by the Unicoin.

Definitions:
1.1. Account: means an account registered by the Client on Unicoin.
1.2. AML: means Anti-Money Laundering, including all Laws applicable to the Parties prohibiting money laundering or any acts or attempted acts to conceal or disguise the identity or origin of; change the form of; or move, transfer, or transport, illicit proceeds, property, funds, Fiat, or Digital Tokens.
1.3. Arbitration: means a process of redressing any issues or disputes in the trading platform under the provision of these terms, Law of Arbitration in Malaysia & Arbitration rules of the Asian International Arbitration Centre.

Fees and Charges:
2.1. Commission: means a fee charged by Unicoin or on behalf of any other parties.
2.2. Transaction fee: means a fee which is payable to Unicoin for each completed Transaction or executed Order.
"""


# # Save the structured data to a JSON file
# save_to_json(structured_data)
