---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["21 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "21.4 Message Building Blocks", "21.4.4 ReportOrError <RptOrErr>", "21.4.4.1 Cancellations <Cxls>", "21.4.4.1.1 CashAccount <CshAcct>"]
file_pages: [505]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 21.4.4.1.1 CashAccount <CshAcct>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 505 to 505.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 505

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       BalanceTo <BalTo> [1..1]  517
         Type <Tp> [1..1]  517
{Or           Code <Cd> [1..1] CodeSet 517
Or}           Proprietary <Prtry> [1..1] ± 517
         QuantityBreakdown <QtyBrkdwn> [0..*]  518
           LotNumber <LotNb> [0..1] ± 518
           LotAmount <LotAmt> [0..1] ± 518
           LotQuantity <LotQty> [0..1] ± 519
           CashSubBalanceType <CshSubBalTp> [0..1] ± 519
       CashSubBalanceIdentification <CshSubBalId> [0..1] ± 519
       Priority <Prty> [0..1] ± 519
       InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 520
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
21.4.4.1.1  CashAccount <CshAcct>
Presence: [0..1]
Definition: Account to or from which a cash entry is made.
Impacted by: C17 "IdentificationOrProxyPresenceRule", C16 "IdentificationAndProxyGuideline"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 505 August 2026
```

