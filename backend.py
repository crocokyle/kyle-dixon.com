import json
import requests


def load_json(filename):
    with open(filename) as json_file:
        resume = json.load(json_file)
    return resume


def request_pdf(resume):
    headers = {
        'Connection': 'keep-alive',
        'sec-ch-ua': '^\\^',
        'Accept': 'application/pdf',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/91.0.4472.77 Safari/537.36',
        'Content-Type': 'application/json',
        'Origin': 'https://resumake.io',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://resumake.io/',
        'Accept-Language': 'en-US,en;q=0.9',
    }
    pdf = requests.post('https://resumake.io/api/generate/resume', headers=headers, data=json.dumps(resume), stream=True)
    return pdf


def save_pdf(pdf):
    with open('static/Kyle Dixon-resume.pdf', 'wb+') as f:
        f.write(pdf.content)


def update_pdf():
    data = load_json('static/resume.json')
    pdf = request_pdf(data)
    save_pdf(pdf)


if __name__ == '__main__':
    update_pdf()
