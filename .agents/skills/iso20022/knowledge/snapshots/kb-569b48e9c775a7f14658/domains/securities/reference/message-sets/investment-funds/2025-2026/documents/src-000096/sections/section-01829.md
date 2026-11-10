---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.7 FinancialInstrumentDetails <FinInstrmDtls>", "47.4.4.7.6 SecuritiesForm <SctiesForm>"]
file_pages: [2568]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.7.6 SecuritiesForm <SctiesForm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2568 to 2568.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2568

```text
policy, for example, with or without. Fund classes are typically denoted by a single character, for
example, 'Class A', 'Class 2'.
Datatype: "Max35Text" on page 5403
47.4.4.7.6  SecuritiesForm <SctiesForm>
Presence: [0..1]
Definition: Form, that is, ownership, of the security, for example, registered or bearer.
Datatype: "FormOfSecurity1Code" on page 5304
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
47.4.4.7.7  DistributionPolicy <DstrbtnPlcy>
Presence: [0..1]
Definition: Income policy relating to a class type, that is, if income is paid out or retained in the fund.
Datatype: "DistributionPolicy1Code" on page 5294
CodeName Name Definition
DIST Distribution Income is distributed to the investors in
the fund.
ACCU Accumulation Income is added to the capital of the
fund.
47.4.4.7.8  ProductGroup <PdctGrp>
Presence: [0..1]
Definition: Company specific description of a group of funds.
Datatype: "Max140Text" on page 5402
47.4.4.7.9  SeriesIdentification <SrsId>
Presence: [0..1]
Definition: Choice of formats for the identification of a series.
Impacted by: C34 "SeriesElementRule"
SeriesIdentification <SrsId> contains the following Series1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SeriesDate <SrsDt> [0..1] ± 2569
   SeriesName <SrsNm> [0..1] Text 2569
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2568 May 2026
```

