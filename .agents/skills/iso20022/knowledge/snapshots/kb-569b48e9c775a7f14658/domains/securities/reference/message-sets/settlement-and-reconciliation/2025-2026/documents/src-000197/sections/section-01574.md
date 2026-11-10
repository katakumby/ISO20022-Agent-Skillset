---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.74 PendingProcessingReason7Code"]
file_pages: [2093]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.74 PendingProcessingReason7Code

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2093 to 2093.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2093

```text
CodeName Name Definition
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
OTHR Other Other. See Narrative.
LALO SecuritiesLoanedOut Financial instruments are out on loan.
COLL SecuritiesPledgedAsCollateral Financial instruments are not deliverable
as they are pledged as collateral.
DENO UnavailableDeliverableDenominatedQuantity Quantity instructed does not match the
denomination available/deliverable.
Physical securities need to be obtained
in deliverable denominated quantities.
CERT WrongCertificatesNumbers Certificate number error.
35.2.2.74  PendingProcessingReason7Code
Definition: Specifies the reason the transaction/instruction is failing settlement. Settlement on the
instructed settlement date is no longer possible.
Type: CodeSet
CodeName Name Definition
BLOC AccountBlocked Your account is blocked, no instruction
can settle over the account.
ADEA AccountServicerDeadlineMissed Instruction was received after the
account servicer's deadline. It will be
managed as per the bilateral service
agreement between the account servicer
and account owner.
DOCY AwaitingDocumentsOrEndorsementsFromYou Awaiting documents or endorsements
from you.
CAIS AwaitingSecurities Awaiting financial instruments from a
corporate action or other procedure, for
example, conversion, dematerialisation,
exchange, registration, stamping,
splitting.
YCOL CollateralShortage Insufficient collateral in your account to
execute the instruction.
CDEL ConditionalDelivery Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditional
delivery rules in the market infrastructure
platform for conditional delivery.
CDAC ConditionalDeliveryAwaitingCancellation Awaiting cancellation of one of the party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2093 March 2026
```

