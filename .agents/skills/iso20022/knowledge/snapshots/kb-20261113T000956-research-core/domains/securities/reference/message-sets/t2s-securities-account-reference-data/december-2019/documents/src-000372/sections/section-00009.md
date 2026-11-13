---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["2 reda.018.001.01 SecuritiesAccountCreationRequestV01", "2.4 Message Building Blocks", "2.4.2 SecuritiesAccount <SctiesAcct>", "2.4.2.4 OpeningDate <OpngDt>"]
file_pages: [11]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.018.001.01"]
---

# 2.4.2.4 OpeningDate <OpngDt>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 11 to 11.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 11

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 81 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 81
   Issuer <Issr> [1..1] Text 81
   SchemeName <SchmeNm> [0..1] Text 81
2.4.2.4  OpeningDate <OpngDt>
Presence: [1..1]
Definition: Legal opening date of the securities account.
Datatype: "ISODate" on page 97
2.4.2.5  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Legal closing date of the securities account.
Datatype: "ISODate" on page 97
2.4.2.6  HoldIndicator <HldInd>
Presence: [1..1]
Definition: Indicates whether the securities account is on hold or not.
Usage:
- Meaning when true: account is in hold status.
- Meaning when false: account is in release status.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 98):
• Meaning When True: True
• Meaning When False: False
2.4.2.7  NegativePosition <NegPos>
Presence: [1..1]
Definition: Indicates whether the securities account can hold a negative position in a security or not.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 98):
• Meaning When True: True
• Meaning When False: False
2.4.2.8  MarketSpecificAttribute <MktSpcfcAttr>
Presence: [0..*]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.018.001.01
SecuritiesAccountCreationRequestV01
Target2-Securities - Securities Account Reference Data 11 December 2019
```

