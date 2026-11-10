---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.1.3.2.20 Issuance <Issnc>", "28.4.2.1.3.2.20.9 IssueSize <IsseSz>"]
file_pages: [1507]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.2.20.9 IssueSize <IsseSz>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1507 to 1507.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1507

```text
Definition: Figure used as a control to verify whether the information provided is correct. It represents
the issue size multiplied by the issue price.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
28.4.2.1.3.2.20.9  IssueSize <IsseSz>
Presence: [0..1]
Definition: Represents the total amount/quantity of the proceeds from the sale of all securities in the
initial offering. This amount/quantity is known after the new issue is priced.
Datatype: "Number" on page 3324
28.4.2.1.3.2.20.10  IssuePrice <IssePric>
Presence: [0..1]
Definition: Initial issue price of the asset.
IssuePrice <IssePric> contains the following elements (see "PriceValue1" on page 3109 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1 3109
28.4.2.1.3.2.20.11  IssuanceDistribution <IssncDstrbtn>
Presence: [0..1]
Definition: Way in which the issue will be marketed to the primary market, via individual dealers (so
called non syndicated distribution) or via a syndicate of managers, underwriters and selling group
members (so called syndicated distribution).
IssuanceDistribution <IssncDstrbtn> contains one of the following
SecuritiesTransactionType31Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1508
Or}   Proprietary <Prtry> [1..1] ± 1508
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1507 August 2026
```

