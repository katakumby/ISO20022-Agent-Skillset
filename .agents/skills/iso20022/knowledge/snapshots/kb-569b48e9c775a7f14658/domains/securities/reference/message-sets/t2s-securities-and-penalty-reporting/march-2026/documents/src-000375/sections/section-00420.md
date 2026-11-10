---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.56 Registration2Code"]
file_pages: [527]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.56 Registration2Code

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 527 to 527.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 527

```text
7.2.2.56  Registration2Code
Definition: Specifies whether registration should occur upon receipt.
Type: CodeSet
CodeName Name Definition
PTYH PartyHold You or your party set the instruction in a
hold/frozen/preadvice mode.
CSDH CSDHold Central securities depository sets the
instruction in a hold/frozen/preadvice
mode.
CDEL ConditionalDelivery Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditional
delivery rules in the market infrastructure
platform for conditional delivery.
CVAL CSDValidation Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditions of
a restriction processing type in the
market infrastructure platform.
7.2.2.57  RepairReason4Code
Definition: Specifies the reason why the settlement instruction has a repair status.
Type: CodeSet
CodeName Name Definition
BATC ProcessingBatch Unrecognised or invalid processing
batch, that is, daytime/real-time while
only possible to settle in overnight batch.
CAEV CorporateAction Corporate action pending on the
financial instrument instructed.
CASH CashAccount Unrecognised or invalid cash account.
CASY ImpossibleCashSettlementSystem Impossible standing arrangements
override instruction for the cash
settlement system.
DDAT SettlementDate Unrecognised or invalid settlement date.
DDEA DealPrice Unrecognised or invalid deal price.
DMON SettlementAmount Unrecognised or invalid settlement
amount.
DQUA Quantity Unrecognised or invalid settlement
quantity.
DSEC Security Unrecognised or invalid financial
instrument identification.
DTRD TradeDate Unrecognised or invalid trade date.
IIND CommonReference Unrecognised, invalid or missing
common reference.
MINO MinimumSettlementQuantity Quantity instructed is lower than the
minimum existing settlement quantity for
the financial instrument.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 527 March 2026
```

