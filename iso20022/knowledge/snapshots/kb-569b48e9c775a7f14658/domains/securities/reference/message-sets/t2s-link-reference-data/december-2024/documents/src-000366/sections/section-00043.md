---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["6 reda.050.001.01 AccountLinkMaintenanceRequestV01", "6.4 Message Building Blocks", "6.4.3 Update <Upd>"]
file_pages: [45, 46]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.050.001.01"]
---

# 6.4.3 Update <Upd>

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 45 to 46.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 45

```text
ValidFrom <VldFr> contains one of the following elements (see "DateAndDateTime2Choice" on
page 60 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 61
Or}   DateTime <DtTm> [1..1] DateTime 61
6.4.3 Update <Upd>
Presence: [1..1]
Definition: Provides data that needs to be maintained.
Update <Upd> contains the following AccountLinkUpdate2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ValidTo <VldTo> [1..1] ± 45
6.4.3.1  ValidTo <VldTo>
Presence: [1..1]
Definition: Defines the date until when the securities account is linked to the cash account.
ValidTo <VldTo> contains one of the following elements (see "DateAndDateTime2Choice" on
page 60 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 61
Or}   DateTime <DtTm> [1..1] DateTime 61
6.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C6 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 67 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 67
   Envelope <Envlp> [1..1] (External Schema) 67
Approved by the Securities SEG on 21 November 2024. reda.050.001.01
AccountLinkMaintenanceRequestV01
Target2-Securities - Link Reference Data 45 December 2024
```

## File page 46

```text
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 21 November 2024. reda.050.001.01
AccountLinkMaintenanceRequestV01
Target2-Securities - Link Reference Data 46 December 2024
```

