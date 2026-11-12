---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000096-account-servicer"
title: "Account Servicer — Investment Funds narrative scope"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
source_labels: ["account servicer"]
aliases: []
role_type: "functional participant role in quoted Functionality context"
message_sets: ["investment-funds"]
message_ids: ["acmt.001.001.08", "acmt.002.001.08", "acmt.003.001.08", "acmt.005.001.06", "acmt.006.001.07", "semt.001.001.03", "semt.002.001.02", "semt.003.001.02", "semt.004.001.02", "semt.005.001.02", "semt.006.001.02", "semt.007.001.02"]
message_families: ["acmt.001", "acmt.002", "acmt.003", "acmt.005", "acmt.006", "semt.001", "semt.002", "semt.003", "semt.004", "semt.005", "semt.006", "semt.007"]
flows: []
source_locations: [{"source_id": "src-000096", "heading": "2 acmt.001.001.08 AccountOpeningInstructionV08", "file_pages": [20], "evidence_id": "src-000096-acmt.001.001.08-p20-c001"}, {"source_id": "src-000096", "heading": "2 acmt.001.001.08 AccountOpeningInstructionV08", "file_pages": [20], "evidence_id": "src-000096-acmt.001.001.08-p20-c002"}, {"source_id": "src-000096", "heading": "3 acmt.002.001.08 AccountDetailsConfirmationV08", "file_pages": [38], "evidence_id": "src-000096-acmt.002.001.08-p38-c001"}, {"source_id": "src-000096", "heading": "4 acmt.003.001.08 AccountModificationInstructionV08", "file_pages": [57], "evidence_id": "src-000096-acmt.003.001.08-p57-c001"}, {"source_id": "src-000096", "heading": "5 acmt.005.001.06 RequestForAccountManagementStatusReportV06", "file_pages": [77], "evidence_id": "src-000096-acmt.005.001.06-p77-c001"}, {"source_id": "src-000096", "heading": "6 acmt.006.001.07 AccountManagementStatusReportV07", "file_pages": [86], "evidence_id": "src-000096-acmt.006.001.07-p86-c001"}, {"source_id": "src-000096", "heading": "17 semt.001.001.03 SecuritiesMessageRejectionV03", "file_pages": [371], "evidence_id": "src-000096-semt.001.001.03-p371-c001"}, {"source_id": "src-000096", "heading": "18 semt.002.001.02 CustodyStatementOfHoldingsV02", "file_pages": [375], "evidence_id": "src-000096-semt.002.001.02-p375-c001"}, {"source_id": "src-000096", "heading": "18 semt.002.001.02 CustodyStatementOfHoldingsV02", "file_pages": [375], "evidence_id": "src-000096-semt.002.001.02-p375-c002"}, {"source_id": "src-000096", "heading": "18 semt.002.001.02 CustodyStatementOfHoldingsV02", "file_pages": [375], "evidence_id": "src-000096-semt.002.001.02-p375-c003"}, {"source_id": "src-000096", "heading": "19 semt.003.001.02 AccountingStatementOfHoldingsV02", "file_pages": [387], "evidence_id": "src-000096-semt.003.001.02-p387-c001"}, {"source_id": "src-000096", "heading": "19 semt.003.001.02 AccountingStatementOfHoldingsV02", "file_pages": [387], "evidence_id": "src-000096-semt.003.001.02-p387-c003"}, {"source_id": "src-000096", "heading": "20 semt.004.001.02 CustodyStatementOfHoldingsCancellationV02", "file_pages": [398], "evidence_id": "src-000096-semt.004.001.02-p398-c001"}, {"source_id": "src-000096", "heading": "21 semt.005.001.02 AccountingStatementOfHoldingsCancellationV02", "file_pages": [403], "evidence_id": "src-000096-semt.005.001.02-p403-c001"}, {"source_id": "src-000096", "heading": "22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02", "file_pages": [408], "evidence_id": "src-000096-semt.006.001.02-p408-c001"}, {"source_id": "src-000096", "heading": "22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02", "file_pages": [408], "evidence_id": "src-000096-semt.006.001.02-p408-c002"}, {"source_id": "src-000096", "heading": "23 semt.007.001.02 StatementOfInvestmentFundTransactionsCancellationV02", "file_pages": [427], "evidence_id": "src-000096-semt.007.001.02-p427-c001"}]
search_terms: ["account servicer"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Account Servicer — Investment Funds

## Definition and applicable context

This source names **account servicer** in the Functionality of the messages listed below. The record is scoped to Investment Funds, May 2026. Classification: functional participant role in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The AccountOpeningInstruction message is sent by an account owner, for example, an investor or its designated agent to the account servicer, for example, a registrar, transfer agent, custodian or securities depository, to instruct the opening of an account or the opening of an account and the establishment of an investment plan.

src-000096, file p20, 2 acmt.001.001.08 AccountOpeningInstructionV08, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

| This participant in clause | Source message subject | Message applicability | Other roles / source expressions | Evidence |
| --- | --- | --- | --- | --- |
| receiver | The AccountOpeningInstruction message | current-message | sender: an account owner, for example, an investor or its designated agent ([an account owner](participant-narrative-src-000096-account-owner.md)); receiver: the account servicer, for example, a registrar, transfer agent, custodian or securities depository ([the account servicer](participant-narrative-src-000096-account-servicer.md)) | [src-000096-acmt.001.001.08-p20-c001-d1](#src-000096-acmt.001.001.08-p20-c001); file p20 |
| sender | The AccountDetailsConfirmation message | current-message | sender: an account servicer, for example, a registrar, transfer agent, custodian bank or securities depository ([an account servicer](participant-narrative-src-000096-account-servicer.md)); receiver: the account owner, for example, an investor ([the account owner](participant-narrative-src-000096-account-owner.md)) | [src-000096-acmt.002.001.08-p38-c001-d1](#src-000096-acmt.002.001.08-p38-c001); file p38 |
| receiver | The AccountModificationInstruction message | current-message | sender: an account owner, for example, an investor or its designated agent ([an account owner](participant-narrative-src-000096-account-owner.md)); receiver: the account servicer, for example, a registrar, transfer agent, custodian bank or securities depository ([the account servicer](participant-narrative-src-000096-account-servicer.md)) | [src-000096-acmt.003.001.08-p57-c001-d1](#src-000096-acmt.003.001.08-p57-c001); file p57 |
| receiver | The RequestForAccountManagementStatusReport message | current-message | sender: an account owner, for example, an investor or its designated agent ([an account owner](participant-narrative-src-000096-account-owner.md)); receiver: the account servicer, for example, a registrar, transfer agent, custodian bank or securities depository ([the account servicer](participant-narrative-src-000096-account-servicer.md)) | [src-000096-acmt.005.001.06-p77-c001-d1](#src-000096-acmt.005.001.06-p77-c001); file p77 |
| sender | The AccountManagementStatusReport message | current-message | sender: an account servicer, for example, a registrar, transfer agent, custodian bank or securities depository ([an account servicer](participant-narrative-src-000096-account-servicer.md)); receiver: the account owner or its designated agent, for example, an investor ([the account owner](participant-narrative-src-000096-account-owner.md); [its designated agent](participant-narrative-src-000096-designated-agent.md)) | [src-000096-acmt.006.001.07-p86-c001-d1](#src-000096-acmt.006.001.07-p86-c001); file p86 |
| sender | the SecuritiesMessageRejection message | current-message | sender: An account servicer, for example, a registrar, transfer agent or custodian bank ([An account servicer](participant-narrative-src-000096-account-servicer.md)); receiver: the account owner, for example, an investor or its authorised agent ([the account owner](participant-narrative-src-000096-account-owner.md)) | [src-000096-semt.001.001.03-p371-c001-d1](#src-000096-semt.001.001.03-p371-c001); file p371 |
| sender | the CustodyStatementOfHoldings message | current-message | sender: An account servicer, for example, a transfer agent ([An account servicer](participant-narrative-src-000096-account-servicer.md)); receiver: the account owner, for example, a fund manager or an account owner's designated agent ([the account owner](participant-narrative-src-000096-account-owner.md)) | [src-000096-semt.002.001.02-p375-c001-d1](#src-000096-semt.002.001.02-p375-c001); file p375 |
| sender | the AccountStatementOfHoldings message | current-message-scope-name-variant | sender: An account servicer, for example, a transfer agent ([An account servicer](participant-narrative-src-000096-account-servicer.md)); receiver: the account owner, for example, a fund manager or an account owner's designated agent ([the account owner](participant-narrative-src-000096-account-owner.md)) | [src-000096-semt.003.001.02-p387-c001-d1](#src-000096-semt.003.001.02-p387-c001); file p387 |
| sender | the CustodyStatementOfHoldingsCancellation message | current-message | sender: An account servicer, for example, a transfer agent ([An account servicer](participant-narrative-src-000096-account-servicer.md)); receiver: the account owner, for example, an investment manager or its authorised representative ([the account owner](participant-narrative-src-000096-account-owner.md)) | [src-000096-semt.004.001.02-p398-c001-d1](#src-000096-semt.004.001.02-p398-c001); file p398 |
| sender | the AccountingStatementofHoldingsCancellation message | current-message | sender: An account servicer, for example, a transfer agent ([An account servicer](participant-narrative-src-000096-account-servicer.md)); receiver: the account owner, for example, a fund manager or an account owner's designated agent ([the account owner](participant-narrative-src-000096-account-owner.md)) | [src-000096-semt.005.001.02-p403-c001-d1](#src-000096-semt.005.001.02-p403-c001); file p403 |
| sender | the StatementOfInvestmentFundTransactions message | current-message | sender: An account servicer, for example, a transfer agent ([An account servicer](participant-narrative-src-000096-account-servicer.md)); receiver: the account owner, for example, an investment manager or its authorised representative ([the account owner](participant-narrative-src-000096-account-owner.md)) | [src-000096-semt.006.001.02-p408-c001-d1](#src-000096-semt.006.001.02-p408-c001); file p408 |
| sender | the StatementOfInvestmentFundTransactionsCancellation message | current-message | sender: An account servicer, for example, a transfer agent ([An account servicer](participant-narrative-src-000096-account-servicer.md)); receiver: the account owner, for example, an investment manager or its authorised representative ([the account owner](participant-narrative-src-000096-account-owner.md)) | [src-000096-semt.007.001.02-p427-c001-d1](#src-000096-semt.007.001.02-p427-c001); file p427 |


Literal action verbs: holds. Their objects, conditions and message context are preserved in the quoted evidence, rather than inferred from the verb alone.

## Complete source evidence

<a id="src-000096-acmt.001.001.08-p20-c001"></a>

### src-000096-acmt.001.001.08-p20-c001

src-000096; file p20; 2 acmt.001.001.08 AccountOpeningInstructionV08; scope.

> The AccountOpeningInstruction message is sent by an account owner, for example, an investor or its designated agent to the account servicer, for example, a registrar, transfer agent, custodian or securities depository, to instruct the opening of an account or the opening of an account and the establishment of an investment plan.

<a id="src-000096-acmt.001.001.08-p20-c002"></a>

### src-000096-acmt.001.001.08-p20-c002

src-000096; file p20; 2 acmt.001.001.08 AccountOpeningInstructionV08; usage.

> The AccountOpeningInstruction is used to open an account directly or indirectly with the account servicer or an intermediary.

<a id="src-000096-acmt.002.001.08-p38-c001"></a>

### src-000096-acmt.002.001.08-p38-c001

src-000096; file p38; 3 acmt.002.001.08 AccountDetailsConfirmationV08; scope.

> The AccountDetailsConfirmation message is sent by an account servicer, for example, a registrar, transfer agent, custodian bank or securities depository to the account owner, for example, an investor to confirm the opening of an account, execution of an AccountModificationInstruction or to return information requested in a GetAccountDetails message.

<a id="src-000096-acmt.003.001.08-p57-c001"></a>

### src-000096-acmt.003.001.08-p57-c001

src-000096; file p57; 4 acmt.003.001.08 AccountModificationInstructionV08; scope.

> The AccountModificationInstruction message is sent by an account owner, for example, an investor or its designated agent to the account servicer, for example, a registrar, transfer agent, custodian bank or securities depository to modify, that is, create, update or delete specific details of an existing account.

<a id="src-000096-acmt.005.001.06-p77-c001"></a>

### src-000096-acmt.005.001.06-p77-c001

src-000096; file p77; 5 acmt.005.001.06 RequestForAccountManagementStatusReportV06; scope.

> The RequestForAccountManagementStatusReport message is sent by an account owner, for example, an investor or its designated agent, to the account servicer, for example, a registrar, transfer agent, custodian bank or securities depository to request the status of an AccountOpeningInstruction, GetAccountDetails or an AccountModificationInstruction.

<a id="src-000096-acmt.006.001.07-p86-c001"></a>

### src-000096-acmt.006.001.07-p86-c001

src-000096; file p86; 6 acmt.006.001.07 AccountManagementStatusReportV07; scope.

> The AccountManagementStatusReport message is sent by an account servicer, for example, a registrar, transfer agent, custodian bank or securities depository to the account owner or its designated agent, for example, an investor to report on the receipt or the processing status of a previously received account management message.

<a id="src-000096-semt.001.001.03-p371-c001"></a>

### src-000096-semt.001.001.03-p371-c001

src-000096; file p371; 17 semt.001.001.03 SecuritiesMessageRejectionV03; scope.

> An account servicer, for example, a registrar, transfer agent or custodian bank, sends the SecuritiesMessageRejection message to the account owner, for example, an investor or its authorised agent, to reject a previously received message on which action cannot be taken.

<a id="src-000096-semt.002.001.02-p375-c001"></a>

### src-000096-semt.002.001.02-p375-c001

src-000096; file p375; 18 semt.002.001.02 CustodyStatementOfHoldingsV02; scope.

> An account servicer, for example, a transfer agent sends the CustodyStatementOfHoldings message to the account owner, for example, a fund manager or an account owner's designated agent to provide detailed holdings of the portfolio at a specified moment in time.

<a id="src-000096-semt.002.001.02-p375-c002"></a>

### src-000096-semt.002.001.02-p375-c002

src-000096; file p375; 18 semt.002.001.02 CustodyStatementOfHoldingsV02; scope.

> The message provides, at a moment in time, the quantity and identification of the financial instruments that the account servicer holds for the account owner.

<a id="src-000096-semt.002.001.02-p375-c003"></a>

### src-000096-semt.002.001.02-p375-c003

src-000096; file p375; 18 semt.002.001.02 CustodyStatementOfHoldingsV02; usage.

> The message should be sent at a frequency agreed bi-laterally between the account servicer and the account owner.

<a id="src-000096-semt.003.001.02-p387-c001"></a>

### src-000096-semt.003.001.02-p387-c001

src-000096; file p387; 19 semt.003.001.02 AccountingStatementOfHoldingsV02; scope.

> An account servicer, for example, a transfer agent sends the AccountStatementOfHoldings message to the account owner, for example, a fund manager or an account owner's designated agent to provide detailed holdings of the portfolio at a specified moment in time.

<a id="src-000096-semt.003.001.02-p387-c003"></a>

### src-000096-semt.003.001.02-p387-c003

src-000096; file p387; 19 semt.003.001.02 AccountingStatementOfHoldingsV02; usage.

> The message should be sent at a frequency agreed bi-laterally between the account servicer and the account owner.

<a id="src-000096-semt.004.001.02-p398-c001"></a>

### src-000096-semt.004.001.02-p398-c001

src-000096; file p398; 20 semt.004.001.02 CustodyStatementOfHoldingsCancellationV02; scope.

> An account servicer, for example, a transfer agent, sends the CustodyStatementOfHoldingsCancellation message to the account owner, for example, an investment manager or its authorised representative to cancel a previously sent CustodyStatementOfHoldings message.

<a id="src-000096-semt.005.001.02-p403-c001"></a>

### src-000096-semt.005.001.02-p403-c001

src-000096; file p403; 21 semt.005.001.02 AccountingStatementOfHoldingsCancellationV02; scope.

> An account servicer, for example, a transfer agent, sends the AccountingStatementofHoldingsCancellation message to the account owner, for example, a fund manager or an account owner's designated agent, to notify the cancellation of a previously sent AccountingStatementOfHoldings message.

<a id="src-000096-semt.006.001.02-p408-c001"></a>

### src-000096-semt.006.001.02-p408-c001

src-000096; file p408; 22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02; scope.

> An account servicer, for example, a transfer agent sends the StatementOfInvestmentFundTransactions message to the account owner, for example, an investment manager or its authorised representative to provide detailed transactions (increases and decreases) of holdings which occurred during a specified period of time.

<a id="src-000096-semt.006.001.02-p408-c002"></a>

### src-000096-semt.006.001.02-p408-c002

src-000096; file p408; 22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02; usage.

> This message should be used at a frequency agreed bi-laterally between the account servicer and the account owner.

<a id="src-000096-semt.007.001.02-p427-c001"></a>

### src-000096-semt.007.001.02-p427-c001

src-000096; file p427; 23 semt.007.001.02 StatementOfInvestmentFundTransactionsCancellationV02; scope.

> An account servicer, for example, a transfer agent sends the StatementOfInvestmentFundTransactionsCancellation message to the account owner, for example, an investment manager or its authorised representative to cancel a previously sent StatementOfInvestmentFundTransactions message.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| acmt.001.001.08 | [Exact message-role evidence](../../../domains/securities/reference/messages/acmt.001.001.08/roles.md) | src-000096-acmt.001.001.08-p20-c001, src-000096-acmt.001.001.08-p20-c002 |
| acmt.002.001.08 | [Exact message-role evidence](../../../domains/securities/reference/messages/acmt.002.001.08/roles.md) | src-000096-acmt.002.001.08-p38-c001 |
| acmt.003.001.08 | [Exact message-role evidence](../../../domains/securities/reference/messages/acmt.003.001.08/roles.md) | src-000096-acmt.003.001.08-p57-c001 |
| acmt.005.001.06 | [Exact message-role evidence](../../../domains/securities/reference/messages/acmt.005.001.06/roles.md) | src-000096-acmt.005.001.06-p77-c001 |
| acmt.006.001.07 | [Exact message-role evidence](../../../domains/securities/reference/messages/acmt.006.001.07/roles.md) | src-000096-acmt.006.001.07-p86-c001 |
| semt.001.001.03 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.001.001.03/roles.md) | src-000096-semt.001.001.03-p371-c001 |
| semt.002.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.002.001.02/roles.md) | src-000096-semt.002.001.02-p375-c001, src-000096-semt.002.001.02-p375-c002, src-000096-semt.002.001.02-p375-c003 |
| semt.003.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.003.001.02/roles.md) | src-000096-semt.003.001.02-p387-c001, src-000096-semt.003.001.02-p387-c003 |
| semt.004.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.004.001.02/roles.md) | src-000096-semt.004.001.02-p398-c001 |
| semt.005.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.005.001.02/roles.md) | src-000096-semt.005.001.02-p403-c001 |
| semt.006.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.006.001.02/roles.md) | src-000096-semt.006.001.02-p408-c001, src-000096-semt.006.001.02-p408-c002 |
| semt.007.001.02 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.007.001.02/roles.md) | src-000096-semt.007.001.02-p427-c001 |


[Message-set flows](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `account servicer`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000096](../../../evidence/omitted/fffd4ab68b421d059524ec38.md) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
