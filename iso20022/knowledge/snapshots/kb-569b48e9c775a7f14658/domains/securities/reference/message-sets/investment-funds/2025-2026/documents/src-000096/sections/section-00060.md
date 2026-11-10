---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["6 acmt.006.001.07 AccountManagementStatusReportV07", "6.4 Message Building Blocks", "6.4.3 StatusReport <StsRpt>", "6.4.3.9 CRSReportingDate <CRSRptgDt>"]
file_pages: [93]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.006.001.07"]
---

# 6.4.3.9 CRSReportingDate <CRSRptgDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 93 to 93.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 93

```text
Definition: Date provided by the account owner to inform the account servicer of the date on which the
holdings must be reported before the account is subsequently closed.
Datatype: "ISODate" on page 5388
6.4.3.9  CRSReportingDate <CRSRptgDt>
Presence: [0..1]
Definition: Date provided by the account owner to inform the account servicer of the date on which the
holdings must be reported before the account is subsequently closed.
Datatype: "ISODate" on page 5388
6.4.4 MarketPracticeVersion <MktPrctcVrsn>
Presence: [0..1]
Definition: Identifies the market practice to which the message conforms.
MarketPracticeVersion <MktPrctcVrsn> contains the following elements (see
"MarketPracticeVersion1" on page 4818 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4818
   Date <Dt> [0..1] YearMonth 4819
   Number <Nb> [0..1] Text 4819
6.4.5 Extension <Xtnsn>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C11 "ExtensionRule"
Extension <Xtnsn> contains the following elements (see "Extension1" on page 4835 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [1..1] Text 4836
   Text <Txt> [1..1] Text 4836
Constraints
• ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
Approved by the Securities SEG on 27 January 2026 acmt.006.001.07
AccountManagementStatusReportV07
Investment Funds - Maintenance 2025 - 2026 93 May 2026
```

