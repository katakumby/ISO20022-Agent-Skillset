---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.1 AccountOwner <AcctOwnr>"]
file_pages: [2494]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.1 AccountOwner <AcctOwnr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2494 to 2494.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2494

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           OtherTransactionIdentification <OthrTxId> [1..1] Text 2557
         ReferenceOwner <RefOwnr> [0..1] ± 2557
       Priority <Prty> [0..1] ± 2558
       DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C21,
C22,
C23,
C24
2558
       ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C21,
C22,
C23,
C24
2559
       ReversalIndicator <RvslInd> [0..1] Indicator 2560
       MessageOriginator <MsgOrgtr> [0..1] ± 2560
       CreationDateTime <CreDtTm> [1..1] DateTime 2560
       TransactionAdditionalDetails <TxAddtlDtls> [0..1] Text 2560
       SupplementaryData <SplmtryData> [0..*] ± C36 2560
Constraints
• AccountOwnerRule
AccountOwner must be present or Transaction(*)/AccountOwner must be present, but not both.
• SafekeepingAccountRule
SafekeepingAccount must be present or Transaction(*)/SafekeepingAccount must be present, but
not both.
72.4.3.1  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
72.4.3.2  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account where financial instruments are maintained.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2494 August 2026
```

