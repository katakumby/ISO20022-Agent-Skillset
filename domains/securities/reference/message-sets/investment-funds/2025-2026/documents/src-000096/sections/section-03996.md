---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.70 EnabledStatusReason1Code"]
file_pages: [5296]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.70 EnabledStatusReason1Code

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5296 to 5296.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5296

```text
66.2.2.70  EnabledStatusReason1Code
Definition: Specifies the reason for an enabled status.
Type: CodeSet
CodeName Name Definition
MODI Modified Modification to the account data is in
process.
66.2.2.71  EqualisationMethodologyType1Code
Definition: Methodology used for the allocation of the performance fees.
Type: CodeSet
CodeName Name Definition
COLI ContingentLiquidation Mandatory redemption of units
processed either at redemption or
crystallization, whose proceeds are due
to the asset manager as performance
fee. Performance fee to be paid by the
investor when the value of the
investment fund units were below their
applicable high-watermark on
subscription date, and above the high-
watermark on redemption date.
DDEP DepreciationDeposit Performance fee to be paid by the
investor when the net asset value
reaches the high-watermark if the net
asset value was under the high-
watermark on subscription date.
EQCR EqualisationCredit Prepayment amount to be paid by the
investor at the moment of the
subscription. The amount is based on
the positive difference between the gross
asset value at subscription and the high-
watermark, when the investment fund
units are subscribed to above their high-
watermark.
66.2.2.72  EUCapitalGain2Code
Definition: Specifies whether capital gain is in the scope of the European directive on taxation of
savings income in the form of interest payments (Council Directive 2003/48/EC 3 June) for an income
realised upon sale, a refund or redemption of shares and units etc.
Type: CodeSet
CodeName Name Definition
EUSI CapitalGainInScope Capital gain is in the scope of the
directive.
EUSO CapitalGainOutScope Capital gain is out of the scope of the
directive.
UKWN CapitalGainUnknown Unknown whether capital gain is in or
out of the scope of the directive.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5296 May 2026
```

