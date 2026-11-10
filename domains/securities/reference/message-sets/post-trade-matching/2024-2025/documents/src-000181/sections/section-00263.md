---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.31 TaxCapacityParty4Choice", "7.1.19.31.1 Code <Cd>"]
file_pages: [321]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.31.1 Code <Cd>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 321 to 321.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 321

```text
7.1.19.31.1  Code <Cd>
Presence: [1..1]
Definition: Party tax capacity expressed as an ISO 20022 code.
Datatype: "TaxLiability1Code" on page 652
CodeName Name Definition
PRIN TaxPrincipal Settlement party is acting as a principal
for tax liability.
AGEN TaxAgent Settlement party is acting as an agent for
tax liability.
7.1.19.31.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Party tax capacity expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.32  SupplementaryData1
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 321
   Envelope <Envlp> [1..1] (External Schema) 322
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
7.1.19.32.1  PlaceAndName <PlcAndNm>
Presence: [0..1]
Definition: Unambiguous reference to the location where the supplementary data must be inserted in
the message instance.
In the case of XML, this is expressed by a valid XPath.
Datatype: "Max350Text" on page 669
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 321 February 2025
```

