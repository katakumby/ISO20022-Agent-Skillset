---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.10 InvestmentFundCashForecast", "12.1.10.1 DefaultFund1", "12.1.10.1.4 IncreaseCoverageAmount <IncrCvrgAmt>"]
file_pages: [405]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.10.1.4 IncreaseCoverageAmount <IncrCvrgAmt>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 405 to 405.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 405

```text
NonClearingMember <NonClrMmb> contains the following elements (see
PartyIdentificationAndAccount31 on page 450 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 450
   AlternateIdentification <AltrnId> [0..1] ± 450
   AdditionalInformation <AddtlInf> [0..1] ± C3 451
   ClearingAccount <ClrAcct> [0..1] ± 451
12.1.10.1.4  IncreaseCoverageAmount <IncrCvrgAmt>
Presence: [0..1]
Definition: Additional amount that the clearing member will have to provide to cover a risk increase. This
results from a risk management decision depending on central counterparty specific criteria.
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
Note: The decimal separator is a dot.
Error handling:
– Error severity: Fatal
– Error Code: D00007
– Error Text: Invalid currency code or too many decimal digits.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 405
```

