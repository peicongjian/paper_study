
import os
import subprocess
import csv
import re

def extract_pdf_text(pdf_path):
    """Extract text from a PDF file using pdftotext."""
    try:
        text = subprocess.check_output(["pdftotext", "-layout", pdf_path, "-"], universal_newlines=True)
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return ""

def clean_text(text):
    """Clean extracted text."""
    cleaned = re.sub(r'\s+', ' ', text)
    cleaned = re.sub(r'^\d+\s*$', '', cleaned, flags=re.MULTILINE)
    return cleaned.strip()

def quick_extract_info(text):
    """Quickly extract key information using simple pattern matching."""
    info = {
        'background': '',
        'solution': '',
        'innovation': '',
        'results': '',
        'related_work': ''
    }
    
    sentences = re.split(r'(?<=[.!?])\s', text)
    
    for sentence in sentences:
        # Background
        if not info['background'] and any(keyword in sentence.lower() for keyword in ['problem', 'issue', 'challenge']):
            info['background'] = sentence.strip()
        
        # Solution
        if not info['solution'] and any(keyword in sentence.lower() for keyword in ['propose', 'introduce', 'design']):
            info['solution'] = sentence.strip()
        
        # Innovation
        if not info['innovation'] and any(keyword in sentence.lower() for keyword in ['novel', 'innovative', 'new']):
            info['innovation'] = sentence.strip()
        
        # Results
        if not info['results'] and any(keyword in sentence.lower() for keyword in ['evaluate', 'result', 'achieve']):
            info['results'] = sentence.strip()
        
        # Related Work
        if not info['related_work'] and any(keyword in sentence.lower() for keyword in ['existing', 'previous', 'related']):
            info['related_work'] = sentence.strip()
    
    return info

def generate_summary(paper_title, file_name, info, text):
    """Generate a simple summary."""
    summary = f"# Paper Summary: {paper_title}\n\n"
    summary += f"## File: {file_name}\n\n"
    
    # Abstract
    abstract = text[:400]
    if len(text) > 400:
        abstract += "..."
    summary += "## Abstract\n"
    summary += abstract + "\n\n"
    
    summary += "## Key Points\n"
    summary += "### 1. Background Problem\n"
    summary += info['background'] if info['background'] else "<!-- Describe the main problem -->\n"
    summary += "\n"
    
    summary += "### 2. Solution Approach\n"
    summary += info['solution'] if info['solution'] else "<!-- Describe the solution -->\n"
    summary += "\n"
    
    summary += "### 3. Innovation\n"
    summary += info['innovation'] if info['innovation'] else "<!-- Describe innovation -->\n"
    summary += "\n"
    
    summary += "### 4. Results\n"
    summary += info['results'] if info['results'] else "<!-- Describe results -->\n"
    summary += "\n"
    
    summary += "### 5. Related Work\n"
    summary += info['related_work'] if info['related_work'] else "<!-- Describe related work -->\n"
    summary += "\n"
    
    return summary

def main():
    paper_dir = "/root/.openclaw/workspace/paper-2026-02"
    csv_file = os.path.join(paper_dir, "papers.csv")
    output_file = "/root/.openclaw/workspace/paper_summary_quick.md"
    
    papers = []
    if os.path.exists(csv_file):
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                papers.append(row)
    
    all_summaries = []
    for paper in papers:
        pdf_files = []
        for file in os.listdir(paper_dir):
            if file.endswith('.pdf'):
                arxiv_match = re.search(r'(\d+\.\d+(?:v\d+)?)', paper['Download Link'])
                if arxiv_match:
                    arxiv_id = arxiv_match.group(1)
                    if arxiv_id in file:
                        pdf_files.append(os.path.join(paper_dir, file))
        
        if pdf_files:
            pdf_path = pdf_files[0]
            print(f"Processing: {paper['Title']}")
            
            text = extract_pdf_text(pdf_path)
            if text:
                cleaned_text = clean_text(text)
                info = quick_extract_info(cleaned_text)
                summary = generate_summary(paper['Title'], os.path.basename(pdf_path), info, cleaned_text)
                all_summaries.append(summary)
        else:
            print(f"PDF file not found for: {paper['Title']}")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Paper Summaries - NVMe, SSD, AI Infrastructure, Storage\n\n")
        f.write("Quick summaries of papers related to NVMe, SSD, AI infrastructure, and storage.\n\n")
        
        for i, summary in enumerate(all_summaries, 1):
            f.write(f"---\n\n")
            f.write(f"## Paper {i}\n\n")
            f.write(summary)
            f.write("\n")
    
    print(f"Generated summary file: {output_file}")
    print(f"Processed {len(all_summaries)} out of {len(papers)} papers")

if __name__ == "__main__":
    main()
