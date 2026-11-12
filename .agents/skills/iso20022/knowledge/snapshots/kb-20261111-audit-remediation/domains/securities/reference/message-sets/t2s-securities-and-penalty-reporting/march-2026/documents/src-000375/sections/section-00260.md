---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.12 Financial Instrument", "7.1.12.2 FinancialInstrument21", "7.1.12.2.2 SecuritiesForm <SctiesForm>"]
file_pages: [337]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.12.2.2 SecuritiesForm <SctiesForm>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 337 to 337.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 337

```text
with or without. Fund classes are typically denoted by a single character, for example, 'Class A', 'Class
2'.
Datatype: "Max35Text" on page 557
7.1.12.2.2  SecuritiesForm <SctiesForm>
Presence: [0..1]
Definition: Specifies the form, that is, ownership, of the security.
Datatype: "FormOfSecurity1Code" on page 511
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
7.1.12.2.3  DistributionPolicy <DstrbtnPlcy>
Presence: [0..1]
Definition: Income policy relating to a class type, that is, if income is paid out or retained in the fund.
Datatype: "DistributionPolicy1Code" on page 503
CodeName Name Definition
DIST Distribution Income is distributed to the investors in
the fund.
ACCU Accumulation Income is added to the capital of the
fund.
7.1.12.2.4  ProductGroup <PdctGrp>
Presence: [0..1]
Definition: Company specific description of a group of funds.
Datatype: "Max140Text" on page 556
7.1.12.2.5  UmbrellaName <UmbrllNm>
Presence: [0..1]
Definition: Name of the umbrella fund in which financial instrument is contained.
Datatype: "Max35Text" on page 557
7.1.12.2.6  BaseCurrency <BaseCcy>
Presence: [0..1]
Definition: Currency of the investment fund class.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 492
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 337 March 2026
```

