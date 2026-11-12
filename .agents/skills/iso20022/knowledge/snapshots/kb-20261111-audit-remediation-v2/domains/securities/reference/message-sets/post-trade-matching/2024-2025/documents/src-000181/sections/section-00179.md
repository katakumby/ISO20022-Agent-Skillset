---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.3 Amount", "7.1.3.3 OtherAmounts16", "7.1.3.3.1 ChargesFees <ChrgsFees>"]
file_pages: [232]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.3.3.1 ChargesFees <ChrgsFees>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 232 to 232.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 232

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RemunerationAmount <RmnrtnAmt> [0..1] ± 242
   BorrowingInterestAmount <BrrwgIntrstAmt> [0..1] ± 242
   BorrowingFee <BrrwgFee> [0..1] ± 243
   NetMarketValue <NetMktVal> [0..1] ± 243
   RemainingFaceValue <RmngFaceVal> [0..1] ± 243
   RemainingBookValue <RmngBookVal> [0..1] ± 244
   ClearingBrokerCommission <ClrBrkrComssn> [0..1] ± 244
   DifferenceInPrice <DiffInPric> [0..1] ± 244
   OddLotFee <OddLotFee> [0..1] Indicator 245
7.1.3.3.1  ChargesFees <ChrgsFees>
Presence: [0..1]
Definition: Amount of money paid for the provision of financial services that cannot be categorised by
another qualifier.
ChargesFees <ChrgsFees> contains the following elements (see "AmountAndDirection29" on
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
7.1.3.3.2  CountryNationalFederalTax <CtryNtlFdrlTax>
Presence: [0..1]
Definition: Amount of country, national or federal tax charged by the jurisdiction in which the account
servicer is located.
CountryNationalFederalTax <CtryNtlFdrlTax> contains the following elements (see
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
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 232 February 2025
```

