---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "3.4 Message Building Blocks", "3.4.9 SubAccountDetails <SubAcctDtls>", "3.4.9.5 BalanceForSubAccount <BalForSubAcct>", "3.4.9.5.17 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>", "3.4.9.5.17.1 SafekeepingPlace <SfkpgPlc>"]
file_pages: [125]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3.4.9.5.17.1 SafekeepingPlace <SfkpgPlc>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 125 to 125.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 125

```text
BalanceAtSafekeepingPlace <BalAtSfkpgPlc> contains the following
AggregateBalancePerSafekeepingPlace42 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlace <SfkpgPlc> [1..1] ± C33 125
   PlaceOfListing <PlcOfListg> [0..1] ± 126
   Pledgee <Pldgee> [0..1] ± C25 126
   AggregateBalance <AggtBal> [1..1] ± 127
   PriceDetails <PricDtls> [1..*] ± C41 127
   ForeignExchangeDetails <FXDtls> [0..*] ± 128
   DaysAccrued <DaysAcrd> [0..1] Quantity 128
   AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [1..1] ± 128
   InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± 129
   AlternateReportingCurrencyAmounts
<AltrnRptgCcyAmts>
[0..1] ± 129
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 129
   ExposureType <XpsrTp> [0..1] ± 130
   BalanceBreakdown <BalBrkdwn> [0..*] ± C8, C37 130
   AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C17,
C38
131
   HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 131
Constraints
• AggregateBalanceGuideline
If AvailableQuantity and NotAvailableQuantity are both present, then the AggregateQuantity should
be the sum of AvailableQuantity and NotAvailableQuantity.
• HoldingAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
present, then it must not contain information that can be provided in a structured field.
3.4.9.5.17.1  SafekeepingPlace <SfkpgPlc>
Presence: [1..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
Impacted by: C33 "SafekeepingPlaceFormatOrLEIRule"
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 125 March 2026
```

