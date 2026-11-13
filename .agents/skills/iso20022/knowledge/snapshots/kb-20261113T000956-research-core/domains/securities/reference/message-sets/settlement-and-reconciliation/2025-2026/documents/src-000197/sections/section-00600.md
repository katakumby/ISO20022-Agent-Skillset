---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["27 sese.033.001.13 SecuritiesFinancingInstructionV13", "27.4 Message Building Blocks", "27.4.8 QuantityAndAccountDetails <QtyAndAcctDtls>", "27.4.8.4 SafekeepingAccount <SfkpgAcct>"]
file_pages: [912]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.033.001.13"]
---

# 27.4.8.4 SafekeepingAccount <SfkpgAcct>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 912 to 912.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 912

```text
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification144" on
page 1664 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1664
   LEI <LEI> [0..1] IdentifierSet 1664
27.4.8.4  SafekeepingAccount <SfkpgAcct>
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
27.4.8.5  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 1572 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1572
   Type <Tp> [0..1] ± 1572
   Name <Nm> [0..1] Text 1572
27.4.8.6  CashAccount <CshAcct>
Presence: [0..1]
Definition: Account to or from which a cash entry is made.
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 912 March 2026
```

