---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "3.4 Message Building Blocks", "3.4.8 BalanceForAccount <BalForAcct>", "3.4.8.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [92]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3.4.8.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 92 to 92.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 92

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
   HoldingAdditionalDetails <HldgAddtlDtls> [0..1] Text 108
   SupplementaryData <SplmtryData> [0..*] ± C40 109
Constraints
• BalanceAtSafekeepingPlaceRule
If SafekeepingPlace is present, then BalanceAtSafekeepingPlace is not allowed.
• FinancialInstrumentAttributesRule
If InvestmentFundsFinancialInstrumentAttributes is present, then FinancialInstrumentAttributes is not
allowed.
• HoldingAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
present, then it must not contain information that can be provided in a structured field.
3.4.8.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instrument representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C14 "DescriptionPresenceRule", C15 "DescriptionUsageRule", C21 "ISINGuideline", C22
"ISINPresenceRule", C23 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 1474 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 1475
   OtherIdentification <OthrId> [0..*]  1475
     Identification <Id> [1..1] Text 1475
     Suffix <Sfx> [0..1] Text 1475
     Type <Tp> [1..1] ± 1476
   Description <Desc> [0..1] Text 1476
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 92 March 2026
```

