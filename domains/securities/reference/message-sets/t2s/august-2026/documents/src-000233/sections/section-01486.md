---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["38 reda.018.001.01 SecuritiesAccountCreationRequestV01", "38.4 Message Building Blocks", "38.4.2 SecuritiesAccount <SctiesAcct>", "38.4.2.8 MarketSpecificAttribute <MktSpcfcAttr>", "38.4.2.8.1 Name <Nm>"]
file_pages: [2104]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.018.001.01"]
---

# 38.4.2.8.1 Name <Nm>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2104 to 2104.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2104

```text
Definition: Additional attributes defined by a central security depositary for a party.
MarketSpecificAttribute <MktSpcfcAttr> contains the following MarketSpecificAttribute1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 2104
   Value <Val> [1..1] Text 2104
38.4.2.8.1  Name <Nm>
Presence: [1..1]
Definition: Specifies the name of the market-specific attribute.
Datatype: "Max35Text" on page 3328
38.4.2.8.2  Value <Val>
Presence: [1..1]
Definition: Specifies the value of the market-specific attribute.
Datatype: "Max350Text" on page 3328
38.4.2.9  Restriction <Rstrctn>
Presence: [0..*]
Definition: Defines the specific processing characteristics for a securities account to ensure
configurability of specific requirements, as prescribed by national legal and regulatory requirements and
practices.
Restriction <Rstrctn> contains the following SystemRestriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [1..1] DateTime 2104
   ValidTo <VldTo> [0..1] DateTime 2104
   Type <Tp> [1..1] Text 2104
38.4.2.9.1  ValidFrom <VldFr>
Presence: [1..1]
Definition: Specifies the date from which the restriction is valid.
Datatype: "ISODateTime" on page 3320
38.4.2.9.2  ValidTo <VldTo>
Presence: [0..1]
Definition: Specifies the date until which the restriction is valid.
Datatype: "ISODateTime" on page 3320
38.4.2.9.3  Type <Tp>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.018.001.01
SecuritiesAccountCreationRequestV01
Target2-Securities 2104 August 2026
```

