---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.11 Miscellaneous", "6.1.11.3 SupplementaryData1", "6.1.11.3.2 Envelope <Envlp>"]
file_pages: [554]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.11.3.2 Envelope <Envlp>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 554 to 554.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 554

```text
Datatype: "Max350Text" on page 609
6.1.11.3.2  Envelope <Envlp>
Presence: [1..1]
Definition: Technical element wrapping the supplementary data.
Type: (External Schema)
Technical component that contains the validated supplementary data information. This technical
envelope allows to segregate the supplementary data information from any other information.
6.1.11.4  Purpose2Choice
Definition: Specifies the underlying reason for the payment transaction.
Usage: Purpose is used by the end-customers, that is initiating party, (ultimate) debtor, (ultimate)
creditor to provide information concerning the nature of the payment. Purpose is a content element,
which is not used for processing by any of the agents involved in the payment chain.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 554
Or}   Proprietary <Prtry> [1..1] Text 554
6.1.11.4.1  Code <Cd>
Presence: [1..1]
Definition: Underlying reason for the payment transaction, as published in an external purpose code list.
Datatype: "ExternalPurpose1Code" on page 596
6.1.11.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Purpose, in a proprietary form.
Datatype: "Max35Text" on page 609
6.1.12 Party Identification
6.1.12.1  PartyIdentification272
Definition: Specifies the identification of a person or an organisation.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 554 March 2026
```

