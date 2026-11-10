---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["57 reda.037.001.01 SecuritiesAccountAuditTrailReportV01", "57.3 Constraints"]
file_pages: [2247]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.037.001.01"]
---

# 57.3 Constraints

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2247 to 2247.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2247

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
{Or         Code <Cd> [1..1] CodeSet 2255
Or}         Proprietary <Prtry> [1..1] Text 2255
       Description <Desc> [0..1] Text 2255
   SupplementaryData <SplmtryData> [0..*] ± C1 2255
57.3 Constraints
C1 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
57.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
57.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following MessageHeader12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 2247
   CreationDateTime <CreDtTm> [0..1] DateTime 2247
   OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 2248
57.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 3328
57.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 3320
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.037.001.01
SecuritiesAccountAuditTrailReportV01
Target2-Securities 2247 August 2026
```

