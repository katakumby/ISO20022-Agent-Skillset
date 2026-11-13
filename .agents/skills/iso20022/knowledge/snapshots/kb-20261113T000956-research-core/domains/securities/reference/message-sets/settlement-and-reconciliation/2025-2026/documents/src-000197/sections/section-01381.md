---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.10 SettlementDetails222", "35.1.26.10.17 NettingEligibility <NetgElgblty>"]
file_pages: [1849]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.10.17 NettingEligibility <NetgElgblty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1849 to 1849.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1849

```text
35.1.26.10.17  NettingEligibility <NetgElgblty>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is eligible for netting.
NettingEligibility <NetgElgblty> contains one of the following elements (see
"NettingEligibility4Choice" on page 1548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1548
Or}   Proprietary <Prtry> [1..1] ± 1549
35.1.26.10.18  CCPEligibility <CCPElgblty>
Presence: [0..1]
Definition: Specifies whether the settlement transaction is CCP (Central Counterparty) eligible.
CCPEligibility <CCPElgblty> contains one of the following elements (see
"CentralCounterPartyEligibility4Choice" on page 1546 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1546
Or}   Proprietary <Prtry> [1..1] ± 1546
35.1.26.10.19  LetterOfGuarantee <LttrOfGrnt>
Presence: [0..1]
Definition: Specifies whether physical settlement may be executed using a letter of guarantee or if the
physical certificates should be used.
LetterOfGuarantee <LttrOfGrnt> contains one of the following elements (see
"LetterOfGuarantee4Choice" on page 1557 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1557
Or}   Proprietary <Prtry> [1..1] ± 1557
35.1.26.10.20  PartialSettlementIndicator <PrtlSttlmInd>
Presence: [0..1]
Definition: Specifies whether partial settlement is allowed.
Datatype: "SettlementTransactionCondition5Code" on page 2170
CodeName Name Definition
PART PartialAllowed Partial settlement is allowed.
NPAR PartialNotAllowed Partial settlement is not allowed.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1849 March 2026
```

