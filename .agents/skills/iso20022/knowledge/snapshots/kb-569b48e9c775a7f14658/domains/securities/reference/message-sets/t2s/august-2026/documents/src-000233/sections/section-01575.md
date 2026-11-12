---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["48 reda.028.001.01 CollateralDataStatusAdviceV01", "48.4 Message Building Blocks", "48.4.3 StatusReasonAndFinancialInstrument <StsRsnAndFinInstrm>", "48.4.3.2 Reason <Rsn>", "48.4.3.2.1 Reason <Rsn>"]
file_pages: [2200]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.028.001.01"]
---

# 48.4.3.2.1 Reason <Rsn>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2200 to 2200.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2200

```text
Reason <Rsn> contains the following StatusReasonInformation13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  2200
{Or     Code <Cd> [1..1] CodeSet 2200
Or}     Proprietary <Prtry> [1..1] ± 2200
   FinancialInstrument <FinInstrm> [0..1] ± C1, C2,
C3, C4,
C5
2200
   AdditionalInformation <AddtlInf> [0..1] Text 2201
48.4.3.2.1  Reason <Rsn>
Presence: [1..1]
Definition: Specifies the reason for the status report.
Reason <Rsn> contains one of the following StatusReason7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2200
Or}   Proprietary <Prtry> [1..1] ± 2200
48.4.3.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the status, as published in an external reason code list.
Datatype: "ExternalCollateralReferenceDataStatusReason1Code" on page 3241
48.4.3.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the status, in a proprietary form.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   SchemeName <SchmeNm> [0..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
48.4.3.2.2  FinancialInstrument <FinInstrm>
Presence: [0..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.028.001.01 CollateralDataStatusAdviceV01
Target2-Securities 2200 August 2026
```

