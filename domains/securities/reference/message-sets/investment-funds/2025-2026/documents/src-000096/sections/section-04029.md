---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.161 PendingOpeningStatusReason1Code"]
file_pages: [5337, 5338]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.161 PendingOpeningStatusReason1Code

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5337 to 5338.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5337

```text
CodeName Name Definition
CUST Custodian Party that safekeeps and administers
assets on behalf of the owner.
INVS Investor Party, either an individual or
organisation, whose assets are being
invested.
66.2.2.161  PendingOpeningStatusReason1Code
Definition: Specifies the reason for a pending account opening status.
Type: CodeSet
CodeName Name Definition
ATHR Authorisation Authorisation is required.
ATHP AuthorisedButPending Authorisation is provided but account
opening is still pending.
FRDM FATCAReportingDateMissing FATCA reporting date is missing.
KYCM KnowYourCustomerDocumentMissing Know Your Customer (KYC) document is
missing.
NOTO NotOpened Account is not yet open, even for partial
use.
REST Restrictions Account will be opened when restrictions
are addressed.
RIGH RightsHolderMissing Rights holder information is missing.
66.2.2.162  PendingSettlementStatusReason2Code
Definition: Specifies the reason for a transfer or settlement instruction settlement pending status.
Type: CodeSet
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5337 May 2026
```

## File page 5338

```text
CodeName Name Definition
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5338 May 2026
```

