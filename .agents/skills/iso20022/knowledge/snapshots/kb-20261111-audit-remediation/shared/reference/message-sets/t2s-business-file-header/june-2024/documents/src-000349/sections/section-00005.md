---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S BusinessFileHeader"
source_ids: ["src-000349"]
source_editions: ["june-2024"]
message_ids: []
heading_path: ["2 head.002.001.01 BusinessFileHeaderV01", "2.2 Structure"]
file_pages: [5]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.002.001.01"]
---

# 2.2 Structure

Source: [src-000349](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_BusinessFileHeader_MessageSet/ISO20022_MDR_Target2Securities_BusinessFileHeader_June2024_v1.pdf`. Locator: one-based file pages 5 to 5.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5

```text
2.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <Xchg> [1..1]  
   PayloadDescription <PyldDesc> [1..1]  5
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
   Payload <Pyld> [0..*] (External Schema) 8
2.3 Constraints
C1 OnlySignatureElement
The XML Signature namespace ("http://www.w3.org/2000/09/xmldsig#") allows for different
XML elements to be root elements. This means the user has to choose amongst these global
elements which one to use as the root element. Only the XML element Signature is allowed.
2.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
2.4.1 PayloadDescription <PyldDesc>
Presence: [1..1]
Definition: Contains information about the payload.
Approved by the Cross SEG Harmonisation Group (CSH) on the 18th of June
2024.
head.002.001.01 BusinessFileHeaderV01
Target2-Securities - Business File Header 5 June 2024
```

