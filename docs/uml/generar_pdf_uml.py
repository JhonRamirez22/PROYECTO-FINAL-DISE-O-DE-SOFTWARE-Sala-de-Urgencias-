#!/usr/bin/env python3
"""Genera el PDF de la especificación UML desde su fuente Markdown.

Uso:
  python docs/uml/generar_pdf_uml.py

Dependencia:
  pip install reportlab
"""

from __future__ import annotations

from pathlib import Path
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import (
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "especificacion-uml-urgencyai.md"
OUTPUT = ROOT / "especificacion-uml-urgencyai.pdf"


def clean_inline(text: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", text)
    return text


def parse_md_lines(lines: list[str]):
    i = 0
    while i < len(lines):
        line = lines[i].rstrip("\n")

        if not line.strip():
            yield ("blank", "")
            i += 1
            continue

        if line.strip() == "---":
            yield ("rule", line)
            i += 1
            continue

        if line.strip() == "\f":
            yield ("pagebreak", "")
            i += 1
            continue

        if line.strip().startswith("```"):
            lang = line.strip().strip("`").strip()
            i += 1
            block: list[str] = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(lines[i].rstrip("\n"))
                i += 1
            i += 1
            yield ("code", (lang, "\n".join(block)))
            continue

        if line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                raw = lines[i].strip()
                cols = [c.strip() for c in raw.strip("|").split("|")]
                rows.append(cols)
                i += 1
            yield ("table", rows)
            continue

        if line.startswith("# "):
            yield ("h1", line[2:].strip())
        elif line.startswith("## "):
            yield ("h2", line[3:].strip())
        elif line.startswith("### "):
            yield ("h3", line[4:].strip())
        elif line.startswith("- "):
            yield ("li", line[2:].strip())
        elif re.match(r"^\d+\.\s+", line):
            yield ("num", line)
        else:
            yield ("p", line)

        i += 1


def build_pdf(source: Path, output: Path) -> None:
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="TitleCenter", parent=styles["Title"], alignment=TA_CENTER, spaceAfter=12))
    styles.add(ParagraphStyle(name="H2", parent=styles["Heading2"], spaceBefore=10, spaceAfter=6))
    styles.add(ParagraphStyle(name="H3", parent=styles["Heading3"], spaceBefore=8, spaceAfter=4))
    styles.add(ParagraphStyle(name="Body", parent=styles["BodyText"], leading=14, spaceAfter=4))
    styles.add(ParagraphStyle(name="BulletList", parent=styles["BodyText"], leftIndent=14, leading=14, spaceAfter=2))
    styles.add(ParagraphStyle(name="CodeBlock", fontName="Courier", fontSize=8.5, leading=10))

    doc = SimpleDocTemplate(
        str(output),
        pagesize=A4,
        topMargin=2.2 * cm,
        bottomMargin=2.0 * cm,
        leftMargin=2.0 * cm,
        rightMargin=2.0 * cm,
        title="Especificación UML UrgencyAI",
        author="Proyecto UrgencyAI",
    )

    story = []
    lines = source.read_text(encoding="utf-8").splitlines()

    for kind, payload in parse_md_lines(lines):
        if kind == "blank":
            story.append(Spacer(1, 0.15 * cm))
        elif kind == "rule":
            story.append(Spacer(1, 0.1 * cm))
        elif kind == "pagebreak":
            story.append(PageBreak())
        elif kind == "h1":
            story.append(Paragraph(clean_inline(payload), styles["TitleCenter"]))
        elif kind == "h2":
            story.append(Paragraph(clean_inline(payload), styles["H2"]))
        elif kind == "h3":
            story.append(Paragraph(clean_inline(payload), styles["H3"]))
        elif kind == "li":
            story.append(Paragraph(f"• {clean_inline(payload)}", styles["BulletList"]))
        elif kind == "num":
            story.append(Paragraph(clean_inline(payload), styles["Body"]))
        elif kind == "code":
            lang, code = payload
            if lang:
                story.append(Paragraph(f"<b>Código:</b> {clean_inline(lang)}", styles["Body"]))
            story.append(
                Preformatted(
                    code,
                    styles["CodeBlock"],
                    dedent=0,
                    maxLineLength=135,
                    newLineChars="\n",
                )
            )
            story.append(Spacer(1, 0.1 * cm))
        elif kind == "table":
            rows = payload
            if len(rows) >= 2 and all(re.match(r"^:?-+:?$", c.replace(" ", "")) for c in rows[1]):
                rows = [rows[0]] + rows[2:]
            rows = [[clean_inline(cell) for cell in row] for row in rows]
            t = Table(rows, repeatRows=1)
            t.setStyle(
                TableStyle(
                    [
                        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#E8EEF7")),
                        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
                        ("FONTSIZE", (0, 0), (-1, -1), 9),
                        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
                        ("VALIGN", (0, 0), (-1, -1), "TOP"),
                        ("LEFTPADDING", (0, 0), (-1, -1), 5),
                        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                        ("TOPPADDING", (0, 0), (-1, -1), 4),
                        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                    ]
                )
            )
            story.append(t)
            story.append(Spacer(1, 0.2 * cm))
        else:
            story.append(Paragraph(clean_inline(payload), styles["Body"]))

    def add_page_number(canvas, _doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.drawRightString(A4[0] - 2.0 * cm, 1.2 * cm, f"Página {_doc.page}")
        canvas.restoreState()

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)


if __name__ == "__main__":
    build_pdf(SOURCE, OUTPUT)
    print(f"PDF generado: {OUTPUT}")
