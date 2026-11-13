---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.14 Identification Information", "6.1.14.4 GenericIdentification32", "6.1.14.4.1 Identification <Id>"]
file_pages: [840]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.14.4.1 Identification <Id>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 840 to 840.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 840

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 840
   Type <Tp> [0..1] CodeSet 840
   Issuer <Issr> [0..1] CodeSet 840
   ShortName <ShrtNm> [0..1] Text 841
6.1.14.4.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the entity.
Datatype: "Max35Text" on page 916
6.1.14.4.2  Type <Tp>
Presence: [0..1]
Definition: Type of identified entity.
Datatype: "PartyType3Code" on page 902
CodeName Name Definition
OPOI OriginatingPOI Point Of Interaction initiating the card
payment transaction.
MERC Merchant Merchant providing goods and service in
the card payment transaction.
ACCP Acceptor Card acceptor, party accepting the card
and presenting transaction data to the
acquirer.
ITAG IntermediaryAgent Party acting on behalf of other parties to
process or forward data to other parties.
ACQR Acquirer Entity acquiring card transactions.
CISS CardIssuer Party that issues cards.
DLIS DelegateIssuer Party to whom the card issuer delegates
to authorise card payment transactions.
6.1.14.4.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity assigning the identification (for example merchant, acceptor, acquirer, or tax authority).
Datatype: "PartyType4Code" on page 902
CodeName Name Definition
MERC Merchant Merchant providing goods and service in
the card payment transaction.
ACCP Acceptor Card acceptor, party accepting the card
and presenting transaction data to the
acquirer.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
840 March 2026
```

