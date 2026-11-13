---
template: false
document_kind: "participant"
review_status: "needs-review"
curated: true
domain: "securities"
participant_id: "participant-narrative-src-000096-investor"
title: "Investor — Investment Funds narrative scope"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
source_labels: ["investor", "investors"]
aliases: []
role_type: "business role or institutional example in quoted Functionality context"
message_sets: ["investment-funds"]
message_ids: ["acmt.001.001.08", "acmt.002.001.08", "acmt.003.001.08", "acmt.005.001.06", "acmt.006.001.07", "reda.004.001.07", "reda.005.001.03", "semt.001.001.03", "sese.012.001.12", "sese.019.001.09", "setr.013.001.05"]
message_families: ["acmt.001", "acmt.002", "acmt.003", "acmt.005", "acmt.006", "reda.004", "reda.005", "semt.001", "sese.012", "sese.019", "setr.013"]
flows: []
source_locations: [{"source_id": "src-000096", "heading": "2 acmt.001.001.08 AccountOpeningInstructionV08", "file_pages": [20], "evidence_id": "src-000096-acmt.001.001.08-p20-c001"}, {"source_id": "src-000096", "heading": "3 acmt.002.001.08 AccountDetailsConfirmationV08", "file_pages": [38], "evidence_id": "src-000096-acmt.002.001.08-p38-c001"}, {"source_id": "src-000096", "heading": "4 acmt.003.001.08 AccountModificationInstructionV08", "file_pages": [57], "evidence_id": "src-000096-acmt.003.001.08-p57-c001"}, {"source_id": "src-000096", "heading": "5 acmt.005.001.06 RequestForAccountManagementStatusReportV06", "file_pages": [77], "evidence_id": "src-000096-acmt.005.001.06-p77-c001"}, {"source_id": "src-000096", "heading": "6 acmt.006.001.07 AccountManagementStatusReportV07", "file_pages": [86], "evidence_id": "src-000096-acmt.006.001.07-p86-c001"}, {"source_id": "src-000096", "heading": "15 reda.004.001.07 FundReferenceDataReportV07", "file_pages": [291], "evidence_id": "src-000096-reda.004.001.07-p291-c001"}, {"source_id": "src-000096", "heading": "15 reda.004.001.07 FundReferenceDataReportV07", "file_pages": [291], "evidence_id": "src-000096-reda.004.001.07-p291-c005"}, {"source_id": "src-000096", "heading": "16 reda.005.001.03 InvestmentFundReportRequestV03", "file_pages": [365], "evidence_id": "src-000096-reda.005.001.03-p365-c001"}, {"source_id": "src-000096", "heading": "17 semt.001.001.03 SecuritiesMessageRejectionV03", "file_pages": [371], "evidence_id": "src-000096-semt.001.001.03-p371-c001"}, {"source_id": "src-000096", "heading": "35 sese.012.001.12 PortfolioTransferInstructionV12", "file_pages": [943], "evidence_id": "src-000096-sese.012.001.12-p943-c001"}, {"source_id": "src-000096", "heading": "35 sese.012.001.12 PortfolioTransferInstructionV12", "file_pages": [943], "evidence_id": "src-000096-sese.012.001.12-p943-c003"}, {"source_id": "src-000096", "heading": "39 sese.019.001.09 AccountHoldingInformationRequestV09", "file_pages": [1442], "evidence_id": "src-000096-sese.019.001.09-p1442-c001"}, {"source_id": "src-000096", "heading": "53 setr.013.001.05 SwitchOrderV05", "file_pages": [3487], "evidence_id": "src-000096-setr.013.001.05-p3487-c006"}, {"source_id": "src-000096", "heading": "53 setr.013.001.05 SwitchOrderV05", "file_pages": [3487], "evidence_id": "src-000096-setr.013.001.05-p3487-c008"}]
search_terms: ["investor", "investors"]
limitations: ["This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.", "Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.", "Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.", "No identifier scheme, alias equivalence or flow applicability is inferred from the participant name."]
---

# Investor — Investment Funds

## Definition and applicable context

This source names **investor** in the Functionality of the messages listed below. The record is scoped to Investment Funds, May 2026. Classification: business role or institutional example in quoted Functionality context. A functional role is not equated with an institution; an institutional example is not made an alias of the function it may perform.

