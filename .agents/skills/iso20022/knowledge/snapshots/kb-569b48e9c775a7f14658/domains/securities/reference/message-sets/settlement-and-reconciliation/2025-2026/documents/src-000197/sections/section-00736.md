---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["31 sese.037.001.09 PortfolioTransferNotificationV09"]
file_pages: [1094, 1095]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.037.001.09"]
---

# 31 sese.037.001.09 PortfolioTransferNotificationV09

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1094 to 1095.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1094

```text
31 sese.037.001.09
PortfolioTransferNotificationV09
31.1 MessageDefinition Functionality
Scope
The PortfolioTransferNotification is sent by an account servicer to another account servicer to exchange
transfer settlement details information during a retail or institutional client portfolio transfer.
The account servicer will typically be local agent or global custodian acting on behalf of an investment
management institution, a broker/dealer or a retail client.
Usage
The exchange of transfer settlement details is the provision, by the delivering account servicer to the
receiving account servicer, of the settlement data (such as trade date, settlement date, delivering
settlement chain, quantities) of the individual transfers that will take place during a full or partial portfolio
transfer. This delivering account servicer message may also include, for validation, the receiving
settlement chain as provided by the client. In case the receiving settlement chain is not available to the
delivering account servicer, the receiving account servicer may in return provide to the delivering
account servicer the receiving settlement chain using the same message.
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information
using the relevant elements in the Business Application Header.
Outline
The PortfolioTransferNotificationV09 MessageDefinition is composed of 6 MessageBuildingBlocks:
A. Pagination
Page number of the message (within a statement) and continuation indicator to indicate that the
statement is to continue or that the message is the last page of the statement.
B. StatementGeneralDetails
Provides general information on the notification.
C. AccountOwner
Party that legally owns the account.
D. SafekeepingAccount
Account to or from which a securities entry is made.
E. BlockChainAddressOrWallet
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1094 March 2026
```

## File page 1095

```text
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
F. TransferNotificationDetails
Details of the transfer.
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1095 March 2026
```

