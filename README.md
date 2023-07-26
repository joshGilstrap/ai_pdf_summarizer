# PDF Summarizer - A 🤗AI powered "companion document" generator 
*Check the pdfs folder for comparable examples!*

This is a summarization program aimed at making a summarized version of academic and technical documents (or really any other pdf that has text).

The most difficult part of this process has been working with PDFs. As you know, PDFs are notoriously difficult to work with and even using PyPDF2 
and FPDF, I've only just managed to get a prototypical resultant PDF. Regardless, I've had success with a few different PDFs and keep getting promising results.

As the title suggests, the resultant PDF is a companion document to the original document and is only (currently!) to be used as such. If the PDF
has important diagrams, code blocks, images, etc. then the original document will need to be examined. It's my hope that you will be able to 
primarily use the resultant PDF for reading and the original for such diagrams.

The resultant PDF currently needs manual post-work to be done as during encoding there are several "unencodables" that need to be found and replaced
with an *. There are strange spaces in the middle of words that I'm also attributing to encoding. These can be ignored if they don't bug you too much.

I've left examples of some papers that have been run through the program, they're really great papers that I think you could learn a lot from!
