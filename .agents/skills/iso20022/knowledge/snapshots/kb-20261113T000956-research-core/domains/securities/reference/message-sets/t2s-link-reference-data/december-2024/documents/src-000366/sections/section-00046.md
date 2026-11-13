---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["7 reda.051.001.01 AccountLinkStatusAdviceV01", "7.4 Message Building Blocks"]
file_pages: [49]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.051.001.01"]
---

# 7.4 Message Building Blocks

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 49 to 49.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 49

```text
C4 SecuritiesAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SecuritiesAccount must be absent.
C5 SecuritiesAccountOrBlockChainAddress3Rule
Either SecuritiesAccount or BlockChainAddressOrWallet must be present but not both.
C6 StatusReasonRule
If Status equals "Rejected" then StatusReason must be present.
C7 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
7.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
7.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
MessageHeader <MsgHdr> contains the following MessageHeader12 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 49
   CreationDateTime <CreDtTm> [0..1] DateTime 49
   OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 49
7.4.1.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 78
7.4.1.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Definition: Date and time at which the message was created.
Datatype: "ISODateTime" on page 75
7.4.1.3  OriginalBusinessInstruction <OrgnlBizInstr>
Presence: [0..1]
Definition: Unique identification of the original instruction.
Approved by the Securities SEG on 21 November 2024. reda.051.001.01 AccountLinkStatusAdviceV01
Target2-Securities - Link Reference Data 49 December 2024
```

