---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.54 InstrumentStructureType <InstrmStrTp>", "13.1.2.3.54.2 Proprietary <Prtry>"]
file_pages: [221]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.54.2 Proprietary <Prtry>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 221 to 221.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 221

```text
CodeName Name Definition
SCBO StructuredCoveredBond Sub structured type of the financial
instrument is a structured covered bond.
STRB StraightBond Sub structured type of the financial
instrument is a straight bond.
STUT StudentLoanTrust Sub structured type of the financial
instrument is a student loan trust.
WBSE WholeBusinessSecurity Sub structured type of the financial
instrument is a whole business security.
13.1.2.3.54.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Instrument sub-structure type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.2.3.55  GlobalType <GblTp>
Presence: [0..1]
Definition: Identifies if the security will be issued in New Global Note (NGN) or Classical Global Note
(CGN).
New Global Note (NGN): Form of global certificate which refers to the books and records of the ICSDs
to determine the issue outstanding amount (IOA).
Classical Global Note (CGN): Form of global certificate which requires physical annotation on the
attached schedule to reflect changes in the issue outstanding amount (IOA).
GlobalType <GblTp> contains one of the following GlobalNote2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 221
Or}   Proprietary <Prtry> [1..1] ± 222
13.1.2.3.55.1  Code <Cd>
Presence: [1..1]
Definition: Global note expressed as an ISO 20022 code.
Datatype: "GlobalNote1Code" on page 515
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 221 March 2024
```

