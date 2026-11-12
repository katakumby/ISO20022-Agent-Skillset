---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.26 RemittanceInformation <RmtInf>", "2.4.2.19.26.2 Structured <Strd>", "2.4.2.19.26.2.7 GarnishmentRemittance <GrnshmtRmt>", "2.4.2.19.26.2.7.1 Type <Tp>"]
file_pages: [123]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.26.2.7.1 Type <Tp>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 123 to 123.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 123

```text
GarnishmentRemittance <GrnshmtRmt> contains the following Garnishment4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  123
     CodeOrProprietary <CdOrPrtry> [1..1]  123
{Or       Code <Cd> [1..1] CodeSet 124
Or}       Proprietary <Prtry> [1..1] Text 124
     Issuer <Issr> [0..1] Text 124
   Garnishee <Grnshee> [0..1] ± 124
   GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 125
   ReferenceNumber <RefNb> [0..1] Text 126
   Date <Dt> [0..1] Date 127
   RemittedAmount <RmtdAmt> [0..1] Amount C2, C19 127
   FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 127
   EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 127
2.4.2.19.26.2.7.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of garnishment.
Type <Tp> contains the following GarnishmentType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  123
{Or     Code <Cd> [1..1] CodeSet 124
Or}     Proprietary <Prtry> [1..1] Text 124
   Issuer <Issr> [0..1] Text 124
2.4.2.19.26.2.7.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Provides the type details of the garnishment.
CodeOrProprietary <CdOrPrtry> contains one of the following GarnishmentType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 124
Or}   Proprietary <Prtry> [1..1] Text 124
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 123 March 2026
```

