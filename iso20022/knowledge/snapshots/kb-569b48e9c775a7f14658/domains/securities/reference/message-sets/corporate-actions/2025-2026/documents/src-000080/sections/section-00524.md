---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "9.4 Message Building Blocks", "9.4.9 CorporateActionConfirmationDetails <CorpActnConfDtls>", "9.4.9.4 CashMovementDetails <CshMvmntDtls>", "9.4.9.4.5 ValueDate <ValDt>"]
file_pages: [688]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9.4.9.4.5 ValueDate <ValDt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 688 to 688.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 688

```text
Definition: Date/Time of the posting (credit or debit) to the account that was initially communicated in
the confirmation.
OriginalPostingDate <OrgnlPstngDt> contains one of the following elements (see
"DateAndDateTime2Choice" on page 848 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 848
Or}   DateTime <DtTm> [1..1] DateTime 849
9.4.9.4.5  ValueDate <ValDt>
Presence: [0..1]
Definition: Date/time when calculating economic benefit for a cash amount.
Datatype: "ISODate" on page 1243
9.4.9.4.6  PostingAmount <PstngAmt>
Presence: [1..1]
Definition: Amount of money that is to be/was posted to the account.
Impacted by: C1 "ActiveCurrency", C6 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 1156
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
9.4.10 AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Provides additional information.
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 688 February 2026
```

