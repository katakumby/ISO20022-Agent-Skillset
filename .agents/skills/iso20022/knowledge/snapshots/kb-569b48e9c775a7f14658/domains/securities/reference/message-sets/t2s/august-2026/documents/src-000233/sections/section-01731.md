---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["66 reda.050.001.01 AccountLinkMaintenanceRequestV01", "66.4 Message Building Blocks", "66.4.3 Update <Upd>"]
file_pages: [2379, 2380]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.050.001.01"]
---

# 66.4.3 Update <Upd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2379 to 2380.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2379

```text
ValidFrom <VldFr> contains one of the following elements (see "DateAndDateTime2Choice" on
page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
66.4.3 Update <Upd>
Presence: [1..1]
Definition: Provides data that needs to be maintained.
Update <Upd> contains the following AccountLinkUpdate2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidTo <VldTo> [1..1] ± 2379
66.4.3.1  ValidTo <VldTo>
Presence: [1..1]
Definition: Defines the date until when the securities account is linked to the cash account.
ValidTo <VldTo> contains one of the following elements (see "DateAndDateTime2Choice" on
page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
66.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C6 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 3011 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.050.001.01
AccountLinkMaintenanceRequestV01
Target2-Securities 2379 August 2026
```

## File page 2380

```text
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.050.001.01
AccountLinkMaintenanceRequestV01
Target2-Securities 2380 August 2026
```

