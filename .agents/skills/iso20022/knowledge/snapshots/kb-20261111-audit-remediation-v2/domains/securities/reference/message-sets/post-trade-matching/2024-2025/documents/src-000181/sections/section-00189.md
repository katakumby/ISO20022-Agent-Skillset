---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.3 Amount", "7.1.3.3 OtherAmounts16", "7.1.3.3.31 RemunerationAmountRequest <RmnrtnAmtReq>"]
file_pages: [242]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.3.3.31 RemunerationAmountRequest <RmnrtnAmtReq>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 242 to 242.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 242

```text
MarketMemberFeeAmount <MktMmbFeeAmt> contains the following elements (see
"AmountAndDirection29" on page 228 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C10 228
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 229
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C10 229
   ForeignExchangeDetails <FXDtls> [0..1] ± 229
7.1.3.3.31  RemunerationAmountRequest <RmnrtnAmtReq>
Presence: [0..1]
Definition: Specifies that this information is available upon request.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.3.3.32  RemunerationAmount <RmnrtnAmt>
Presence: [0..1]
Definition: Specifies the source and amount of any other remuneration received or to be received by the
broker in connection with the transaction.
RemunerationAmount <RmnrtnAmt> contains the following elements (see "AmountAndDirection29"
on page 228 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C10 228
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 229
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C10 229
   ForeignExchangeDetails <FXDtls> [0..1] ± 229
7.1.3.3.33  BorrowingInterestAmount <BrrwgIntrstAmt>
Presence: [0..1]
Definition: Amount to be paid by the lender to the borrower calculated based on the interest rate.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 242 February 2025
```

