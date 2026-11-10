---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "9.4 Message Building Blocks", "9.4.1 GroupHeader <GrpHdr>", "9.4.3.11 OriginalTransactionReference <OrgnlTxRef>", "9.4.3.11.11 RemittanceInformation <RmtInf>", "9.4.3.11.11.2 Structured <Strd>", "9.4.3.11.11.2.7 GarnishmentRemittance <GrnshmtRmt>", "9.4.3.11.11.2.7.1 Type <Tp>"]
file_pages: [1140]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.028.001.07"]
---

# 9.4.3.11.11.2.7.1 Type <Tp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1140 to 1140.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1140

```text
GarnishmentRemittance <GrnshmtRmt> contains the following Garnishment4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  1140
     CodeOrProprietary <CdOrPrtry> [1..1]  1140
{Or       Code <Cd> [1..1] CodeSet 1141
Or}       Proprietary <Prtry> [1..1] Text 1141
     Issuer <Issr> [0..1] Text 1141
   Garnishee <Grnshee> [0..1] ± 1141
   GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 1142
   ReferenceNumber <RefNb> [0..1] Text 1143
   Date <Dt> [0..1] Date 1144
   RemittedAmount <RmtdAmt> [0..1] Amount C2, C8 1144
   FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 1144
   EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 1144
9.4.3.11.11.2.7.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of garnishment.
Type <Tp> contains the following GarnishmentType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  1140
{Or     Code <Cd> [1..1] CodeSet 1141
Or}     Proprietary <Prtry> [1..1] Text 1141
   Issuer <Issr> [0..1] Text 1141
9.4.3.11.11.2.7.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Provides the type details of the garnishment.
CodeOrProprietary <CdOrPrtry> contains one of the following GarnishmentType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1141
Or}   Proprietary <Prtry> [1..1] Text 1141
Approved by the Payments SEG on 12 January 2026 pacs.028.001.07 FIToFIPaymentStatusRequestV07
Payments Clearing and Settlement - Maintenance 2025 -
2026
1140 March 2026
```

