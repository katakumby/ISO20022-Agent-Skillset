---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["26 head.002.001.01 BusinessFileHeaderV01", "26.2 Structure"]
file_pages: [615]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.002.001.01"]
---

# 26.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 615 to 615.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 615

```text
26.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <Xchg> [1..1]  
   PayloadDescription <PyldDesc> [1..1]  615
     PayloadData <PyldData> [1..1]  616
       PayloadIdentifier <PyldIdr> [1..1] Text 616
       CreationDateAndTime <CreDtAndTm> [1..1] DateTime 616
       PossibleDuplicateFlag <PssblDplctFlg> [0..1] Indicator 616
     ApplicationSpecifics <ApplSpcfcs> [0..1]  617
       SystemUser <SysUsr> [0..1] Text 617
       Signature <Sgntr> [0..1] (External Schema) 617
       TotalNumberOfDocuments <TtlNbOfDocs> [1..1] Quantity 617
     PayloadType <PyldTp> [1..1] Text 618
     ManifestData <MnfstData> [0..*]  618
       DocumentType <DocTp> [1..1] Text 618
       NumberOfDocuments <NbOfDocs> [1..1] Quantity 618
   Payload <Pyld> [0..*] (External Schema) 618
26.3 Constraints
C1 OnlySignatureElement
The XML Signature namespace ("http://www.w3.org/2000/09/xmldsig#") allows for different
XML elements to be root elements. This means the user has to choose amongst these global
elements which one to use as the root element. Only the XML element Signature is allowed.
26.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
26.4.1 PayloadDescription <PyldDesc>
Presence: [1..1]
Definition: Contains information about the payload.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
head.002.001.01 BusinessFileHeaderV01
Target2-Securities 615 August 2026
```

