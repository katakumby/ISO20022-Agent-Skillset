---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.30 FXStandingInstruction4Choice", "35.1.16.30.1 Indicator <Ind>"]
file_pages: [1562]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.30.1 Indicator <Ind>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1562 to 1562.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1562

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1562
Or}   Proprietary <Prtry> [1..1] ± 1562
35.1.16.30.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether the forex standing instruction in place should apply.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.16.30.2  Proprietary <Prtry>
Presence: [1..1]
Definition: FX Standing instruction information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.31  SecuritiesTradeDetails100
Definition: Details of the securities trade.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeDate <TradDt> [0..1] ± 1563
   OpeningSettlementDate <OpngSttlmDt> [1..1] ± 1563
   NumberOfDaysAccrued <NbOfDaysAcrd> [0..1] Quantity C20 1563
   InstructionProcessingAdditionalDetails
<InstrPrcgAddtlDtls>
[0..1] Text 1563
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1562 March 2026
```

