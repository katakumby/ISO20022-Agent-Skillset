---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["2 acmt.001.001.08 AccountOpeningInstructionV08", "2.4 Message Building Blocks", "2.4.6 AccountParties <AcctPties>"]
file_pages: [29]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.001.001.08"]
---

# 2.4.6 AccountParties <AcctPties>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 29 to 29.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 29

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountingStatus <AcctgSts> [0..1] ± 4630
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
2.4.6 AccountParties <AcctPties>
Presence: [1..1]
Definition: Information related to parties that are related to the account, for example, primary account
owner.
Approved by the Securities SEG on 27 January 2026 acmt.001.001.08 AccountOpeningInstructionV08
Investment Funds - Maintenance 2025 - 2026 29 May 2026
```

