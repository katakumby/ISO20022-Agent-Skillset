---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.10 InvestmentAccount76", "66.1.24.10.1 Name <Nm>"]
file_pages: [4634]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.10.1 Name <Nm>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4634 to 4634.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4634

```text
Constraints
• AccountDataElementRule
One of the elements (Name, Designation, FundType, FundFamilyName, SecurityDetails,
AccountOwner, Intermediary, Account Servicer) must be present.
66.1.24.10.1  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
66.1.24.10.2  Designation <Dsgnt>
Presence: [0..1]
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
registered, for example, to a funds supermarket, but holdings for each investor have to be reconciled
individually.
Datatype: "Max35Text" on page 5403
66.1.24.10.3  FundType <FndTp>
Presence: [0..1]
Definition: Legal form of the fund, for example, UCITS, SICAV, OEIC, Unit Trust, and FCP.
Datatype: "Max35Text" on page 5403
66.1.24.10.4  FundFamilyName <FndFmlyNm>
Presence: [0..1]
Definition: Name of the investment fund family.
Datatype: "Max350Text" on page 5403
66.1.24.10.5  SecurityDetails <SctyDtls>
Presence: [0..1]
Definition: Detailed information about the investment fund associated to the account.
Impacted by: C15 "IdentificationGuideline"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4634 May 2026
```