The first explicit source context is:

> The AccountOpeningInstruction message is sent by an account owner, for example, an investor or its designated agent to the account servicer, for example, a registrar, transfer agent, custodian or securities depository, to instruct the opening of an account or the opening of an account and the establishment of an investment plan.

src-000096, file p20, 2 acmt.001.001.08 AccountOpeningInstructionV08, scope. The complete evidence register below retains every matched occurrence. A formal definition beyond those clauses remains unestablished.

## Responsibilities, actions and relationships

The following relationships are literal clause extractions. **Message applicability** distinguishes the current message from a related message or unresolved anaphoric reference. These relationships do not transfer an institutional example to the functional sender role. Full conditions and qualifications remain in the evidence quotes.

No complete directed clause was assigned to this exact role label; the narrative evidence still establishes its stated context.

## Complete source evidence

<a id="src-000096-acmt.001.001.08-p20-c001"></a>

### src-000096-acmt.001.001.08-p20-c001

src-000096; file p20; 2 acmt.001.001.08 AccountOpeningInstructionV08; scope.

> The AccountOpeningInstruction message is sent by an account owner, for example, an investor or its designated agent to the account servicer, for example, a registrar, transfer agent, custodian or securities depository, to instruct the opening of an account or the opening of an account and the establishment of an investment plan.

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

<a id="src-000096-reda.004.001.07-p291-c001"></a>

### src-000096-reda.004.001.07-p291-c001

src-000096; file p291; 15 reda.004.001.07 FundReferenceDataReportV07; scope.

> The FundReferenceDataReport message is sent by a report provider, for example, a fund promoter, fund management company, transfer agent, or market data provider to the report recipient, for example, a professional investor, investment fund distributor, market data provider, regulator or other interested party, to provide the key reference data for financial instruments to facilitate trading.

<a id="src-000096-reda.004.001.07-p291-c005"></a>

### src-000096-reda.004.001.07-p291-c005

src-000096; file p291; 15 reda.004.001.07 FundReferenceDataReportV07; usage.

> in a request / response environment, with the InvestmentFundReportRequest, for example, initiated by report users (data vendors, professional investors, regulators or investment fund distributors) in enabling the user to control the flow and updates of information.

<a id="src-000096-reda.005.001.03-p365-c001"></a>

### src-000096-reda.005.001.03-p365-c001

src-000096; file p365; 16 reda.005.001.03 InvestmentFundReportRequestV03; scope.

> The InvestmentFundReportRequest message is sent by a report user, for example, a professional investor, investment fund distributor, market data provider, regulator or other interested party to the report provider, for example, a fund promoter, fund management company, transfer agent, or market data provider to request a report.

<a id="src-000096-semt.001.001.03-p371-c001"></a>

### src-000096-semt.001.001.03-p371-c001

src-000096; file p371; 17 semt.001.001.03 SecuritiesMessageRejectionV03; scope.

> An account servicer, for example, a registrar, transfer agent or custodian bank, sends the SecuritiesMessageRejection message to the account owner, for example, an investor or its authorised agent, to reject a previously received message on which action cannot be taken.

<a id="src-000096-sese.012.001.12-p943-c001"></a>

### src-000096-sese.012.001.12-p943-c001

src-000096; file p943; 35 sese.012.001.12 PortfolioTransferInstructionV12; scope.

> The PortfolioTransferInstruction message is sent by an instructing party, for example, a (new) plan manager (transferee), to the executing party, for example, a (old) plan manager (transferor), on behalf of the initiating party, for example, an investor (client), to instruct the transfer of financial instruments from the client's account at the old plan manager (transferor) to the clients account at the new plan manager (transferee).

<a id="src-000096-sese.012.001.12-p943-c003"></a>

### src-000096-sese.012.001.12-p943-c003

src-000096; file p943; 35 sese.012.001.12 PortfolioTransferInstructionV12; usage.

> The account may be owned by one or more individual investors or one or more corporate investors.

<a id="src-000096-sese.019.001.09-p1442-c001"></a>

### src-000096-sese.019.001.09-p1442-c001

src-000096; file p1442; 39 sese.019.001.09 AccountHoldingInformationRequestV09; scope.

