---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.31 Payment", "66.1.31.2 PaymentCard29", "66.1.31.2.8 SecurityCode <SctyCd>"]
file_pages: [5048]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.31.2.8 SecurityCode <SctyCd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5048 to 5048.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5048

```text
CardIssuerIdentification <CardIssrId> contains one of the following elements (see
"PartyIdentification125Choice" on page 4909 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4909
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4909
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4910
66.1.31.2.8  SecurityCode <SctyCd>
Presence: [0..1]
Definition: Security code written on, or in, the card.
Datatype: "Max35Text" on page 5403
66.1.31.2.9  SequenceNumber <SeqNb>
Presence: [0..1]
Definition: Number distinguishing two or more payment cards with the same account number.
Datatype: "Max3Text" on page 5404
66.1.31.3  PaymentInstrument17
Definition: Instrument used to process a payment instruction.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5048 May 2026
```

