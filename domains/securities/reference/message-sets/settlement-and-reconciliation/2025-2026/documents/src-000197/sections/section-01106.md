---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.16 SettlementTypeAndAdditionalParameters13"]
file_pages: [1548]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.16 SettlementTypeAndAdditionalParameters13

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1548 to 1548.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1548

```text
35.1.16.16  SettlementTypeAndAdditionalParameters13
Definition: Provides transaction type and identification information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CommonIdentification <CmonId> [0..1] Text 1548
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 1548
   ReconciliationIndicator <RcncltnInd> [0..1] Indicator 1548
35.1.16.16.1  CommonIdentification <CmonId>
Presence: [0..1]
Definition: Unique reference agreed upon by the two trade counterparties to identify the trade.
Datatype: "Max35Text" on page 2192
35.1.16.16.2  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [0..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 2192
35.1.16.16.3  ReconciliationIndicator <RcncltnInd>
Presence: [0..1]
Definition: Indicates whether the settlement transaction was already sent on the market and that it is
only sent by an account owner to an account servicer for reconciliation purposes.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.16.17  NettingEligibility4Choice
Definition: Choice of format for the netting eligibility information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1548
Or}   Proprietary <Prtry> [1..1] ± 1549
35.1.16.17.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether the settlement transaction is eligible for netting.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1548 March 2026
```

