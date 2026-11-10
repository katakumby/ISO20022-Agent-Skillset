---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.4 AggregateBalancePerSafekeepingPlace4", "66.1.5.4.11 BalanceBreakdownDetails <BalBrkdwnDtls>"]
file_pages: [4367]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.4.11 BalanceBreakdownDetails <BalBrkdwnDtls>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4367 to 4367.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4367

```text
ForeignExchangeDetails <FXDtls> contains the following elements (see "ForeignExchangeTerms6"
on page 4530 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C2 4531
   QuotedCurrency <QtdCcy> [1..1] CodeSet C2 4531
   ExchangeRate <XchgRate> [1..1] Rate 4531
   QuotationDate <QtnDt> [0..1] DateTime 4531
   QuotingInstitution <QtgInstn> [0..1] ± 4531
66.1.5.4.11  BalanceBreakdownDetails <BalBrkdwnDtls>
Presence: [0..*]
Definition: Net position of a segregated holding of a single security within the overall position held in a
securities account, eg, sub-balance per status.
BalanceBreakdownDetails <BalBrkdwnDtls> contains the following elements (see
"SubBalanceInformation2" on page 4359 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] ± 4360
{Or   SubBalanceType <SubBalTp> [1..1] CodeSet 4360
Or}   ExtendedSubBalanceType <XtndedSubBalTp> [1..1] Text 4362
   AdditionalBalanceBreakdownDetails
<AddtlBalBrkdwnDtls>
[0..*] ± 4362
66.1.5.4.12  AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls>
Presence: [0..*]
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account.
AdditionalBalanceBreakdownDetails <AddtlBalBrkdwnDtls> contains the following elements (see
"AdditionalBalanceInformation2" on page 4367 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Quantity <Qty> [1..1] ± 4368
{Or   SubBalanceType <SubBalTp> [1..1] CodeSet 4368
Or}   ExtendedSubBalanceType <XtndedSubBalTp> [1..1] Text 4369
66.1.5.5  AdditionalBalanceInformation2
Definition: Net position of a segregated holding of a single security within the overall position held in the
securities account, eg, sub-balance per status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4367 May 2026
```

