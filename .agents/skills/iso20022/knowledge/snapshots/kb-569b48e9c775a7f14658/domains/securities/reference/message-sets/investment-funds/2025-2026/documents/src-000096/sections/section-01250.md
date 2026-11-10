---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.4 Message Building Blocks", "41.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "41.4.4.8.15 TransactionOverhead <TxOvrhd>", "41.4.4.8.15.2 IndividualFee <IndvFee>", "41.4.4.8.15.2.8 NonStandardSLAReference <NonStdSLARef>"]
file_pages: [1755]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.4.4.8.15.2.8 NonStandardSLAReference <NonStdSLARef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1755 to 1755.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1755

```text
41.4.4.8.15.2.8  NonStandardSLAReference <NonStdSLARef>
Presence: [0..1]
Definition: Reference to a sales agreement that overrides normal processing or the Service Level
Agreement (SLA), such as a fee (charge/commission).
Datatype: "Max35Text" on page 5403
41.4.4.8.15.2.9  RecipientIdentification <RcptId>
Presence: [0..1]
Definition: Party entitled to the amount of money resulting from a fee (charge/commission).
RecipientIdentification <RcptId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
41.4.4.8.15.3  IndividualTax <IndvTax>
Presence: [0..*]
Definition: Individual tax amount.
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1755 May 2026
```

