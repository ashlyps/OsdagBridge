
import logging
from pathlib import Path
from datetime import date

from osdagbridge.core.reports.report_generator import (
    ReportMetadata,
    ReportOptions,
    ReportRequest,
    build_report_payload,
    generate_report,
)

logging.basicConfig(level=logging.INFO)

root = Path(__file__).resolve().parent

metadata = ReportMetadata(
    project_name="OsdagBridge Report Generator Enhancement Test",
    project_location="Test Case",
    designer="FOSSEE Internship",
    client="Report Generator Validation",
    company="OsdagBridge",
    subtitle="Enhanced Report - Formatting Validation",
    job_number="REPORT-TEST-001",
    report_date=date.today().isoformat(),
    additional_comments=(
        "Report generation test using placeholder input. "
        "No structural analysis or design verification performed."
    ),
)

options = ReportOptions(
    sections=[
        "loads",
        "analysis",
        "design_checks",
        "drawings",
    ],
    include_figures=True,
    include_toc=True,
    include_pdf=True,
)

request = ReportRequest(
    metadata=metadata,
    options=options,
    output_dir=str(root),
    file_stem="Report_After",
)

# The repository's example_basic.yaml is a placeholder.
# These are demonstration inputs, not verified design data.
input_dict = {
    "project.name": "example_basic",
    "span_m": 30.0,
}

# Do not invent analysis results or design checks.
output_dict = {}

payload = build_report_payload(
    request,
    input_dict,
    output_dict,
)

print("Generating Report_After.pdf...", flush=True)

result = generate_report(payload, request)

print("PDF:", result.pdf_path)
print("TEX:", result.tex_path)

if result.pdf_path and Path(result.pdf_path).is_file():
    print("SUCCESS: Report_After.pdf generated!")
else:
    print("PDF generation failed. Check compiler logs.")
    if result.tex_path:
        print("LaTeX source:", result.tex_path)
