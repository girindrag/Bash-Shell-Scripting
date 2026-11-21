#!/usr/bin/env python3
"""
Generate a professional, multi-page PDF revision handbook for Bash Shell Scripting.
"""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, Preformatted
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (pages after cover)
        if self._pageNumber > 1:
            self.drawString(54, 11 * inch - 36, "Bash Shell Scripting — SRE & DevOps Mastery Handbook")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, 11 * inch - 42, 8.5 * inch - 54, 11 * inch - 42)

        # Footer
        footer_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(8.5 * inch - 54, 36, footer_text)
        self.drawString(54, 36, "Confidential & Practical Revision Notes | Girindra Mohan")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 48, 8.5 * inch - 54, 48)
        self.restoreState()


def build_pdf(filename="Bash_Shell_Scripting_Mastery_Handbook.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom Color Palette
    PRIMARY = colors.HexColor("#0F172A")    # Dark slate
    ACCENT = colors.HexColor("#2563EB")     # Royal blue
    SECONDARY = colors.HexColor("#0D9488")  # Teal
    MUTED = colors.HexColor("#475569")      # Muted slate
    CODE_BG = colors.HexColor("#F8FAFC")    # Code background
    BORDER = colors.HexColor("#E2E8F0")     # Light border

    # Custom Typography Styles
    title_style = ParagraphStyle(
        "CoverTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=28,
        leading=34,
        textColor=PRIMARY,
        spaceAfter=10
    )

    subtitle_style = ParagraphStyle(
        "CoverSubtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=13,
        leading=18,
        textColor=MUTED,
        spaceAfter=25
    )

    h1_style = ParagraphStyle(
        "Heading1_Custom",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=18,
        leading=22,
        textColor=PRIMARY,
        spaceBefore=16,
        spaceAfter=10,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        "Heading2_Custom",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=13,
        leading=17,
        textColor=ACCENT,
        spaceBefore=12,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        "Body_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        textColor=PRIMARY,
        spaceAfter=8
    )

    bullet_style = ParagraphStyle(
        "Bullet_Custom",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=13.5,
        textColor=PRIMARY,
        leftIndent=15,
        firstLineIndent=-10,
        spaceAfter=4
    )

    code_style = ParagraphStyle(
        "CodeBlock",
        parent=styles["Normal"],
        fontName="Courier",
        fontSize=8.5,
        leading=11.5,
        textColor=colors.HexColor("#0F172A"),
        spaceBefore=4,
        spaceAfter=4
    )

    story = []

    # -------------------------------------------------------------
    # COVER / HEADER
    # -------------------------------------------------------------
    story.append(Spacer(1, 20))
    story.append(Paragraph("BASH SHELL SCRIPTING", title_style))
    story.append(Paragraph("Production Engineering & SRE Handbook — Zero to Top-1% Mastery", subtitle_style))
    
    meta_data = [
        [Paragraph("<b>Author:</b> Girindra Mohan", body_style), Paragraph("<b>Target Focus:</b> DevOps, SRE, Cloud, Edge", body_style)],
        [Paragraph("<b>Status:</b> Living Handbook & Revision Guide", body_style), Paragraph("<b>Repo:</b> girindrag/Bash-Shell-Scripting", body_style)]
    ]
    meta_table = Table(meta_data, colWidths=[250, 250])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('BOX', (0,0), (-1,-1), 1, BORDER),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 20))

    # -------------------------------------------------------------
    # SECTION 1: ROADMAP & CURRICULUM
    # -------------------------------------------------------------
    story.append(Paragraph("1. Complete 5-Stage Mastery Curriculum", h1_style))
    story.append(Paragraph(
        "Bash is not merely a scripting language; it is the <b>orchestration fabric of Unix systems</b>. "
        "The following 5-stage roadmap defines the path from fundamental mechanics to enterprise production automation:",
        body_style
    ))

    stages = [
        ["Stage", "Domain", "Key Capabilities & Concepts"],
        ["Stage 1", "Foundations & Mental Models", "Execution model, shebang portability, variable storage, quoting rules, streams & redirection."],
        ["Stage 2", "Idiomatic Syntax & Flow", "Parameter expansions, arithmetic $(( )), modern [[ ]] conditionals, loops, safe array processing."],
        ["Stage 3", "OS Internals & Mechanics", "Fork/exec lifecycle, subshells, trap & signal handling, file descriptors, FIFOs, concurrency."],
        ["Stage 4", "Production Architecture", "set -euo pipefail, GNU flag parsing (getopts), defensive quoting, shellcheck & bats testing."],
        ["Stage 5", "Production Capstone", "sysmesh-cli: Enterprise log rotation, system health telemetry, atomic locking, automated backup."]
    ]
    roadmap_table = Table(stages, colWidths=[65, 150, 285])
    roadmap_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), PRIMARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('BOX', (0, 0), (-1, -1), 1, PRIMARY),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
    ]))
    story.append(roadmap_table)
    story.append(Spacer(1, 15))

    # -------------------------------------------------------------
    # SECTION 2: MODULE 1 DEEP DIVE
    # -------------------------------------------------------------
    story.append(Paragraph("2. Module 1: The Anatomy of a Script & The Shebang", h1_style))
    story.append(Paragraph("<b>The Kitchen & Recipe Mental Model:</b>", h2_style))
    story.append(Paragraph(
        "Interactive terminal commands are like shouting one instruction at a time to a kitchen chef. "
        "A shell script is a recipe card containing the entire procedure pre-written. "
        "The very first line — the <b>Shebang</b> — designates which chef reads the recipe.",
        body_style
    ))

    story.append(Paragraph("<b>Key Principles:</b>", h2_style))
    story.append(Paragraph("• <b>Portability:</b> Always declare <code>#!/usr/bin/env bash</code> on Line 1 Byte 0. Avoid hardcoded paths like <code>/bin/bash</code> which vary across Linux, macOS, and BSD.", bullet_style))
    story.append(Paragraph("• <b>Executable Bit:</b> Fresh Unix files lack execution permission. Grant it via <code>chmod +x script.sh</code> before running with <code>./script.sh</code>.", bullet_style))
    story.append(Paragraph("• <b>Sequential Execution:</b> Commands execute strictly line-by-line from top to bottom.", bullet_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Completed Exercise Code:</b> <code>server-info.sh</code>", h2_style))

    m1_code = """#!/usr/bin/env bash
echo "--- SRE NODE REPORT ---"

hostname

pwd

date
echo "--- END OF REPORT ---" """
    
    code_table = Table([[Paragraph(f"<pre>{m1_code}</pre>", code_style)]], colWidths=[500])
    code_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CODE_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(code_table)

    story.append(PageBreak())

    # -------------------------------------------------------------
    # SECTION 3: MODULE 2 DEEP DIVE
    # -------------------------------------------------------------
    story.append(Paragraph("3. Module 2: Variables, Types & The Golden Rule of Quoting", h1_style))
    story.append(Paragraph("<b>Mental Model: Labeled Boxes on the Storage Shelf:</b>", h2_style))
    story.append(Paragraph(
        "Variables are memory locations given human-readable labels. In Bash, <i>all variables are stored as strings</i> under the hood. "
        "Assigning values requires absolute precision: spaces around the assignment operator are forbidden.",
        body_style
    ))

    story.append(Paragraph("<b>Crucial Rules & Pitfalls:</b>", h2_style))
    story.append(Paragraph("• <b>No Spaces Around '=':</b> <code>VAR=\"val\"</code> is valid. <code>VAR = \"val\"</code> tries to execute a binary named VAR with arguments.", bullet_style))
    story.append(Paragraph("• <b>The Golden Rule of Double Quotes:</b> Always enclose variable references in double quotes (<code>\"$VAR\"</code>). Unquoted variables undergo <i>Word Splitting</i> and <i>Pathname Expansion (Globbing)</i>, which can destroy paths with spaces.", bullet_style))
    story.append(Paragraph("• <b>Parameter Braces:</b> Use <code>${VAR}</code> when appending static text: <code>\"${APP_ENV}_release\"</code> distinguishes the variable name from surrounding text.", bullet_style))
    story.append(Paragraph("• <b>Single vs. Double Quotes:</b> Single quotes (<code>'...'</code>) are literal (no expansion). Double quotes (<code>\"...\"</code>) allow variable and command expansion.", bullet_style))

    story.append(Spacer(1, 6))
    story.append(Paragraph("<b>Completed Exercise Code:</b> <code>deploy_config.sh</code>", h2_style))

    m2_code = """#!/usr/bin/env bash
# Defining all variables
APP_NAME="PAYTM"
APP_ENV="PRODUCTION"
CLUSTER_REGION="US-EAST-1"
INSTANCE_COUNT=5
DEPLOYMENT_ID="${APP_ENV}_${APP_NAME}_release"

echo "====================================="
echo "STARTING DEPLOYMENT"
echo "====================================="
echo "Application : $APP_NAME"
echo "Target Env  : $APP_ENV"
echo "Region      : $CLUSTER_REGION"
echo "Instances   : $INSTANCE_COUNT"
echo "Deployment ID  : $DEPLOYMENT_ID" """

    code_table2 = Table([[Paragraph(f"<pre>{m2_code}</pre>", code_style)]], colWidths=[500])
    code_table2.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), CODE_BG),
        ('BOX', (0,0), (-1,-1), 1, BORDER),
        ('LEFTPADDING', (0,0), (-1,-1), 12),
        ('TOPPADDING', (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(code_table2)

    story.append(Spacer(1, 15))

    # -------------------------------------------------------------
    # SECTION 4: PREVIEW OF MODULE 3 & BEYOND
    # -------------------------------------------------------------
    story.append(Paragraph("4. Next Session Preview: Module 3 & Telemetry", h1_style))
    story.append(Paragraph(
        "In Module 3, we transition from static scripts to <b>dynamic system awareness</b> using "
        "<b>Command Substitution: <code>$(...)</code></b>.",
        body_style
    ))
    story.append(Paragraph("• <b>The Spy Envelope Model:</b> Rather than letting a command shout its output to the terminal, <code>$(command)</code> captures its standard output into an envelope stored in a variable.", bullet_style))
    story.append(Paragraph("• <b>Modern vs. Legacy:</b> Never use backticks (<code>`command`</code>). Modern Bash requires <code>$(command)</code>, which supports nesting and clean readability.", bullet_style))
    story.append(Paragraph("• <b>Target Challenge:</b> Build <code>system_telemetry.sh</code> to capture architecture, kernel version, hostname, and ISO timestamps dynamically for SRE node reporting.", bullet_style))

    story.append(Spacer(1, 10))

    # -------------------------------------------------------------
    # SRE QUICK REFERENCE CARD
    # -------------------------------------------------------------
    story.append(Paragraph("5. SRE Quick Reference & Debugging Checklist", h1_style))
    cheatsheet = [
        ["Intent", "Idiomatic Bash Syntax", "Notes & Warnings"],
        ["Shebang", "#!/usr/bin/env bash", "Always line 1 byte 0; portable across POSIX."],
        ["Set Permissions", "chmod +x script.sh", "Required before direct execution with ./"],
        ["Variable Assign", "SERVICE=\"api-gateway\"", "ZERO spaces around the '=' operator."],
        ["Safe Variable Read", "\"$SERVICE\"", "Always double-quote to stop word-splitting."],
        ["Parameter Append", "\"${SERVICE}_v2\"", "Curly braces delineate the identifier."],
        ["Command Capture", "TS=$(date \"+%Y-%m-%d\")", "Captures command stdout into variable."],
        ["Syntax Check", "bash -n script.sh", "Validates syntax without running commands."]
    ]
    cs_table = Table(cheatsheet, colWidths=[105, 165, 230])
    cs_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), SECONDARY),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 8.5),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('BOX', (0, 0), (-1, -1), 1, SECONDARY),
        ('INNERGRID', (0, 0), (-1, -1), 0.5, BORDER),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor("#F8FAFC")]),
    ]))
    story.append(cs_table)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"✅ Generated {filename} successfully.")

if __name__ == "__main__":
    build_pdf()
