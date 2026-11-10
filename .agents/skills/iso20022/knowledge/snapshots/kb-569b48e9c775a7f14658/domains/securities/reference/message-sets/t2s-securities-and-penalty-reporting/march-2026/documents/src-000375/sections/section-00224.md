---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.14 Balance30", "7.1.5.14.3 SubAccountDetails <SubAcctDtls>", "7.1.5.14.3.4 BalanceForSubAccount <BalForSubAcct>", "7.1.5.14.3.4.11 PriceDetails <PricDtls>"]
file_pages: [300]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.14.3.4.11 PriceDetails <PricDtls>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 300 to 300.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 300

```text
CodeName Name Definition
CASH Cash Option to choose cash.
SECU Security Distribution of securities to holders.
7.1.5.14.3.4.11  PriceDetails <PricDtls>
Presence: [0..*]
Definition: Price of the financial instrument in one or more currencies.
Impacted by: C41 "ValueRule"
PriceDetails <PricDtls> contains the following elements (see "PriceInformation20" on page 447 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 447
   Value <Val> [1..1] ± 447
   ValueType <ValTp> [1..1] ± 448
   SourceOfPrice <SrcOfPric> [0..1] ± 448
   QuotationDate <QtnDt> [0..1] ± 448
Constraints
• ValueRule
If TypeOfPriceCode is not MRKT, then Value may not be expressed with UnknownIndicator.
7.1.5.14.3.4.12  ForeignExchangeDetails <FXDtls>
Presence: [0..*]
Definition: Information needed to process a currency exchange or conversion.
ForeignExchangeDetails <FXDtls> contains the following elements (see "ForeignExchangeTerms34"
on page 343 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C2 343
   QuotedCurrency <QtdCcy> [1..1] CodeSet C2 344
   ExchangeRate <XchgRate> [1..1] Rate 344
   QuotationDate <QtnDt> [0..1] DateTime 344
   QuotingInstitution <QtgInstn> [0..1] ± 344
7.1.5.14.3.4.13  DaysAccrued <DaysAcrd>
Presence: [0..1]
Definition: Specifies the number of days used for calculating the accrued interest amount.
Datatype: "Number" on page 554
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 300 March 2026
```

