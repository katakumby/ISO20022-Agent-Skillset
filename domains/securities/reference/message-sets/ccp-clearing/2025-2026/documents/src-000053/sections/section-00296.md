---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.4 Collateral", "12.1.4.2 Collateral6", "12.1.4.2.3 CollateralType <CollTp>"]
file_pages: [385]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.4.2.3 CollateralType <CollTp>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 385 to 385.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 385

```text
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
12.1.4.2.3  CollateralType <CollTp>
Presence: [1..1]
Definition: Provides the type of collateral, such as securities or cash.
Datatype: CollateralType1Code on page 475
CodeName Name Definition
CASH Cash Collateral type is cash.
SECU Securities Collateral type is securities.
LCRE LetterOfCredit Instrument issued by a bank substituting
its name and credit standing for that of
its customer. A letter of credit is a written
undertaking of the bank, issued for the
account of a customer (the applicant), to
honour a demand for payment, upon the
beneficiary's compliance with the terms
and conditions set forth in the
undertaking.
OTHR Other Other assets that could be used as
collateral.
12.1.5 Currency Exchange
12.1.5.1  ForeignExchangeTerms17
Definition: Provides information about the terms of the foreign exchange transaction.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 385
```

