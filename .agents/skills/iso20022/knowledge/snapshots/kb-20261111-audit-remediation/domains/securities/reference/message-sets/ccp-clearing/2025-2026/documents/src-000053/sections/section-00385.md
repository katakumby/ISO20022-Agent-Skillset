---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.2 Message Datatypes", "12.2.2 CodeSet", "12.2.2.16 MarginProduct1Code"]
file_pages: [478]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.2.2.16 MarginProduct1Code

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 478 to 478.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 478

```text
External code sets can be downloaded from www.iso20022.org.
Type: CodeSet
Format
minLength 1
maxLength 4
12.2.2.16  MarginProduct1Code
Definition: Specifies the underlying product of the margin.
Type: CodeSet
CodeName Name Definition
EQUI Equities Specifies that the margin is related to
equities.
FIXI FixedIncome Specifies that the margin is related to
fixed income.
12.2.2.17  MarginType1Code
Definition: Indicates the type of margin, for example, initial margin, variation margin, initial deposit or
coupon margin.
Type: CodeSet
CodeName Name Definition
SEMA SettlementRiskMargin Margin required to cover the risk of non
settlement of the underlying. Also used
to cover the risk linked to the non
settlement on payment platforms (for
example TARGET2 vs CLS).
ADFM AdditionalDefaultFundMargin Additional margin required to cover the
daily risk encountered by the central
counterparty before the clearing member
is actually called to cover the default
fund. Indeed, central counterparty
calculates the margin on the default fund
on a daily basis but only calls the
clearing member at the end of the
month.
SCMA ShortChargeMargin Margin required to cover the
concentration risk linked to the default of
the seller of the "protection" (for example
CDS seller).
COMA CouponMargin Margin required to cover the non
payment of the monthly premium (for
credit derivatives).
UFMA UpfrontMargin Margin required to cover the non
payment of the upfront premium (for
credit derivatives).
CEMA CreditEventMargin Margin required to cover the risk of any
event linked to the underlying (for
example the payment default by the
issuer of a debt).
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 478
```

