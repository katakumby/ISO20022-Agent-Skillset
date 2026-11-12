---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.2 CommonFinancialInstrumentAttributes12", "13.1.6.2.20 Issuance <Issnc>", "13.1.6.2.20.9 IssueSize <IsseSz>"]
file_pages: [267]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.2.20.9 IssueSize <IsseSz>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 267 to 267.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 267

```text
Definition: Figure used as a control to verify whether the information provided is correct. It represents
the issue size multiplied by the issue price.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 506
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
13.1.6.2.20.9  IssueSize <IsseSz>
Presence: [0..1]
Definition: Represents the total amount/quantity of the proceeds from the sale of all securities in the
initial offering. This amount/quantity is known after the new issue is priced.
Datatype: "Number" on page 532
13.1.6.2.20.10  IssuePrice <IssePric>
Presence: [0..1]
Definition: Initial issue price of the asset.
IssuePrice <IssePric> contains the following elements (see "PriceValue1" on page 498 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1 498
13.1.6.2.20.11  IssuanceDistribution <IssncDstrbtn>
Presence: [0..1]
Definition: Way in which the issue will be marketed to the primary market, via individual dealers (so
called non syndicated distribution) or via a syndicate of managers, underwriters and selling group
members (so called syndicated distribution).
IssuanceDistribution <IssncDstrbtn> contains one of the following
SecuritiesTransactionType31Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 268
Or}   Proprietary <Prtry> [1..1] ± 268
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 267 March 2024
```

