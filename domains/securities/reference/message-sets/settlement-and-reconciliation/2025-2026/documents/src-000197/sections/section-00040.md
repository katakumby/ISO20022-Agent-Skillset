---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.9 SubAccountDetails <SubAcctDtls>", "2.4.9.5 BalanceForSubAccount <BalForSubAcct>", "2.4.9.5.18 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>", "2.4.9.5.18.1 SafekeepingPlace <SfkpgPlc>"]
file_pages: [68]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.9.5.18.1 SafekeepingPlace <SfkpgPlc>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 68 to 68.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 68

```text
BalanceAtSafekeepingPlace <BalAtSfkpgPlc> contains the following
AggregateBalancePerSafekeepingPlace43 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlace <SfkpgPlc> [1..1] ± C35 68
   PlaceOfListing <PlcOfListg> [0..1] ± 69
   Pledgee <Pldgee> [0..1] ± C27 69
   AggregateBalance <AggtBal> [1..1] ± 70
   AvailableBalance <AvlblBal> [0..1] ± 70
   NotAvailableBalance <NotAvlblBal> [0..1] ± 71
   PriceDetails <PricDtls> [0..*] ± C44 71
   ForeignExchangeDetails <FXDtls> [0..*] ± 71
   DaysAccrued <DaysAcrd> [0..1] Quantity 72
   AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [0..1] ± C18 72
   InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± C18 72
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 73
   ExposureType <XpsrTp> [0..1] ± 73
   BalanceBreakdown <BalBrkdwn> [0..*] ± C9, C39 73
   AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C19,
C40
74
   HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 75
Constraints
• AggregateBalanceGuideline
If AvailableQuantity and NotAvailableQuantity are both present, then the AggregateQuantity should
be the sum of AvailableQuantity and NotAvailableQuantity.
• HoldingAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if HoldingAdditionnalDetails is present,
then it must not contain information that can be provided in a structured field.
2.4.9.5.18.1  SafekeepingPlace <SfkpgPlc>
Presence: [1..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
Impacted by: C35 "SafekeepingPlaceFormatOrLEIRule"
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 68 March 2026
```

