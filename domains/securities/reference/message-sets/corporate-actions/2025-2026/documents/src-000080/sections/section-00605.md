---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks", "14.4.3 AccountAndStatementDetails <AcctAndStmtDtls>", "14.4.3.5 CorporateActionEventAndBalance <CorpActnEvtAndBal>", "14.4.3.5.3 Balance <Bal>", "14.4.3.5.3.3 TotalInstructedBalanceDetails <TtlInstdBalDtls>", "14.4.3.5.3.3.7 OptionDetails <OptnDtls>", "14.4.3.5.3.3.7.12 OptionInstructionDetails <OptnInstrDtls>", "14.4.3.5.3.3.7.12.5 InstructionDate <InstrDt>"]
file_pages: [794]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
---

# 14.4.3.5.3.3.7.12.5 InstructionDate <InstrDt>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 794 to 794.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 794

```text
InstructionQuantity <InstrQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1091 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1092
Or   FaceAmount <FaceAmt> [1..1] Amount 1092
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1092
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1092
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
14.4.3.5.3.3.7.12.5  InstructionDate <InstrDt>
Presence: [1..1]
Definition: Date of the instruction.
Datatype: "ISODate" on page 1243
14.4.3.5.3.3.7.12.6  ProtectDate <PrtctDt>
Presence: [0..1]
Definition: Date of the client protect instruction.
Datatype: "ISODate" on page 1243
14.4.3.5.3.3.7.12.7  CoverProtectDate <CoverPrtctDt>
Presence: [0..1]
Definition: Date of the cover protect Instruction
Datatype: "ISODate" on page 1243
14.4.3.5.3.3.7.12.8  BidPrice <BidPric>
Presence: [0..1]
Definition: Bid price of the instruction.
BidPrice <BidPric> contains one of the following elements (see "PriceFormat74Choice" on page 1074
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1074
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1075
     PriceValue <PricVal> [1..1] Rate 1075
Or   AmountPrice <AmtPric> [1..1] ± 1075
Or}   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1075
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 794 February 2026
```

