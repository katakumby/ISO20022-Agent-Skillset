---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08"]
file_pages: [482]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.022.001.08"]
---

# 16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 482 to 482.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 482

```text
16 sese.022.001.08
SecuritiesStatusOrStatementQueryStatusAdv
iceV08
16.1 MessageDefinition Functionality
Scope
An account servicer sends a SecuritiesStatusOrStatementQueryStatusAdvice to an account owner to
advise the status of a status query or statement query previously sent by the account owner.
The account servicer/owner relationship may be:
- a central securities depository or another settlement market infrastructure acting on behalf of their
participants
- an agent (sub-custodian) acting on behalf of their global custodian customer, or
- a custodian acting on behalf of an investment management institution or a broker/dealer.
Usage
The message may also be used to:
- re-send a message previously sent,
- provide a third party with a copy of a message for information,
- re-send to a third party a copy of a message for information using the relevant elements in the
Business Application Header.
Outline
The SecuritiesStatusOrStatementQueryStatusAdviceV08 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. QueryDetails
Unambiguous identification of the query as per the account owner.
B. AccountOwner
Party that legally owns the account.
C. SafekeepingAccount
Account to or from which a securities entry is made.
D. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
E. StatusOrStatementRequested
Details of the request.
Approved by the Securities SEG on 27 January 2026 sese.022.001.08
SecuritiesStatusOrStatementQueryStatusAdviceV0
8
Settlement And Reconciliation - Maintenance 2025 - 2026 482 March 2026
```

