---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.22 SecuritiesMovementDetails <SctiesMvmntDtls>", "7.4.13.22.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [466]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.22.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 466 to 466.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 466

```text
IssuePrice <IssePric> contains one of the following elements (see "PriceFormat74Choice" on
page 1074 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1074
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1075
     PriceValue <PricVal> [1..1] Rate 1075
Or   AmountPrice <AmtPric> [1..1] ± 1075
Or}   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1075
7.4.13.22.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Specifies whether the value is a debit or credit.
Datatype: "CreditDebitCode" on page 1205
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
7.4.13.22.3  TemporaryFinancialInstrumentIndicator <TempFinInstrmInd>
Presence: [0..1]
Definition: Specifies that the security identified is a temporary security identification used for processing
reasons, for example, contra security used in the US.
TemporaryFinancialInstrumentIndicator <TempFinInstrmInd> contains one of the following
elements (see "TemporaryFinancialInstrumentIndicator3Choice" on page 906 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   TemporaryIndicator <TempInd> [1..1] Indicator 906
Or}   Proprietary <Prtry> [1..1] ± 906
7.4.13.22.4  NonEligibleProceedsIndicator <NonElgblPrcdsInd>
Presence: [0..1]
Definition: Specifies information regarding outturn resources that cannot be processed by the Central
Securities Depository (CSD). Special delivery instruction is required from the account owner for the
corporate action outcome to be credited.
NonEligibleProceedsIndicator <NonElgblPrcdsInd> contains one of the following
NonEligibleProceedsIndicator5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 467
Or}   Proprietary <Prtry> [1..1] ± 467
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 466 February 2026
```

