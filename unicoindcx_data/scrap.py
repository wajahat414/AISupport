import requests
from bs4 import BeautifulSoup
import json
from openai import OpenAI
from datetime import datetime
import os

client = OpenAI(
    api_key="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"
)


url = "https://www.unicoindcx.com"


def getHtmlDataFromUrl(url: str):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup


def generate_json(raw_text: str, source="unknown"):

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {
                "role": "system",
                "content": "You are an assistant that formats data into JSON.",
            },
            {
                "role": "user",
                "content": f"Extract and format the following text into JSON: {raw_text}",
            },
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "unicoindcx_info_data",
                "schema": {
                    "type": "object",
                    "properties": {
                        "platform_info": {
                            "type": "object",
                            "properties": {
                                "platform_name": {
                                    "type": "string",
                                    "description": "The name of the crypto platform (e.g., Unicoin).",
                                },
                                "service_description": {
                                    "type": "string",
                                    "description": "A general description of the platform and its services.",
                                },
                                "terms_and_conditions": {
                                    "type": "object",
                                    "properties": {
                                        "last_updated": {
                                            "type": "string",
                                            "description": "The last date the terms were updated.",
                                        },
                                        "sections": {
                                            "type": "array",
                                            "items": {
                                                "type": "object",
                                                "properties": {
                                                    "section_name": {
                                                        "type": "string",
                                                        "description": "The name of the section (e.g., Definitions, Fees, etc.).",
                                                    },
                                                    "content": {
                                                        "type": "string",
                                                        "description": "Content under the section, typically describing its rules, definitions, or services.",
                                                    },
                                                    "faq": {
                                                        "type": "array",
                                                        "items": {
                                                            "type": "object",
                                                            "properties": {
                                                                "question": {
                                                                    "type": "string",
                                                                    "description": "Frequently asked question regarding the section.",
                                                                },
                                                                "answer": {
                                                                    "type": "string",
                                                                    "description": "Answer to the frequently asked question.",
                                                                },
                                                            },
                                                            "required": [
                                                                "question",
                                                                "answer",
                                                            ],
                                                        },
                                                        "description": "Frequently asked questions and answers related to this section.",
                                                    },
                                                },
                                                "required": ["section_name", "content"],
                                            },
                                        },
                                    },
                                    "required": ["last_updated", "sections"],
                                },
                                "contact_details": {
                                    "type": "object",
                                    "properties": {
                                        "support_email": {
                                            "type": "string",
                                            "description": "The email address for support contact.",
                                        },
                                        "support_phone": {
                                            "type": "string",
                                            "description": "The phone number for support contact.",
                                        },
                                        "faq_url": {
                                            "type": "string",
                                            "description": "A URL linking to frequently asked questions or help resources.",
                                        },
                                    },
                                },
                            },
                            "required": [
                                "platform_name",
                                "service_description",
                                "terms_and_conditions",
                            ],
                        }
                    },
                    "required": ["platform_info"],
                    "additionalProperties": True,
                },
                "strict": False,
            },
        },
    )

    output_json = completion.choices[0].message
    print(output_json.content)
    standardarized_json = json.loads(output_json.content)
    standardarized_json["metadata"] = {
        "source": source,
        "timestamp": datetime.now().isoformat(),
    }
    print(standardarized_json)
    return standardarized_json


def extract_data(soup: BeautifulSoup):
    cleaned_text = ""
    for path in soup.find_all("path"):
        path.decompose()

    for tag in soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"]):
        text = tag.get_text().strip()
        if text:

            cleaned_text += text
    return cleaned_text


def save_data(structured_data: json):
    with open("unicoin_data.json", "w") as json_file:
        json.dump(structured_data, json_file, indent=4)


def main():

    soup = getHtmlDataFromUrl(url)
    cleaned_text: str = extract_data(soup)
    formatted_json = generate_json(
        raw_text=cleaned_text, source="UnicoinDcxPlatfromInfo"
    )
    save_data(formatted_json)


if __name__ == "__main__":
    main()


{
    "$schema": "http://json-schema.org/draft-07/schema#",
}
