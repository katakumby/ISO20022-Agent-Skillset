---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.1 AmendmentIndicator <AmdmntInd>"]
file_pages: [2346]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.1 AmendmentIndicator <AmdmntInd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2346 to 2346.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2346

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Identification <Id> [1..1] Text 2521
         Type <Tp> [0..1] ± 2521
         Name <Nm> [0..1] Text 2521
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2522
Constraints
• BulkCashSettlementDetailsRule
Either one or more occurrences of IndividualExecutionDetails/CashSettlementDetails or
BulkCashSettlementDetails may be present, but not both.
• OrderOriginatorEligibility3Rule
Either InvestmentAccountDetails/OrderOriginatorEligibility or one or more occurrences of
IndividualExecutionDetails/RelatedPartyDetails/OrderOriginatorEligibility may be present, but not
both.
• SettlementCurrencyRule
If BulkCashSettlementDetails is present, then Currency in IndividualExecutionDetails/
SettlementAmount must be the same in all occurrences of IndividualExecutionDetails.
• TotalSettlementCurrencyRule
If TotalSettlementAmount is present, then Currency in IndividualExecutionDetails/SettlementAmount,
must be the same in all occurrences of IndividualExecutionDetails.
46.4.5.1  AmendmentIndicator <AmdmntInd>
Presence: [0..1]
Definition: Indicates whether the confirmation is an amendment of a previous confirmation.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
46.4.5.2  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual orders, as assigned by the
instructing party. This identifier links the individual orders together.
Datatype: "Max35Text" on page 5403
46.4.5.3  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Definition: Market in which the advised trade transaction was executed.
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2346 May 2026
```

