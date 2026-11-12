---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S BusinessFileHeader"
source_ids: ["src-000349"]
source_editions: ["june-2024"]
message_ids: []
heading_path: ["2 head.002.001.01 BusinessFileHeaderV01", "2.4 Message Building Blocks", "2.4.1 PayloadDescription <PyldDesc>", "2.4.1.1 PayloadData <PyldData>"]
file_pages: [6]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.002.001.01"]
---

# 2.4.1.1 PayloadData <PyldData>

Source: [src-000349](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`. Locator: one-based file pages 6 to 6.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 6

```text
PayloadDescription <PyldDesc> contains the following PayloadDescription2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PayloadData <PyldData> [1..1]  6
     PayloadIdentifier <PyldIdr> [1..1] Text 6
     CreationDateAndTime <CreDtAndTm> [1..1] DateTime 6
     PossibleDuplicateFlag <PssblDplctFlg> [0..1] Indicator 6
   ApplicationSpecifics <ApplSpcfcs> [0..1]  7
     SystemUser <SysUsr> [0..1] Text 7
     Signature <Sgntr> [0..1] (External Schema) 7
     TotalNumberOfDocuments <TtlNbOfDocs> [1..1] Quantity 7
   PayloadType <PyldTp> [1..1] Text 8
   ManifestData <MnfstData> [0..*]  8
     DocumentType <DocTp> [1..1] Text 8
     NumberOfDocuments <NbOfDocs> [1..1] Quantity 8
2.4.1.1  PayloadData <PyldData>
Presence: [1..1]
Definition: This component is used to identify the instance of the document exchanged.
PayloadData <PyldData> contains the following PayloadData2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PayloadIdentifier <PyldIdr> [1..1] Text 6
   CreationDateAndTime <CreDtAndTm> [1..1] DateTime 6
   PossibleDuplicateFlag <PssblDplctFlg> [0..1] Indicator 6
2.4.1.1.1  PayloadIdentifier <PyldIdr>
Presence: [1..1]
Definition: String of characters that uniquely identifies the file, which was delivered by the sender.
Datatype: "Max35Text" on page 10
2.4.1.1.2  CreationDateAndTime <CreDtAndTm>
Presence: [1..1]
Definition: Date and time when the file was created by the sender.
Datatype: "ISODateTime" on page 9
2.4.1.1.3  PossibleDuplicateFlag <PssblDplctFlg>
Presence: [0..1]
Approved by the Cross SEG Harmonisation Group (CSH) on the 18th of June
2024.
head.002.001.01 BusinessFileHeaderV01
Target2-Securities - Business File Header 6 June 2024
```

