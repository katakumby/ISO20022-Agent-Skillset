---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["5 pacs.007.001.14 FIToFIPaymentReversalV14", "5.4 Message Building Blocks", "5.4.3 TransactionInformation <TxInf>", "5.4.3.21 OriginalTransactionReference <OrgnlTxRef>", "5.4.3.21.11 RemittanceInformation <RmtInf>", "5.4.3.21.11.2 Structured <Strd>", "5.4.3.21.11.2.7 GarnishmentRemittance <GrnshmtRmt>", "5.4.3.21.11.2.7.1 Type <Tp>"]
file_pages: [681]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.007.001.14"]
---

# 5.4.3.21.11.2.7.1 Type <Tp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 681 to 681.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 681

```text
GarnishmentRemittance <GrnshmtRmt> contains the following Garnishment4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  681
     CodeOrProprietary <CdOrPrtry> [1..1]  681
{Or       Code <Cd> [1..1] CodeSet 682
Or}       Proprietary <Prtry> [1..1] Text 682
     Issuer <Issr> [0..1] Text 682
   Garnishee <Grnshee> [0..1] ± 682
   GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 683
   ReferenceNumber <RefNb> [0..1] Text 684
   Date <Dt> [0..1] Date 685
   RemittedAmount <RmtdAmt> [0..1] Amount C2, C11 685
   FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 685
   EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 685
5.4.3.21.11.2.7.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of garnishment.
Type <Tp> contains the following GarnishmentType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  681
{Or     Code <Cd> [1..1] CodeSet 682
Or}     Proprietary <Prtry> [1..1] Text 682
   Issuer <Issr> [0..1] Text 682
5.4.3.21.11.2.7.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Provides the type details of the garnishment.
CodeOrProprietary <CdOrPrtry> contains one of the following GarnishmentType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 682
Or}   Proprietary <Prtry> [1..1] Text 682
Approved by the Payments SEG on 12 January 2026 pacs.007.001.14 FIToFIPaymentReversalV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
681 March 2026
```

