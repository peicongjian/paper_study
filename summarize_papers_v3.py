
import os
import subprocess
import csv
import json
import re
from collections import defaultdict

def extract_pdf_text(pdf_path):
    """Extract text from a PDF file using pdftotext."""
    try:
        # Extract text from PDF
        text = subprocess.check_output(["pdftotext", "-layout", pdf_path, "-"], universal_newlines=True)
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return ""

def clean_text(text):
    """Clean extracted text by removing unnecessary characters and formatting."""
    # Remove multiple newlines and tabs
    cleaned = re.sub(r'\s+', ' ', text)
    # Remove page numbers and headers
    cleaned = re.sub(r'^\d+\s*$', '', cleaned, flags=re.MULTILINE)
    # Remove unnecessary whitespace at start/end
    return cleaned.strip()

def find_abstract(text):
    """Find abstract section in different formats with better precision."""
    patterns = [
        # arXiv format with "Abstract" followed by content
        (r'Abstract\s*(\n|[\.\:])\s*([^\n]*?)(?=\n\s*1\s*Introduction|\n\s*Introduction|\n\s*I\.|\n\s*1\s*\.|$)', re.DOTALL),
        (r'ABSTRACT\s*(\n|[\.\:])\s*([^\n]*?)(?=\n\s*1\s*Introduction|\n\s*Introduction|\n\s*I\.|\n\s*1\s*\.|$)', re.DOTALL),
        # IEEE format with keywords after abstract
        (r'Abstract\s*[\.\:]\s*([^\n]*?)\s*Keywords:', re.DOTALL),
        (r'ABSTRACT\s*[\.\:]\s*([^\n]*?)\s*Keywords:', re.DOTALL),
        # Simple abstract extraction
        (r'Abstract\s*([^\n]*?)(?=\n1\s|$)', re.DOTALL),
    ]
    
    for pattern, flags in patterns:
        match = re.search(pattern, text, flags)
        if match:
            abstract = ''
            for group in match.groups():
                if group and len(group.strip()) > 50 and len(group.strip()) < 3000:
                    abstract += group
            
            if abstract:
                abstract = abstract.strip()
                abstract = re.sub(r'\s+', ' ', abstract)
                return abstract
    
    # Fallback: extract first 500 characters
    return text[:500].strip()

def extract_authors(text):
    """Extract authors from different formats."""
    patterns = [
        # Authors in arXiv style: Author1, Author2, ...
        (r'(\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*(?:,\s[A-Z][a-z]+(?:\s[A-Z][a-z]+)*)*)\s*\b',),
        # Authors with affiliations: John Doe1, Jane Smith2, ...
        (r'(\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*(?:,\s[A-Z][a-z]+(?:\s[A-Z][a-z]+)*)*)\s*[1-9]*\s*(?:,\s*[1-9]*\s*)?',),
        # Authors with departments or universities
        (r'by\s*([^\n]*?)\s*\b(?:Abstract|ABSTRACT|Introduction|1\s*Introduction)', re.DOTALL),
        # Simple author extraction
        (r'(\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*(?:,\s[A-Z][a-z]+(?:\s[A-Z][a-z]+)*)*)',),
    ]
    
    for pattern in patterns:
        if len(pattern) == 2:
            match = re.search(pattern[0], text, pattern[1])
        else:
            match = re.search(pattern[0], text)
        
        if match:
            authors = match.group(1).strip()
            if len(authors) > 2 and len(authors) < 200 and any(char.isalpha() for char in authors):
                # Clean up authors
                authors = re.sub(r'\s+', ' ', authors)
                authors = re.sub(r'\s*,\s*', ', ', authors)
                authors = re.sub(r'\s*and\s*', ', ', authors)
                # Remove affiliations and numbers
                authors = re.sub(r'\s*[1-9]+\s*', '', authors)
                authors = re.sub(r'\([^)]*\)', '', authors)
                authors = re.sub(r'<[^>]*>', '', authors)
                authors = re.sub(r'[^\w\s,]+', '', authors)
                authors = authors.strip()
                
                if authors and len(authors.split()) > 1 and len(authors) < 200:
                    return authors
    
    return ''

