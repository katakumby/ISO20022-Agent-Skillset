---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["78 semt.033.001.01 SecuritiesTransactionCancellationRequestReportV01", "78.4 Message Building Blocks", "78.4.3 Cancellations <Cxls>", "78.4.3.1 AccountOwner <AcctOwnr>"]
file_pages: [2709]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.033.001.01"]
---

# 78.4.3.1 AccountOwner <AcctOwnr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2709 to 2709.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2709

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C11,
C12,
C13,
C14,
C15
2719
         SettlementQuantity <SttlmQty> [1..1] ± 2720
         SettlementAmount <SttlmAmt> [0..1] ± 2720
         TradeDate <TradDt> [0..1] ± 2721
         SettlementDate <SttlmDt> [1..1] ± 2721
         DeliveringSettlementParties <DlvrgSttlmPties> [0..1] ± C16,
C17,
C18,
C19
2721
         ReceivingSettlementParties <RcvgSttlmPties> [0..1] ± C16,
C17,
C18,
C19
2722
Constraints
• AccountOwnerRule
AccountOwner must be present or Cancellation(*)/AccountOwner must be present, but not both.
• ProcessingStatusRule
ProcessingStatus must be present or Cancellation(*)/ProcessingStatus must be present, but not
both.
• SafekeepingAccountRule
SafekeepingAccount must be present or Cancellation(*)/SafekeepingAccount must be present, but
not both.
78.4.3.1  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
78.4.3.2  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.033.001.01
SecuritiesTransactionCancellationRequestReportV0
1
Target2-Securities 2709 August 2026
```

