from collections import Counter

def most_common_lines(pages, position='top', num_lines=3):
    """
    Finds repeated lines (headers or footers) by checking the first/last few lines of each page.
    """
    line_counter = Counter()
    for text in pages:
        lines = text.split('\n')
        slice_lines = lines[:num_lines] if position == 'top' else lines[-num_lines:]
        for line in slice_lines:
            line_counter[line.strip()] += 1
    # Keep lines that appear 3+ times
    return set([line for line, count in line_counter.items() if count > 2])

def remove_headers_footers(pages):
    headers = most_common_lines(pages, position='top')
    footers = most_common_lines(pages, position='bottom')

    cleaned = []
    for text in pages:
        lines = text.split('\n')
        new_lines = [line for line in lines if line.strip() not in headers and line.strip() not in footers]
        cleaned.append("\n".join(new_lines))
    return cleaned

import re

def extract_headings(pages):
    headings = []
    current_main = None
    current_sub = None

    for page in pages:
        lines = page.split('\n')
        for line in lines:
            line = line.strip()

            # Match main section heading: e.g., "SECTION 4    VOLTAGE DROP"
            if re.match(r'^SECTION\s+\d+\s+.+$', line):
                current_main = {
                    'section': line,
                    'subsections': []
                }
                headings.append(current_main)

            # Match L2 heading: e.g., "4.3 DETERMINATION OF..."
            elif re.match(r'^\d+\.\d+\s+.+$', line):
                current_sub = {
                    'title': line,
                    'subpoints': []
                }
                if current_main:
                    current_main['subsections'].append(current_sub)

            # Match L3 heading: e.g., "4.3.3 Three-phase..."
            elif re.match(r'^\d+\.\d+\.\d+\s+.+$', line):
                if current_sub:
                    current_sub['subpoints'].append(line)

    return headings
