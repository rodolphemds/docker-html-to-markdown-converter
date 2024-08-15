import html2text

def convert_html_to_md(html_file, md_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    md_content = html2text.html2text(html_content)
    
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(md_content)

if __name__ == "__main__":
    html_file = 'changelog.html'
    md_file = 'changelog.md'
    
    convert_html_to_md(html_file, md_file)
    print(f"Conversion terminée : {html_file} -> {md_file}")