---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "76.4 Message Building Blocks", "76.4.3 Modifications <Mods>", "76.4.3.4 Modification <Mod>", "76.4.3.4.6 RequestDetails <ReqDtls>", "76.4.3.4.6.9 SecuritiesRTGS <SctiesRTGS>"]
file_pages: [2675]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 76.4.3.4.6.9 SecuritiesRTGS <SctiesRTGS>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2675 to 2675.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2675

```text
CodeName Name Definition
PARQ PartialSettlementQuantityThresholdAllowed Partial settlement is allowed but must
satisfy a minimum quantity of securities
(quantity defined in static data).
76.4.3.4.6.9  SecuritiesRTGS <SctiesRTGS>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is to be settled through an RTGS or a non
RTGS system.
SecuritiesRTGS <SctiesRTGS> contains one of the following elements (see
"SecuritiesRTGS4Choice" on page 2997 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 2997
Or}   Proprietary <Prtry> [1..1] ± 2997
76.4.3.4.6.10  HoldIndicator <HldInd>
Presence: [0..1]
Definition: Specifies whether the transaction is on hold/blocked/frozen.
HoldIndicator <HldInd> contains the following elements (see "HoldIndicator6" on page 3025 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 3025
   Reason <Rsn> [0..*] ± 3026
76.4.3.4.6.11  MatchingDenial <MtchgDnl>
Presence: [0..1]
Definition: Specifies the matching processing change requested.
MatchingDenial <MtchgDnl> contains one of the following elements (see "MatchingDenied3Choice"
on page 3161 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3161
Or}   Proprietary <Prtry> [1..1] ± 3162
76.4.3.4.6.12  UnilateralSplit <UnltrlSplt>
Presence: [0..1]
Definition: Specifies that the transaction is requested to be unilaterally split.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2675 August 2026
```

