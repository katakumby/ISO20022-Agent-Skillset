---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.8 BalanceForAccount <BalForAcct>", "2.4.8.18 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>", "2.4.8.18.1 SafekeepingPlace <SfkpgPlc>"]
file_pages: [44]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.8.18.1 SafekeepingPlace <SfkpgPlc>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 44 to 44.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 44

```text
BalanceAtSafekeepingPlace <BalAtSfkpgPlc> contains the following
AggregateBalancePerSafekeepingPlace43 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlace <SfkpgPlc> [1..1] ± C35 44
   PlaceOfListing <PlcOfListg> [0..1] ± 45
   Pledgee <Pldgee> [0..1] ± C27 45
   AggregateBalance <AggtBal> [1..1] ± 46
   AvailableBalance <AvlblBal> [0..1] ± 46
   NotAvailableBalance <NotAvlblBal> [0..1] ± 47
   PriceDetails <PricDtls> [0..*] ± C44 47
   ForeignExchangeDetails <FXDtls> [0..*] ± 47
   DaysAccrued <DaysAcrd> [0..1] Quantity 48
   AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [0..1] ± C18 48
   InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± C18 48
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 49
   ExposureType <XpsrTp> [0..1] ± 49
   BalanceBreakdown <BalBrkdwn> [0..*] ± C9, C39 50
   AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C19,
C40
50
   HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 51
Constraints
• AggregateBalanceGuideline
If AvailableQuantity and NotAvailableQuantity are both present, then the AggregateQuantity should
be the sum of AvailableQuantity and NotAvailableQuantity.
• HoldingAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if HoldingAdditionnalDetails is present,
then it must not contain information that can be provided in a structured field.
2.4.8.18.1  SafekeepingPlace <SfkpgPlc>
Presence: [1..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
Impacted by: C35 "SafekeepingPlaceFormatOrLEIRule"
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 44 March 2026
```

