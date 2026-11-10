---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "25.4 Message Building Blocks", "25.4.5 RequestDetails <ReqDtls>", "25.4.5.10 HoldIndicator <HldInd>"]
file_pages: [811]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.031.001.11"]
---

# 25.4.5.10 HoldIndicator <HldInd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 811 to 811.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 811

```text
SecuritiesRTGS <SctiesRTGS> contains one of the following elements (see
"SecuritiesRTGS4Choice" on page 1554 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1554
Or}   Proprietary <Prtry> [1..1] ± 1554
25.4.5.10  HoldIndicator <HldInd>
Presence: [0..1]
Definition: Specifies whether the transaction is on hold/blocked/frozen.
HoldIndicator <HldInd> contains the following elements (see "HoldIndicator6" on page 1592 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 1593
   Reason <Rsn> [0..*] ± 1593
25.4.5.11  MatchingDenial <MtchgDnl>
Presence: [0..1]
Definition: Specifies the matching processing change requested.
MatchingDenial <MtchgDnl> contains one of the following elements (see "MatchingDenied3Choice"
on page 1951 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1951
Or}   Proprietary <Prtry> [1..1] ± 1951
25.4.5.12  UnilateralSplit <UnltrlSplt>
Presence: [0..1]
Definition: Specifies that the transaction is requested to be unilaterally split.
UnilateralSplit <UnltrlSplt> contains one of the following elements (see "UnilateralSplit3Choice" on
page 1580 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1581
Or}   Proprietary <Prtry> [1..1] ± 1581
25.4.5.13  Linkages <Lnkgs>
Presence: [0..*]
Definition: Information regarding the linkage requested.
Approved by the Securities SEG on 27 January 2026 sese.031.001.11
SecuritiesSettlementConditionModificationStatusAd
viceV11
Settlement And Reconciliation - Maintenance 2025 - 2026 811 March 2026
```

