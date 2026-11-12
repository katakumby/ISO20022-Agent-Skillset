---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["14 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "14.4 Message Building Blocks", "14.4.4 ReportOrError <RptOrErr>", "14.4.4.1 Cancellations <Cxls>", "14.4.4.1.1 CashAccount <CshAcct>"]
file_pages: [314]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 14.4.4.1.1 CashAccount <CshAcct>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 314 to 314.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 314

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       BalanceTo <BalTo> [1..1]  326
         Type <Tp> [1..1]  326
{Or           Code <Cd> [1..1] CodeSet 326
Or}           Proprietary <Prtry> [1..1] ± 326
         QuantityBreakdown <QtyBrkdwn> [0..*]  327
           LotNumber <LotNb> [0..1] ± 327
           LotAmount <LotAmt> [0..1] ± 327
           LotQuantity <LotQty> [0..1] ± 328
           CashSubBalanceType <CshSubBalTp> [0..1] ± 328
       CashSubBalanceIdentification <CshSubBalId> [0..1] ± 328
       Priority <Prty> [0..1] ± 328
       InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 329
Constraints
• CashAccountOwnerRule
CashAccountOwner must be present or Cancellation(*)/AccountOwner must be present, but not
both.
• CashAccountRule
CashAccount must be present or Cancellation(*)/CashAccount must be present, but not both.
• CashAccountServicerRule
CashAccountServicer must be present or Cancellation(*)/AccountOwner must be present, but not
both.
• ProcessingStatusRule
ProcessingStatus must be present or Cancellation(*)/ProcessingStatus must be present, but not
both.
14.4.4.1.1  CashAccount <CshAcct>
Presence: [0..1]
Definition: Account to or from which a cash entry is made.
Impacted by: C17 "IdentificationOrProxyPresenceRule", C16 "IdentificationAndProxyGuideline"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
314 March 2024
```

