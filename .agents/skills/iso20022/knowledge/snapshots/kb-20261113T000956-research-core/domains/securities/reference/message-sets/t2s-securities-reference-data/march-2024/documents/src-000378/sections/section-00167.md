---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.4 Warrant4", "13.1.2.4.3 Type <Tp>", "13.1.2.4.3.1 Code <Cd>"]
file_pages: [231]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.4.3.1 Code <Cd>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 231 to 231.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 231

```text
Definition: Indicates when a warrant can be exercised.
Type <Tp> contains one of the following WarrantStyle3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 231
Or}   Proprietary <Prtry> [1..1] ± 231
13.1.2.4.3.1  Code <Cd>
Presence: [1..1]
Definition: Warrant style expressed as an ISO 20022 code.
Datatype: "WarrantStyle1Code" on page 529
CodeName Name Definition
AMER American Option can be exercised before or on
expiry date.
EURO European Option that can be exercised on expiry
date only.
BERM Bermudan Option that can be exercised on multiple
discrete dates prior to, or on expiry date.
13.1.2.4.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Warrant style expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.2.4.4  WarrantAgent <WarrtAgt>
Presence: [0..*]
Definition: Entity appointed by the issuer to process the exercising of warrants, sometimes responsible
for the issuance of the warrants into the market.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 231 March 2024
```

