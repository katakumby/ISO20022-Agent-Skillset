---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.17 SubscriptionLegDetails <SbcptLegDtls>", "53.4.5.17.8 TransactionOverhead <TxOvrhd>", "53.4.5.17.8.2 IndividualFee <IndvFee>", "53.4.5.17.8.2.8 NonStandardSLAReference <NonStdSLARef>"]
file_pages: [3642]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.17.8.2.8 NonStandardSLAReference <NonStdSLARef>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3642 to 3642.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3642

```text
53.4.5.17.8.2.8  NonStandardSLAReference <NonStdSLARef>
Presence: [0..1]
Definition: Reference to a sales agreement that overrides normal processing or the Service Level
Agreement (SLA), such as a fee (charge/commission).
Datatype: "Max35Text" on page 5403
53.4.5.17.8.2.9  RecipientIdentification <RcptId>
Presence: [0..1]
Definition: Party entitled to the amount of money resulting from a fee (charge/commission).
RecipientIdentification <RcptId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
53.4.5.17.8.3  IndividualTax <IndvTax>
Presence: [0..*]
Definition: Individual tax amount.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3642 May 2026
```

