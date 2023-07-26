from PyPDF2 import PdfReader
from fpdf import FPDF
from transformers import pipeline
from pathlib import Path

pdf_path = Path(__file__).parent/"pdfs/linkedin_post.pdf"
reader = PdfReader(pdf_path)

# Known characters that throw errors when writing to pdf
known_uncodeables = ["\ufb01", "\u2019", "\u201c", "\u201d", "\u2248", "\u2212", "\ufb00", "\ufb02",
                    "\ufb03", "\u2013", "\u2018", "\u2014", "\u2009", "\ufffd", "\u2190", "\u221e",
                    "\u2265", "\u2032"]


def main():
    # Summarizer pipeline - BART model is trained on CNN/DailyMail dataset
    summarizer = pipeline("summarization", model= "facebook/bart-large-cnn")

    page_summaries = []

    # read_by_paragraph(reader.pages, page_summaries, summarizer)

    read_by_page(reader.pages, page_summaries, summarizer)

    write_to_textfile(page_summaries)
    
    export_to_pdf()


# Search through summary for known uncodeable characters and replace them with *
def clean_text(text):
    for chars in text:
        if chars in known_uncodeables:
            text = text.replace(chars, "*")
    return text


# Find every page and feed it in to the summarizer for summary
def read_by_page(pages, summaries, summarizer):
    for page in pages:
        test = page.extract_text()
        summaries.append(summarizer(test, max_length=int(len(test) / 4), min_length=5))


# Find every paragraph and feed it in to the summarizer for summary
def read_by_paragraph(pages, summaries, summarizer):
    for page in pages:
        text = page.extract_text()
        paragraphs = text.split(".\n")
        for paragraph in paragraphs:
            if len(paragraph) < 30:
                summaries.append(paragraph)
                continue
            summaries.append(summarizer(paragraph, max_length=int(len(paragraph) / 4), min_length=5))


def write_to_textfile(summaries):
    # Write summaries to text file
    with open("summary.txt", "w", encoding='UTF-8') as f:
        for summary in summaries:
            clean_text(summary[0]['summary_text'])
            f.write(summary[0]['summary_text'])
            

def export_to_pdf():
    # Open summary file
    text_file = open("summary.txt", "r+", encoding='utf-8')

    # Setup pdf
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.set_line_width(0.05)

    # Write summary to pdf
    for item in text_file:
        pdf.write(10, txt=item)

    # Save pdf
    pdf.output("raw_summary.pdf")


if __name__ == "__main__":
    main()




# Keeping in case I have to use these again
# page[0]['summary_text'] = page[0]['summary_text'].replace("\ufb01", "*")
# page[0]['summary_text'] = page[0]['summary_text'].replace("\u2019", "*")
# page[0]['summary_text'] = page[0]['summary_text'].replace("\u201c", "*")
# page[0]['summary_text'] = page[0]['summary_text'].replace("\u201d", "*")
# page[0]['summary_text'] = page[0]['summary_text'].replace("\u2248", "*")
# page[0]['summary_text'] = page[0]['summary_text'].replace("\u2212", "*")
# page[0]['summary_text'] = page[0]['summary_text'].replace("\ufb00", "*")
# page[0]['summary_text'] = page[0]['summary_text'].replace("\ufb02", "*")
# page[0]['summary_text'] = page[0]['summary_text'].replace("\ufb03", "*")
# page[0]['summary_text'] = page[0]['summary_text'].replace("\u2013", "*")
# page[0]['summary_text'] = page[0]['summary_text'].replace("\u2018", "*")
# page[0]['summary_text'] = page[0]['summary_text'].replace("\u2014", "*")
# page[0]['summary_text'] = page[0]['summary_text'].replace("\u2009", "*")
# page[0]['summary_text'] = page[0]['summary_text'].replace("\ufffd", "*")
# page[0]['summary_text'] = page[0]['summary_text'].replace("\u2190", "*")
# page[0]['summary_text'] = page[0]['summary_text'].replace("\u221e", "*")
# page[0]['summary_text'] = page[0]['summary_text'].replace("\u2265", "*")
# page[0]['summary_text'] = page[0]['summary_text'].replace("\u2032", "*")
