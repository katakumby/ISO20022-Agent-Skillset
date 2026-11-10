---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.4 DrawdownStatus1Choice", "66.1.45.4.1 Code <Cd>"]
file_pages: [5171]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.4.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5171 to 5171.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5171

```text
66.1.45.4.1  Code <Cd>
Presence: [1..1]
Definition: Status expressed as a code.
Datatype: "DrawdownStatus1Code" on page 5295
CodeName Name Definition
FULL Full Pension is fully in drawdown.
NONE None Pension is not in drawdown.
PART Partial Pension is in partial drawdown.
66.1.45.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.45.5  ProformaStatusReason1Choice
Definition: Choice of formats for a proforma status reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5171
Or}   Reason <Rsn> [1..*]  5172
     Code <Cd> [1..1]  5172
{Or       Code <Cd> [1..1] CodeSet 5172
Or}       Proprietary <Prtry> [1..1] ± 5172
     AdditionalInformation <AddtlInf> [0..1] Text 5173
66.1.45.5.1  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: There is no reason available or to report for the proforma account status.
Datatype: "NoReasonCode" on page 5331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5171 May 2026
```

