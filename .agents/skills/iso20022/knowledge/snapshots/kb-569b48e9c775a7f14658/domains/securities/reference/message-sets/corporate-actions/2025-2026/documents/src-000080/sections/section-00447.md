---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.10 SecuritiesMovementDetails <SctiesMvmntDtls>", "8.4.12.10.13 CurrencyOption <CcyOptn>"]
file_pages: [601]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.10.13 CurrencyOption <CcyOptn>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 601 to 601.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 601

```text
FractionDisposition <FrctnDspstn> contains one of the following elements (see
"FractionDispositionType27Choice" on page 894 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 894
Or}   Proprietary <Prtry> [1..1] ± 894
8.4.12.10.13  CurrencyOption <CcyOptn>
Presence: [0..1]
Definition: Currency in which cash proceeds are to be credited or debited.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 1157
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
8.4.12.10.14  DateDetails <DtDtls>
Presence: [1..1]
Definition: Provides information about the dates related to securities movement.
DateDetails <DtDtls> contains the following SecurityDate25 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PostingDate <PstngDt> [1..1] ± 601
   AvailableDate <AvlblDt> [0..1] ± 602
   PariPassuDate <PrpssDt> [0..1] ± 602
   DividendRankingDate <DvddRnkgDt> [0..1] ± 602
   EarliestPaymentDate <EarlstPmtDt> [0..1] ± 603
   PaymentDate <PmtDt> [0..1] ± 603
8.4.12.10.14.1  PostingDate <PstngDt>
Presence: [1..1]
Definition: Date of the posting (credit or debit) to the account.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 601 February 2026
```

