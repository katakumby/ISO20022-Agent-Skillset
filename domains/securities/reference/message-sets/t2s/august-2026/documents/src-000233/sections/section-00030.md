---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["4 admi.007.001.01 ReceiptAcknowledgementV01", "4.2 Structure"]
file_pages: [63]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.007.001.01"]
---

# 4.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 63 to 63.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 63

```text
4.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <RctAck> [1..1]  
   MessageIdentification <MsgId> [1..1]  64
     MessageIdentification <MsgId> [1..1] Text 64
     CreationDateTime <CreDtTm> [0..1] DateTime 64
     QueryName <QryNm> [0..1] Text 64
   Report <Rpt> [1..*]  64
     RelatedReference <RltdRef> [1..1]  65
       Reference <Ref> [1..1] Text 65
       MessageName <MsgNm> [0..1] Text 65
       ReferenceIssuer <RefIssr> [0..1] ± 65
     RequestHandling <ReqHdlg> [1..1]  66
       StatusCode <StsCd> [1..1] Text 66
       StatusDateTime <StsDtTm> [0..1] DateTime 66
       Description <Desc> [0..1] Text 66
   SupplementaryData <SplmtryData> [0..*] ± C3 66
4.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
4.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.007.001.01 ReceiptAcknowledgementV01
Target2-Securities 63 August 2026
```

