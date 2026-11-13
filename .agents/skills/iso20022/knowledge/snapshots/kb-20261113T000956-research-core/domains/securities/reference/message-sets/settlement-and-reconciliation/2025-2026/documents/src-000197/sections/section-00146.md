---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.1 MessageDefinition Functionality"]
file_pages: [198, 199]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
---

# 8.1 MessageDefinition Functionality

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 198 to 199.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 198

```text
8 semt.017.001.14
SecuritiesTransactionPostingReportV14
8.1 MessageDefinition Functionality
Scope
SecuritiesTransactionPostingReport is sent by an account servicer to an account owner to provide the
details of increases and decreases of holdings which occurred during a specified period, for all or
selected securities in the specified safekeeping account or sub-safekeeping account which the account
servicer holds for the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of its
participants
- an agent (sub-custodian) acting on behalf of its global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
This message may be used as a trade date based or a settlement date based statement.
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesTransactionPostingReportV14 MessageDefinition is composed of 8
MessageBuildingBlocks:
A. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
B. StatementGeneralDetails
Provides general information to the report.
C. AccountOwner
Party that legally owns the account.
D. SafekeepingAccount
Account to or from which a securities entry is made.
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 198 March 2026
```

## File page 199

```text
E. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
F. IntermediaryInformation
Information about the party that provides services relating to financial products to investors, for
example, advice on products and placement of orders for the investment fund.
G. FinancialInstrumentDetails
Reporting per financial instrument.
H. SubAccountDetails
Details at sub-account level.
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 199 March 2026
```

