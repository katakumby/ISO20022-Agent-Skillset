---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.3 Amount", "7.1.3.3 OtherAmounts16", "7.1.3.3.10 RegulatoryAmount <RgltryAmt>"]
file_pages: [235]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.3.3.10 RegulatoryAmount <RgltryAmt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 235 to 235.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 235

```text
Definition: An amount that is not indicated by a known business denomination.
Other <Othr> contains the following elements (see "AmountAndDirection29" on page 228 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C10 228
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 229
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C10 229
   ForeignExchangeDetails <FXDtls> [0..1] ± 229
7.1.3.3.10  RegulatoryAmount <RgltryAmt>
Presence: [0..1]
Definition: Amount of money charged by a regulatory authority, for example, Securities and Exchange
fees.
RegulatoryAmount <RgltryAmt> contains the following elements (see "AmountAndDirection29" on
page 228 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C10 228
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 229
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C10 229
   ForeignExchangeDetails <FXDtls> [0..1] ± 229
7.1.3.3.11  SpecialConcession <SpclCncssn>
Presence: [0..1]
Definition: Amount of drawdown or other reduction from or in addition to the deal price.
SpecialConcession <SpclCncssn> contains the following elements (see "AmountAndDirection29" on
page 228 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C10 228
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 229
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C10 229
   ForeignExchangeDetails <FXDtls> [0..1] ± 229
7.1.3.3.12  StampDuty <StmpDty>
Presence: [0..1]
Definition: Amount of stamp duty.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 235 February 2025
```

