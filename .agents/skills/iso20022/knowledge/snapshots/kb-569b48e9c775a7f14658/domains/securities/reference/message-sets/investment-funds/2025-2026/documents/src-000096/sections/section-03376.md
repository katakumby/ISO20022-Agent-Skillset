---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.9 InvestmentAccount73", "66.1.24.9.1 Identification <Id>"]
file_pages: [4620]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.9.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4620 to 4620.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4620

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OpeningDate <OpngDt> [0..1] ± 4630
   ClosingDate <ClsgDt> [0..1] ± 4630
   NegativeIndicator <NegInd> [0..1] Indicator 4631
   ProcessingOrder <PrcgOrdr> [0..1] CodeSet 4631
   Liability <Lblty> [0..1] ± 4631
   InvestorProfile <InvstrPrfl> [0..*] ± 4631
   FiscalYear <FsclYr> [0..1] ± 4632
Constraints
• FinancialInstrumentDetailsGuideline
FinancialInstrumentDetails may be present if a single investment fund is associated to the
investment account. If several investment funds are associated to the investment account, the
FundFamilyName only should be specified.
• IncomePreferenceReinvestment1Rule
If IncomePreference is CASH (Cash), then ReinvestmentDetails is not allowed.
On Condition
    /IncomePreference is equal to value 'Cash'
Following Must be True
    /ReinvestmentDetails[*] Must be absent
• ReinvestmentPercentage1Rule
Sum of all occurrences of ReinvestmentDetails/ReinvestmentPercentage must not be greater than
100.
66.1.24.9.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
66.1.24.9.2  Name <Nm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
66.1.24.9.3  Designation <Dsgnt>
Presence: [0..1]
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4620 May 2026
```

