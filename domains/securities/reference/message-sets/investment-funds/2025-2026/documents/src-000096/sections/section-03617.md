---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.29 AllOtherCash1", "66.1.28.29.2 Currency <Ccy>"]
file_pages: [4867]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.29.2 Currency <Ccy>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4867 to 4867.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4867

```text
Definition: Indicates whether all remaining assets in a portfolio not listed for transfer should be
liquidated and transferred as cash.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.28.29.2  Currency <Ccy>
Presence: [0..1]
Definition: Currency of the cash.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.28.30  AdditiononalInformation13
Definition: Restrictions, remarks or notes that may be applied to an account or investment plan.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Limitation <Lmttn> [0..1] Text 4867
   AdditionalInformation <AddtlInf> [0..1] Text 4867
   AccountValidation <AcctVldtn> [0..1] Text 4868
   Type <Tp> [0..1] Text 4868
   Regulator <Rgltr> [0..1] ± 4868
   Status <Sts> [0..1]  4868
{Or     Code <Cd> [1..1] CodeSet 4868
Or}     Proprietary <Prtry> [1..1] ± 4869
   Period <Prd> [0..1] ± 4869
66.1.28.30.1  Limitation <Lmttn>
Presence: [0..1]
Definition: Restrictions and/or limitations on the account or party.
Datatype: "Max350Text" on page 5403
66.1.28.30.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4867 May 2026
```