> The AccountHoldingInformationRequest message is sent by an instructing party, for example, a (new) plan manager (transferee), to the executing party, for example, a (old) plan manager (transferor), on behalf of the initiating party, for example, an investor (client), to request information about financial instruments held on behalf of the client.

<a id="src-000096-setr.013.001.05-p3487-c006"></a>

### src-000096-setr.013.001.05-p3487-c006

src-000096; file p3487; 53 setr.013.001.05 SwitchOrderV05; usage.

> The message caters for switch transactions that result in an additional cash payment from the investor or a transaction that results in a net payment to the investor.

<a id="src-000096-setr.013.001.05-p3487-c008"></a>

### src-000096-setr.013.001.05-p3487-c008

src-000096; file p3487; 53 setr.013.001.05 SwitchOrderV05; usage.

> This functionality is to be used by institutions that set up two accounts per investor, rather than one investment account.

## Applicable messages and flow navigation

| Exact message | Canonical evidence | Participant occurrence IDs |
| --- | --- | --- |
| acmt.001.001.08 | [Exact message-role evidence](../../../domains/securities/reference/messages/acmt.001.001.08/roles.md) | src-000096-acmt.001.001.08-p20-c001 |
| acmt.002.001.08 | [Exact message-role evidence](../../../domains/securities/reference/messages/acmt.002.001.08/roles.md) | src-000096-acmt.002.001.08-p38-c001 |
| acmt.003.001.08 | [Exact message-role evidence](../../../domains/securities/reference/messages/acmt.003.001.08/roles.md) | src-000096-acmt.003.001.08-p57-c001 |
| acmt.005.001.06 | [Exact message-role evidence](../../../domains/securities/reference/messages/acmt.005.001.06/roles.md) | src-000096-acmt.005.001.06-p77-c001 |
| acmt.006.001.07 | [Exact message-role evidence](../../../domains/securities/reference/messages/acmt.006.001.07/roles.md) | src-000096-acmt.006.001.07-p86-c001 |
| reda.004.001.07 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.004.001.07/roles.md) | src-000096-reda.004.001.07-p291-c001, src-000096-reda.004.001.07-p291-c005 |
| reda.005.001.03 | [Exact message-role evidence](../../../domains/securities/reference/messages/reda.005.001.03/roles.md) | src-000096-reda.005.001.03-p365-c001 |
| semt.001.001.03 | [Exact message-role evidence](../../../domains/securities/reference/messages/semt.001.001.03/roles.md) | src-000096-semt.001.001.03-p371-c001 |
| sese.012.001.12 | [Exact message-role evidence](../../../domains/securities/reference/messages/sese.012.001.12/roles.md) | src-000096-sese.012.001.12-p943-c001, src-000096-sese.012.001.12-p943-c003 |
| sese.019.001.09 | [Exact message-role evidence](../../../domains/securities/reference/messages/sese.019.001.09/roles.md) | src-000096-sese.019.001.09-p1442-c001 |
| setr.013.001.05 | [Exact message-role evidence](../../../domains/securities/reference/messages/setr.013.001.05/roles.md) | src-000096-setr.013.001.05-p3487-c006, src-000096-setr.013.001.05-p3487-c008 |


[Message-set flows](../../../domains/securities/reference/message-sets/investment-funds/2025-2026/flows/index.md) is contextual navigation. Matching a message or role label does not by itself assert participation in every flow; flow-specific responsibilities require their own evidence.

## Source labels, identifiers and limitations

Source spellings: `investor`, `investors`. Case and explicit singular/plural spelling variants are grouped only within this publication. No additional alias or identification scheme is asserted.

- This record preserves explicit narrative participation and actions; a standalone formal definition has not been established from these Functionality clauses. See issue-000021.
- Scope is this publication and its quoted message contexts. Same-name records in other publications are not merged or asserted equivalent.
- Examples, alternatives, conditions, related-message statements and negative requirements retain their full source wording. Mention alone does not establish a sender, receiver or initiator.
- No identifier scheme, alias equivalence or flow applicability is inferred from the participant name.

[src-000096](../../../evidence/omitted/fffd4ab68b421d059524ec38.md) · [Issue register](../../../tracking/issues.md) · [Participant catalog](../../../catalog/participants.md)
