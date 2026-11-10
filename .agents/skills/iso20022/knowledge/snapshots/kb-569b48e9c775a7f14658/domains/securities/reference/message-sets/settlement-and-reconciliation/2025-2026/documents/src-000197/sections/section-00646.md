---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11", "28.4 Message Building Blocks", "28.4.6 RepoCallRequestStatus <RepoCallReqSts>", "28.4.7.6 TripartyAgentServiceProviderCollateralTransactionIdentification <TrptyAgtSvcPrvdrCollTxId>"]
file_pages: [976]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.034.001.11"]
---

# 28.4.7.6 TripartyAgentServiceProviderCollateralTransactionIdentification <TrptyAgtSvcPrvdrCollTxId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 976 to 976.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 976

```text
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 2192
28.4.7.6  TripartyAgentServiceProviderCollateralTransactionIdentification
<TrptyAgtSvcPrvdrCollTxId>
Presence: [0..1]
Definition: Unique identification identifying the triparty collateral management transaction from the
triparty-agent's/service-provider's point of view.
Datatype: "Max35Text" on page 2192
28.4.7.7  ClientTripartyCollateralTransactionIdentification <ClntTrptyCollTxId>
Presence: [0..1]
Definition: Unique reference identifying the triparty collateral management transaction from the client's
point of view.
Datatype: "Max35Text" on page 2192
28.4.7.8  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification144" on
page 1664 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1664
   LEI <LEI> [0..1] IdentifierSet 1664
28.4.7.9  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 1340 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1341
   Type <Tp> [0..1] ± 1341
   Name <Nm> [0..1] Text 1341
28.4.7.10  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.034.001.11
SecuritiesFinancingStatusAdviceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 976 March 2026
```

