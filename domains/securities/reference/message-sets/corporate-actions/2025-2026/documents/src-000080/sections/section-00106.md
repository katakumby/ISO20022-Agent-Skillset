---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.21 RateAndAmountDetails <RateAndAmtDtls>", "3.4.11.21.10 IssuerDeclaredExchangeRate <IssrDclrdXchgRate>"]
file_pages: [162]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.21.10 IssuerDeclaredExchangeRate <IssrDclrdXchgRate>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 162 to 162.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 162

```text
Definition: Amount included in the dividend/NAV that is identified as gains directly or indirectly derived
from interest payments, for example, in the context of the EU Savings directive.
TaxableIncomePerDividendShare <TaxblIncmPerDvddShr> contains the following elements (see
"RateTypeAndAmountAndStatus26" on page 906 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RateType <RateTp> [1..1]  907
{Or     Code <Cd> [1..1] CodeSet 907
Or}     Proprietary <Prtry> [1..1] ± 907
   Amount <Amt> [1..1] Amount C1 908
   RateStatus <RateSts> [0..1]  C52 908
{Or     Code <Cd> [1..1] CodeSet 908
Or}     Proprietary <Prtry> [1..1] ± 908
3.4.11.21.10  IssuerDeclaredExchangeRate <IssrDclrdXchgRate>
Presence: [0..1]
Definition: Exchange rate (provided by the issuer) between the dividend or interest rate in the paid
currency and the declared dividend or interest rate.
IssuerDeclaredExchangeRate <IssrDclrdXchgRate> contains the following elements (see
"ForeignExchangeTerms38" on page 871 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 872
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 872
   ExchangeRate <XchgRate> [1..1] Rate 872
3.4.11.21.11  TaxOnIncome <TaxOnIncm>
Presence: [0..1]
Definition: Overall tax withheld at source by fund managers prior to considering the tax obligation of
each unit holder.
TaxOnIncome <TaxOnIncm> contains one of the following elements (see
"RateAndAmountFormat57Choice" on page 1123 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1123
Or   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 1123
Or}   Amount <Amt> [1..1] Amount C1 1123
3.4.11.21.12  BidInterval <BidIntrvl>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 162 February 2026
```

