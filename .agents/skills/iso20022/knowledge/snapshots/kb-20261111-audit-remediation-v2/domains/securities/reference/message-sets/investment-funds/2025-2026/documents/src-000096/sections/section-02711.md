---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.19 ForeignExchangeDetails <FXDtls>", "53.4.5.19.5 QuotingInstitution <QtgInstn>"]
file_pages: [3794]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.19.5 QuotingInstitution <QtgInstn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3794 to 3794.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3794

```text
53.4.5.19.5  QuotingInstitution <QtgInstn>
Presence: [0..1]
Definition: Party that proposes a foreign exchange rate.
QuotingInstitution <QtgInstn> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
53.4.5.20  FinancialAdvice <FinAdvc>
Presence: [0..1]
Definition: Specifies if advice has been received from an independent financial advisor.
Datatype: "FinancialAdvice1Code" on page 5302
CodeName Name Definition
RECE Received Advice has been received from an
independent financial advisor.
NREC NotReceived Advice has not been received from an
independent financial advisor.
UKWN Unknown It is not known whether or not advice has
been received from an independent
financial advisor.
53.4.5.21  NegotiatedTrade <NgtdTrad>
Presence: [0..1]
Definition: Specifies whether the trade is negotiated.
Datatype: "NegotiatedTrade1Code" on page 5331
CodeName Name Definition
NEGO Negotiated Trade is negotiated.
NNGO NotNegotiated Trade is not negotiated.
UNKW Unknown Whether the trade is negotiated or not is
unknown.
53.4.5.22  CustomerConductClassification <CstmrCndctClssfctn>
Presence: [0..1]
Definition: Assessment of the customer's behaviour at the time of the account opening application.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3794 May 2026
```

