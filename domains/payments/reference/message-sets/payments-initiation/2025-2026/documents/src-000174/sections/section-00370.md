---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.17 RemittanceInformation <RmtInf>", "5.4.2.18.17.2 Structured <Strd>", "5.4.2.18.17.2.7 GarnishmentRemittance <GrnshmtRmt>", "5.4.2.18.17.2.7.1 Type <Tp>"]
file_pages: [520]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.17.2.7.1 Type <Tp>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 520 to 520.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 520

```text
GarnishmentRemittance <GrnshmtRmt> contains the following Garnishment4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  520
     CodeOrProprietary <CdOrPrtry> [1..1]  520
{Or       Code <Cd> [1..1] CodeSet 521
Or}       Proprietary <Prtry> [1..1] Text 521
     Issuer <Issr> [0..1] Text 521
   Garnishee <Grnshee> [0..1] ± 521
   GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 522
   ReferenceNumber <RefNb> [0..1] Text 523
   Date <Dt> [0..1] Date 524
   RemittedAmount <RmtdAmt> [0..1] Amount C2, C12 524
   FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 524
   EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 524
5.4.2.18.17.2.7.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of garnishment.
Type <Tp> contains the following GarnishmentType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  520
{Or     Code <Cd> [1..1] CodeSet 521
Or}     Proprietary <Prtry> [1..1] Text 521
   Issuer <Issr> [0..1] Text 521
5.4.2.18.17.2.7.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Provides the type details of the garnishment.
CodeOrProprietary <CdOrPrtry> contains one of the following GarnishmentType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 521
Or}   Proprietary <Prtry> [1..1] Text 521
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 520 March 2026
```

