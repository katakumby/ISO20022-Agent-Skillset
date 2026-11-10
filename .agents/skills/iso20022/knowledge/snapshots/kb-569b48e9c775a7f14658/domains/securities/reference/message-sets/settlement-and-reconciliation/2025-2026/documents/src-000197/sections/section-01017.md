---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.11 Financial Instrument", "35.1.11.1 FinancialInstrumentAttributes111", "35.1.11.1.38 ContractSize <CtrctSz>"]
file_pages: [1455]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.11.1.38 ContractSize <CtrctSz>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1455 to 1455.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1455

```text
MinimumNominalQuantity <MinNmnlQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1726 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1726
Or   FaceAmount <FaceAmt> [1..1] Amount 1726
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1726
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1727
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
35.1.11.1.38  ContractSize <CtrctSz>
Presence: [0..1]
Definition: Ratio or multiplying factor used to convert one contract into a quantity.
Impacted by: C12 "DigitalTokenUnitUsageRule"
ContractSize <CtrctSz> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1726 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1726
Or   FaceAmount <FaceAmt> [1..1] Amount 1726
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1726
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1727
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
35.1.11.1.39  UnderlyingFinancialInstrumentIdentification <UndrlygFinInstrmId>
Presence: [0..*]
Definition: Identification of the underlying security.
Impacted by: C10 "DescriptionPresenceRule", C11 "DescriptionUsageRule", C14 "ISINGuideline", C15
"ISINPresenceRule", C16 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1455 March 2026
```

