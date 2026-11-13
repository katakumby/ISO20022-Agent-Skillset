---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.26 Settlement Details", "35.1.26.9 SettlementDetails223", "35.1.26.9.5 BeneficialOwnership <BnfclOwnrsh>"]
file_pages: [1838]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.26.9.5 BeneficialOwnership <BnfclOwnrsh>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1838 to 1838.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1838

```text
CodeName Name Definition
PARQ PartialSettlementQuantityThresholdAllowed Partial settlement is allowed but must
satisfy a minimum quantity of securities
(quantity defined in static data).
35.1.26.9.5  BeneficialOwnership <BnfclOwnrsh>
Presence: [0..1]
Definition: Specifies whether there was change of beneficial ownership.
BeneficialOwnership <BnfclOwnrsh> contains one of the following elements (see
"BeneficialOwnership4Choice" on page 1600 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1600
Or}   Proprietary <Prtry> [1..1] ± 1600
35.1.26.9.6  BlockTrade <BlckTrad>
Presence: [0..1]
Definition: Specifies whether the settlement instruction was a block parent or child.
BlockTrade <BlckTrad> contains one of the following elements (see "BlockTrade4Choice" on
page 1573 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1574
Or}   Proprietary <Prtry> [1..1] ± 1574
35.1.26.9.7  CCPEligibility <CCPElgblty>
Presence: [0..1]
Definition: Specifies whether the settlement transaction was CCP (Central Counterparty) eligible.
CCPEligibility <CCPElgblty> contains one of the following elements (see
"CentralCounterPartyEligibility4Choice" on page 1546 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1546
Or}   Proprietary <Prtry> [1..1] ± 1546
35.1.26.9.8  CashClearingSystem <CshClrSys>
Presence: [0..1]
Definition: Specifies the category of cash clearing system, for example, cheque clearing.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1838 March 2026
```

