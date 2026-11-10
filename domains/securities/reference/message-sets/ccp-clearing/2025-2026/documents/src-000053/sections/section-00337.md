---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.11 Margin Call Calculation", "12.1.11.1 MarginCalculation2", "12.1.11.1.7 MarginTypeAmount <MrgnTpAmt>", "12.1.11.1.7.3 OtherMargin <OthrMrgn>", "12.1.11.1.7.3.2 Amount <Amt>", "12.1.11.1.7.3.2.2 ReportingAmount <RptgAmt>"]
file_pages: [430]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.11.1.7.3.2.2 ReportingAmount <RptgAmt>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 430 to 430.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 430

```text
Datatype: ActiveCurrencyAndAmount on page 470
Constraints
• ActiveCurrency
(Rule)
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
Error handling:
– Error severity: Fatal
– Error Code: D00005
– Error Text: Invalid currency code
• CurrencyAmount
(Rule)
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Error handling:
– Error severity: Fatal
– Error Code: D00007
– Error Text: Invalid currency code or too many decimal digits.
12.1.11.1.7.3.2.2  ReportingAmount <RptgAmt>
Presence: [1..1]
Definition: Amount expressed in the reporting currency.
Datatype: ImpliedCurrencyAndAmount on page 472
12.1.11.1.7.3.3  CreditDebitIndicator <CdtDbtInd>
Presence: [0..1]
Definition: Specifies whether the margin type position is short or long, that is, whether the balance is a
negative or positive balance.
Datatype: CreditDebitCode on page 476
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
12.1.11.2  MarginCalculation1
Definition: Provides the total margin amount, the collateral amount on deposit and the total minimum
requirement that used to calculate the margin result, either an excess or a deficit.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 430
```

