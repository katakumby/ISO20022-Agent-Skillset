---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.14 InvestmentAccount75", "66.1.24.14.13 TaxReporting <TaxRptg>"]
file_pages: [4651]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.14.13 TaxReporting <TaxRptg>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4651 to 4651.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4651

```text
Definition: Method by which the tax (withholding tax) is to be processed, that is, either withheld at
source or tax information is reported to tax authorities or tax information is reported due to the provision
of a tax certificate.
Datatype: "TaxWithholdingMethod3Code" on page 5376
CodeName Name Definition
MITX MinorityInterestTax Minority interest tax is withheld.
INVE InvestmentCompany Withholding tax is applied to an
investment company.
ACCT Accountant Dividend tax is exempt according to the
accountant.
EXMT Exempt Dividend tax is exempt.
REPT ReportTax Tax information is reported to the tax
authorities and therefore not withheld at
source.
CRTF TaxCertificate Tax certificate is provided by the
beneficiary from its tax authority in its
country of residence. Therefore, the
obligation of withholding tax is waived
and tax information will be reported to
the tax authorities.
WHCO WithholdingCorporateTax Withholding tax is applied to a corporate.
WTHD WithholdTax Tax is withheld at source.
WTRE WithholdTaxAndReport Tax is withheld at source and the tax
information is also reported to the tax
authorities.
66.1.24.14.13  TaxReporting <TaxRptg>
Presence: [0..*]
Definition: Details for the reporting of tax, for example, the country of taxation.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4651 May 2026
```

