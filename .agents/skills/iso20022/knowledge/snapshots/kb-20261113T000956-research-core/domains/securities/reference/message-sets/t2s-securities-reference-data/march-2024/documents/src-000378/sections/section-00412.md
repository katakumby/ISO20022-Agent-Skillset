---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.16 Transaction Type", "13.1.16.1 TradeTransactionCondition7Choice", "13.1.16.1.2 Proprietary <Prtry>"]
file_pages: [505]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.16.1.2 Proprietary <Prtry>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 505 to 505.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 505

```text
CodeName Name Definition
SCCR SpecialCumCapitalRepayments Indicates whether the trade is executed
special cum capital repayments.
SECR SpecialExCapitalRepayments Indicates whether the trade is executed
special ex capital repayments.
CAST CashSettlement Indicates whether the trade is executed
with a cash settlement.
SPPR SpecialPrice Indicates whether the trade is executed
with a special price.
SPCU SpecialCumDividend Indicates whether the trade is executed
with a special cum
dividend, that is, buying after the ex date
and getting the dividend.
SPEX SpecialExDividend Indicates whether the trade is executed
with a special ex
dividend, that is, selling before the ex
date without the coupon.
GTDL GuaranteedDelivery Indicates whether the delivery of the
financial instrument on settlement date
is guaranteed.
13.1.16.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trade transaction condition expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.2 Message Datatypes
13.2.1 Amount
13.2.1.1  ActiveCurrencyAnd13DecimalAmount
Definition: A number of monetary units specified in an active currency where the unit of currency is
explicit and compliant with ISO 4217. The number of fractional digits (or minor unit of currency) is not
checked as per ISO 4217: It must be lesser than or equal to 13.
Note: The decimal separator is a dot.
Type: Amount
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 505 March 2024
```

