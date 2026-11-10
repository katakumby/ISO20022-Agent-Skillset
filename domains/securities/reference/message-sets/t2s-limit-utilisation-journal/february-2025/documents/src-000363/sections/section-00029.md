---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000363"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.3 Amount"]
file_pages: [31]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.3 Amount

Source: [src-000363](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart2_Target2Securities_LimitUtilisationJournal_v1.pdf`. Locator: one-based file pages 31 to 31.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 31

```text
4.1.3 Amount
4.1.3.1  Amount2Choice
Definition: Choice between an amount with or without the currency.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountWithoutCurrency <AmtWthtCcy> [1..1] Amount 31
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C4 31
4.1.3.1.1  AmountWithoutCurrency <AmtWthtCcy>
Presence: [1..1]
Definition: Number of monetary units specified in a currency where the unit of currency is implied by the
context.
Datatype: "ImpliedCurrencyAndAmount" on page 40
4.1.3.1.2  AmountWithCurrency <AmtWthCcy>
Presence: [1..1]
Definition: Number of monetary units specified in a currency where the unit of currency is explicit.
Impacted by: C1 "ActiveCurrency", C4 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 40
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
4.1.4 Date Time
4.1.4.1  DateAndDateTime2Choice
Definition: Choice between a date or a date and time format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 32
Or}   DateTime <DtTm> [1..1] DateTime 32
Approved by the Securities on the 16th January 2025 and Payments SEG on
the 24th January 2025 under the lead of the Securities SEG.
Message Items Types
Target2-Securities - Limit Utilisation Journal 31 February 2025
```

