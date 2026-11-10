---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "3.4 Message Building Blocks", "3.4.8 BalanceForAccount <BalForAcct>", "3.4.8.17 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>", "3.4.8.17.1 SafekeepingPlace <SfkpgPlc>"]
file_pages: [102]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3.4.8.17.1 SafekeepingPlace <SfkpgPlc>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 102 to 102.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 102

```text
BalanceAtSafekeepingPlace <BalAtSfkpgPlc> contains the following
AggregateBalancePerSafekeepingPlace42 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlace <SfkpgPlc> [1..1] ± C33 102
   PlaceOfListing <PlcOfListg> [0..1] ± 103
   Pledgee <Pldgee> [0..1] ± C25 103
   AggregateBalance <AggtBal> [1..1] ± 104
   PriceDetails <PricDtls> [1..*] ± C41 104
   ForeignExchangeDetails <FXDtls> [0..*] ± 105
   DaysAccrued <DaysAcrd> [0..1] Quantity 105
   AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [1..1] ± 105
   InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± 106
   AlternateReportingCurrencyAmounts
<AltrnRptgCcyAmts>
[0..1] ± 106
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 106
   ExposureType <XpsrTp> [0..1] ± 107
   BalanceBreakdown <BalBrkdwn> [0..*] ± C8, C37 107
   AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C17,
C38
108
   HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 108
Constraints
• AggregateBalanceGuideline
If AvailableQuantity and NotAvailableQuantity are both present, then the AggregateQuantity should
be the sum of AvailableQuantity and NotAvailableQuantity.
• HoldingAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
present, then it must not contain information that can be provided in a structured field.
3.4.8.17.1  SafekeepingPlace <SfkpgPlc>
Presence: [1..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
Impacted by: C33 "SafekeepingPlaceFormatOrLEIRule"
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 102 March 2026
```

