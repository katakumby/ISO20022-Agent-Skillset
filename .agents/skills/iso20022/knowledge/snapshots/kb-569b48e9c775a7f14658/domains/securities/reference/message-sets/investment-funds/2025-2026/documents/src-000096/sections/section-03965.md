---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.50 Transfer Status", "66.1.50.6 PendingSettlementStatus3Choice", "66.1.50.6.1 Reason <Rsn>"]
file_pages: [5262, 5263]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.50.6.1 Reason <Rsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5262 to 5263.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5262

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..1] CodeSet 5262
Or   ExtendedReason <XtndedRsn> [1..1] Text 5264
Or   DataSourceScheme <DataSrcSchme> [1..1] ± 5264
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5264
66.1.50.6.1  Reason <Rsn>
Presence: [1..1]
Definition: Reason for the settlement pending status.
Datatype: "PendingSettlementStatusReason2Code" on page 5337
CodeName Name Definition
AWSH AwaitingSharesFromCounterparty Securities have not yet been received
from the counterparty.
BLOC AccountBlocked Your account is blocked, no instruction
can settle over the account.
CAIS AwaitingSecurities Awaiting securities from corporate action
issue or other procedures, for example,
conversion, dematerialisation, exchange,
registration, stamping, splitting, etc.
CLAC CounterpartyInsufficientSecurities Insufficient deliverable securities in the
counterparty's account, or counterparty
does not hold the securities.
DOCC AwaitingDocumentsOrEndorsementsFromCoun
terparty
Awaiting documents or endorsements
from the counterparty.
DOCY AwaitingDocumentsOrEndorsementsFromYou Awaiting documents or endorsements
from you.
IAAD StatusReasonInvestigation Pending reason is being investigated.
LACK LackOfSecurities Insufficient deliverable securities in your
account.
LINK PendingLinkedInstruction Your instruction is pending settlement
because the instruction linked to it is
pending.
PHCK PhysicalSecuritiesVerification Physical shares have been received and
are being checked for authenticity.
PHSE PhysicalDeliveryDelay Settlement is physical and securities are
being delivered.
SBLO SecuritiesBlocked Settlement is pending. The securities are
blocked due to, for example, a corporate
action event, re-alignment.
MINF MissingInformation Information, for example, telephone
number, contact person, is missing.
ACOP AccountNotOpen Account must already be opened in
order to process the transfer.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5262 May 2026
```

## File page 5263

```text
CodeName Name Definition
IINV UnderInvestigation Intermediary is investigating the reason
why the transfer is pending.
CINV UnderClientInvestigation Client has been informed of a problem
and is investigating.
AINV UnderTransferAgentInvestigation Transfer agent is investigating.
WTRF AwaitingTransferAgentStatus Transfer is being processed by the
transfer agent, awaiting status from
transfer agent.
USUA UsualTransactionTime Usual transfer agent's processing
timeframe.
ASTA AwaitingStatus At your request, the Intermediary is
checking the status of your instruction
with the transfer agent.
AFST ApplicationFormSent Application form has been sent to the
transfer agent.
STST StockTransferFormSent Stock transfer form has been sent to the
counterparty to sign and forward to the
transfer agent.
LPRO LongerProcessing Longer processing timeframe for this
type of transfer, due to documentation
requirements.
ADRQ AdditionalDocumentsRequested Additional documents have been
requested by the transfer agent.
ADS1 AdditionalDocumentsSent1 Additional documents have been sent.
ADS2 AdditionalDocumentsSent2 Upon request of the transfer agent, the
intermediary has sent additional
documents. The transfer agent has
confirmed that all the necessary
information is now in place.
DRJC DocumentsRejected Documents are rejected by the transfer
agent.
CYIN AwaitingCounterpartyReceipt Counterparty has not sent an instruction
to receive. Check with counterparty.
CYDV AwaitingCounterpartyDelivery Counterparty has not sent an instruction
to deliver or delivered the shares. Check
with counterparty.
OVER NormalProcessingPeriodLapsed Normal processing period for the
instruction has lapsed. The transfer
agent has been or will be contacted.
WCPA WrongCounterpartyAccount Wrong counterparty account details.
SDUT LackOfStampDutyInformation Instruction is pending as stamp duty
information is missing.
TAPR TransferAgentProcessing Transfer is being processed by transfer
agent.
XCNF ExpectedConfirmation Confirmation is expected from transfer
agent.
ESCA Escalation Special follow-up is taking place.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5263 May 2026
```

