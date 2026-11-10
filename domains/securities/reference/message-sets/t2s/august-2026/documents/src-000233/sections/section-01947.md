---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "76.4 Message Building Blocks", "76.4.3 Modifications <Mods>", "76.4.3.1 AccountOwner <AcctOwnr>"]
file_pages: [2664]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 76.4.3.1 AccountOwner <AcctOwnr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2664 to 2664.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2664

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         SettlementQuantity <SttlmQty> [1..1] ± 2685
         SettlementAmount <SttlmAmt> [0..1] ± 2685
         TradeDate <TradDt> [0..1] ± 2686
         SettlementDate <SttlmDt> [1..1] ± 2686
         DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C18,
C19,
C20,
C21
2686
         ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C18,
C19,
C20,
C21
2687
Constraints
• AccountOwnerRule
AccountOwner must be present or Modification(*)/AccountOwner must be present, but not both.
• ProcessingStatusRule
ProcessingStatus must be present or Modification(*)/ProcessingStatus must be present, but not both.
• SafekeepingAccountRule
SafekeepingAccount must be present or Modification(*)/SafekeepingAccount must be present, but
not both.
76.4.3.1  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
76.4.3.2  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2664 August 2026
```

