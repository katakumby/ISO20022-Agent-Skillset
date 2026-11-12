---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.3 SettlementDetails232", "35.1.26.3.13 LegalRestrictions <LglRstrctns>"]
file_pages: [1800]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.3.13 LegalRestrictions <LglRstrctns>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1800 to 1800.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1800

```text
35.1.26.3.13  LegalRestrictions <LglRstrctns>
Presence: [0..1]
Definition: Regulatory restrictions applicable to a security.
LegalRestrictions <LglRstrctns> contains one of the following elements (see "Restriction5Choice" on
page 1551 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1551
Or}   Proprietary <Prtry> [1..1] ± 1552
35.1.26.3.14  SettlementSystemMethod <SttlmSysMtd>
Presence: [0..1]
Definition: Specifies whether the settlement instruction is to be settled through the default or the
alternate settlement system.
SettlementSystemMethod <SttlmSysMtd> contains one of the following elements (see
"SettlementSystemMethod4Choice" on page 1532 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1532
Or}   Proprietary <Prtry> [1..1] ± 1532
35.1.26.3.15  NettingEligibility <NetgElgblty>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is eligible for netting.
NettingEligibility <NetgElgblty> contains one of the following elements (see
"NettingEligibility4Choice" on page 1548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1548
Or}   Proprietary <Prtry> [1..1] ± 1549
35.1.26.3.16  CCPEligibility <CCPElgblty>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is CCP (Central Counterparty) eligible.
CCPEligibility <CCPElgblty> contains one of the following elements (see
"CentralCounterPartyEligibility4Choice" on page 1546 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1546
Or}   Proprietary <Prtry> [1..1] ± 1546
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1800 March 2026
```

