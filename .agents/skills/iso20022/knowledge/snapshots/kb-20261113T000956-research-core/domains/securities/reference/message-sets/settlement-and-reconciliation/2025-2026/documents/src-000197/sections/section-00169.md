---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "8.4 Message Building Blocks", "8.4.8 SubAccountDetails <SubAcctDtls>", "8.4.8.1 AccountOwner <AcctOwnr>"]
file_pages: [245]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.017.001.14"]
---

# 8.4.8.1 AccountOwner <AcctOwnr>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 245 to 245.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 245

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         ValueDate <ValDt> [0..1] ± 269
         AcknowledgedStatusTimeStamp
<AckdStsTmStmp>
[0..1] DateTime 269
         MatchedStatusTimeStamp <MtchdStsTmStmp> [0..1] DateTime 269
         DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C21,
C22,
C23,
C24
269
         ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C21,
C22,
C23,
C24
270
         ReversalIndicator <RvslInd> [0..1] Indicator 272
         TransactionAdditionalDetails <TxAddtlDtls> [0..1] Text 272
       SupplementaryData <SplmtryData> [0..*] ± C42 272
Constraints
• SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
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
8.4.8.1  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "PartyIdentification144" on
page 1664 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1664
   LEI <LEI> [0..1] IdentifierSet 1664
8.4.8.2  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 semt.017.001.14
SecuritiesTransactionPostingReportV14
Settlement And Reconciliation - Maintenance 2025 - 2026 245 March 2026
```

