---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["6 reda.023.001.01 SecuritiesAccountModificationRequestV01", "6.4 Message Building Blocks", "6.4.3 Modification <Mod>", "6.4.3.2 RequestedModification <ReqdMod>", "6.4.3.2.2 SystemRestriction <SysRstrctn>", "6.4.3.2.2.2 ValidTo <VldTo>"]
file_pages: [54, 55]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.023.001.01"]
---

# 6.4.3.2.2.2 ValidTo <VldTo>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 54 to 55.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 54

```text
Definition: Specifies the date from which the restriction is valid.
Datatype: "ISODateTime" on page 97
6.4.3.2.2.2  ValidTo <VldTo>
Presence: [0..1]
Definition: Specifies the date until which the restriction is valid.
Datatype: "ISODateTime" on page 97
6.4.3.2.2.3  Type <Tp>
Presence: [1..1]
Definition: Specifies the identification of a restriction.
Datatype: "Max35Text" on page 100
6.4.3.2.3  MarketSpecificAttribute <MktSpcfcAttr>
Presence: [1..1]
Definition: Additional attributes defined by a central security depositary for a party.
MarketSpecificAttribute <MktSpcfcAttr> contains the following MarketSpecificAttribute1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 54
   Value <Val> [1..1] Text 54
6.4.3.2.3.1  Name <Nm>
Presence: [1..1]
Definition: Specifies the name of the market-specific attribute.
Datatype: "Max35Text" on page 100
6.4.3.2.3.2  Value <Val>
Presence: [1..1]
Definition: Specifies the value of the market-specific attribute.
Datatype: "Max350Text" on page 100
6.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C1 "SupplementaryDataRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.023.001.01
SecuritiesAccountModificationRequestV01
Target2-Securities - Securities Account Reference Data 54 December 2019
```

## File page 55

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 84 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 84
   Envelope <Envlp> [1..1] (External Schema) 84
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.023.001.01
SecuritiesAccountModificationRequestV01
Target2-Securities - Securities Account Reference Data 55 December 2019
```

