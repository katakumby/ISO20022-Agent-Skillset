---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.14 Balance30", "7.1.5.14.3 SubAccountDetails <SubAcctDtls>", "7.1.5.14.3.4 BalanceForSubAccount <BalForSubAcct>", "7.1.5.14.3.4.20 HoldingAdditionalDetails <HldgAddtlDtls>"]
file_pages: [304]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.14.3.4.20 HoldingAdditionalDetails <HldgAddtlDtls>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 304 to 304.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 304

```text
BalanceAtSafekeepingPlace <BalAtSfkpgPlc> contains the following elements (see
"AggregateBalancePerSafekeepingPlace44" on page 307 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlace <SfkpgPlc> [1..1] ± C33 307
   PlaceOfListing <PlcOfListg> [0..1] ± 308
   Pledgee <Pldgee> [0..1] ± C29 308
   AggregateBalance <AggtBal> [1..1] ± 309
   AvailableBalance <AvlblBal> [0..1] ± 309
   NotAvailableBalance <NotAvlblBal> [0..1] ± 310
   PriceDetails <PricDtls> [0..*] ± C41 310
   ForeignExchangeDetails <FXDtls> [0..*] ± 310
   DaysAccrued <DaysAcrd> [0..1] Quantity 311
   AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [0..1] ± C19 311
   InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± C19 311
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 312
   ExposureType <XpsrTp> [0..1] ± 312
   BalanceBreakdown <BalBrkdwn> [0..*] ± C10,
C35
313
   AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C21,
C37
313
   HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 314
Constraints
• AggregateBalanceGuideline
If AvailableQuantity and NotAvailableQuantity are both present, then the AggregateQuantity should
be the sum of AvailableQuantity and NotAvailableQuantity.
• HoldingAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if HoldingAdditionnalDetails is present,
then it must not contain information that can be provided in a structured field.
7.1.5.14.3.4.20  HoldingAdditionalDetails <HldgAddtlDtls>
Presence: [0..1]
Definition: Provides additional information on the holding.
Datatype: "Max350Text" on page 557
7.1.5.14.3.4.21  SupplementaryData <SplmtryData>
Presence: [0..*]
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 304 March 2026
```

