---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.11 Margin Call Calculation", "12.1.11.1 MarginCalculation2", "12.1.11.1.7 MarginTypeAmount <MrgnTpAmt>", "12.1.11.1.7.2 VariationMargin <VartnMrgn>", "12.1.11.1.7.2.7 FailsHaircut <FlsHrcut>", "12.1.11.1.7.2.7.2 ReportingAmount <RptgAmt>"]
file_pages: [427]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.11.1.7.2.7.2 ReportingAmount <RptgAmt>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 427 to 427.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 427

```text
– Error Text: Invalid currency code
• CurrencyAmount
(Rule)
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Error handling:
– Error severity: Fatal
– Error Code: D00007
– Error Text: Invalid currency code or too many decimal digits.
12.1.11.1.7.2.7.2  ReportingAmount <RptgAmt>
Presence: [1..1]
Definition: Amount expressed in the reporting currency.
Datatype: ImpliedCurrencyAndAmount on page 472
12.1.11.1.7.3  OtherMargin <OthrMrgn>
Presence: [0..*]
Definition: Provides details on the margin type and amount.
Impacted by: C17 VariationMarginTextualRule
OtherMargin <OthrMrgn> contains the following Margin4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  428
{Or     Code <Cd> [1..1] CodeSet 428
Or}     Proprietary <Prtry> [1..1] ± 429
   Amount <Amt> [1..1]  429
     OriginalCurrencyAmount <OrgnlCcyAmt> [0..1] Amount   'C1,
  'C7
429
     ReportingAmount <RptgAmt> [1..1] Amount 430
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 430
Constraints
• VariationMarginTextualRule
(Rule)
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 427
```

