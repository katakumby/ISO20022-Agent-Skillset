---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.10 SecuritiesMovementDetails <SctiesMvmntDtls>", "8.4.12.10.15 RateDetails <RateDtls>", "8.4.12.10.15.5 FiscalStamp <FsclStmp>"]
file_pages: [606]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.10.15.5 FiscalStamp <FsclStmp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 606 to 606.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 606

```text
8.4.12.10.15.5  FiscalStamp <FsclStmp>
Presence: [0..1]
Definition: Percentage of fiscal tax to apply.
Datatype: "Percentage14Rate" on page 1247
8.4.12.10.15.6  ApplicableRate <AplblRate>
Presence: [0..1]
Definition: Rate applicable to the event announced, for example, redemption rate for a redemption
event.
Datatype: "Percentage14Rate" on page 1247
8.4.12.10.15.7  TaxCreditRate <TaxCdtRate>
Presence: [0..1]
Definition: Amount of money per equity allocated as the result of a tax credit.
TaxCreditRate <TaxCdtRate> contains one of the following elements (see "RateFormat27Choice" on
page 1106 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 1106
Or}   Amount <Amt> [1..1] Amount C1 1107
8.4.12.10.15.8  FinancialTransactionTaxRate <FinTxTaxRate>
Presence: [0..1]
Definition: Rate of financial transaction tax.
Datatype: "Percentage14Rate" on page 1247
8.4.12.10.15.9  WithholdingTaxRate <WhldgTaxRate>
Presence: [0..*]
Definition: Percentage of a cash distribution that will be withheld by the tax authorities of the jurisdiction
of the issuer, for which a relief at source and/or reclaim may be possible.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 606 February 2026
```

