---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.14 InvestmentAccount75", "66.1.24.14.1 AccountStatusUpdateInstruction <AcctStsUpdInstr>"]
file_pages: [4647]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.14.1 AccountStatusUpdateInstruction <AcctStsUpdInstr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4647 to 4647.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4647

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PowerOfAttorneyLevelOfControl <PwrOfAttnyLvlOfCtrl> [0..1] ± 4658
   AccountingStatus <AcctgSts> [0..1] ± 4658
   OpeningDate <OpngDt> [0..1] ± 4659
   ClosingDate <ClsgDt> [0..1] ± 4659
   NegativeIndicator <NegInd> [0..1] Indicator 4659
   ProcessingOrder <PrcgOrdr> [0..1] CodeSet 4659
   Liability <Lblty> [0..1] ± 4659
   ModifiedInvestorProfile <ModfdInvstrPrfl> [0..*]  4660
     ModificationScopeIndication <ModScpIndctn> [1..1] CodeSet 4660
     InvestorProfile <InvstrPrfl> [1..1] ± 4660
   FiscalYear <FsclYr> [0..1] ± 4661
Constraints
• AccountElementRule
One of the elements (AccountStatusUpdateInstruction, Name, Designation, Type, OwnershipType,
TaxExemption, StatementFrequency, ReferenceCurrency, Language, IncomePreference,
ReinvestmentDetails, TaxWithholdingMethod, TaxReporting, LetterIntentDetails,
AccumulationRightReference, RequiredSignatoriesNumber, FundFamilyName,
ModifiedFinancialInstrumentDetails, RoundingDetails, Account Servicer, BlockedStatus,
AccountUsageType, ForeignStatusCertification, AccountSignatureDateTime,
TransactionChannelType, InvestmentAccountCategory, Pledging, Collateral, ThirdPartyRights,
PowerOfAttorneyLevelOfControl, AccountingStatus, OpeningDate, ClosingDate, NegativeIndicator,
ProcessingOrder, Liability, ModifiedInvestorProfile, FiscalYear) must be present.
• FinancialInstrumentDetailsGuideline
ModifiedFinancialInstrumentDetails/FinancialInstrumentDetails may be present if a single investment
fund is associated to the investment account. If several investment funds are associated to the
investment account, the FundFamilyName only should be specified.
• IncomePreferenceReinvestmentRule
If IncomePreference is CASH (Cash), then ReinvestmentDetails is not allowed.
On Condition
    /IncomePreference is equal to value 'Cash'
Following Must be True
    /ReinvestmentDetails[*] Must be absent
• ReinvestmentPercentageRule
Sum of all occurrences of ReinvestmentDetails/ReinvestmentPercentage must not be greater than
100.
66.1.24.14.1  AccountStatusUpdateInstruction <AcctStsUpdInstr>
Presence: [0..1]
Definition: Change of account status is instructed.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4647 May 2026
```

