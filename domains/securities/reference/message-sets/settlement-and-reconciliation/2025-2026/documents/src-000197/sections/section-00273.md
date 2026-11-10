---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["11 semt.020.001.07 SecuritiesMessageCancellationAdviceV07", "11.2 Structure"]
file_pages: [407]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.020.001.07"]
---

# 11.2 Structure

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 407 to 407.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 407

```text
The SecuritiesMessageCancellationAdviceV07 MessageDefinition is composed of 5
MessageBuildingBlocks:
A. Reference
Reference to the message advised to be cancelled by the account servicer.
B. AccountOwner
Party that legally owns the account.
C. SafekeepingAccount
Account to or from which a securities entry is made.
D. BlockChainAddressOrWallet
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
E. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
11.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesMsgCxlAdvc> [1..1]  C3, C4,
C5
   Reference <Ref> [1..1] ± C2, C6 408
   AccountOwner <AcctOwnr> [0..1] ± 410
   SafekeepingAccount <SfkpgAcct> [0..1] ± 410
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 410
   SupplementaryData <SplmtryData> [0..*] ± C7 410
11.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 OtherMessageIdentificationUsageRule
If OtherMessageIdentification is used, then the message to be cancelled must not be one that
can be identified using of the message identification available in the choice list.
C3 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Approved by the Securities SEG on 27 January 2026 semt.020.001.07
SecuritiesMessageCancellationAdviceV07
Settlement And Reconciliation - Maintenance 2025 - 2026 407 March 2026
```

