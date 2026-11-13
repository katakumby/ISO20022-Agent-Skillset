---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.23 UnderlyingCustomerCreditTransfer <UndrlygCstmrCdtTrf>", "4.4.3.27.23.30 RemittanceInformation <RmtInf>", "4.4.3.27.23.30.2 Structured <Strd>", "4.4.3.27.23.30.2.7 GarnishmentRemittance <GrnshmtRmt>", "4.4.3.27.23.30.2.7.1 Type <Tp>"]
file_pages: [524]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.23.30.2.7.1 Type <Tp>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 524 to 524.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 524

```text
GarnishmentRemittance <GrnshmtRmt> contains the following Garnishment4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  524
     CodeOrProprietary <CdOrPrtry> [1..1]  524
{Or       Code <Cd> [1..1] CodeSet 525
Or}       Proprietary <Prtry> [1..1] Text 525
     Issuer <Issr> [0..1] Text 525
   Garnishee <Grnshee> [0..1] ± 525
   GarnishmentAdministrator <GrnshmtAdmstr> [0..1] ± 526
   ReferenceNumber <RefNb> [0..1] Text 527
   Date <Dt> [0..1] Date 528
   RemittedAmount <RmtdAmt> [0..1] Amount C2, C12 528
   FamilyMedicalInsuranceIndicator
<FmlyMdclInsrncInd>
[0..1] Indicator 528
   EmployeeTerminationIndicator <MplyeeTermntnInd> [0..1] Indicator 528
4.4.3.27.23.30.2.7.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the type of garnishment.
Type <Tp> contains the following GarnishmentType1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CodeOrProprietary <CdOrPrtry> [1..1]  524
{Or     Code <Cd> [1..1] CodeSet 525
Or}     Proprietary <Prtry> [1..1] Text 525
   Issuer <Issr> [0..1] Text 525
4.4.3.27.23.30.2.7.1.1  CodeOrProprietary <CdOrPrtry>
Presence: [1..1]
Definition: Provides the type details of the garnishment.
CodeOrProprietary <CdOrPrtry> contains one of the following GarnishmentType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 525
Or}   Proprietary <Prtry> [1..1] Text 525
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
524 March 2026
```

