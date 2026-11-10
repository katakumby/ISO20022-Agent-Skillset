---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.17 AggregateBalancePerSafekeepingPlace44"]
file_pages: [2899]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.17 AggregateBalancePerSafekeepingPlace44

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2899 to 2899.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2899

```text
82.1.5.17  AggregateBalancePerSafekeepingPlace44
Definition: Net position of a segregated holding, in a single security, within the overall position held in a
securities account at a specified place of safekeeping.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlace <SfkpgPlc> [1..1] ± C33 2899
   PlaceOfListing <PlcOfListg> [0..1] ± 2900
   Pledgee <Pldgee> [0..1] ± C29 2900
   AggregateBalance <AggtBal> [1..1] ± 2901
   AvailableBalance <AvlblBal> [0..1] ± 2901
   NotAvailableBalance <NotAvlblBal> [0..1] ± 2902
   PriceDetails <PricDtls> [0..*] ± C41 2902
   ForeignExchangeDetails <FXDtls> [0..*] ± 2902
   DaysAccrued <DaysAcrd> [0..1] Quantity 2903
   AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [0..1] ± C19 2903
   InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± C19 2903
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 2904
   ExposureType <XpsrTp> [0..1] ± 2904
   BalanceBreakdown <BalBrkdwn> [0..*] ± C10,
C35
2905
   AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C21,
C37
2905
   HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 2906
Constraints
• AggregateBalanceGuideline
If AvailableQuantity and NotAvailableQuantity are both present, then the AggregateQuantity should
be the sum of AvailableQuantity and NotAvailableQuantity.
• HoldingAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if HoldingAdditionnalDetails is present,
then it must not contain information that can be provided in a structured field.
82.1.5.17.1  SafekeepingPlace <SfkpgPlc>
Presence: [1..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository (CSD) or an International Central Securities
Depository (ICSD).
Impacted by: C33 "SafekeepingPlaceFormatOrLEIRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2899 August 2026
```

