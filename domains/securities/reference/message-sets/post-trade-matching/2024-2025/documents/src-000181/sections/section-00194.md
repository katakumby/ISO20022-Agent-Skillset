---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Cash"]
file_pages: [247]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5 Cash

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 247 to 247.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 247

```text
Definition: Unique and unambiguous identifier of a certificate assigned by the issuer.
Impacted by: C21 "ISO8532AndIssuerSchemeNameRule"
CertificateNumber <CertNb> contains the following elements (see "SecuritiesCertificate3" on
page 272 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Number <Nb> [1..1] Text 272
   Issuer <Issr> [0..1] Text 272
   SchemeName <SchmeNm> [0..1] Text 272
Constraints
• ISO8532AndIssuerSchemeNameRule
If Number is ISO 8532 (Format for transmission of certificate numbers), then Issuer and
SchemeName must not be used.
7.1.5 Cash
7.1.5.1  CashSettlementSystem4Choice
Definition: Choice of format for the cash settlement system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 247
Or}   Proprietary <Prtry> [1..1] ± 247
7.1.5.1.1  Code <Cd>
Presence: [1..1]
Definition: Cash settlement system expressed as an ISO 20022 code.
Datatype: "CashSettlementSystem2Code" on page 619
CodeName Name Definition
GROS GrossSettlementSystem Settle money through gross settlement
system.
NETS NetSettlementSystem Settle money through net settlement
system.
7.1.5.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Cash settlement system expressed as a proprietary code.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 247 February 2025
```

