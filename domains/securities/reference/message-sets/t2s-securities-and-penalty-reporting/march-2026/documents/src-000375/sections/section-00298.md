---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous", "7.1.18.18 TaxCapacityParty4Choice", "7.1.18.18.1 Code <Cd>"]
file_pages: [375]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.18.1 Code <Cd>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 375 to 375.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 375

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 375
Or}   Proprietary <Prtry> [1..1] ± 375
7.1.18.18.1  Code <Cd>
Presence: [1..1]
Definition: Party tax capacity expressed as an ISO 20022 code.
Datatype: "TaxLiability1Code" on page 541
CodeName Name Definition
PRIN TaxPrincipal Settlement party is acting as a principal
for tax liability.
AGEN TaxAgent Settlement party is acting as an agent for
tax liability.
7.1.18.18.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Party tax capacity expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.18.19  SupplementaryData1
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 375
   Envelope <Envlp> [1..1] (External Schema) 376
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
7.1.18.19.1  PlaceAndName <PlcAndNm>
Presence: [0..1]
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 375 March 2026
```

