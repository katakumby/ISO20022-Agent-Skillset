---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["4 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "4.4 Message Building Blocks", "4.4.3 Transactions <Txs>", "4.4.3.1 AccountOwner <AcctOwnr>"]
file_pages: [98]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 4.4.3.1 AccountOwner <AcctOwnr>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 98 to 98.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 98

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           OtherTransactionIdentification <OthrTxId> [1..1] Text 161
         ReferenceOwner <RefOwnr> [0..1] ± 161
       Priority <Prty> [0..1] ± 162
       DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C21,
C22,
C23,
C24
162
       ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C21,
C22,
C23,
C24
163
       ReversalIndicator <RvslInd> [0..1] Indicator 164
       MessageOriginator <MsgOrgtr> [0..1] ± 164
       CreationDateTime <CreDtTm> [1..1] DateTime 164
       TransactionAdditionalDetails <TxAddtlDtls> [0..1] Text 164
       SupplementaryData <SplmtryData> [0..*] ± C36 164
Constraints
• AccountOwnerRule
AccountOwner must be present or Transaction(*)/AccountOwner must be present, but not both.
• SafekeepingAccountRule
SafekeepingAccount must be present or Transaction(*)/SafekeepingAccount must be present, but
not both.
4.4.3.1  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 432 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 432
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 432
4.4.3.2  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account where financial instruments are maintained.
Approved by the Securities SEG 19 February 2026. semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities - Securities and Penalty Reporting 98 March 2026
```

