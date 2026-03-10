import pdfplumber
import re

def parse_resume(file):

    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"

    text_lower = text.lower()

    # ---------------- CGPA ----------------
    cgpa_match = re.search(r'(sgpa|cgpa|gpa)[:\s]*([0-9]\.[0-9]{1,2})', text_lower)
    cgpa = float(cgpa_match.group(2)) if cgpa_match else None


    # ---------------- BRANCH ----------------
    branch = None
    branches = {
        "computer science": "CSE",
        "information technology": "IT",
        "electronics": "ECE",
        "electrical": "EEE",
        "mechanical": "ME",
        "civil": "CE"
    }

    for k, v in branches.items():
        if k in text_lower:
            branch = v
            break


    # ---------------- INTERNSHIPS ----------------
    intern = len(re.findall(r'\bintern\b|\binternship\b', text_lower))


    # ---------------- PROJECT COUNT ----------------
    project_count = 0

    project_section = re.search(
        r'(projects|project experience)(.*?)(education|certifications|skills)',
        text_lower,
        re.DOTALL
    )

    if project_section:

        section_text = project_section.group(2)

        lines = section_text.split("\n")

        project_lines = [
            l.strip() for l in lines
            if len(l.strip()) > 8
            and not l.strip().startswith("•")
            and not l.strip().startswith("-")
        ]

        project_count = len(project_lines)


    # ---------------- CERTIFICATIONS ----------------
    cert_section = re.search(r'certifications(.*)', text_lower, re.DOTALL)

    cert = 0
    if cert_section:
        lines = cert_section.group(1).split("\n")
        cert = len([l for l in lines if len(l.strip()) > 3])


    return {
        "cgpa": cgpa,
        "branch": branch,
        "intern": intern,
        "proj": project_count,
        "cert": cert
    }