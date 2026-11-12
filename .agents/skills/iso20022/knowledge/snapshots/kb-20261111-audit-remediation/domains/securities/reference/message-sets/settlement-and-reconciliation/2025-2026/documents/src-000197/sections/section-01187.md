---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.90 SettlementTransactionCondition43Choice"]
file_pages: [1638]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.90 SettlementTransactionCondition43Choice

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1638 to 1638.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1638

```text
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.16.90  SettlementTransactionCondition43Choice
Definition: Choice of format for the settlement transaction conditions.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1638
Or}   Proprietary <Prtry> [1..1] ± 1638
35.1.16.90.1  Code <Cd>
Presence: [1..1]
Definition: Settlement conditions expressed as an ISO 20022 code.
Datatype: "SettlementTransactionCondition18Code" on page 2166
CodeName Name Definition
CLEN Clean Tax-exempt financial instruments are to
be settled.
DLWM DeliveryWithoutMatching Matching receipt instruction not required
(only for concerned international or
national central securities depositories).
DIRT Dirty Taxable financial instruments are to be
settled.
GATE GatingEventParticipation Gating event participation. Hold until
event start time.
NOMC NoAutomaticMarketClaim No market claim should be automatically
generated.
BPSS PartialSuccessfulBuyIn Identification of settlement instructions
created as a result of a partial successful
buy-in.
PHYS Physical Securities are to be physically settled.
SPDL SpecialDelivery Settlement transactions to be settled
with special delivery.
SPST SplitSettlement Money and financial instruments settle in
different locations.
35.1.16.90.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement conditions expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1638 March 2026
```

