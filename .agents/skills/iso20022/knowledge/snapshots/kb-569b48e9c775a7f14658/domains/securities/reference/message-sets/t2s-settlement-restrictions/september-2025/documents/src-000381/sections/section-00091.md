---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["5 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "5.4 Message Building Blocks", "5.4.3 Modifications <Mods>", "5.4.3.4 Modification <Mod>", "5.4.3.4.6 RequestDetails <ReqDtls>", "5.4.3.4.6.9 SecuritiesRTGS <SctiesRTGS>"]
file_pages: [120]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 5.4.3.4.6.9 SecuritiesRTGS <SctiesRTGS>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 120 to 120.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 120

```text
CodeName Name Definition
PARQ PartialSettlementQuantityThresholdAllowed Partial settlement is allowed but must
satisfy a minimum quantity of securities
(quantity defined in static data).
5.4.3.4.6.9  SecuritiesRTGS <SctiesRTGS>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is to be settled through an RTGS or a non
RTGS system.
SecuritiesRTGS <SctiesRTGS> contains one of the following elements (see
"SecuritiesRTGS4Choice" on page 238 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 238
Or}   Proprietary <Prtry> [1..1] ± 238
5.4.3.4.6.10  HoldIndicator <HldInd>
Presence: [0..1]
Definition: Specifies whether the transaction is on hold/blocked/frozen.
HoldIndicator <HldInd> contains the following elements (see "HoldIndicator6" on page 243 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 244
   Reason <Rsn> [0..*] ± 244
5.4.3.4.6.11  MatchingDenial <MtchgDnl>
Presence: [0..1]
Definition: Specifies the matching processing change requested.
MatchingDenial <MtchgDnl> contains one of the following elements (see "MatchingDenied3Choice"
on page 289 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 289
Or}   Proprietary <Prtry> [1..1] ± 289
5.4.3.4.6.12  UnilateralSplit <UnltrlSplt>
Presence: [0..1]
Definition: Specifies that the transaction is requested to be unilaterally split.
Approved by the Securities SEG on 21 August 2025 semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities - Settlement Restrictions 120 September 2025
```

