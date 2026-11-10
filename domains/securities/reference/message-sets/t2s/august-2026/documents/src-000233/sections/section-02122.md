---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.16 Balance30", "82.1.5.16.2 BalanceForAccount <BalForAcct>", "82.1.5.16.2.20 HoldingAdditionalDetails <HldgAddtlDtls>"]
file_pages: [2880]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.16.2.20 HoldingAdditionalDetails <HldgAddtlDtls>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2880 to 2880.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2880

```text
BalanceAtSafekeepingPlace <BalAtSfkpgPlc> contains the following elements (see
"AggregateBalancePerSafekeepingPlace44" on page 2899 for details)
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
82.1.5.16.2.20  HoldingAdditionalDetails <HldgAddtlDtls>
Presence: [0..1]
Definition: Provides additional information on the holding.
Datatype: "Max350Text" on page 3328
82.1.5.16.2.21  SupplementaryData <SplmtryData>
Presence: [0..*]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2880 August 2026
```

