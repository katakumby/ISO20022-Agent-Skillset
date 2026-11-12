---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["72 semt.027.001.01 SecuritiesSettlementTransactionQueryResponseV01", "72.4 Message Building Blocks", "72.4.3 Transactions <Txs>", "72.4.3.4 Transaction <Tx>", "72.4.3.4.18 TransactionDetails <TxDtls>", "72.4.3.4.18.30 Priority <Prty>"]
file_pages: [2558]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.027.001.01"]
---

# 72.4.3.4.18.30 Priority <Prty>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2558 to 2558.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2558

```text
72.4.3.4.18.30  Priority <Prty>
Presence: [0..1]
Definition: Specifies whether the transaction is to be executed with a high priority.
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 2981 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 2981
Or}   Proprietary <Prtry> [1..1] ± 2981
72.4.3.4.18.31  DeliveringSettlementParties <DlvrgSttlmPties>
Presence: [0..1]
Definition: Identifies the chain of delivering settlement parties.
Impacted by: C21 "Party2PresenceRule", C22 "Party3PresenceRule", C23 "Party4PresenceRule", C24
"Party5PresenceRule"
DeliveringSettlementParties <DlvrgSttlmPties> contains the following elements (see
"SettlementParties78" on page 3115 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 3115
   Party1 <Pty1> [0..1] ± 3116
   Party2 <Pty2> [0..1] ± 3116
   Party3 <Pty3> [0..1] ± 3117
   Party4 <Pty4> [0..1] ± 3117
   Party5 <Pty5> [0..1] ± 3117
Constraints
• Party2PresenceRule
If Party2 is present, then Party1 must be present.
On Condition
    /Party2 is present
Following Must be True
    /Party1 Must be present
• Party3PresenceRule
If Party3 is present, then Party2 must be present.
On Condition
    /Party3 is present
Following Must be True
    /Party2 Must be present
• Party4PresenceRule
If Party4 is present, then Party3 must be present.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.027.001.01
SecuritiesSettlementTransactionQueryResponseV0
1
Target2-Securities 2558 August 2026
```

