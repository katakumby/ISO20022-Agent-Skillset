---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.4 Message Building Blocks", "44.4.3 PreviousReference <PrvsRef>", "44.4.4.1 MasterReference <MstrRef>"]
file_pages: [2133]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.4.4.1 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2133 to 2133.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2133

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 2300
           LEI <LEI> [0..1] IdentifierSet 2300
         DrawerIdentification <DrwrId> [0..1] ± 2301
Or       CashAccountDetails <CshAcctDtls> [1..1]  C1 2301
         AccountIdentification <AcctId> [0..1] Text 2301
         Type <Tp> [0..1] ± 2301
Or}       BlockChainCashWallet <BlckChainCshWllt> [1..1]  2302
         Identification <Id> [1..1] Text 2302
         Type <Tp> [0..1] ± 2302
         Name <Nm> [0..1] Text 2302
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2303
   TotalSettlementAmount <TtlSttlmAmt> [0..1] Amount C3, C10 2303
Constraints
• BulkCashSettlementDetailsRule
Either one or more occurrences of IndividualOrderDetails/CashSettlementDetails or
BulkCashSettlementDetails may be present, but not both.
• OrderOriginatorEligibility3Rule
Either InvestmentAccountDetails/OrderOriginatorEligibility or one or more occurrences of
IndividualOrderDetails/RelatedPartyDetails/OrderOriginatorEligibility may be present, but not both.
• SettlementCurrencyRule
If BulkCashSettlementDetails is present, then Currency in IndividualOrderDetails/SettlementAmount,
if present, must be the same in all occurrences of IndividualOrderDetails.
• TotalSettlementCurrencyRule
If TotalSettlementAmount is present, then Currency in IndividualOrderDetails/SettlementAmount, if
present, must be the same in all occurrences of IndividualOrderDetails.
44.4.4.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual orders, as assigned by the
instructing party. This identifier links the individual orders together.
Datatype: "Max35Text" on page 5403
44.4.4.2  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Definition: Market in which the advised trade transaction was executed.
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2133 May 2026
```

