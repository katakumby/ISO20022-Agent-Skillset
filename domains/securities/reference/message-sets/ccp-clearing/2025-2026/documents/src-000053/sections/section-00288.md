---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.2 Account Identification", "12.1.2.2 AccountIdentification4Choice", "12.1.2.2.2 Other <Othr>"]
file_pages: [377]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.2.2.2 Other <Othr>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 377 to 377.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 377

```text
– Error Text: Invalid IBAN format or invalid check digits.
12.1.2.2.2  Other <Othr>
Presence: [1..1]
Definition: Unique identification of an account, as assigned by the account servicer, using an
identification scheme.
Other <Othr> contains the following elements (see GenericAccountIdentification1 on page 374 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 374
   SchemeName <SchmeNm> [0..1]  374
{Or     Code <Cd> [1..1] CodeSet 374
Or}     Proprietary <Prtry> [1..1] Text 374
   Issuer <Issr> [0..1] Text 374
12.1.3 Amount
12.1.3.1  AmountAndDirection21
Definition: Amount of money debited or credited on the books of an account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C2,
  'C6
377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 378
12.1.3.1.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money in the cash entry.
Impacted by:   'C2 ActiveOrHistoricCurrency  ',   'C6 CurrencyAmount  '
Datatype: ActiveOrHistoricCurrencyAndAmount on page 471
Constraints
• ActiveOrHistoricCurrency
(Rule)
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 377
```

