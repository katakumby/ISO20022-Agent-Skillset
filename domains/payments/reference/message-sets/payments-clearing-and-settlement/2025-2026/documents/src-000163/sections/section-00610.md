---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.47 RemittanceInformation <RmtInf>", "6.4.2.47.2 Structured <Strd>", "6.4.2.47.2.7 GarnishmentRemittance <GrnshmtRmt>", "6.4.2.47.2.7.1 Type <Tp>"]
file_pages: [823]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.47.2.7.1 Type <Tp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 823 to 823.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 823

```text
GarnishmentRemittance <GrnshmtRmt> contains the following Garnishment4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  823
     CodeOrProprietary <CdOrPrtry> [1..1]  823
{Or       Code <Cd> [1..1] CodeSet 824
Or}       Proprietary <Prtry> [1..1] Text 824
     Issuer <Issr> [0..1] Text 824
   Garnishee <Grnshee> [0..1] ± 824
   GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 825
   ReferenceNumber <RefNb> [0..1] Text 826
   Date <Dt> [0..1] Date 827
   RemittedAmount <RmtdAmt> [0..1] Amount C2, C12 827
   FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 827
   EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 827
6.4.2.47.2.7.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of garnishment.
Type <Tp> contains the following GarnishmentType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  823
{Or     Code <Cd> [1..1] CodeSet 824
Or}     Proprietary <Prtry> [1..1] Text 824
   Issuer <Issr> [0..1] Text 824
6.4.2.47.2.7.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Provides the type details of the garnishment.
CodeOrProprietary <CdOrPrtry> contains one of the following GarnishmentType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 824
Or}   Proprietary <Prtry> [1..1] Text 824
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
823 March 2026
```

