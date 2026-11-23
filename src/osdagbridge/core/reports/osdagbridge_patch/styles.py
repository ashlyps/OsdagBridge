
"""
Centralized styling configuration for OsdagBridge reports.

This module stores reusable formatting settings.
"""

# Document settings
PAGE_SIZE = "a4paper"
PAGE_MARGIN = "1in"
FONT_SIZE = "12pt"

# Color palette
COLORS = {
    "primary": "91B014",
    "text": "000000",
    "table_header": "EAF1D8",
    "table_border": "000000",
}

# Table formatting
TABLE_STYLE = {
    "column_padding": "6pt",
    "row_stretch": 1.12,
    "rule_width": "0.5pt",
    "extra_row_height": "0.6pt",
    "longtable_pre": "0pt",
    "longtable_post": "6pt",
}

# Page layout
PAGE_STYLE = {
    "line_spacing": 1.15,
    "minimum_table_space": 5,
}

# Chart formatting
CHART_STYLE = {
    "dpi": 150,
    "ur_threshold": 1.0,
    "pass_color": "#91B014",
    "fail_color": "#D9534F",
}
