---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.32 Transaction Type", "82.1.32.3 TransactionActivity3Choice", "82.1.32.3.2 Proprietary <Prtry>"]
file_pages: [3208]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.32.3.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3208 to 3208.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3208

```text
CodeName Name Definition
BOLE BorrowingLendingActivity Transaction relates to lending/borrowing.
CLAI MarketClaim Transaction relates to a market claim
following a corporate action.
COLL CollateralActivity Transaction relates to collateral.
CORP CorporateActionActivity Transaction relates to corporate action.
SETT SettlementandClearingActivity Transaction relates to settlement and
clearing.
82.1.32.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Transaction type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.2 Message Datatypes
82.2.1 Amount
82.2.1.1  ActiveCurrencyAnd13DecimalAmount
Definition: A number of monetary units specified in an active currency where the unit of currency is
explicit and compliant with ISO 4217. The number of fractional digits (or minor unit of currency) is not
checked as per ISO 4217: It must be lesser than or equal to 13.
Note: The decimal separator is a dot.
Type: Amount
This data type contains the following XML attribute:
Name Attribute XML Name Datatype
Currency Ccy "ActiveCurrencyCode" on page 3212
Format
minInclusive 0
totalDigits 18
fractionDigits 13
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3208 August 2026
```

