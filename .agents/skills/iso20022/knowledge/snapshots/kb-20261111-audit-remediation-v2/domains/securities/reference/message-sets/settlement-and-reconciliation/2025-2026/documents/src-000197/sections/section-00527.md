---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10", "24.4 Message Building Blocks", "24.4.5 AdditionalInformation <AddtlInf>", "24.4.5.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>"]
file_pages: [796]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.030.001.10"]
---

# 24.4.5.1 AccountOwnerTransactionIdentification <AcctOwnrTxId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 796 to 796.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 796

```text
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
• SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
24.4.5.1  AccountOwnerTransactionIdentification <AcctOwnrTxId>
Presence: [0..1]
Definition: Identification of the transaction as known by the account owner. Will be used in a unilateral
split to provide the executing party with the account owner identification of each split transaction.
Datatype: "Max35Text" on page 2192
24.4.5.2  ClassificationType <ClssfctnTp>
Presence: [0..1]
Definition: Type of instrument involved in the transactions on which the modification request should
apply.
ClassificationType <ClssfctnTp> contains one of the following elements (see
"ClassificationType32Choice" on page 1535 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] IdentifierSet 1536
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 1536
24.4.5.3  SafekeepingAccount <SfkpgAcct>
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
24.4.5.4  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
Approved by the Securities SEG on 27 January 2026 sese.030.001.10
SecuritiesSettlementConditionsModificationRequest
V10
Settlement And Reconciliation - Maintenance 2025 - 2026 796 March 2026
```

