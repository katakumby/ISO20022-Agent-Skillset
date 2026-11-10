---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["3 acmt.002.001.08 AccountDetailsConfirmationV08", "3.4 Message Building Blocks", "3.4.6 AccountParties <AcctPties>"]
file_pages: [48]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.002.001.08"]
---

# 3.4.6 AccountParties <AcctPties>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 48 to 48.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 48

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InvestmentAccountCategory <InvstmtAcctCtgy> [0..1] ± 4570
   Pledging <Pldgg> [0..1] CodeSet 4570
   Collateral <Coll> [0..1] CodeSet 4570
   ThirdPartyRights <ThrdPtyRghts> [0..1] ± 4571
   PowerOfAttorneyLevelOfControl <PwrOfAttnyLvlOfCtrl> [0..1] ± 4571
   AccountingStatus <AcctgSts> [0..1] ± 4571
   OpeningDate <OpngDt> [0..1] ± 4572
   ClosingDate <ClsgDt> [0..1] ± 4572
   NegativeIndicator <NegInd> [0..1] Indicator 4572
   ProcessingOrder <PrcgOrdr> [0..1] CodeSet 4572
   Liability <Lblty> [0..1] ± 4572
   InvestorProfile <InvstrPrfl> [0..*] ± 4573
   FiscalYear <FsclYr> [0..1] ± 4574
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
3.4.6 AccountParties <AcctPties>
Presence: [0..1]
Definition: Confirmation of information related to parties that are related to the account, for example,
primary account owner.
Approved by the Securities SEG on 27 January 2026 acmt.002.001.08 AccountDetailsConfirmationV08
Investment Funds - Maintenance 2025 - 2026 48 May 2026
```

