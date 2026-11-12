---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.23 Identification Information", "66.1.23.20 GenericIdentification30", "66.1.23.20.3 SchemeName <SchmeNm>"]
file_pages: [4553]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.23.20.3 SchemeName <SchmeNm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4553 to 4553.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4553

```text
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 5403
66.1.23.20.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: "Max35Text" on page 5403
66.1.23.21  GenericIdentification6
Definition: Balance expressed with a data source scheme.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [1..1] Text 4553
   Information <Inf> [1..1] Text 4553
   Balance <Bal> [1..1] Quantity 4553
66.1.23.21.1  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max8Text" on page 5404
66.1.23.21.2  Information <Inf>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Exact4AlphaNumericText" on page 5402
66.1.23.21.3  Balance <Bal>
Presence: [1..1]
Definition: Value of the balance.
Datatype: "Number" on page 5400
66.1.23.22  AdditionalReference11
Definition: References a related message or provides another reference, such as a pool reference,
linking a set of messages. The party which issued the related reference may be the Sender of the
referenced message or a party other than the Sender.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4554
   ReferenceIssuer <RefIssr> [0..1] ± 4554
   MessageName <MsgNm> [0..1] Text 4554
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4553 May 2026
```