def extract_keywords(text):
    """Extract keywords from different formats."""
    patterns = [
        (r'Keywords?\s*:?\s*([^\n]*?)\s*(?:1\s*Introduction|Introduction|I\.|II\.|Background)', re.DOTALL),
        (r'Index Terms?\s*:?\s*([^\n]*?)\s*(?:1\s*Introduction|Introduction|I\.|II\.|Background)', re.DOTALL),
    ]
    
    for pattern, flags in patterns:
        match = re.search(pattern, text, flags)
        if match:
            keywords = match.group(1).strip()
            keywords = re.sub(r'\s+', ' ', keywords)
            if len(keywords) > 5 and len(keywords) < 200:
                return keywords
    
    return ''

def parse_paper_info(text):
    """Extract paper information with improved parsing."""
    info = {
        'title': '',
        'authors': '',
        'abstract': '',
        'keywords': '',
        'sections': defaultdict(str)
    }
    
    # Extract authors
    authors = extract_authors(text)
    if authors:
        info['authors'] = authors
    
    # Extract keywords
    keywords = extract_keywords(text)
    if keywords:
        info['keywords'] = keywords
    
    # Extract abstract
    abstract = find_abstract(text)
    if abstract:
        info['abstract'] = abstract
    
    # Extract sections
    section_pattern = r'(\d+\.\s+[^\n]+)\s*(?:\n|$)'
    sections = re.findall(section_pattern, text)
    for section_title in sections:
        section_title = section_title.strip()
        if len(section_title) < 50 and any(keyword in section_title.lower() for keyword in 
                                           ['introduction', 'related work', 'method', 'approach', 
                                            'results', 'evaluation', 'conclusion', 'discussion', 
                                            'background']):
            section_start = text.find(section_title)
            if section_start != -1:
                next_section = None
                for other_section in sections:
                    other_title = other_section.strip()
                    other_start = text.find(other_title)
                    if other_start > section_start and other_title != section_title:
                        if next_section is None or other_start < next_section:
                            next_section = other_start
                
                if next_section:
                    content = text[section_start:next_section].strip()
                else:
                    content = text[section_start:].strip()
                
                info['sections'][section_title] = content[:300].strip() if len(content) > 300 else content
    
    return info

