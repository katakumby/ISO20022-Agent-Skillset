---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.24 SecuritiesMovementDetails <SctiesMvmntDtls>", "3.4.11.24.14 CurrencyOption <CcyOptn>"]
file_pages: [188]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.24.14 CurrencyOption <CcyOptn>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 188 to 188.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 188

```text
FractionDisposition <FrctnDspstn> contains one of the following elements (see
"FractionDispositionType26Choice" on page 899 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 899
Or}   Proprietary <Prtry> [1..1] ± 900
3.4.11.24.14  CurrencyOption <CcyOptn>
Presence: [0..1]
Definition: Currency in which cash proceeds are to be credited/debited.
Impacted by: C2 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 1157
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
3.4.11.24.15  TradingPeriod <TradgPrd>
Presence: [0..1]
Definition: Period during which intermediate or outturn securities are tradable in a secondary market.
TradingPeriod <TradgPrd> contains one of the following elements (see "Period12Choice" on
page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
3.4.11.24.16  DateDetails <DtDtls>
Presence: [1..1]
Definition: Provides information about the dates related to securities movement.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 188 February 2026
```

