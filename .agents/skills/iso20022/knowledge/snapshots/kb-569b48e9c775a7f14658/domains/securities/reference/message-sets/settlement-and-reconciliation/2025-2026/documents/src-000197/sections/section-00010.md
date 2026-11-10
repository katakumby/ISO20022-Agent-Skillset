---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.5 SafekeepingAccount <SfkpgAcct>"]
file_pages: [30]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.5 SafekeepingAccount <SfkpgAcct>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 30 to 30.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 30

```text
Definition: Party that manages the account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
AccountServicer <AcctSvcr> contains the following elements (see "PartyIdentification136" on
page 1671 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1672
   LEI <LEI> [0..1] IdentifierSet 1672
2.4.5 SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount26" on
page 1345 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1345
   Type <Tp> [0..1] ± 1345
   Name <Nm> [0..1] Text 1345
   Designation <Dsgnt> [0..1] Text 1345
2.4.6 BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet1" on page 1594 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1594
   Type <Tp> [0..1] ± 1594
   Name <Nm> [0..1] Text 1595
   Designation <Dsgnt> [0..1] Text 1595
2.4.7 IntermediaryInformation <IntrmyInf>
Presence: [0..10]
Definition: Information about the party that provides services relating to financial products to investors,
for example, advice on products and placement of orders for the investment fund.
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 30 March 2026
```

