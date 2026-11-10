---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.24 SecuritiesMovementDetails <SctiesMvmntDtls>", "3.4.11.24.2 CreditDebitIndicator <CdtDbtInd>"]
file_pages: [183]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.24.2 CreditDebitIndicator <CdtDbtInd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 183 to 183.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 183

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
3.4.11.24.2  CreditDebitIndicator <CdtDbtInd>
Presence: [1..1]
Definition: Specifies whether the value is a debit or credit.
Datatype: "CreditDebitCode" on page 1205
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
3.4.11.24.3  TemporaryFinancialInstrumentIndicator <TempFinInstrmInd>
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
3.4.11.24.4  NonEligibleProceedsIndicator <NonElgblPrcdsInd>
Presence: [0..1]
Definition: Specifies information regarding outturn resources that cannot be processed by the Central
Securities Depository (CSD). Special delivery instruction is required from the account owner for the
corporate action outcome to be credited.
NonEligibleProceedsIndicator <NonElgblPrcdsInd> contains one of the following
NonEligibleProceedsIndicator5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 184
Or}   Proprietary <Prtry> [1..1] ± 184
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 183 February 2026
```

