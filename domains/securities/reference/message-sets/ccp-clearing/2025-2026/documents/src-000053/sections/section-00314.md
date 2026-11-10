---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.10 InvestmentFundCashForecast", "12.1.10.1 DefaultFund1", "12.1.10.1.3 Contribution <Cntrbtn>", "12.1.10.1.3.1 Account <Acct>"]
file_pages: [403]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.10.1.3.1 Account <Acct>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 403 to 403.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 403

```text
Contribution <Cntrbtn> contains the following Contribution1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Account <Acct> [0..1] ± 403
   RequiredAmount <ReqrdAmt> [1..1] Amount   'C1,
  'C7
403
   IncreaseCoverageAmount <IncrCvrgAmt> [0..1] Amount   'C1,
  'C7
404
   NonClearingMember <NonClrMmb> [0..1] ± 404
12.1.10.1.3.1  Account <Acct>
Presence: [0..1]
Definition: Segregation done by the central counterparty based on trading venues/products or other
attributes.
Account <Acct> contains one of the following elements (see AccountIdentification4Choice on
page 376 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet   'C8 376
Or}   Other <Othr> [1..1] ± 377
12.1.10.1.3.2  RequiredAmount <ReqrdAmt>
Presence: [1..1]
Definition: Total contribution required by the clearing member to participate to the default fund.
Impacted by:   'C1 ActiveCurrency  ',   'C7 CurrencyAmount  '
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
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 403
```

