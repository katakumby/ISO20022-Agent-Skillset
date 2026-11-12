---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10", "24.4 Message Building Blocks", "24.4.4 RequestDetails <ReqDtls>", "24.4.4.11 MatchingDenial <MtchgDnl>"]
file_pages: [794]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.030.001.10"]
---

# 24.4.4.11 MatchingDenial <MtchgDnl>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 794 to 794.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 794

```text
HoldIndicator <HldInd> contains the following elements (see "HoldIndicator6" on page 1592 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 1593
   Reason <Rsn> [0..*] ± 1593
24.4.4.11  MatchingDenial <MtchgDnl>
Presence: [0..1]
Definition: Specifies the matching processing change requested.
MatchingDenial <MtchgDnl> contains one of the following elements (see "MatchingDenied3Choice"
on page 1951 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1951
Or}   Proprietary <Prtry> [1..1] ± 1951
24.4.4.12  UnilateralSplit <UnltrlSplt>
Presence: [0..1]
Definition: Specifies that the transaction is requested to be unilaterally split.
UnilateralSplit <UnltrlSplt> contains one of the following elements (see "UnilateralSplit3Choice" on
page 1580 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1581
Or}   Proprietary <Prtry> [1..1] ± 1581
24.4.4.13  Linkages <Lnkgs>
Presence: [0..*]
Definition: Information regarding the linkage requested.
Linkages <Lnkgs> contains the following elements (see "Linkages73" on page 1646 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ProcessingPosition <PrcgPos> [0..1] ± C11 1646
   MessageNumber <MsgNb> [0..1] ± C20 1647
   Reference <Ref> [1..1] ± 1647
   ReferenceOwner <RefOwnr> [0..1] ± 1648
Approved by the Securities SEG on 27 January 2026 sese.030.001.10
SecuritiesSettlementConditionsModificationRequest
V10
Settlement And Reconciliation - Maintenance 2025 - 2026 794 March 2026
```

