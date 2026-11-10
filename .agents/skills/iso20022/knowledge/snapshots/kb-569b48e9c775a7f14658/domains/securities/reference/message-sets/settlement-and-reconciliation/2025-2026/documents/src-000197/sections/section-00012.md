---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.8 BalanceForAccount <BalForAcct>", "2.4.8.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [33]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.8.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 33 to 33.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 33

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     AccountBaseCurrencyAmounts <AcctBaseCcyAmts> [0..1] ± C18 48
     InstrumentCurrencyAmounts <InstrmCcyAmts> [0..1] ± C18 48
     QuantityBreakdown <QtyBrkdwn> [0..*] ± 49
     ExposureType <XpsrTp> [0..1] ± 49
     BalanceBreakdown <BalBrkdwn> [0..*] ± C9, C39 50
     AdditionalBalanceBreakdown <AddtlBalBrkdwn> [0..*] ± C19,
C40
50
     HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 51
   HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 51
   SupplementaryData <SplmtryData> [0..*] ± C42 51
Constraints
• AggregateBalanceGuideline
If AvailableQuantity and NotAvailableQuantity are both present, then the AggregateQuantity should
be the sum of AvailableQuantity and NotAvailableQuantity.
• BalanceAtSafekeepingPlaceRule
If SafekeepingPlace is present, then BalanceAtSafekeepingPlace is not allowed.
• FinancialInstrumentAttributesRule
If InvestmentFundsFinancialInstrumentAttributes is present, then FinancialInstrumentAttributes is not
allowed.
• HoldingAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
present, then it must not contain information that can be provided in a structured field.
2.4.8.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C15 "DescriptionPresenceRule", C16 "DescriptionUsageRule", C23 "ISINGuideline", C24
"ISINPresenceRule", C25 "OtherIdentificationPresenceRule"
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 33 March 2026
```

