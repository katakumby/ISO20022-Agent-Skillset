---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 semt.013.001.07 IntraPositionMovementInstructionV07", "4.4 Message Building Blocks", "4.4.11 IntraPositionDetails <IntraPosDtls>", "4.4.11.3 SecuritiesSubBalanceIdentification <SctiesSubBalId>"]
file_pages: [148]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.013.001.07"]
---

# 4.4.11.3 SecuritiesSubBalanceIdentification <SctiesSubBalId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 148 to 148.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 148

```text
SettlementQuantity <SttlmQty> contains one of the following elements (see
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
4.4.11.3  SecuritiesSubBalanceIdentification <SctiesSubBalId>
Presence: [0..1]
Definition: Number identifying a securities sub balance type (for example, restriction identification
etc…).
SecuritiesSubBalanceIdentification <SctiesSubBalId> contains the following elements (see
"GenericIdentification37" on page 1498 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1498
   Issuer <Issr> [0..1] Text 1498
4.4.11.4  SettlementDate <SttlmDt>
Presence: [1..1]
Definition: Date and time at which the securities are to be moved.
SettlementDate <SttlmDt> contains one of the following elements (see "DateAndDateTime2Choice"
on page 1441 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
4.4.11.5  BalanceFrom <BalFr>
Presence: [1..1]
Definition: Balance from which the securities are moving.
Approved by the Securities SEG on 27 January 2026 semt.013.001.07
IntraPositionMovementInstructionV07
Settlement And Reconciliation - Maintenance 2025 - 2026 148 March 2026
```

