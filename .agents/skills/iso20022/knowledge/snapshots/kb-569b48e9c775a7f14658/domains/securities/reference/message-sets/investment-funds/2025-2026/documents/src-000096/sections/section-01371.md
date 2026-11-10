---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.1 AmendmentIndicator <AmdmntInd>"]
file_pages: [1927]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.1 AmendmentIndicator <AmdmntInd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1927 to 1927.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1927

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         Identification <Id> [1..1] Text 2099
         Type <Tp> [0..1] ± 2099
         Name <Nm> [0..1] Text 2099
         DigitalLedgerIdentification <DgtlLdgrId> [1..1] IdentifierSet 2100
Constraints
• BulkCashSettlementDetailsRule
Either one or more occurrences of IndividualExecutionDetails/CashSettlementDetails or
BulkCashSettlementDetails may be present, but not both.
• RequestedSettlementCurrencyRule
If RequestedSettlementCurrency is present, it must be the same Currency as in all occurrences of
IndividualExecutionDetails/SettlementAmount.
• SettlementCurrencyRule
If BulkCashSettlementDetails is present, then Currency in IndividualExecutionDetails/
SettlementAmount must be the same in all occurrences of IndividualExecutionDetails.
43.4.5.1  AmendmentIndicator <AmdmntInd>
Presence: [0..1]
Definition: Indicates whether the confirmation is an amendment of a previous confirmation.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
43.4.5.2  MasterReference <MstrRef>
Presence: [0..1]
Definition: Unique and unambiguous identifier for a group of individual orders, as assigned by the
instructing party. This identifier links the individual orders together.
Datatype: "Max35Text" on page 5403
43.4.5.3  PlaceOfTrade <PlcOfTrad>
Presence: [0..1]
Definition: Market in which the advised trade transaction was executed.
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1927 May 2026
```

