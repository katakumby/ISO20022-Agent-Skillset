---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12"]
file_pages: [19, 20]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2 semt.002.001.12 SecuritiesBalanceCustodyReportV12

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 19 to 20.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 19

```text
2 semt.002.001.12
SecuritiesBalanceCustodyReportV12
2.1 MessageDefinition Functionality
Scope
An account servicer sends a SecuritiesBalanceCustodyReport to an account owner to provide, at a
moment in time, the quantity and identification of the financial instruments that the account servicer
holds for the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of their
participants, or
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer, or
- a transfer agent acting on behalf of a fund manager or an account owner's designated agent.
Usage
The message can also include availability and the location of holdings to facilitate trading and minimise
settlement issues. The message reports all information per financial instrument, that is, when a financial
instrument is held at multiple places of safekeeping, the total holdings for all locations can be provided.
The message should be sent at a frequency agreed bi-laterally between the account servicer and the
account owner. The message may be provided on a trade date, contractual or settlement date basis.
There may be one or more intermediary parties, for example, an intermediary or a concentrator
between the account owner and account servicer.
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesBalanceCustodyReportV12 MessageDefinition is composed of 10
MessageBuildingBlocks:
A. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 19 March 2026
```

## File page 20

```text
B. StatementGeneralDetails
Provides general information on the report.
C. AccountOwner
Party that legally owns the account.
D. AccountServicer
Party that manages the account on behalf of the account owner, that is manages the registration
and booking of entries on the account, calculates balances on the account and provides
information about the account.
E. SafekeepingAccount
Account to or from which a securities entry is made.
F. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
G. IntermediaryInformation
Information about the party that provides services relating to financial products to investors, for
example, advice on products and placement of orders for the investment fund.
H. BalanceForAccount
Net position of a segregated holding, in a single security, within the overall position held in a
securities account.
I. SubAccountDetails
Sub-account of the safekeeping or investment account.
J. AccountBaseCurrencyTotalAmounts
Total valuation amounts provided in the base currency of the account.
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 20 March 2026
```

