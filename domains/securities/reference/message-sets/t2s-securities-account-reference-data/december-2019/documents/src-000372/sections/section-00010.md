---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["2 reda.018.001.01 SecuritiesAccountCreationRequestV01", "2.4 Message Building Blocks", "2.4.2 SecuritiesAccount <SctiesAcct>", "2.4.2.8 MarketSpecificAttribute <MktSpcfcAttr>", "2.4.2.8.1 Name <Nm>"]
file_pages: [12]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.018.001.01"]
---

# 2.4.2.8.1 Name <Nm>

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 12 to 12.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 12

```text
Definition: Additional attributes defined by a central security depositary for a party.
MarketSpecificAttribute <MktSpcfcAttr> contains the following MarketSpecificAttribute1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 12
   Value <Val> [1..1] Text 12
2.4.2.8.1  Name <Nm>
Presence: [1..1]
Definition: Specifies the name of the market-specific attribute.
Datatype: "Max35Text" on page 100
2.4.2.8.2  Value <Val>
Presence: [1..1]
Definition: Specifies the value of the market-specific attribute.
Datatype: "Max350Text" on page 100
2.4.2.9  Restriction <Rstrctn>
Presence: [0..*]
Definition: Defines the specific processing characteristics for a securities account to ensure
configurability of specific requirements, as prescribed by national legal and regulatory requirements and
practices.
Restriction <Rstrctn> contains the following SystemRestriction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidFrom <VldFr> [1..1] DateTime 12
   ValidTo <VldTo> [0..1] DateTime 12
   Type <Tp> [1..1] Text 12
2.4.2.9.1  ValidFrom <VldFr>
Presence: [1..1]
Definition: Specifies the date from which the restriction is valid.
Datatype: "ISODateTime" on page 97
2.4.2.9.2  ValidTo <VldTo>
Presence: [0..1]
Definition: Specifies the date until which the restriction is valid.
Datatype: "ISODateTime" on page 97
2.4.2.9.3  Type <Tp>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.018.001.01
SecuritiesAccountCreationRequestV01
Target2-Securities - Securities Account Reference Data 12 December 2019
```

