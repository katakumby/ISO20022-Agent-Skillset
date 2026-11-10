---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000369"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["6 reda.022.001.02 PartyModificationRequestV02", "6.4 Message Building Blocks", "6.4.3 Modification <Mod>", "6.4.3.2 RequestedModification <ReqdMod>", "6.4.3.2.9 SystemRestriction <SysRstrctn>", "6.4.3.2.9.1 ValidFrom <VldFr>"]
file_pages: [74, 75]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.022.001.02"]
---

# 6.4.3.2.9.1 ValidFrom <VldFr>

Source: [src-000369](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_PartyReferenceData_2023_2024_v1.pdf`. Locator: one-based file pages 74 to 75.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 74

```text
6.4.3.2.9.1  ValidFrom <VldFr>
Presence: [1..1]
Definition: Specifies the date from which the restriction is valid.
Datatype: "ISODateTime" on page 185
6.4.3.2.9.2  ValidTo <VldTo>
Presence: [0..1]
Definition: Specifies the date until which the restriction is valid.
Datatype: "ISODateTime" on page 185
6.4.3.2.9.3  Type <Tp>
Presence: [1..1]
Definition: Specifies the identification of a restriction.
Datatype: "Max35Text" on page 188
6.4.3.2.10  MarketSpecificAttribute <MktSpcfcAttr>
Presence: [1..1]
Definition: Additional attributes defined by a central security depositary for a party.
MarketSpecificAttribute <MktSpcfcAttr> contains the following MarketSpecificAttribute1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 74
   Value <Val> [1..1] Text 74
6.4.3.2.10.1  Name <Nm>
Presence: [1..1]
Definition: Specifies the name of the market-specific attribute.
Datatype: "Max35Text" on page 188
6.4.3.2.10.2  Value <Val>
Presence: [1..1]
Definition: Specifies the value of the market-specific attribute.
Datatype: "Max350Text" on page 187
6.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C4 "SupplementaryDataRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.022.001.02 PartyModificationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
74 March 2024
```

## File page 75

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 163 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 163
   Envelope <Envlp> [1..1] (External Schema) 163
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
reda.022.001.02 PartyModificationRequestV02
Target2-Securities - Party Reference Data - Maintenance
2023 - 2024
75 March 2024
```

