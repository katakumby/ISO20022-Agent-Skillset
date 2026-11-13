---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.75 PendingProcessingReason8Code"]
file_pages: [2094]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.75 PendingProcessingReason8Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2094 to 2094.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2094

```text
CodeName Name Definition
CDLR ConditionalDeliveryAwaitingRelease Instruction is in a hold/frozen/preadvice
mode. Market infrastructure platform is
awaiting release.
CSDH CSDHold Central securities depository sets the
instruction in a hold/frozen/preadvice
mode.
CVAL CSDValidation Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditions of
a restriction processing type in the
market infrastructure platform.
GLOB GlobalFormSecurities Settlement cannot be executed; financial
instruments are in global form.
INBC IncompleteNumberCount Not all the instructions part of a pool
have been received.
LIQU InsufficientCentralBankLiquidity Central bank liquidity is insufficient.
MONY InsufficientMoney Insufficient money in your account.
LACK LackOfSecurities Insufficient financial instruments in your
account.
FLIM MaximumForeignLimitReached Insufficient deliverable financial
instruments in your account as maximum
foreign limit has been reached.
MINO MinimumSettlementAmount Quantity instructed is lower than the
minimum existing settlement quantity for
the financial instrument.
MUNO MultipleSettlementAmount Quantity instructed is not a multiple of an
existing settlement quantity lot for the
financial instrument.
NEXT NextProcess Next process is launched. No processing
pending problems to be reported.
NOFX NoForeignExchangeInstruction A foreign exchange instruction from you
is missing.
LALO SecuritiesLoanedOut Financial instruments are out on loan.
COLL SecuritiesPledgedAsCollateral Financial instruments are not deliverable
as they are pledged as collateral.
OTHR Other Other. See Narrative.
CERT WrongCertificatesNumbers Certificate number error.
DENO UnavailableDeliverableDenominatedQuantity Quantity instructed does not match the
denomination available/deliverable.
Physical securities need to be obtained
in deliverable denominated quantities.
35.2.2.75  PendingProcessingReason8Code
Definition: Specifies the reason the transaction/instruction is failing settlement. Settlement on the
instructed settlement date is no longer possible.
Type: CodeSet
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2094 March 2026
```

