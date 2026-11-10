---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "25.4 Message Building Blocks"]
file_pages: [806]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.031.001.11"]
---

# 25.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 806 to 806.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 806

```text
not be executed, then all the other transactions/instructions/notifications must also be kept
pending. Therefore the use of code WITH must be limited to combine up to 2 or 3 transactions/
instructions/notifications.
25.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
25.4.1 RequestReference <ReqRef>
Presence: [1..1]
Definition: Identification of the SecuritiesSettlementConditionsModificationRequest.
Datatype: "Max35Text" on page 2192
25.4.2 AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification144" on
page 1664 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1664
   LEI <LEI> [0..1] IdentifierSet 1664
25.4.3 SafekeepingAccount <SfkpgAcct>
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
25.4.4 BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
Approved by the Securities SEG on 27 January 2026 sese.031.001.11
SecuritiesSettlementConditionModificationStatusAd
viceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 806 March 2026
```

