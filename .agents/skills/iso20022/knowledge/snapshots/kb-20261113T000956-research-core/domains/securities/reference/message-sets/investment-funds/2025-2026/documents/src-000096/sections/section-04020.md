---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.130 InvestorType4Code"]
file_pages: [5328]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.130 InvestorType4Code

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5328 to 5328.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5328

```text
66.2.2.130  InvestorType4Code
Definition: Specifies the type of investor.
Type: CodeSet
CodeName Name Definition
BOT3 BothProfessionalPerSeAndElectiveProfessional Investor is both professional per se and
elective professional.
NPRF NotProfessionalPerSeElectiveProfessional Investor is neither professional per se or
elective professional.
PRF3 ProfessionalPerSeNotElectiveProfessional Investor is professional per se but not
elective professional.
PRF4 ElectiveProfessionalNotProfessionalPerSe Investor is an elective professional but
not professional per se.
66.2.2.131  KnowYourCustomerCheckType1Code
Definition: Specifies the type of Know Your Customer (KYC) or anti-money laundering due diligence to
which the investor has been subjected.
Type: CodeSet
CodeName Name Definition
ENHA Enhanced Enhanced check, typically carried out on
accounts that are considered high risk.
ORDN Ordinary Ordinary check, typically carried out on
standard accounts.
SIMP Simple Simple check, typically carried out on
accounts that have a low risk of anti-
money laundering, such as an account
owned by a financial institution.
66.2.2.132  LanguageCode
Definition: Specifies a language.
Type: CodeSet
Constraints
• ValidationByTable
Must be a valid terrestrial language.
66.2.2.133  LateReport1Code
Definition: Specifies whether a transaction report is late.
Type: CodeSet
CodeName Name Definition
LAT1 Late The confirmation is late.
LAT2 LateBecausePartial The confirmation is late because the
trade was executed as a number of
partials.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5328 May 2026
```

