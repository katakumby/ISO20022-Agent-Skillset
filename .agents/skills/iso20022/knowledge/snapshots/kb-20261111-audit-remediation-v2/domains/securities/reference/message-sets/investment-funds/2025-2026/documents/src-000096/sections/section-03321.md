---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.3 InvestmentAccount74", "66.1.24.3.1 Identification <Id>"]
file_pages: [4559, 4560]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.3.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4559 to 4560.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4559

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
66.1.24.3.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
66.1.24.3.2  AccountStatus <AcctSts>
Presence: [0..1]
Definition: Status of the account.
Impacted by: C6 "ClosedStatus1Rule", C7 "ClosedStatus2Rule", C8 "ClosedStatus3Rule", C9
"ClosedStatus4Rule", C10 "ClosedStatus5Rule", C11 "ClosedStatus6Rule", C14
"EnabledDisabledStatus1Rule", C15 "EnabledDisabledStatus2Rule", C32 "StatusElementRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4559 May 2026
```

## File page 4560

```text
AccountStatus <AcctSts> contains the following elements (see "AccountStatus2" on page 5174 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Enabled <Nbld> [0..1] ± 5176
   Disabled <Dsbld> [0..1] ± 5176
   Pending <Pdg> [0..1] ± 5177
   PendingOpening <PdgOpng> [0..1] ± 5177
   Proforma <Profrm> [0..1] ± 5177
   Closed <Clsd> [0..1] ± 5178
   ClosurePending <ClsrPdg> [0..1] ± 5178
   Other <Othr> [0..*] ± 5179
Constraints
• ClosedStatus1Rule
If Closed is present then Enabled is not allowed.
On Condition
    /Closed is present
Following Must be True
    /Enabled Must be absent
• ClosedStatus2Rule
If Closed is present then Disabled is not allowed.
On Condition
    /Closed is present
Following Must be True
    /Disabled Must be absent
• ClosedStatus3Rule
If Closed is present then Pending is not allowed.
On Condition
    /Closed is present
Following Must be True
    /Pending Must be absent
• ClosedStatus4Rule
If Closed is present then PendingOpening is not allowed.
On Condition
    /Closed is present
Following Must be True
    /PendingOpening Must be absent
• ClosedStatus5Rule
If Closed is present then Proforma is not allowed.
On Condition
    /Closed is present
Following Must be True
    /Proforma Must be absent
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4560 May 2026
```

