---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.1 MasterReference <MstrRef>"]
file_pages: [1717]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.1 MasterReference <MstrRef>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1717 to 1717.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1717

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}             ProprietaryIdentification <PrtryId> [1..1] Text 1883
           LEI <LEI> [0..1] IdentifierSet 1883
         DrawerIdentification <DrwrId> [0..1] ± 1884
Or       CashAccountDetails <CshAcctDtls> [1..1]  C1 1884
         AccountIdentification <AcctId> [0..1] Text 1884
         Type <Tp> [0..1] ± 1884
Or}       BlockChainCashWallet <BlckChainCshWllt> [1..1]  1885
         Identification <Id> [1..1] Text 1885
         Type <Tp> [0..1] ± 1885
         Name <Nm> [0..1] Text 1885
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 1886
Constraints
• BulkCashSettlementDetailsRule
Either IndividualOrderDetails/CashSettlementDetails or BulkCashSettlementDetails may be present,
but not both.
• RequestedSettlementCurrencyRule
If RequestedSettlementCurrency is present, it must be the same Currency as in all occurrences of
IndividualOrderDetails/SettlementAmount, if present.
• SettlementCurrencyRule
If BulkCashSettlementDetails is present, then Currency in IndividualOrderDetails/SettlementAmount,
if present, must be the same in all occurrences of IndividualOrderDetails.
41.4.4.1  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual orders, as assigned by the
instructing party. This identifier links the individual orders together.
Datatype: "Max35Text" on page 5403
41.4.4.2  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Definition: Market in which the advised trade transaction was executed.
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1717 May 2026
```

