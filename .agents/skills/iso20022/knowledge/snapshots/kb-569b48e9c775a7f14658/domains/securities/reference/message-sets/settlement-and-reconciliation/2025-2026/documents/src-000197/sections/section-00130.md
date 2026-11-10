---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10"]
file_pages: [178, 179]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.016.001.10"]
---

# 7 semt.016.001.10 IntraPositionMovementPostingReportV10

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 178 to 179.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 178

```text
7 semt.016.001.10
IntraPositionMovementPostingReportV10
7.1 MessageDefinition Functionality
Scope
The IntraPositionMovementPostingReport is sent by an account servicer to an account owner to
provide the details of increases and decreases in securities with a given status within a holding, that is,
intra-position transfers, which occurred during a specified period, for all or selected securities in a
specified safekeeping account which the account servicer holds for the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of its
participant
- an agent (sub-custodian) acting on behalf of its global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
:
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information
using the relevant elements in the Business Application Header.
Outline
The IntraPositionMovementPostingReportV10 MessageDefinition is composed of 6
MessageBuildingBlocks:
A. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
B. StatementGeneralDetails
General information related to the report.
C. AccountOwner
Party that legally owns the account.
Approved by the Securities SEG on 27 January 2026 semt.016.001.10
IntraPositionMovementPostingReportV10
Settlement And Reconciliation - Maintenance 2025 - 2026 178 March 2026
```

## File page 179

```text
D. SafekeepingAccount
Account to or from which a securities entry is made.
E. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
F. FinancialInstrument
Reporting per financial instrument.
Approved by the Securities SEG on 27 January 2026 semt.016.001.10
IntraPositionMovementPostingReportV10
Settlement And Reconciliation - Maintenance 2025 - 2026 179 March 2026
```

