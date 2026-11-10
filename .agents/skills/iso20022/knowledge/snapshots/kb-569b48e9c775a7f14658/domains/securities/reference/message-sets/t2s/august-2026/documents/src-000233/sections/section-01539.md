---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["43 reda.023.001.01 SecuritiesAccountModificationRequestV01", "43.4 Message Building Blocks", "43.4.3 Modification <Mod>", "43.4.3.2 RequestedModification <ReqdMod>", "43.4.3.2.2 SystemRestriction <SysRstrctn>", "43.4.3.2.2.2 ValidTo <VldTo>"]
file_pages: [2161, 2162]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.023.001.01"]
---

# 43.4.3.2.2.2 ValidTo <VldTo>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2161 to 2162.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2161

```text
Definition: Specifies the date from which the restriction is valid.
Datatype: "ISODateTime" on page 3320
43.4.3.2.2.2  ValidTo <VldTo>
Presence: [0..1]
Definition: Specifies the date until which the restriction is valid.
Datatype: "ISODateTime" on page 3320
43.4.3.2.2.3  Type <Tp>
Presence: [1..1]
Definition: Specifies the identification of a restriction.
Datatype: "Max35Text" on page 3328
43.4.3.2.3  MarketSpecificAttribute <MktSpcfcAttr>
Presence: [1..1]
Definition: Additional attributes defined by a central security depositary for a party.
MarketSpecificAttribute <MktSpcfcAttr> contains the following MarketSpecificAttribute1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 2161
   Value <Val> [1..1] Text 2161
43.4.3.2.3.1  Name <Nm>
Presence: [1..1]
Definition: Specifies the name of the market-specific attribute.
Datatype: "Max35Text" on page 3328
43.4.3.2.3.2  Value <Val>
Presence: [1..1]
Definition: Specifies the value of the market-specific attribute.
Datatype: "Max350Text" on page 3328
43.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C1 "SupplementaryDataRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.023.001.01
SecuritiesAccountModificationRequestV01
Target2-Securities 2161 August 2026
```

## File page 2162

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 3011 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.023.001.01
SecuritiesAccountModificationRequestV01
Target2-Securities 2162 August 2026
```

