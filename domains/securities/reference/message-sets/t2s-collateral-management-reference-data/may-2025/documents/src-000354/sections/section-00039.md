---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["6 reda.028.001.01 CollateralDataStatusAdviceV01", "6.4 Message Building Blocks", "6.4.3 StatusReasonAndFinancialInstrument <StsRsnAndFinInstrm>", "6.4.3.2 Reason <Rsn>", "6.4.3.2.1 Reason <Rsn>"]
file_pages: [43]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.028.001.01"]
---

# 6.4.3.2.1 Reason <Rsn>

Source: [src-000354](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 43 to 43.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 43

```text
Reason <Rsn> contains the following StatusReasonInformation13 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  43
{Or     Code <Cd> [1..1] CodeSet 43
Or}     Proprietary <Prtry> [1..1] ± 43
   FinancialInstrument <FinInstrm> [0..1] ± C1, C2,
C3, C4,
C5
43
   AdditionalInformation <AddtlInf> [0..1] Text 44
6.4.3.2.1  Reason <Rsn>
Presence: [1..1]
Definition: Specifies the reason for the status report.
Reason <Rsn> contains one of the following StatusReason7Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 43
Or}   Proprietary <Prtry> [1..1] ± 43
6.4.3.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the status, as published in an external reason code list.
Datatype: "ExternalCollateralReferenceDataStatusReason1Code" on page 79
6.4.3.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the status, in a proprietary form.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 65 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 65
   SchemeName <SchmeNm> [0..1] Text 65
   Issuer <Issr> [0..1] Text 65
6.4.3.2.2  FinancialInstrument <FinInstrm>
Presence: [0..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Approved by the Securities SEG on 17 April 2025. reda.028.001.01 CollateralDataStatusAdviceV01
Target2-Securities - Collateral Management Reference Data 43 May 2025
```

