---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["30 sese.036.001.10 SecuritiesFinancingModificationInstructionV10", "30.4 Message Building Blocks", "30.4.6 SettlementParameters <SttlmParams>", "30.4.6.20 EligibleForCollateral <ElgblForColl>"]
file_pages: [1086]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.036.001.10"]
---

# 30.4.6.20 EligibleForCollateral <ElgblForColl>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1086 to 1086.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1086

```text
30.4.6.20  EligibleForCollateral <ElgblForColl>
Presence: [0..1]
Definition: Specifies whether securities should be included in the pool of securities eligible for collateral
purposes.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
30.4.7 DeliveringSettlementParties <DlvrgSttlmPties>
Presence: [0..1]
Definition: Identifies the chain of delivering settlement parties.
Impacted by: C6 "BookTransferGuideline", C11 "DepositoryGuideline", C21 "Party2PresenceRule", C22
"Party3PresenceRule", C23 "Party4PresenceRule", C24 "Party5PresenceRule", C32
"SettlementChainGuideline"
DeliveringSettlementParties <DlvrgSttlmPties> contains the following elements (see
"SettlementParties127" on page 1760 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Depository <Dpstry> [0..1] ± 1762
   Party1 <Pty1> [0..1] ± C26,
C28
1763
   Party2 <Pty2> [0..1] ± C26,
C28
1764
   Party3 <Pty3> [0..1] ± C26,
C28
1764
   Party4 <Pty4> [0..1] ± C26,
C28
1765
   Party5 <Pty5> [0..1] ± C26,
C28
1766
Constraints
• BookTransferGuideline
In case of own account internal transfer, own account external transfer, portfolio transfer and in
specie transfer (see SecuritiesTransactionType), the account of (delivering) Party2 at (delivering)
Party1 must be provided.
For more details, see the relevant market practice document on www.smpg.info.
• DepositoryGuideline
In a delivery, the receiving depository is to be understood as the requested depository of the
receiving counterparty.
In a receive, the delivering depository is to be understood as the requested depository of the
delivering counterparty.
Approved by the Securities SEG on 27 January 2026 sese.036.001.10
SecuritiesFinancingModificationInstructionV10
Settlement And Reconciliation - Maintenance 2025 - 2026 1086 March 2026
```

