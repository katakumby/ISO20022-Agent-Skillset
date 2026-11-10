---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["23 sese.029.001.08 SecuritiesSettlementAllegementRemovalAdviceV08", "23.4 Message Building Blocks", "23.4.7 TransactionDetails <TxDtls>", "23.4.7.9 Investor <Invstr>"]
file_pages: [781]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.029.001.08"]
---

# 23.4.7.9 Investor <Invstr>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 781 to 781.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 781

```text
Impacted by: C13 "Party2PresenceRule", C14 "Party3PresenceRule", C15 "Party4PresenceRule", C16
"Party5PresenceRule"
ReceivingSettlementParties <RcvgSttlmPties> contains the following elements (see
"SettlementParties125" on page 1751 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 1752
   Party1 <Pty1> [0..1] ± C18,
C20
1752
   Party2 <Pty2> [0..1] ± C18,
C20
1753
   Party3 <Pty3> [0..1] ± C18,
C20
1753
   Party4 <Pty4> [0..1] ± C18,
C20
1754
   Party5 <Pty5> [0..1] ± C18,
C20
1755
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
On Condition
    /Party4 is present
Following Must be True
    /Party3 Must be present
• Party5PresenceRule
If Party5 is present, then Party4 must be present.
On Condition
    /Party5 is present
Following Must be True
    /Party4 Must be present
23.4.7.9  Investor <Invstr>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.029.001.08
SecuritiesSettlementAllegementRemovalAdviceV08
Settlement And Reconciliation - Maintenance 2025 - 2026 781 March 2026
```

