---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["15 sese.021.001.08 SecuritiesTransactionStatusQueryV08", "15.2 Structure"]
file_pages: [477]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.021.001.08"]
---

# 15.2 Structure

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 477 to 477.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 477

```text
Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
E. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
15.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesTxStsQry> [1..1]  C3, C4,
C5
   StatusAdviceRequested <StsAdvcReqd> [1..1]  C2 478
     Number <Nb> [1..1] ± C6 478
     References <Refs> [1..*] ± 479
   AccountOwner <AcctOwnr> [0..1] ± 480
   SafekeepingAccount <SfkpgAcct> [0..1] ± 480
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 480
   SupplementaryData <SplmtryData> [0..*] ± C7 480
15.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 ReferenceRule
The reference used to identify the transaction must be in line with the identification available for
the status advice requested by the SecuritiesTransactionStatusQuery. For example, a
SecuritiesTransactionStatusQuery must not request a
SecuritiesSettlementTransactionStatusAdvice using a CorporateActionEventIdentification.
C3 SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
This constraint is defined at the MessageDefinition level.
C4 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Approved by the Securities SEG on 27 January 2026 sese.021.001.08
SecuritiesTransactionStatusQueryV08
Settlement And Reconciliation - Maintenance 2025 - 2026 477 March 2026
```

