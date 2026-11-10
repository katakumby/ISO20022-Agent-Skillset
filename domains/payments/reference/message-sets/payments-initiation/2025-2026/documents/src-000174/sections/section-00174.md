---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.12 OriginalTransactionReference <OrgnlTxRef>", "3.4.3.7.12.11 RemittanceInformation <RmtInf>", "3.4.3.7.12.11.2 Structured <Strd>", "3.4.3.7.12.11.2.7 GarnishmentRemittance <GrnshmtRmt>", "3.4.3.7.12.11.2.7.1 Type <Tp>"]
file_pages: [251]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.12.11.2.7.1 Type <Tp>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 251 to 251.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 251

```text
GarnishmentRemittance <GrnshmtRmt> contains the following Garnishment4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  251
     CodeOrProprietary <CdOrPrtry> [1..1]  251
{Or       Code <Cd> [1..1] CodeSet 252
Or}       Proprietary <Prtry> [1..1] Text 252
     Issuer <Issr> [0..1] Text 252
   Garnishee <Grnshee> [0..1] ± 252
   GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 253
   ReferenceNumber <RefNb> [0..1] Text 254
   Date <Dt> [0..1] Date 255
   RemittedAmount <RmtdAmt> [0..1] Amount C2, C8 255
   FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 255
   EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 255
3.4.3.7.12.11.2.7.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of garnishment.
Type <Tp> contains the following GarnishmentType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  251
{Or     Code <Cd> [1..1] CodeSet 252
Or}     Proprietary <Prtry> [1..1] Text 252
   Issuer <Issr> [0..1] Text 252
3.4.3.7.12.11.2.7.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Provides the type details of the garnishment.
CodeOrProprietary <CdOrPrtry> contains one of the following GarnishmentType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 252
Or}   Proprietary <Prtry> [1..1] Text 252
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 251 March 2026
```