def generate_summary(pdf_path, paper_title, paper_info):
    """Generate a structured summary of the paper."""
    summary = f"# Paper Summary: {paper_title}\n\n"
    summary += f"## File: {os.path.basename(pdf_path)}\n\n"
    
    if paper_info['authors']:
        summary += f"## Authors: {paper_info['authors']}\n\n"
    
    if paper_info['keywords']:
        summary += f"## Keywords: {paper_info['keywords']}\n\n"
    
    if paper_info['abstract']:
        summary += "## Abstract\n"
        summary += paper_info['abstract'] + "\n\n"
    
    summary += "## Key Points\n"
    
    summary += "### 1. Background Problem\n"
    intro = ''
    for section_title, content in paper_info['sections'].items():
        if 'introduction' in section_title.lower() or 'background' in section_title.lower():
            intro += content
    if intro:
        summary += f"{intro[:200]}...\n\n"
    else:
        # Look for background in abstract
        if 'problem' in paper_info['abstract'].lower() or 'issue' in paper_info['abstract'].lower() or 'challenge' in paper_info['abstract'].lower():
            # Find background sentences
            background = []
            sentences = re.split(r'(?<=[.!?])\s', paper_info['abstract'])
            for sentence in sentences:
                if any(keyword in sentence.lower() for keyword in ['problem', 'issue', 'challenge', 'limitation', 'need']):
                    background.append(sentence.strip())
            if background:
                summary += ' '.join(background) + "\n\n"
            else:
                summary += "<!-- Describe the main problem the paper addresses -->\n\n"
        else:
            summary += "<!-- Describe the main problem the paper addresses -->\n\n"
    
    summary += "### 2. Solution Approach\n"
    approach = ''
    for section_title, content in paper_info['sections'].items():
        if 'method' in section_title.lower() or 'approach' in section_title.lower() or 'solution' in section_title.lower():
            approach += content
    if approach:
        summary += f"{approach[:200]}...\n\n"
    else:
        if 'propose' in paper_info['abstract'].lower() or 'introduce' in paper_info['abstract'].lower() or 'design' in paper_info['abstract'].lower():
            solution = []
            sentences = re.split(r'(?<=[.!?])\s', paper_info['abstract'])
            for sentence in sentences:
                if any(keyword in sentence.lower() for keyword in ['propose', 'introduce', 'design', 'develop', 'implement', 'solution']):
                    solution.append(sentence.strip())
            if solution:
                summary += ' '.join(solution) + "\n\n"
            else:
                summary += "<!-- Explain the proposed solution -->\n\n"
        else:
            summary += "<!-- Explain the proposed solution -->\n\n"
    
    summary += "### 3. Innovation\n"
    innovative = []
    if 'novel' in paper_info['abstract'].lower() or 'innovative' in paper_info['abstract'].lower() or 'new' in paper_info['abstract'].lower():
        sentences = re.split(r'(?<=[.!?])\s', paper_info['abstract'])
        for sentence in sentences:
            if any(keyword in sentence.lower() for keyword in ['novel', 'innovative', 'new', 'first', 'unique', 'breakthrough']):
                innovative.append(sentence.strip())
    if innovative:
        summary += ' '.join(innovative) + "\n\n"
    else:
        summary += "<!-- What makes this work innovative? -->\n\n"
    
    summary += "### 4. Results\n"
    results = ''
    for section_title, content in paper_info['sections'].items():
        if 'results' in section_title.lower() or 'evaluation' in section_title.lower() or 'performance' in section_title.lower():
            results += content
    if results:
        summary += f"{results[:200]}...\n\n"
    else:
        if 'evaluate' in paper_info['abstract'].lower() or 'result' in paper_info['abstract'].lower() or 'achieve' in paper_info['abstract'].lower():
            results = []
            sentences = re.split(r'(?<=[.!?])\s', paper_info['abstract'])
            for sentence in sentences:
                if any(keyword in sentence.lower() for keyword in ['evaluate', 'result', 'achieve', 'demonstrate', 'show', 'improve']):
                    results.append(sentence.strip())
            if results:
                summary += ' '.join(results) + "\n\n"
            else:
                summary += "<!-- Present key experimental results -->\n\n"
        else:
            summary += "<!-- Present key experimental results -->\n\n"
    
    summary += "### 5. Related Work\n"
    related = ''
    for section_title, content in paper_info['sections'].items():
        if 'related work' in section_title.lower() or 'previous work' in section_title.lower() or 'literature' in section_title.lower():
            related += content
    if related:
        summary += f"{related[:200]}...\n\n"
    else:
        if 'existing' in paper_info['abstract'].lower() or 'previous' in paper_info['abstract'].lower() or 'related' in paper_info['abstract'].lower():
            related = []
            sentences = re.split(r'(?<=[.!?])\s', paper_info['abstract'])
            for sentence in sentences:
                if any(keyword in sentence.lower() for keyword in ['existing', 'previous', 'related', 'traditional', 'conventional']):
                    related.append(sentence.strip())
            if related:
                summary += ' '.join(related) + "\n\n"
            else:
                summary += "<!-- Discuss related papers and how this work compares -->\n\n"
        else:
            summary += "<!-- Discuss related papers and how this work compares -->\n\n"
    
    if paper_info['sections']:
        summary += "## Section Details\n"
        for section_title, content in paper_info['sections'].items():
            summary += f"### {section_title}\n"
            summary += f"{content[:200]}..."
            if len(content) > 200:
                summary += "..."
            summary += "\n\n"
    
    return summary

def main():
    # Configuration
    paper_dir = "/root/.openclaw/workspace/paper-2026-02"
    csv_file = os.path.join(paper_dir, "papers.csv")
    output_file = "/root/.openclaw/workspace/paper_summary.md"
    
    # Read papers from CSV
    papers = []
    if os.path.exists(csv_file):
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                papers.append(row)
    
    # Process each paper
    all_summaries = []
    for paper in papers:
        # Find the corresponding PDF file
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
                paper_info = parse_paper_info(cleaned_text)
                
                summary = generate_summary(pdf_path, paper['Title'], paper_info)
                all_summaries.append(summary)
        else:
            print(f"PDF file not found for: {paper['Title']}")
    
    # Write all summaries to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Paper Summaries - NVMe, SSD, AI Infrastructure, Storage\n\n")
        f.write("This document contains summaries of papers related to NVMe, SSD, AI infrastructure, and storage technologies.\n\n")
        
        for i, summary in enumerate(all_summaries, 1):
            f.write(f"---\n\n")
            f.write(f"## Paper {i}\n\n")
            f.write(summary)
            f.write("\n")
    
    print(f"\nSummary file generated: {output_file}")
    print(f"Processed {len(all_summaries)} out of {len(papers)} papers")

if __name__ == "__main__":
    main()
