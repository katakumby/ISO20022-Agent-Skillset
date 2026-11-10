---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.17 Identification Information", "82.1.17.10 GenericIdentification56"]
file_pages: [2968]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.17.10 GenericIdentification56

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2968 to 2968.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2968

```text
Definition: Name or number assigned by an entity to enable recognition of that entity, for example,
account identifier.
Datatype: "Max35Text" on page 3328
82.1.17.10  GenericIdentification56
Definition: Proprietary information related to a balance.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2968
   Issuer <Issr> [1..1] Text 2968
   SchemeName <SchmeNm> [0..1] Text 2968
   Balance <Bal> [1..1] Quantity 2968
82.1.17.10.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: "Exact4AlphaNumericText" on page 3325
82.1.17.10.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 3328
82.1.17.10.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: "Max35Text" on page 3328
82.1.17.10.4  Balance <Bal>
Presence: [1..1]
Definition: Value of the balance.
Datatype: "DecimalNumber" on page 3324
82.1.17.11  GenericIdentification13
Definition: Information related to an identification, for example, party identification or account
identification.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2968 August 2026
```

