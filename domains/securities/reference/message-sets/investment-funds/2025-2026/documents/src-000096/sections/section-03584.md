---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.17 CancellationRight1Choice"]
file_pages: [4834]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.17 CancellationRight1Choice

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4834 to 4834.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4834

```text
Definition: Indicates the last page.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.28.17  CancellationRight1Choice
Definition: Choice of formats for the cancellation right.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4834
Or}   Proprietary <Prtry> [1..1] ± 4834
66.1.28.17.1  Code <Cd>
Presence: [1..1]
Definition: Cancellation right expressed as a code.
Datatype: "CancellationRight1Code" on page 5279
CodeName Name Definition
VALI Entitled Investor is entitled to a "cooling off"
period with cancellation rights under
compliance rules.
NOXO ExecutionOnly Investor is not entitled to cancellation
rights under compliance rules, as the
investor is an execution's only client.
NOWA WaiverAgreement Investor is not entitled to cancellation
rights under compliance rules as the
investor has agreed to waive those
rights.
NOIN Institutional Investor is not entitled to cancellation
rights under compliance rules as the
investor is a financial institution.
66.1.28.17.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Cancellation right expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4834 May 2026
```

