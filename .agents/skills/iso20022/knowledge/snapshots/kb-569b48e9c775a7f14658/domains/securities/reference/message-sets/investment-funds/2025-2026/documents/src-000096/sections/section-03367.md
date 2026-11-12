---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.7 InvestmentAccountOwnershipInformation16", "66.1.24.7.17 TaxExemption <TaxXmptn>"]
file_pages: [4610]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.7.17 TaxExemption <TaxXmptn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4610 to 4610.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4610

```text
66.1.24.7.17  TaxExemption <TaxXmptn>
Presence: [0..1]
Definition: Tax advantage specific to the account party.
TaxExemption <TaxXmptn> contains one of the following elements (see
"TaxExemptionReason2Choice" on page 5250 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5251
Or}   Proprietary <Prtry> [1..1] ± 5254
66.1.24.7.18  TaxReporting <TaxRptg>
Presence: [0..*]
Definition: Details for the reporting of tax, for example, the country of taxation.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4610 May 2026
```

