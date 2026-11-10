---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "4.4 Message Building Blocks", "4.4.3.8 TransactionInformation <TxInf>", "4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.8.9.11 RemittanceInformation <RmtInf>", "4.4.3.8.9.11.2 Structured <Strd>", "4.4.3.8.9.11.2.7 GarnishmentRemittance <GrnshmtRmt>", "4.4.3.8.9.11.2.7.1 Type <Tp>"]
file_pages: [382]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.007.001.13"]
---

# 4.4.3.8.9.11.2.7.1 Type <Tp>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 382 to 382.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 382

```text
GarnishmentRemittance <GrnshmtRmt> contains the following Garnishment4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  382
     CodeOrProprietary <CdOrPrtry> [1..1]  382
{Or       Code <Cd> [1..1] CodeSet 383
Or}       Proprietary <Prtry> [1..1] Text 383
     Issuer <Issr> [0..1] Text 383
   Garnishee <Grnshee> [0..1] ± 383
   GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 384
   ReferenceNumber <RefNb> [0..1] Text 385
   Date <Dt> [0..1] Date 386
   RemittedAmount <RmtdAmt> [0..1] Amount C2, C9 386
   FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 386
   EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 386
4.4.3.8.9.11.2.7.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of garnishment.
Type <Tp> contains the following GarnishmentType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  382
{Or     Code <Cd> [1..1] CodeSet 383
Or}     Proprietary <Prtry> [1..1] Text 383
   Issuer <Issr> [0..1] Text 383
4.4.3.8.9.11.2.7.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Provides the type details of the garnishment.
CodeOrProprietary <CdOrPrtry> contains one of the following GarnishmentType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 383
Or}   Proprietary <Prtry> [1..1] Text 383
Approved by the Payments SEG on 12 January 2026 pain.007.001.13 CustomerPaymentReversalV13
Payments Initiation - Maintenance 2025 - 2026 382 March 2026
```

