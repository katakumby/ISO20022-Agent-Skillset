---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.2.1.3 Debt <Debt>", "28.4.2.1.2.1.3.54 InstrumentStructureType <InstrmStrTp>", "28.4.2.1.2.1.3.54.2 Proprietary <Prtry>"]
file_pages: [1244]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.1.3.54.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1244 to 1244.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1244

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
28.4.2.1.2.1.3.54.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Instrument sub-structure type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
28.4.2.1.2.1.3.55  GlobalType <GblTp>
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
{Or   Code <Cd> [1..1] CodeSet 1244
Or}   Proprietary <Prtry> [1..1] ± 1245
28.4.2.1.2.1.3.55.1  Code <Cd>
Presence: [1..1]
Definition: Global note expressed as an ISO 20022 code.
Datatype: "GlobalNote1Code" on page 3255
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1244 August 2026
```

